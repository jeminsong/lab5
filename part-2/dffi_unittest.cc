
/* Do not edit below this line. */
/* Do not edit below this line. */
/* Do not edit below this line. */

#include <gtest/gtest.h>

#include <climits>
#include <cstdio>
#include <future>
#include <limits>

#include "dffi_functions.h"

// Thanks to Paul Inventado
// https://github.com/google/googletest/issues/348#issuecomment-431714269
#define MAX_DURATION_MS 500
// Fail immediately.
#define ASSERT_DURATION_LE(millisecs, stmt)                                 \
  {                                                                         \
    std::promise<bool> completed;                                           \
    auto stmt_future = completed.get_future();                              \
    std::thread(                                                            \
        [&](std::promise<bool>& completed) {                                \
          stmt;                                                             \
          completed.set_value(true);                                        \
        },                                                                  \
        std::ref(completed))                                                \
        .detach();                                                          \
    if (stmt_future.wait_for(std::chrono::milliseconds(millisecs)) ==       \
        std::future_status::timeout)                                        \
      GTEST_FATAL_FAILURE_("\tExecution time greater than " #millisecs      \
                           " milliseconds.\n\tRevise algorithm for better " \
                           "performance and check for "                     \
                           "infinite loops.");                              \
  }

// Defer failure
#define EXPECT_DURATION_LE(millisecs, stmt)                                    \
  {                                                                            \
    std::promise<bool> completed;                                              \
    auto stmt_future = completed.get_future();                                 \
    std::thread(                                                               \
        [&](std::promise<bool>& completed) {                                   \
          stmt;                                                                \
          completed.set_value(true);                                           \
        },                                                                     \
        std::ref(completed))                                                   \
        .detach();                                                             \
    if (stmt_future.wait_for(std::chrono::milliseconds(millisecs)) ==          \
        std::future_status::timeout)                                           \
      GTEST_NONFATAL_FAILURE_("\tExecution time greater than " #millisecs      \
                              " milliseconds.\n\tRevise algorithm for better " \
                              "performance and check for "                     \
                              "infinite loops.");                              \
  }

#define FP_DELTA 0.001
namespace {

// Tests PromptForDouble()
TEST(PromptForDoubleTest, ViaPipe) {
  // Fake stdin using pipes
  // See https://stackoverflow.com/a/73666797 for an example
  // Works only on Unix-like operating systems where you can use
  // a pipe to replace STDIN.
  int my_pipe[2];
  int status = pipe(my_pipe);
  ASSERT_NE(status, -1);
  // Swap the stdin file descriptor with the read end of the pipe
  status = dup2(my_pipe[0], STDIN_FILENO);
  ASSERT_NE(status, -1);

  size_t n_bytes{0};

  // Number of inputs/tests
  size_t n_inputs{3};

  // What is the input that you'd like to send?
  const char* fake_input[] = {"123.456\n", "0.0\n", "-123.456\n"};
  int fake_input_size[2];
  for (int i = 0; i < n_inputs; i++) {
    fake_input_size[i] = strlen(fake_input[i]);
  }
  // What value do we expect?
  double expected_value[] = {123.456, 0.0, -123.456};

  for (int i = 0; i < n_inputs; i++) {
    n_bytes = write(my_pipe[1], fake_input[i], fake_input_size[i]);
    ASSERT_EQ(n_bytes, fake_input_size[i]);
    EXPECT_DURATION_LE(
        MAX_DURATION_MS,
        EXPECT_NEAR(expected_value[i],
                    PromptForDouble(""),
                    FP_DELTA));
  }
  // Close up our pipe.
  close(my_pipe[1]);
  close(my_pipe[0]);
}

// Tests TruncateDouble()

// Tests negative input.
TEST(TruncateDoubleTest, Negative) {
  EXPECT_DURATION_LE(MAX_DURATION_MS,
                     EXPECT_EQ(-0, TruncateDouble(-0.0123145)));
  EXPECT_DURATION_LE(MAX_DURATION_MS,
                     EXPECT_EQ(-5, TruncateDouble(-5.0123145)));
  EXPECT_DURATION_LE(MAX_DURATION_MS,
                     EXPECT_EQ(-3, TruncateDouble(-3.0123145)));
  EXPECT_DURATION_LE(MAX_DURATION_MS,
                     EXPECT_EQ(-12345, TruncateDouble(-12345.0123145)));
  EXPECT_DURATION_LE(MAX_DURATION_MS,
                     EXPECT_EQ(-34, TruncateDouble(-34.0123145)));
  EXPECT_DURATION_LE(
      MAX_DURATION_MS,
      EXPECT_EQ(std::numeric_limits<int>::min(),
                TruncateDouble(double(std::numeric_limits<int>::min()) * 2.0)));
}

// Tests positive input.
TEST(TruncateDoubleTest, Positive) {
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(0, TruncateDouble(0.0123145)));
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(5, TruncateDouble(5.0123145)));
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(3, TruncateDouble(3.0123145)));
  EXPECT_DURATION_LE(MAX_DURATION_MS,
                     EXPECT_EQ(12345, TruncateDouble(12345.0123145)));
  EXPECT_DURATION_LE(MAX_DURATION_MS,
                     EXPECT_EQ(34, TruncateDouble(34.0123145)));
  EXPECT_DURATION_LE(
      MAX_DURATION_MS,
      EXPECT_EQ(std::numeric_limits<int>::max(),
                TruncateDouble(double(std::numeric_limits<int>::max()) * 2.0)));
}

}  // namespace


/* Do not edit below this line. */
/* Do not edit below this line. */
/* Do not edit below this line. */

#include <gtest/gtest.h>
#include <limits.h>

#include <cstdio>
#include <future>

// for pipe() and dup2()
#include <unistd.h>

#include "rectarea_functions.h"

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

namespace {

// Tests PromptForInt()
TEST(PromptForIntTest, ViaPipe) {
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
  size_t n_inputs{2};

  // What is the input that you'd like to send?
  const char* fake_input[] = {"42\n", "-42\n"};
  int fake_input_size[2];
  for (int i = 0; i < n_inputs; i++) {
    fake_input_size[i] = strlen(fake_input[i]);
  }
  // What value do we expect?
  int expected_value[] = {42, -42};

  for (int i = 0; i < n_inputs; i++) {
    n_bytes = write(my_pipe[1], fake_input[i], fake_input_size[i]);
    ASSERT_EQ(n_bytes, fake_input_size[i]);
    EXPECT_DURATION_LE(
        MAX_DURATION_MS,
        EXPECT_EQ(expected_value[i],
                  PromptForInt("")));
  }
  // Close up our pipe.
  close(my_pipe[1]);
  close(my_pipe[0]);
}

// Tests RectangleArea()
// Tests negative input.
TEST(RectangleAreaTest, Negative) {
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(0, RectangleArea(-10, 4)));
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(0, RectangleArea(-10, -4)));
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(0, RectangleArea(10, -4)));
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(0, RectangleArea(0, 0)));
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(0, RectangleArea(0, 123)));
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(0, RectangleArea(123, 0)));
}

// Tests some trivial cases.
TEST(RectangleAreaTest, Positive) {
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(1, RectangleArea(1, 1)));
  EXPECT_DURATION_LE(MAX_DURATION_MS, EXPECT_EQ(200, RectangleArea(20, 10)));
  EXPECT_DURATION_LE(MAX_DURATION_MS,
                     EXPECT_EQ(164034, RectangleArea(701, 234)));
  EXPECT_DURATION_LE(MAX_DURATION_MS,
                     EXPECT_EQ(4478819, RectangleArea(2371, 1889)));
}

}  // namespace

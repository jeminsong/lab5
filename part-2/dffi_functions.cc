// Jemin Song
// jeminsong0119@csu.fullerton.edu
// @jeminsong0119
// Partners: @notyela

#include "dffi_functions.h"

double PromptForDouble(const std::string& query) {
  std::cout << query;

  double user_input = 0.0;
  std::cin >> user_input;

  return user_input;
}

int TruncateDouble(double decimal_number) {
  double integer_part = std::trunc(decimal_number);
  int converted_integer_part = 0;
  if (integer_part >= static_cast<double>(std::numeric_limits<int>::max())) {
    converted_integer_part = std::numeric_limits<int>::max();
  } else if (integer_part <=
             static_cast<double>(std::numeric_limits<int>::min())) {
    converted_integer_part = std::numeric_limits<int>::min();
  } else {
    converted_integer_part = static_cast<int>(integer_part);
  }
  return converted_integer_part;
}
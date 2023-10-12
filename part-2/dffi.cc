// Jemin Song
// jeminsong0119@csu.fullerton.edu
// @jeminsong0119
// Partners: @notyela

#include <iostream>
#include <limits>
#include <string>

#include "dffi_functions.h"

constexpr float kInchesInFeet{12.0};
constexpr float kEighthsInInch{8.0};

int main(int argc, char const *argv[]) {
  double input_decimal_feet{PromptForDouble(
      "Enter the number of feet you wish to convert to feet-inch: ")};
  if (input_decimal_feet >=
      static_cast<double>(std::numeric_limits<int>::max())) {
    std::cout << "The input is too larger to convert to an integer. Exiting.\n";
    return 1;
  } else if (input_decimal_feet <=
             static_cast<double>(std::numeric_limits<int>::min())) {
    std::cout << "The input is too small to convert to an integer. Exiting.\n";
    return 1;
  }

  std::string sign = (input_decimal_feet < 0) ? "-" : "";

  if (input_decimal_feet < 0.0) {
    input_decimal_feet = -input_decimal_feet;
  }
  int feet_integer_component = TruncateDouble(input_decimal_feet);
  double feet_fractional_component =
      input_decimal_feet - static_cast<double>(feet_integer_component);
  double decimal_inches = feet_fractional_component * kInchesInFeet;
  int inches_integer_component = TruncateDouble(decimal_inches);
  double inches_fractional_component =
      decimal_inches - static_cast<double>(inches_integer_component);
  double decimal_eighths = inches_fractional_component * kEighthsInInch;
  int eighths_integer_component = TruncateDouble(decimal_eighths);

  std::cout << sign << input_decimal_feet << " feet is " << sign
            << feet_integer_component << " feet, " << inches_integer_component
            << " and " << eighths_integer_component << "/8 inches\n";

  return 0;
}

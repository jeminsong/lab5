// TODO: Add your own header

#include <iostream>
#include <limits>
#include <string>

#include "dffi_functions.h"

int main(int argc, char const *argv[]) {
  // There are 12 inches in every feet.
  constexpr float kInchesInFeet{12.0};
  // There are 8 eights of an inch in every inch.
  constexpr float kEighthsInInch{8.0};

  // TODO: Declare a double type variable named input_decimal_feet and
  // initialize it to the return value of PromptForDouble(). Use the
  // prompt:
  // "Enter the number of feet you wish to convert to feet-inch: "

  // TODO: Verify that the entered value is safe to work with. In other
  // words, if the value of input_decimal_feet is too large or too small
  // we need to print an error message and exit the program.
  //    if input_decimal_feet is greater than or equal to the largest integer
  //      value,
  //    then
  //      print
  //      "The input is too larger to convert to an integer. Exiting.\n";
  //      and return 1.
  //    else if input_decimal_feet is less than or equal to the smallest
  //       integer value,
  //    then
  //      print
  //      "The input is too small to convert to an integer. Exiting.\n";
  //      and return 1.
  // Hint: You can get the largest value for an int variable using the
  // expression:
  // std::numeric_limits<int>::max()
  // and you can get the smallest value for an int variable using the
  // expression:
  // std::numeric_limits<int>::min()


  // TODO: Declare a string variable named sign and initiazlie it to an
  // empty string ("")

  // TODO: if input_decimal_feet is less than 0.0,
  //       then
  // assign -input_decimal_feet to input_decimal_feet which makes
  // the negative value, positive.
  // And assign "-" to the variable sign.


  // TODO: Declare an integer type variable named feet_integer_component
  // and initialize it to the return value
  // of TruncateDouble(input_decimal_feet)

  // TODO: Declare a double type variable named feet_fractional_component
  // and initialize it to the expression
  // input_decimal_feet - static_cast<double>(feet_integer_component)

  // TODO: Declare a double type variable named decimal_inches and
  // initialize it to the expression
  // feet_fractional_component * kInchesInFeet

  // TODO: Declare an integer variable named inches_integer_component and
  // initialize it to the return value of TruncateDouble(decimal_inches)

  // TODO:Declare a double type variable named inches_fractional_component
  // and initialize it to the expression
  // decimal_inches - static_cast<double>(inches_integer_component)

  // TODO: Declare a double type variable named decimal_eighths and 
  // initialize it to the expression
  // inches_fractional_component * kEighthsInInch

  // TODO: Declare an integer type variable named eighths_integer_component
  // and initlialize it to the return value  TruncateDouble(decimal_eighths).

  // TODO: Print to the terminal each element below seperating each item
  // with a space.
  // the variable sign
  // input_decimal_feet
  // " feet is "
  // sign
  // feet_integer_component
  // " feet "
  // inches_integer_component
  // " and "
  // eighths_integer_component
  // "/8 inches\n"
  // The output must match what is given in the README so that our 
  // automated tests can verify your program's output.

  return 0;
}
// TODO: Add your own header

#include "dffi_functions.h"

// Prompt for a double (decimal) input and return the double value
//
// The function takes one argument which is the prompt printed
// to the terminal.
//
// The function returns a double (decimal) value which is whatever was
// typed at the terminal.
//
// Typical usage:
//   double bank_balance{PromptForDouble("How much money do you have? ")};
//   percentage = PromptForDouble("What's the interest rate? ");
double PromptForDouble(const std::string& query) {
  // TODO: Write the body of this function such that it
  // 1. Print the prompt to the terminal
  // 2. Declares a double typed variable named user_input and
  //    initialize it to 0.0
  // 3. Read the value typed at the keyboard and store it in the
  //    variable named user_input
  // 4. Return user_input to the function's caller

  // TODO: Remove the return below and replace it with your own
  // return statement given the instructions above.
  return -1;
}

// Truncates (cuts off, no rounding) the input and returns an
// integer representing the truncated double.
//
// The function takes one argument which is a double value.
//
// The function returns an integer value which is whatever the
// input double value was except truncated to the closest integer
// value.
//
// Typical usage:
//   double csuf_tuition{7234.84}
//   int dollars_no_cents{TruncateDouble(csuf_tuition)};
int TruncateDouble(double decimal_number) {
  // TODO: Write this function such that it
  // 1. Declare a double type variable named integer_part, initialize it to the    return value of trunc(decimal_number)
  //    The function truc() is part of the standard library and you can learn
  //    more about it at https://en.cppreference.com/w/cpp/numeric/math/trunc.
  // 2. Declare an integer type variable named converted_intger_part,
  //    initialize it to the value 0.
  // 3. Because a double may be significantly larger or significantly
  //    smaller than an integer, we need to see if we can safely use the
  //    value stored in integer_part.
  //    if integer_part is greater than or equal to the largest integer
  //      value, then assing the largest integer value to
  //      converted_integer_part.
  //    else if integer_part is less than or equal to the smallest integer
  //      value, then assing the smallest integer value to
  //      converted_integer_part.
  //    else use static_cast<int> to convert integer_part to an int and
  //      assign it to converted_integer_part.
  // 4. return converted_integer_part
  //
  // Hint 1: You can get the largest value for an int variable using the
  // expression:
  // std::numeric_limits<int>::max()
  // and you can get the smallest value for an int variable using the
  // expression:
  // std::numeric_limits<int>::min()
  // Hint 2: To cast a variable use static_cast<int>(), see 
  // https://en.cppreference.com/w/cpp/language/static_cast

  // TODO: Remove the return below and replace it with your own
  // return statement given the instructions above.
  return -1;
  
}
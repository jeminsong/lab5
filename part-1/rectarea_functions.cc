// TODO: Add your own header

// Don't forget to #include the header file associated with
// this source file.
#include "rectarea_functions.h"

// Prompt for an integer input and return the integer value
//
// The function takes one argument which is the prompt printed
// to the terminal.
//
// The function returns an integer value which is whatever was
// typed at the terminal.
//
// Typical usage:
//   int height{PromptForInt("How tall are you? ")};
//   n_fingers = PromptForInt("How many fingers do you have? ");
int PromptForInt(const std::string& query) {
  // TODO: Write the body of this function such that it
  // 1. Print the prompt to the terminal
  // 2. Declares an integer typed variable named user_input and
  //    initialize it to 0
  // 3. Read the value typed at the keyboard and store it in the
  //    variable named user_input
  // 4. Return user_input to the function's caller

  // TODO: Remove the return below and replace it with your own
  // return statement given the instructions above.
  return -1;
}

// Calculate the area of a triangle defined by length and width.
//
// The area of a triangle is the product of the length and width.
//
// Although rectangles with negative length and width exist, this program
// is meant to be used to calculate the positive area of rectangles one
// could encounter in the physical world.
//
// Because of this requirement, length and width must be positive
// integers. Values less than 1 mean that the rectangle has 0 area.
//
// Typical usage:
//   int input_length{13};
//   int input_width{17};
//   int area{RectangleArea(input_length, input_width)};
//
// \param length the length of the rectangle
// \param width the width the rectangle
// \returns the area of the rectangle defined by \p length and \p width
int RectangleArea(int length, int width) {
  // TODO: Write this function such that it
  // 1. Declares an integer variable named area and initializes it
  //    to zero.
  // 2. Check if length is greater than zero and width is greater than
  //    zero.
  //    if true, then calculate the area given the length and width
  //                  and assign it to the variable area.
  // 3. Return area to the function's caller

  // TODO: Remove the return below and replace it with your own
  // return statement given the instructions above.
  return -1;
}

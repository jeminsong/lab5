// Jemin Song
// jeminsong0119@csu.fullerton.edu
// @jeminsong0119
// Partners: @notnyela

#include <iostream>
#include <string>

#include "rectarea_functions.h"

int main(int argc, char const* argv[]) {
  int input_length{PromptForInt(" Enter the length of the rectangle: ")};
  int input_width{PromptForInt("Enter the width of the rectangle: ")};

  int area{RectangleArea(input_length, input_width)};

  std::cout << input_length << " x " << input_width << " = " << area << "\n";
  return 0;
}
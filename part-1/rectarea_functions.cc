// Jemin Song
// jeminsong0119@csu.fullerton.edu
// @jeminsong0119
// Partners: @notyela

#include "rectarea_functions.h"
int PromptForInt(const std::string& query) {
  std::cout << query;
  int user_input = 0;
  std::cin >> user_input;
  return user_input;
}
int RectangleArea(int length, int width) {
  int area{0};
  if (length > 0 && width > 0) {
    area = length * width;
  } else {
    area = 0;
  }
  return area;
}
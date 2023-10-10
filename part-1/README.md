# What to Do

1. Read the entire README with your partner before doing anything else.
1. With your partner, edit the `rectarea.cc` source file using VS Code. Add the required header. Replace all the TODO comments with working code. Remember, make small changes and compile often.
1. Your program must use the functions defined in `rectarea_functions.cc`. Do not change the prototype of this function (name, return type, argument types). Updated `rectarea_functions.h` to have all the required prototypes. Read the TODOs for guidance.
1. Compile your program with the `make` shell command. Use the **debug compile error** procedure to debug any compile errors.
1. Run your program with the `./rectarea` shell command.
1. Test that your program passes all of the test cases in the test suite above. If your program suffers a runtime error, use the **debug runtime error** procedure to debug the error. If your program does not produce the expected output, use the **debug logic error** procedure to debug the error.
1. Check your header with the `make header` shell command. Correct any errors.
1. Check for format errors with the `make format` shell command. Correct any errors.
1. Check for lint errors with the `make lint` shell command. Correct any errors.
1. Test your program against automated test with the `make test` command. Debug any runtime errors or logic errors using the same procedures.
1. After your program passes all of these tests and checks, push your code to GitHub. Use the usual trio of commands: `git add`, `git commit`, and `git push`.
1. Move on to part-2

# Calculating the Area of a Rectangle

A [rectangle](https://en.wikipedia.org/wiki/Rectangle) is a four sided polygon with four right angles. A rectangle is defined by its length and width.

Given the length _l_ and width _w_ of a rectangle, one can calculate the area of a rectangle by finding the product of length and width, _l_ × _w_.

The purpose of this exercise is to gain practice using the following elements:
* Using instructor provided [unit tests](https://en.wikipedia.org/wiki/Unit_testing).
* Defining functions
* Working with multiple files

This project is defined in 4 files:
* `rectarea.cc`
* `rectarea_functions.cc`
* `rectarea_functions.h` - Add a header, do not make any other changes.
* `rectarea_unittest.cc` - Do not edit or change this file.

In `rectarea.cc`, our main function for our program is defined. In this file, we use the function `int PromptForInt(const std::string& query);` to ask the computer use for input. Once we have the input collected, we pass the length and width to the function `int RectangleArea(int length, int width)`.

The function `int RectangleArea(int length, int width)` is defined in the file `rectangle_area_functions.cc`. The compiler separately compiles each file and then combines the output from each compilation step into an executable binary file (a .exe file).

This project demonstrated [modular programming](https://en.wikipedia.org/wiki/Modular_programming) where different elements of our programs are defined in different files. Imagine trying to write a large program like a web browser, word processor, or operating system in just a single file. The amount of code in the file would make it difficult to navigate and chnange. For this and many other reasons, programmers like to break their programs down into multiple files. In our project, we have one file which has our main program `rectangle_area.cc` and another file which contains the functions used in our main program `rectangle_area_functions.cc`.

The file `rectarea_functions.h` is called a [header file](https://google.github.io/styleguide/cppguide.html#Header_Files). Notice that it is almost the same name as `rectarea_functions.cc` except that the file extension `.cc` has been changed to `.h`. This tells the programmer that it is the header file for the C++ source file named `rectangle_area_functions.cc`. The header file is used to help the programmer and compiler know what is available for use in a given `.cc` file.

Another benefit of modular programming is that we can break our program down into independent pieces which can be tested independently. As our programs increase in complexity, we will be writing more units of code that we need to make sure function correctly. One way to do this is to follow the practice of [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development). 

Test-driven development is where the tests are written first and then we develop the software to pass the tests. The motivation is that if the person who wrote the specification (your instructor) understands what they want, then tests can be written to document how the code is going to be used. Then the developer (you, the student) can develop your software and know that it is correct(-ish) if it passes the tests.

We can never really know if the code is correct because the tests could be flawed or wrong. Regardless, test-driven development is an effective way to communicate how we would like our programs to behave.

In this exercise, [unit tests](https://en.wikipedia.org/wiki/Unit_testing) have been included which test the function `int RectangleArea(int length, int width)`. To run the unit tests, use the command `make unittest`.

If any of the tests fail, use the output to go back and revise your code and re-run the unit tests. Once you have all your tests passing, then you likely have all the parts working correctly.

Remember, verifying a unit (a part) does not mean that the entire program (the system that uses the parts) is working correctly. That part is still up to the developer to verify through rigorous testing. As a starting point, you can use the instructor's partial tests with `make test`.

## Requirements

Write a program that takes two integers as a command line argument which represent the length and width of a non-degenerate, positive area rectangle. Calculate the area using the function `int RectangleArea(int length, int width)` which is defined in `rectangle_area_functions.cc`. Print a message to the terminal showing the length, width and the area of the rectangle. See the Example Output Section for more details.

A rectangle is defined by a positive length and a positive width. Rectangles defined by lengths or widths that are less than or equal to 0 have 0 area.

You shall use [cout](https://en.cppreference.com/w/cpp/io/cout) to print messages to the terminal.

You shall use [cin](https://en.cppreference.com/w/cpp/io/cin) to read in values from the keyboard.

The starting code defines a series of `TODO` comments which you can use to formulate your plan and develop your program.

Write your program progressively. Compile your program often and check that you're making progress. Make sure your program behaves the way you expect.

The output of your program must match the output given in the section Example Output below.

To compile your program, you use the `make` command. A Makefile is provided for this exercise.

The Makefile has the following targets:

* all: builds the project
* clean: removes object and dependency files
* spotless: removes everything the clean target removes and all binaries
* format: outputs a [`diff`](https://en.wikipedia.org/wiki/Diff) showing where your formatting differes from the [Google C++ style guide](https://google.github.io/styleguide/cppguide.html)
* lint: output of the [linter](https://en.wikipedia.org/wiki/Lint_(software)) to give you tips on how to improve your code
* header: check to make sure your files have the appropriate header
* test: run tests to help you verify your program is meeting the assignment's requirements. This does not grade your assignment.
* unittest: run unit tests to verify parts of your program performs according to the instructor supplied unit tests.

## Don't Forget

Please remember that:

- You need to put a header in every file.
- You need to follow the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html).
- Remove the `TODO` comments.

## Testing Your Code

Computers only ever do exactly what they are told, exactly the way they are told it, and never anything else. Testing is an important process to writing a program. You need to test for the program to behave correctly and test that the program behaves incorrectly in a predictable way.

As programmers we have to remember that there are a lot of ways that we can write the wrong program and only one to a few ways to write the correct program. We have to be aware of [cognitive biases](https://en.wikipedia.org/wiki/List_of_cognitive_biases) that we may exercise that lead us to believe we have correctly completed our program. That belief may be incorrect and our software may have errors. [Errors in software](https://www.wired.com/2005/11/historys-worst-software-bugs/) may lead to loss of [life](https://www.nytimes.com/2019/03/14/business/boeing-737-software-update.html), [property](https://en.wikipedia.org/wiki/Mariner_1), [reputation](https://en.wikipedia.org/wiki/Pentium_FDIV_bug), or [all of the above](https://en.wikipedia.org/wiki/2009%E2%80%9311_Toyota_vehicle_recalls).

### Test Strategy

Start simple, and work your way up. Good tests are specific, cover a broad range of fundamentally different possibilities, can identify issues quickly, easily, and directly, without need for much set up, and can almost be diagnosed by inspection if the code fails to execute the test correctly.

## Example Output

Please ensure your program's output is identical to the example below.

```
$ make unittest
set -e; clang++ -MM -g -O3 -Wall -pedantic -pipe -std=c++17 -D LINUX -nostdinc++ -I/usr/include/c++/11 -I/usr/include/x86_64-linux-gnu/c++/11 -D AMD64 rectarea_functions.cc 	| sed 's/\(rectarea_functions\)\.o[ :]*/.o rectarea_functions.d : /g' > rectarea_functions.d; 	[ -s rectarea_functions.d ] || rm -f rectarea_functions.d
set -e; clang++ -MM -g -O3 -Wall -pedantic -pipe -std=c++17 -D LINUX -nostdinc++ -I/usr/include/c++/11 -I/usr/include/x86_64-linux-gnu/c++/11 -D AMD64 rectarea.cc 	| sed 's/\(rectarea\)\.o[ :]*/.o rectarea.d : /g' > rectarea.d; 	[ -s rectarea.d ] || rm -f rectarea.d
clang++ -g -O3 -Wall -pedantic -pipe -std=c++17 -D LINUX -nostdinc++ -I/usr/include/c++/11 -I/usr/include/x86_64-linux-gnu/c++/11 -D AMD64 -c rectarea_functions.cc
Running main() from ./googletest/src/gtest_main.cc
[==========] Running 3 tests from 2 test suites.
[----------] Global test environment set-up.
[----------] 1 test from PromptForIntTest
[ RUN      ] PromptForIntTest.ViaPipe
[       OK ] PromptForIntTest.ViaPipe (0 ms)
[----------] 1 test from PromptForIntTest (0 ms total)

[----------] 2 tests from RectangleAreaTest
[ RUN      ] RectangleAreaTest.Negative
[       OK ] RectangleAreaTest.Negative (0 ms)
[ RUN      ] RectangleAreaTest.Positive
[       OK ] RectangleAreaTest.Positive (0 ms)
[----------] 2 tests from RectangleAreaTest (0 ms total)

[----------] Global test environment tear-down
[==========] 3 tests from 2 test suites ran. (1 ms total)
[  PASSED  ] 3 tests.
$ make
set -e; clang++ -MM -g -O3 -Wall -pedantic -pipe -std=c++17 -D LINUX -nostdinc++ -I/usr/include/c++/11 -I/usr/include/x86_64-linux-gnu/c++/11 -D AMD64 rectarea_functions.cc 	| sed 's/\(rectarea_functions\)\.o[ :]*/.o rectarea_functions.d : /g' > rectarea_functions.d; 	[ -s rectarea_functions.d ] || rm -f rectarea_functions.d
set -e; clang++ -MM -g -O3 -Wall -pedantic -pipe -std=c++17 -D LINUX -nostdinc++ -I/usr/include/c++/11 -I/usr/include/x86_64-linux-gnu/c++/11 -D AMD64 rectarea.cc 	| sed 's/\(rectarea\)\.o[ :]*/.o rectarea.d : /g' > rectarea.d; 	[ -s rectarea.d ] || rm -f rectarea.d
clang++ -g -O3 -Wall -pedantic -pipe -std=c++17 -D LINUX -nostdinc++ -I/usr/include/c++/11 -I/usr/include/x86_64-linux-gnu/c++/11 -D AMD64 -c rectarea.cc
clang++ -g -O3 -Wall -pedantic -pipe -std=c++17 -D LINUX -nostdinc++ -I/usr/include/c++/11 -I/usr/include/x86_64-linux-gnu/c++/11 -D AMD64 -c rectarea_functions.cc
clang++ -g -O3 -Wall -pedantic -pipe -std=c++17 -L /usr/lib/gcc/x86_64-linux-gnu/11 -o rectarea rectarea.o rectarea_functions.o 
$ ./rectarea
Enter the length of the rectangle: 23   
Enter the width of the rectangle: 17
23 x 17 = 391
$ ./rectarea
Enter the length of the rectangle: -13 45
Enter the width of the rectangle: -13 x 45 = 0
$ ./rectarea
Enter the length of the rectangle: 32
Enter the width of the rectangle: 0
32 x 0 = 0
```

## Test Cases
Test your program before moving on. For each of the test cases below,

1. Look at the test suite, and identify the first test case, its input, and expected output.
1. Run your program with `./date_difference` .
1. Provide the program with the test case input.
1. If the program crashes, use the **debug runtime error** flowchart to debug the error.
1. Observe the program output and decide whether the actual output matches the expected output.
1. If the output **does not match**, declare that the program fails the test. Use the **debug logic error** flowchart to debug the error.
1. Otherwise (the output **does match**), repeat step 2 with the next test case.

If the program works correctly (meaning no runtime or logic errors) for every test case, declare that the program passes the test. You can move on to releasing your code for part 1.


| Test Case | Input      | Expected Output                               |
|-----------|------------|-----------------------------------------------|
| 1         | 12.345     | `12.345 feet is 12 feet, 4 and 1/8 inches`    |
| 2         | 0.125      | `0.125 feet is 0 feet, 1 and 4/8 inches`      |
| 3         | 0.00125    | `0.00125 feet is 0 feet, 0 inches`            |
| 4         | -0.00125   | `-0.00125 feet is -0 feet, 0 inches`          |
| 5         | -13.567    | `-13.567 feet is -13 feet, 6 and 6/8 inches`  |
| 6         | 10         | `10 feet is 10 feet, 0 inches`                |

## Format Check

Use the `make format` command to check your programs formatting. Correctly formatting your source code is a requirement of the grading rubric.

If you make significant changes to your source file, test it again to confirm that it still passes the test suite. Sometimes a small change that looks benign can actually create a bug.

Below is an example of the output of `make format` when you have correctly formatted code.
```
$ make format
2022-09-25 14:20:54,529 - INFO - Checking format for file: decimal_feet_to_feet_inch.cc
2022-09-25 14:20:54,569 - INFO - 😀 Formatting looks pretty good! 🥳
$
```


## Lint Check
Use the `make lint` command to check your program for lint. If you find that your program has lint, then take the necessary steps to correct your program so it is lint free. Lint free source code is a requirement of the grading rubric.

If you make significant changes to your source file, test it again to confirm that it still passes the test suite. Sometimes a small change that looks benign can actually create a bug.

Below is an example of the output of `make lint` when you have correctly formatted code.
```
$ make lint
2022-09-25 14:22:30,017 - INFO - Linting file: rectarea.cc
2022-09-25 14:22:34,139 - INFO - 😀 Linting passed 🥳
2022-09-25 14:22:34,139 - INFO - This is not an auto-grader.
2022-09-25 14:22:34,140 - INFO - Make sure you followed all the instructions and requirements.
$
```

Below is an example of the output of `make lint` when you have source code with lint. The output is showing you that there are comments with `TODO` and that `TODO` should not be left in a completed program. Change it to `DONE` or `TODOX` to mark it completed.

```
$ make lint
2023-10-02 01:34:37,068 - INFO - Linting file: rectarea.cc
2023-10-02 01:34:41,866 - ERROR - Linter found improvements.
2023-10-02 01:34:41,866 - WARNING - /mnt/cpsc120/cpsc-120-solution-lab-05/part-1/rectarea.cc:1:1: warning: missing username/bug in TODO [google-readability-todo]
// TODO: Add your own header
^~~~~~~~~~~~~~~~~~~~~~~~~~~~
// TODO(mshafae): Add your own header
/mnt/cpsc120/cpsc-120-solution-lab-05/part-1/rectarea.cc:10:3: warning: missing username/bug in TODO [google-readability-todo]
  // TODO: Declare an integer variable and name it input_length and
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // TODO(mshafae): Declare an integer variable and name it input_length and
2023-10-02 01:34:51,284 - ERROR - 🤯😳😤😫🤬
2023-10-02 01:34:51,284 - ERROR - Use the output from this program to help guide you.
2023-10-02 01:34:51,284 - ERROR - If you get stuck, ask your instructor for help.
2023-10-02 01:34:51,284 - ERROR - Remember, you can find the Google C++ style online at https://google.github.io/styleguide/cppguide.html.
make: *** [Makefile:100: lint] Error 1
```

## Push Your Code

After you have certified that your code passes the test suite and format check, release the code by pushing it to GitHub.

As usual, you need to
1. Use a computer that is authenticated to git. If your computer is not already authenticated, use the `gcf.sh` script in the **Git Configuration & Authentication* page in Canvas.
1. Add modified file(s) with the `git add` shell command.
1. Create a git commit with the `git commit -m "<MESSAGE>"` shell command.
1. Send the commit to GitHub.com with the `git push` shell command.
1. Refresh the web view of your repo and confirm that your push went through.

If any of these steps trigger an error message, use the **debug command error** flowchart to resolve the problem.

## Next Steps

Start part-2 of the lab.



## Lecture 7

### Scratch Project

+   [Previous works](https://drive.google.com/drive/folders/0B05KF1rCZn8baEFGVGVMNm1tbUk)

### Review

+   Values and Data types
    +   Integer 
        +   `int`
        +   123, 456, 1234567
    +   Floating-point number
        +   `float`
        +   3.125, 4.875
        +   0.1 is not accurate
        +   Accurate enough in practice
    +   String
        +   `str`
        +   Quoted
        +   `'abc'`, `"123"`
+   Variables
    +   `=` Assignment
        +   Variable is defined by assignment.
            +   `x = 5`
            +   `y = 'abc'`
    +   [Variable name](https://automatetheboringstuff.com/chapter1/#calibre_link-107)
+   More data types
    +   `tuple`
        +   `tpl = (3,5)`
    +   `list`
        +   `lst = [1,2,3,4]`
        +   `lst[1] = 9`
    +   `dict`
        +   `dct = {}`
        +   `dct = {1:2}`
        +   `dct['name'] = 'MZ'`
+   Expression
    +   Values and operators
    +   Arithmetic operators: `+` `-` `*`, `/`, `//`, `%`, `**`, `()`
+   Functions
    +   Call: append brackets and parameters (if needed)
    +   `print`
        +   `print('hello, world!')`
    +   `input`
        +   `x = input('I need a string')`
    +   `len`
        +   `print(len('abcd'))`
    +   `str`
        +   `print('abc'+123)`
        +   `print('abc'+str(123))`
    +   `int`
        +   `print(int(1.234))`
        +   `print(int(-1.234))`
    +   `float`
        +   `print(0.1+float('0.2'))`
    +   `eval`
        +   `print('1+2+3*4+5')`
+   [Practice Questions](https://automatetheboringstuff.com/chapter1/)

### Flow Control

+   [Flow chart](https://automatetheboringstuff.com/chapter2/#calibre_link-1903)
+   Boolean Values
    +   `True`
    +   `False`
    +   `true` and `false` are no good
+   Comparison operators
    +   `==`
        +   `float` is not accurate.
    +   `!=`
    +   `<`
    +   `<=`
    +   `>`
    +   `>=`
    +   Compare values of different types
        +   `string` versus `int`
        +   `int` versus `float`
+   Boolean operators
    +   `and`
    +   `or`
    +   `not`
    +   Precedence: `not` > `and` > `or`
+   Truthy and falsey values
    +   Truthy values
        +   Non-zero integers
        +   Non-zero `float`
        +   Non-empty `string`
    +   Falsey values
        +   `0`
        +   `0.0`
        +   `''`
    +   The are more truthy and falsey values. Not NOW.
+   Conditions: a boolean expression
+   Block of code
    +   Selection
        +   `if`
        +   `if`-`else`
        +   `if`-`elif`-`else`
        +   `if`-`elif`-`else`
    +   Iteration
        +   `while`
        +   `for` loop
        +   `break`
        +   `continue`
    +   Exception handling
        +   `try`-`except`

### Debugger

+   Breakpoint
+   Go
+   Step (Into)
+   (Step) Over
+   (Step) Out
+   Quit

### Task 4

+   Write a program to ensure the user input an even number which is not 4.

### Task 5

+   Draw [Rokumonsen](https://www.google.com.tw/search?q=Rokumonsen)
+   Draw Ichimonsen (一文銭)
+   Draw Sanjurokumonsen (三十六文銭)

### `pyautogui`: open your eyes!

+   [Sample code 1](lec07-1.py)
+   Define a function
    +   `def` block
+   `screenshot()`
+   `pixel`
    +   `(R,G,B)`
+   How to take a screen shot
    +   Windows: print screen key
        +   Hold alt, then press print screen
            +   This gives you a picture of window on focus
        +   Use Microsoft Paint to save the screenshot into png file
+   [Sample code 2](lec07-2.py)
+   `locateOnScreen()`
+   `locateAllOnScreen()`
+   Task: Check all boxes!
    +   Practice [here](https://goo.gl/forms/dr5mkE7Z9dKiJ3gI3)
+   Task: Make your drawing program
    +   More readable: use `def` block
    +   Less dependent on maximizing window
        +   Use screen shot and `locateOnScreen`
+   Issues
    +   `screenshot` is slow
    +   `locateOnScreen` is very slow
    +   Hard to recognize objects
    +   [`trexutil`](trexutil.py)
        +   Use `(83, 83, 83) in screenshot(region=(x, y, w, h)).im` to detect
        +   Use `screenshot(region=(x, y, w, h)).save('test.png')` to save screenshoted image to `test.png`

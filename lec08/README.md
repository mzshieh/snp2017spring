## Lecture 8

### Flow Control

+   [Flow chart](https://automatetheboringstuff.com/chapter2/#calibre_link-1903)
+   Boolean Values
    +   `True` and `False` are Boolean values
    +   `true` and `false` are variable names
+   Comparison operators
    +   `==`, `!=`, `<`, `<=`, `>`, `>=`
    +   Tips
        +   `float` is not accurate.
        +   Compare different types
            +   `'1'!=1` is `True`
            +   `1.0==1` is `True`
+   Boolean operators
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
+   Conditions: a boolean expression

### Python Grammar

+   Block of code
    +   Selection
        +   `if`
        +   `if`-`else`
        +   `if`-`elif`
        +   `if`-`elif`-`else`
    +   Iteration
        +   `while`
        +   `for` loop
        +   `break`
        +   `continue`
    +   Exception handling
        +   `try`-`except`
        +   `try`-`except`-`else`
+   `pass`
    +   A statement to do nothing

### Task 4

+   Write a program to ensure the user input an even number which is not 4.
+   Hint: Use `try`-`except`
+   Hint: Use `int()`, `%` (modulo), `//` (integer division)

### Function

+   `def your_function()`
+   `return`
    +   The function is terminated either by `return` or by the end of the block.
    +   `None`: if there is no `return` or just `return` nothing
+   `def your_function_with_parameter(parameter)`
    +   Argument
+   `def your_function_with_parameters(parameter1, parameter2)`
    +   More arguments
+   `def your_function_with_parameters(*args)`
    +   Variable length list of arguments can be passed by `args` which is a `tuple`.
    +   More flexible
    +   Access data via index `i`: `args[i]`
+   `def your_function_with_parameters(**kwargs)`
    +   Keyword argument
    +   `print(some_str, end='')`
    +   `print(some_str_1, some_str_2, sep=',')`
    +   Access data via key string
        +   `kwargs['end']`
        +   `kwargs['sep']`
+   Please do not overwrite the arguments in your function now. We will discuss what will happen if you do so later.
+   Scope
    +   Variables are defined by assignment statements
    +   Global
        +   Defined in global scope
        +   `global`
            +   `global some_var`: `some_var` in this function is the global `some_var`
            +   You must do this if you're going to write global variables
    +   Local
        +   Defined in local scope
    +   Principles
        +   Local variables cannot be used globally.
        +   A local scope cannot access local variables in other scopes.
        +   A local variable and a global variable may have the same name, but only local variable can be accessed.
        +   You may still read the global variable correctly if no local variable is using the same name.

### Debugger

+   Breakpoint
+   Go
+   Step (Into)
+   (Step) Over
+   (Step) Out
+   Quit

### `pyautogui`: open your eyes!

+   [Sample code 1](lec07-1.py)
    +   Report the color of the position pointed by your mouse
+   `screenshot()`
+   `pixel`
    +   `(R,G,B)`
+   How to take a screen shot
    +   Windows: print screen key
        +   Hold alt, then press print screen
            +   This gives you a picture of window on focus
        +   Use Microsoft Paint to save the screenshot into png file
+   [Sample code 2](lec07-2.py)
    +   Check all boxes on the screen
+   `locateOnScreen()`
+   `locateAllOnScreen()`
+   Issues on [Lonely T-Rex](http://www.trex-game.skipser.com/)
    +   `screenshot` is slow
    +   `locateOnScreen` is very slow
    +   Hard to recognize objects
    +   [`trexutil`](trexutil.py) provides faster `screenshot`
        +   Put it to the same folder
        +   `from trexutil import screenshot`
        +   Use `(83, 83, 83) in screenshot(region=(x, y, w, h)).im` to detect
            +   Smaller area, faster `screenshot`
        +   Use `screenshot(region=(x, y, w, h)).save('test.png')` to save screenshoted image to `test.png`

### Task 5

+   Draw [Rokumonsen](https://www.google.com.tw/search?q=Rokumonsen)
    +   [Sample code](ichimon.py): Draw Ichimonsen (一文銭)
+   Draw Sanjurokumonsen (三十六文銭)
+   Hint: Use `for` and `def` to make your code readable
+   Hint: Use `pyautogui.screenshot` and `locateOnScreen`

### Task 6

+   Check all boxes on this [page](https://goo.gl/forms/dr5mkE7Z9dKiJ3gI3)
+   Hint: Use `scroll` or press page down

### Mini project

+   [Lonely T-Rex](http://www.trex-game.skipser.com/)
+   Expected score: 500+
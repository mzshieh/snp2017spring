## Lecture 9

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

### Review

+   Boolean Values
    +   `True`
    +   `False`
    +   `true` and `false` are no good
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

### Flow Control: Selection

+   Conditions: a boolean expression
+   Block of code
    +   Don't forget colon `:`
    +   Indent: spaces and tabs are allowed
        +   Recommend: 4 spaces
+   `if`
+   `else`
+   `elif`

### Flow Control: Loops

+   `while`
    +   `ctrl`+`C` to stop your (buggy) program
+   `break`
+   `continue`
+   `for`
+   `range()`
    +   `range(n)`: `0`, `1`, ..., `n-1`
    +   `range(start,stop)`: `start`, `start+1`, ..., `stop-1`
        +   Math: `[start,stop)`
    +   `range(start,stop,step)`
        +   If `step` is positive: `start`, `start+step`, ..., `start+k*step` where `k` is the maximum integer such that `start+k*step < stop`.
        +   If `step` is negative: `start`, `start+step`, ..., `start+k*step` where `k` is the maximum integer such that `start+k*step > stop`.
        +   If `step` is zero or non-integral: cause a `ValueError`
+   Nested loops

### Flow Control: Exception

+   It is complicated. We are not going to cover much about it.
+   `try`
+   `except`
+   [Sample Code](lec09.py)

### Task 5

+   Draw [Rokumonsen](https://www.google.com.tw/search?q=Rokumonsen)
+   Draw Ichimonsen (一文銭)
+   Draw Sanjurokumonsen (三十六文銭)

### Task 6

+   Ask user to input a 4-digit number such that
    +   Must be an integer.
        +  `'one two three four'` is not OK.
        +  `1234.0` is not OK.
        +  `1234` is OK.
    +   Any digit appears at most once
        +   `5566` is not OK.
    +   Leading zero is acceptable.
        +   `0123` is OK.
    +   User's input have four digits
        +   `123` is not OK.
+   Repeat until the user cooperates.

### Practice Question: Chapter 2

+   See the [textbook](https://automatetheboringstuff.com/chapter2/)

### Function

+   `def your_function()`
+   `return`
    +   The function is terminated either by `return` or by the end of the block.
    +   `None`: if there is no `return` or just `return` nothing
+   `def your_function_with_parameter(parameter)`
    +   Argument
+   `def your_function_with_parameters(parameter1, parameter2)`
    +   More arguments
+   Variable length list of arguments
    +   More flexible
    +   We will teach you how to declare such functions later.
+   Keyword argument
    +   `print(some_str, end='')`
    +   `print(some_str_1, some_str_2, sep=',')`
    +   We will teach you how to declare function with keyword arguments later.
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

### `import`

+   `sys`
    +   `sys.exit()`
+   `random`
    +   `random.random()`
    +   `random.randint()`

### Debugger

+   Breakpoint
+   Go
+   Step (Into)
+   (Step) Over
+   (Step) Out
+   Quit

### Task 7

+   Guess a secret number from `0` to `9`
+   `5` chances

### Task 8

+   Implement the game [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)
+   The `i`-th charactor of a string `x`: `x[i]`
    +   Zero base
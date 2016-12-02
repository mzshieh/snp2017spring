## Lecture 11

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

### Scratch Project

+   Next week!

### Review

+   `if`, `else`, `elif`
+   `while`, `for`
    +   `break`, `continue`
+   `try`, `except`
+   [Slide](snp_lec11.pdf)

### Debugger

+   Breakpoint
+   Go
+   Step (Into)
+   (Step) Over
+   (Step) Out
+   Quit

### `import`

+   `sys`
    +   `sys.exit()`
+   `random`
    +   `random.random()`
    +   `random.randint()`

### Function

+   `def your_function()`
    +   Example:
        +   Run `mspaint` and maximize the window
+   `return`
    +   The function is terminated either by `return` or by the end of the block.
    +   `None`: if there is no `return` or just `return` nothing
    +   Example: `pyautogui.size()`
+   `def your_function_with_parameter(parameter)`
    +   Argument
    +   Example: `floor`, `round`
+   `def your_function_with_parameters(parameter1, parameter2)`
    +   More arguments
    +   Example: `pyautogui.moveTo()`
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

### Task 7

+   Guess a secret number from `0` to `9`
    +   Use `random`
+   `5` chances

### Task 8 minus

+   Implement a two digit version of the game [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)
+   Use `def`

### Task 8

+   Implement the game [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)
+   The `i`-th charactor of a string `x`: `x[i]`
    +   Zero base

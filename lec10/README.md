## Lecture 10

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

### Scratch Project

+   [Sample two-player ScratchX project](lec10.sbx)

### Review

+   Condition: a boolean expression
+   Block of code
    +   Don't forget colon `:`
    +   Indent: spaces and tabs are allowed
        +   Recommend: 4 spaces
+   Loops
    +   `while`
        +   `ctrl`+`C` to stop your (buggy) program
    +   `for`
        +   `range()`
    +   `break`
    +   `continue`
    +   Nested loops

+   Exception
    +   It is complicated. We are not going to cover much about it.
    +   `try`
    +   `except`
        +   Specified types

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
    +   Use `random`
+   `5` chances

### Task 8 minus

+   Implement a two digit version of the game [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)
+   Use `def`

### Task 8

+   Implement the game [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)
+   The `i`-th charactor of a string `x`: `x[i]`
    +   Zero base

### [Term Project Preview](http://snp2016.nctu.me/)
## Lecture 7

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

### Review

+   Goal:
    +   To teach imperative programming
        +   Functions
        +   Syntax
        +   Algorithms
    +   To teach how to control computers
+   Approach: limited but sufficient information
    +   Might be against the best practice
        +   You may learn more after this course
+   The Interactive Shell
    +   Run `python`
    +   Run IDLE
    +   Has `>>>` or `...`
+   How to Find Help
    +   Search engine
    +   [Stackoverflow](http://stackoverflow.com/)
    +   Asking Smart Programming Questions
+   Expression
    +   Values and operators
    +   Arithmetic operators: `+` `-` `*`, `/`, `//`, `%`, `**`, `()`
+   Data types
    +   Integer: exact
    +   Floating-point number: accurate enough in practice
    +   String
        +   Concatenate: `+`
        +   Repeat: `*`
+   Basic functions
    +   `print()`
    +   `input()`
    +   `len()`
    +   `str()`
    +   `int()`
    +   `float()`
    +   `eval()`

### Task 0

+   Goal: Open Microsoft Paint and maximize it
+   Using mouse (with your eyes?)
    +   Click start
    +   Find the application and click it
    +   Wait until Microsoft Paint is opened (Important)
    +   Click the maximize button
+   Using keyboard (without your eyes?)
    +   Press windows key (Click start?)
    +   Type `mspaint` (Find the application?)
    +   Press enter (Click it?)
    +   Wait until Microsoft Paint is opened
    +   Hold windows key, then press up (Maximize)
+   Sample code
+   If the task is not a provided function, then you have to program.
+   Decompose the task into instructions supported by the system environment.


### Task 1

+   Draw a triangle
    +   Green
    +   Filled
+   Draw a rectangle
    +   Brown
    +   Filled
+   Draw a christmass tree
    +   [Example](https://scratch.mit.edu/projects/115904117/)

### Task 2

+   Draw a circle
    +   Green
    +   Filled
+   Draw a tilt rectangle
    +   Brown
    +   Filled
+   Draw a tree
    +   [With branches](https://scratch.mit.edu/projects/115838437)

### Task 3

+   Do whatever you want via using `pyautogui`

### `pyautogui`

+   Keyboard
    +   Type
        +   `pyautogui.typewrite(text,delay)`
    +   Press
        +   `pyautogui.press(key)`
        +   [Key table](https://automatetheboringstuff.com/chapter18/#calibre_link-36)
    +   Hot key
        +   `pyautogui.hotkey(key1, key2, ..., keys)`
        +   Example: `pyautogui.hotkey('ctrl', 'c')`

+   For those who feel `pyautogui` is too long, please try `gui = pyautogui` then `gui.moveTo(1,1)`
    +   This might make your code hard to read.

### Chapter 1 Homework

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

+   Conditions: a boolean expression
+   Block of code
+   `if`
+   `else`
+   `elif`
+   `while`
+   `break`
+   `continue`
+   `for`
+   `range()`
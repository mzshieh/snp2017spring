## Lecture 8

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

### Review

+   Package installation is the hardest part in this course
    +   [Tutorial](../install.md)
+   Did all of you finish task 1 and task 2?
    +   Save the result as a file
    +   Upload to E3(https://e3.nctu.edu.tw/)
+   Wait is important
    +   You have to wait until the precondition of the next instruction is ready for use.
        +   It takes time to open `mspaint`.
    +   Precondition and initialization
        +   Instant noodle
            +   What if you didn't boil the water?
        +   Scramble eggs
            +   What if you didn't scramble?
        +   Even experienced programmer may forget to initialize!
            +   The instructor forgot to fill hot water into the instant noodle cup.
+   `int()` will convert a `float` into integer
    +   Preserve the integral part only
        +   `int(1.9)` is `1`
        +   `int(0.5)` is `0`
        +   `int(-0.9)` is `0`
        +   `int(-1.7)` is `-1`
+   Formatting `float` 
    +   With string operator `%`: [`printf` style](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)
        +   `%.3f` means print `3` digits after the decimal point.
    +   [New method](https://docs.python.org/3/library/stdtypes.html#str.format) is complicated. Not NOW.
+   For more information about the floating-point numbers in Python, please refer to the [official tutorial](https://docs.python.org/3/tutorial/floatingpoint.html).
    +   See also: [Wikipedia](https://en.wikipedia.org/wiki/IEEE_floating_point)
    +   Keyword: Binary numbers
+   Let's review the practice questions of [chapter 1](https://automatetheboringstuff.com/chapter1/).
+   `eval()` is powerful
+   Boolean Values
    +   `True`
    +   `False`
    +   `true` and `false` are no good
+   Comparison operators
    +   `==`
        +   `float` and `int` are comparable.
        +   `float` is not accurate.
        +   `float` can be `NaN` (not a number)
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

### Boolean values (Continued)

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

### Flow Control: Selection

+   Conditions: a boolean expression
+   Block of code
    +   Don't forget colon `:`
    +   Indent: spaces and tabs are allowed
        +   Recommend: 4 spaces
+   `if`
+   `else`
+   `elif`

### Task 4

`int()` is not ideal to convert `float` into `int`. Write a program that round a `float` into its closest integer.
+   Use `int()`, `input()` and `print()`
+   You may assume the input is always a valid `float`
+   If there are two closest integers, then output the even one.
    +   四捨、六入、五成雙
+   You might need to ask some questions in the [chatroom](https://chatroom-mzshieh.c9users.io)

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
    +   `range(start,stop,step)`: `start`, `start+step`, ..., `start+k*step` where `k` is the maximum integer such that `start+k*step < stop`.
+   Nested loops

### Task 5

+   Draw [Rokumonsen](https://www.google.com.tw/search?q=Rokumonsen)
+   Draw Ichimonsen (一文銭)
+   Draw Sanjurokumonsen (三十六文銭)

### Practice Question: Chapter 2

+   See the [textbook](https://automatetheboringstuff.com/chapter2/)

### Flow Control: Exception

+   It is complicated. We are not going to cover much about it.
    +   Official [tutorial](https://docs.python.org/3/tutorial/errors.html)
+   [Example code](lec08.py)

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

### `import`

+   `sys`
    +   `sys.exit()`
+   `random`
    +   `random.random()`
    +   `random.randint()`
+   `pyperclip`
    +   `pyperclip.copy(str)`
    +   `pyperclip.paste()`

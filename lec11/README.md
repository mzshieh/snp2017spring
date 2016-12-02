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

### Lists and Tuples

+   `type()`
+   List
    +   Empty list: `[]`
    +   May have elements of different types
        +   `[12, 3.4, None, True, 'string', print]`
    +   Access (zero-based) `i`-th element of `list x`: `x[i]`
        +   try `[123,456][1]`
        +   try `[12, 3.4, None, True, 'string', print][5]('hello world')`
        +   try `[123,456][1.0]`
    +   The elements are mutable (modifiable)
+   Tuple
    +   Empty tuple: `()`
    +   Single element tuple: `(element,)`
        +   try `type(('str'))` and `type(('str',)`
    +   `(12, 3.4, None, True, 'string', print)`
    +   The elements are immutable (not modifiable)
+   `list()` and `tuple()`
    +   Try `list(('a','b','c'))`
    +   Try `tuple(['d','e','f'])`
    +   Try `list('hello')`
    +   Try `tuple('hello')`
+   `append()`
+   `in`
+   `not in`
+   Auto boxing & auto unboxing
    +   [code](lec11.py)
+   Try to simplify or to accomplish
    +   Bull and cow: 4-digit version
    +   Draw a tree: more complicated version

### Task 8

+   Implement the game [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)
+   The `i`-th charactor of a string `x`: `x[i]`
    +   Zero base

### More about Lists

+   Negative index: `some_list[-1]`
+   Sublists with slices: try `print([0,1,2,3,4][1:3])`
    +   Inclusive, exclusive
+   Concatenation `+`
+   Replication `*`
+   Delete an element of certain position:`del`
+   `index()`
    +   try `print([0,1,2,0].index(0))`
+   `insert(pos,val)`: insert `val` to position `pos`
    +   Let `a = [0,1,2]`. What will happen if we perform `a.insert(1,3)`?
+   `remove(val)`: remove an element of value `val`
    +   Let `a = [1,0,0,1]`. What will happen if we perform `a.remove(1)`?
+   `sort()`: sort the list ascendingly

### Dictionary

+   `list` is indexed by `int`
    +   From `0` to `len()-1`
+   `instructor = {'Name': 'MZ', 'Height': 178, 'Weight': 108}`
    +   try `print(instructor['Name'])`
    +   try `print(instructor['age'])`
+   Dictionary is indexed by keys (words).
    +   Word: key
    +   Definition: value
    +   A set of key-value pairs
+   Empty dictionary: `{}`
+   `keys()`
+   `values()`
+   `items()`
+   `in`
    +   try `print('MZ' in instructor)`
    +   try `print('Name' in instructor)`
    +   try `print(('Name','MZ') in instructor)`
+   `get(key,val)`: If `key` is missing, then return `val`
+   `setdefault(key,val)`: if there is no such `key`, initialize the key-value pair to `(key,val)` and return `val`. Otherwise return the value corresponding `key`.
+   Pretty printing: `pprint`

### Function definition
+   `def fn(arg,*arg_list,**arg_dict):`
+   `def fn(arg,*args,**kwargs):`
+   Unlimited number of positional argument: using list
    +   Use `[]`
+   Keyword argument: using dictionary!
    +   Use `get()`

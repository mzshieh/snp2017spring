## Lecture 13

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

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
+   `in`
+   `not in`
+   Auto boxing & auto unboxing
    +   [code](lec13-1.py)
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
+   `index()`
    +   try `print([0,1,2,0].index(0))`
+   `insert(pos,val)`: insert `val` to position `pos`
    +   Let `a = [0,1,2]`. What will happen if we perform `a.insert(1,3)`?
+   `append(val)`
+   `pop()`: remove the last element and return its value
+   `pop(pos)`: remove the elemement of position `pos`
+   `remove(val)`: remove an element of value `val`
    +   Let `a = [1,0,0,1]`. What will happen if we perform `a.remove(1)`?
+   `sort()`: sort the list ascendingly

### Dictionary

+   `list` is indexed by `int`
    +   From `0` to `len()-1`
+   Dictionary is indexed by keys (words).
    +   Word: key
    +   Definition: value
    +   A set of key-value pairs
+   `instructor = {'Name': 'MZ', 'Height': 178, 'Weight': 108}`
    +   try `print(instructor['Name'])`
    +   try `print(instructor['age'])`
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
    +   Use `*my_list` to pass a `list`
    +   Use `*my_dict` to pass a `dict`
+   Unlimited number of positional argument: using list
    +   Use `[]`
+   Keyword argument: using dictionary!
    +   Use `get()`

### `pyautogui`: open your eyes!

+   [Sample code 1](lec13-2.py)
+   `screenshot()`
+   `pixel()`
    +   `(R,G,B)`
+   How to take a screen shot
    +   Windows: print screen key
        +   Hold alt, then press print screen
            +   This gives you a picture of window on focus
        +   Use Microsoft Paint to save the screenshot into png file
+   [Sample code 2](lec13-3.py)
+   `locateOnScreen()`
+   `locateAllOnScreen()`
+   Task: Check all boxes!
    +   Practice [here](https://goo.gl/forms/dr5mkE7Z9dKiJ3gI3)
+   Task: Make your tree drawing program
    +   Some complex branches: [code](lec13-4.py)
    +   More readable: use `def` block
    +   Less dependent on maximizing window
        +   Use screen shot and `locateOnScreen`
        +   Use dictionary to handle the filenames

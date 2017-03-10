## Lecture 14

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

### Lists, Tuples and Strings

+   `type()`
+   Strings are immutable.
+   `in`
    +   `'1' in '1234'`
    +   `'12' in '1234'`
+   `not in`
+   Auto boxing & auto unboxing
    +   `a, b = '12'`
+   The `i`-th charactor of a string `x`: `x[i]`
    +   Zero base
+   Negative index: `some_str[-1]`
+   Sublists with slices: try `print('abcde'[1:3])`
    +   Inclusive, exclusive
+   Concatenation `+`
+   Replication `*`
+   `index()`
    +   try `print('01230'.index(0))`
+   Lists are mutable
    +   `insert(pos,val)`: insert `val` to position `pos`
        +   Let `a = [0,1,2]`. What will happen if we perform `a.insert(1,3)`?
    +   `append(val)`
    +   `pop()`: remove the last element and return its value
    +   `pop(pos)`: remove the elemement of position `pos`
    +   `remove(val)`: remove an element of value `val`
        +   Let `a = [1,0,0,1]`. What will happen if we perform `a.remove(1)`?
    +   `sort()`: sort the list ascendingly

### Task 8

+   Implement the game [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)
+   You may start with this [sample code](lec14-1.py)

### Task 8 helper

+   Write a program to help your partener to play the game.

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

+   [Sample code 1](lec14-2.py)
+   `screenshot()`
+   `pixel()`
    +   `(R,G,B)`
+   How to take a screen shot
    +   Windows: print screen key
        +   Hold alt, then press print screen
            +   This gives you a picture of window on focus
        +   Use Microsoft Paint to save the screenshot into png file
+   [Sample code 2](lec14-3.py)
+   `locateOnScreen()`
+   `locateAllOnScreen()`
+   Task: Check all boxes!
    +   Practice [here](https://goo.gl/forms/dr5mkE7Z9dKiJ3gI3)
+   Task: Make your tree drawing program
    +   Some complex branches: [code](lec14-4.py)
    +   More readable: use `def` block
    +   Less dependent on maximizing window
        +   Use screen shot and `locateOnScreen`
        +   Use dictionary to handle the filenames

### `requests`

+   A website has different looks
    +   When transfering its content, it looks like a sequence of bytes
    +   A sequence of bytes? A sequence of characters? A string.
    +   We need a different kind of eyes
+   `import requests`: don't forget `s`
+   URL: Uniform Resource Locator
    +   這術語好長我們叫他網址好了
+   `result = requests.get('https://raw.githubusercontent.com/mzshieh/snp2016fall/master/README.md')`
    +   這網址好長請試著複製貼上吧
+   `result.text`
    +   這內容好字串：`type(result.text)`
    +   String processing
        +   `str`
        +   `import re`: regular expression
+   `result.raise_for_status()`
    +   連網頁做了好多事情，要是網址有錯瀏覽器會直接當掉給你看嗎？
    +   It is OK to raise an exception, but always using `try-except` blocks is tedious.
        +   Java is tedious: almost always `try` or `throws` (`raise` in Python)
    +   `raise_for_status()`: If there is any exception, raise it now.
+   Save the content
    +   Open a file to save it: `the_file = open('a_name.html', 'wb')`
        +   Filename: `a_name`
        +   Mode: `wb` means "write binary"
            +   `the_file.write(chunk)`: write a chunk of bytes
        +   Mode: `wt` means "write text"
            +   `the_file.write(some_str)`: write a string
    +   `for chunk in result.iter_content(102400):` to iterate 102400-byte chunks of `result`
    +   Remember to close the file: `the_file.close()`
    +   Sample [code](lec14-5.py)

### String processing

+   Escape Characters: [Table](https://automatetheboringstuff.com/chapter6/#calibre_link-40)
+   Multiline Strings: triple quotes ```   
+   Indexing:
    +   `print('123'[0])`
    +   `print('123'[-1])`
+   `index()`
    +   `print('123123123'.index('312'))`
+   Slicing: 
    +   `print('abcde'[2:])`
    +   `print('abcde'[:2])`
    +   `print('abcde'[1:3])`
+   `in` and `not in`
    +   `print('abc' in 'zabcy')`
    +   `print('gg' not in 'zabcy')`
+   `upper()` and `lower()`
+   `isupper()`, `islower()`, `isdecimal()`, `isalpha()`, `isalnum()`
    +   try `'123.0'.isdecimal()`
+   `join(list_str)`
    +   try `', '.join([str(i) for i in range(10)])`
+   `split(string)`
    +   try `'<a href="https://automatetheboringstuff.com/">'.split('"')`
+   `startswith(string)` and `endswith(string)`
    +   Many URLs start with `http` and end with `html`
+   `strip()`, `rstrip()`, `lstrip()`
+   Task: open all URLs which end with `html` in a wikipedia page.
    +   `import webbrowser` then use `webbrowser.open(URL)` to open the page
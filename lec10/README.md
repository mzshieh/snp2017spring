## Lecture 10

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

### More on `list` and `tuple`

+   `type(value)`
+   List
    +   Empty list: `[]`
    +   May have elements of different types
        +   `[12, 3.4, None, True, 'string', print]`
    +   Access (zero-based) `i`-th element of `list x`: `x[i]`
        +   try `[123,456][1]`
        +   try `[12, 3.4, None, True, 'string', print][5]('hello world')`
        +   try `[123,456][1.0]`
    +   Lists are mutable: you may change the contents!
+   Tuple
    +   Empty tuple: `()`
    +   Single element tuple: `(element,)`
        +   Try `type(('str'))` and `type(('str',)`
    +   Comprehension
        +   Try `type((x for x in range(5)))` 
        +   Use `tuple(x for x in range(5))` to generate `(0,1,2,3,4)`
    +   `(12, 3.4, None, True, 'string', print)`
    +   The elements are immutable: you may not change the contests!
+   `list()` and `tuple()`
    +   Try `list(('a','b','c'))`
    +   Try `tuple(['d','e','f'])`
    +   Try `list('hello')`
    +   Try `tuple('hello')`
+   Negative index: `a_list_or_tuple[-1]`
+   Slice
    +   `print([0,1,2,3,4][1:3])`
    +   `print([0,1,2,3,4][2:])`
    +   `print([0,1,2,3,4][:4])`
    +   `print([0,1,2,3,4][-3:])`
    +   `print([0,1,2,3,4][:-3])`
    +   `print([0,1,2,3,4][3:1])`
    +   Inclusive, exclusive
+   `in`
+   `not in`
+   Concatenation `+`
+   Replication `*`
+   `index()`
    +   try `print([0,1,2,0].index(0))`
+   Auto boxing & auto unboxing
    +   [code](lec10-1.py)

### Lists are Mutable

+   `insert(pos,val)`: insert `val` to position `pos`
    +   Let `a = [0,1,2]`. What will happen if we perform `a.insert(1,3)`?
+   `append(val)`
+   `pop()`: remove the last element and return its value
+   `pop(pos)`: remove the elemement of position `pos`
+   `remove(val)`: remove an element of value `val`
    +   Let `a = [1,0,0,1]`. What will happen if we perform `a.remove(1)`?
+   `sort()`: sort the list ascendingly

### More on `dict`

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
+   `dict` is mutable
    +  Add a new item via assignment
        +  `a_dict[key]=val`
    +  Modify an item via assignment
        +  a_dict[key]=val`
    +  Remove an item via `del`
        +  `del a_dict[key]`
        +  `del` can also undefine a variable.
+   Iterate a dictionary
    +   `keys()`
    +   `values()`
    +   `items()`
+   `in`
    +   try `print('MZ' in instructor)`
    +   try `print('Name' in instructor)`
    +   try `print(('Name','MZ') in instructor)`
+   `get(key,val)`: If `key` is missing, then return `val`
    +   Try to use an undefined item to compute.
+   `setdefault(key,val)`: if there is no such `key`, initialize the key-value pair to `(key,val)` and return `val`. Otherwise return the value corresponding `key`.

### Function definition
+   `def fn(arg,*arg_list,**arg_dict):`
+   `def fn(arg,*args,**kwargs):`
    +   Use `*my_list` to pass a `list`
    +   Use `*my_dict` to pass a `dict`
+   Unlimited number of positional argument: using `list`
    +   Use `[]`
+   Keyword argument: using dictionary!
    +   Use `get()`

### `requests` Reads Webpages

+   A website has different looks
    +   When transfering its content, it looks like a sequence of bytes
    +   A sequence of bytes? A sequence of characters? A string.
    +   We need a different kind of eyes
+   `import requests`: don't forget `s`
+   URL: Uniform Resource Locator
    +   這術語好長我們叫他網址好了
+   `result = requests.get('https://raw.githubusercontent.com/mzshieh/snp2017spring/master/README.md')`
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
        +   Filename: `a_name.html`
        +   Mode: `wb` means "write binary"
            +   `the_file.write(chunk)`: write a chunk of bytes
        +   Mode: `wt` means "write text"
            +   `the_file.write(some_str)`: write a string
    +   `for chunk in result.iter_content(102400):` to iterate 102400-byte chunks of `result`
    +   Remember to close the file: `the_file.close()`
    +   Sample [code](lec10-2.py)

### String processing

+   Escape Characters: [Table](https://automatetheboringstuff.com/chapter6/#calibre_link-40)
+   Multiline Strings: triple quotes `'''`
+   Integers, characters and strings
    +   `chr`
        +   try `chr(65)`
    +   `ord`
        +   try `ord('A')`
    +   Python uses `str`'s of length 1 to represent characters.
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
+   Task: Download an image from a webpage.
    +   Hint: reuse [previous sample code](lec10-2.py)
    +   Hint: find `<img` in `result.text`. You should discover there is a URL appened to a `src=` nearby.
    +   Bonus: Download random 3 images from a webpage
    +   Bonus: Download all identifiable images from a webpage
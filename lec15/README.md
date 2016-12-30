## Lecture 15

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

### `pyautogui`: open your eyes!

+   [Sample code 1](lec15-1.py)
+   `screenshot()`
+   `pixel()`
    +   `(R,G,B)`
+   How to take a screen shot
    +   Windows: print screen key
        +   Hold alt, then press print screen
            +   This gives you a picture of window on focus
        +   Use Microsoft Paint to save the screenshot into png file
+   [Sample code 2](lec15-2.py)
+   `locateOnScreen()`
+   `locateAllOnScreen()`
+   Task: Check all boxes!
    +   Practice [here](https://goo.gl/forms/dr5mkE7Z9dKiJ3gI3)
+   Task: Make your tree drawing program
    +   Some complex branches: [code](lec15-3.py)
    +   More readable: use `def` block
    +   Less dependent on maximizing window
        +   Use screen shot and `locateOnScreen`

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
        +   錯誤時還是會讓你拿到一個網頁顯示錯誤，因此還是有 `result.text`
    +   It is OK to raise an exception, but always using `try-except` blocks is tedious.
        +   Java is tedious: almost always `try` or `throws` (`raise` in Python)
    +   `raise_for_status()`: If there is any exception, raise it now.
+   Save the content
    +   Binary
        +   Open a file to save it: `the_file = open('a_name.html', 'wb')`
            +   Filename: `a_name`
            +   `the_file.write(chunk)`: write a chunk of bytes
        +   `for chunk in result.iter_content(102400):` to iterate 102400-byte chunks of `result`
        +   Remember to close the file: `the_file.close()`
        +   Sample [code](lec15-4.py)
    +   Text:
        +   Open a text file to write: `out = open('out.txt','wt')`
        +   `print(anything,file=out)`
        +   Remember to close the file: `out.close()`

### String processing

+   Escape Characters: [Table](https://automatetheboringstuff.com/chapter6/#calibre_link-40)
+   Multiline Strings: triple quotes `'''`
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

### Beautiful soup

+   `from bs4 import BeautifulSoup` and using `BeautifulSoup` versus `import bs4` and using `bs4.BeautifulSoup`
+   Parsing HTML: the real webpages
    +   View source!
+   [Example code 1](lec15-5.py)
    +   `find(tag)`
        +   Get a `Tag` from the html
        +   Try `type(div)`
+   [Example code 2](lec15-6.py)
    +   Get information from `Tag`: use `.get`
    +   `.get` is safer than `[]`
+   [Example code 4](lec15-7.py)
    +   `find_all` returns a list
    +   CSS selector: `select(tag)`
        +   Get all `tag`s
        +   Return a list
+   [Example code 3](lec15-8.py)
    +   Advanced `find` usage
        +   Accessing attributes
            +   keyword argument
            +   dictionary
    +   Try `soup.select('div.find_by_class')`
+   [Example code 5](lec15-9.py)
    +   Try to use `select` to replace `find`
+   Redo Task: open five webpages
    +   Tag: `a`
    +   Attribute: `href`
+   [Sample code](lec15-10.py)
+   `find_all(tag)` returns a list
+   CSS selector: `select(tag)`
    +   Get all `tag`s
    +   Return a list
    +   Similar to `find_all`
    +   Special attribute: `class` and `id`
        +   Use `requests` to get `https://tw.news.yahoo.com/sports/` and cook `soup`
        +   `class` use `.` : Try `soup.select('div.yom-mod.yom-blist')`
        +   `id` use `#`: Try `soup.select('div#mediamegatron')`
+   Redo Task: open five webpages
    +   Tag: `a`
    +   Attribute: `href`
    +   `endswith('html')`
    +   `import webbrowser`
+   Task: Open five images in browser
    +   Tag: `img`
    +   Attribute: `src`
+   Task: Save five images from some webpage
+   Task: Crawl the [Yahoo Sport News](https://tw.news.yahoo.com/sports/)
    +   找出五條新聞，並選出報導中的第一句話。
        +   Hint: `<p class="first">`
    +   Bonus: 擷取報導附圖。
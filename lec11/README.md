## Lecture 11

### Propose questions in the [Chatroom](https://chatroom-mzshieh.c9users.io/)

### Beautiful soup

+   `from bs4 import BeautifulSoup` and using `BeautifulSoup` versus `import bs4` and using `bs4.BeautifulSoup`
+   Parsing HTML: the real webpages
    +   View source!
+   [Example code 1](lec11-1.py)
    +   [HTML](https://mzshieh.github.io/snp2016/html/1.html)
    +   `find(tag)`
        +   Get a `Tag` from the html
        +   Try `type(div)`
+   [Example code 2](lec11-2.py)
    +   [HTML](https://mzshieh.github.io/snp2016/html/2.html)
    +   Get information from `Tag`: use `.get`
    +   `.get` is safer than `[]`
+   [Example code 3](lec11-3.py)
    +   [HTML](https://mzshieh.github.io/snp2016/html/4.html)
    +   `find_all` returns a list
    +   CSS selector: `select(tag)`
        +   Get all `tag`s
        +   Return a list
+   [Example code 4](lec11-4.py)
    +   [HTML](https://mzshieh.github.io/snp2016/html/3.html)
    +   Advanced `find` usage
        +   Accessing attributes
            +   keyword argument
            +   dictionary
    +   Try `soup.select('div.find_by_class')`
+   [Example code 5](lec11-5.py)
    +   [HTML](https://mzshieh.github.io/snp2016/html/5.html)
    +   Try to use `select` to replace `find`
+   Redo Task: open five webpages
    +   Tag: `a`
    +   Attribute: `href`
+   [Sample code](lec11-6.py)
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
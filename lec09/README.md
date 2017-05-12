## Lecture 9

### Function

+   `def your_function()`
+   `return`
    +   The function is terminated either by `return` or by the end of the block.
    +   `None`: if there is no `return` or just `return` nothing
+   `def your_function_with_parameter(parameter)`
    +   Argument
+   `def your_function_with_parameters(parameter1, parameter2)`
    +   More arguments
+   `def your_function_with_parameters(*args)`
    +   Variable length list of arguments can be passed by `args` which is a `tuple`.
    +   More flexible
    +   Access data via index `i`: `args[i]`
+   `def your_function_with_parameters(**kwargs)`
    +   Keyword argument
    +   `print(some_str, end='')`
    +   `print(some_str_1, some_str_2, sep=',')`
    +   Access data via key string
        +   `kwargs['end']`
        +   `kwargs['sep']`
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

### Debugger

+   Breakpoint
+   Go
+   Step (Into)
+   (Step) Over
+   (Step) Out
+   Quit

### Iterator and Iterables

+   Iterables: bags of items
    +   `list`
    +   `tuple`
    +   `str`
    +   `range`
        +   `range(n)`
        +   `range(L,U)`
        +   `range(L,U,step)`
+   Iterator: an access to a certain item and the iterator to its next item
    +   `it = iter(iterables)`
    +   `next(it)`
+   Some useful tools  
    +   [`zip`](https://docs.python.org/3/library/functions.html#zip)
    +   [`enumerate`](https://docs.python.org/3/library/functions.html#enumerate)
    +   [`map`](https://docs.python.org/3/library/functions.html#map)
        +   `lambda x: int(10*x**0.5)`
    +   [`sum`](https://docs.python.org/3/library/functions.html#sum)
    +   [`filter`](https://docs.python.org/3/library/functions.html#filter)
        +   `lambda x: x % 2 == 0`
    +   [`all`](https://docs.python.org/3/library/functions.html#all)
    +   [`any`](https://docs.python.org/3/library/functions.html#any)
+   List comprehension
    +   `[int(10*x**0.5) for x in range(0,100,5) if x % 2 == 0]`
+   More tools
    +   [`itertools`](https://docs.python.org/3/library/itertools.html)

### Random

+   [`import random`](https://docs.python.org/3/library/random.html)
    +   Random integer from `a` to `b`: `random.randint(a,b)`
    +   Random floating point number in `[0.0,1.0)`: `random.random()` 
    +   Randomly shuffle a list `lst`: `random.shuffle(lst)`
    +   Random choice from a sequence: `random.choice(seq)`
    +   Random `k` samples from a population: `random.sample(population,k)`

### Game: Guess a secret number

+   Guess a secret number from `0` to `9`
    +   Sample code
+   Guess a secret number from `0` to `9` with hints
    +   Sample code
+   [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)
    +   Sample code
+   Task: write a program to helps you play Bulls and Cows
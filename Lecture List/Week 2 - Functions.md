# Python Week 2 by P’ Kumamon (Functions)

Copyright by P' Kumamon IT14.
For education purpose only

Follow me on GitHub!
[https://github.com/sagelga](https://github.com/sagelga)

----------

# What is function?

Functions are **"self contained" modules of code that accomplish a specific task.** Functions usually "take in" data, process it, and "return" a result. Once a function is written, it can be used over and over and over again. Functions can be "called" from the inside of other functions.

Functions **"Encapsulate" a task** (they combine many instructions into a single line of code). Most programming languages provide many built in functions that would otherwise require many steps to accomplish, for example computing the square root of a number. In general, we don't care **how** a function does what it does, only that it "does it"!

When a function is "called" the program "leaves" the current section of code and begins to execute the first line inside the function. Thus the function "flow of control" is:


1. The program comes to a line of code containing a "function call".
2. The program enters the function (starts at the first line in the function code).
3. **All instructions** inside of the function are executed from top to bottom.
4. The program leaves the function **and goes back to where it started from.**
5. Any data computed and **RETURNED** by the function is used in place of the function in the original line of code.
----------
## Why do we Write Functions?
1. They allow us to conceive of our program as a bunch of sub-steps. (Each sub-step can be its own function. When any program seems too hard, just break the overall program into sub-steps!)
2. They allow us to **reuse code instead of rewriting it.**
3. Functions allow us to **keep our variable namespace clean** (local variables only "live" as long as the function does). In other words, function_1 can use a variable called i, and function_2 can also use a variable called i and there is no confusion. Each variable i only exists when the computer is executing the given function.
4. Functions **allow us to test small parts of our program in isolation from the rest.** This is especially true in interpreted langaues, such as Matlab, but can be useful in C, Java, ActionScript, etc.

Definitions by Utah University http://www.cs.utah.edu/~germain/PPS/Topics/functions.html


# Getting start with functions

### Declaring new function
```python
def kumamon():
    print("Hello. My name is Kumamon")
```
This is a function called kumamon()

How to use a function declared
```python
kumamon()
```

It’s just that! No need to use anything else!

### Wrapping up the declaration and definition
```python
def kumamon():
  print("Hello. My name is Kumamon")
kumamon()
```
The interpreter will read line 1 and line 3. Then it starts executing line 3 by doing thing inside line 1

### Throw in variables
```python
def kumamon(value):
  print("This costs", value, "baht")

kumamon(200)
```

### Throw in and out of variables
```python
def main(value, value2):
  print("The answer is", kumamon(value, value2))

def kumamon(num1, num2):
  return num1+num2-5

main(int(input()), int(input()))
```

# Built-In Functions

If you want to make a new function name, consider how you create a new name.
If you choose the same name as the built-in function, Python will NOT work
These are lists of built-in functions in Python

| abs()         | dict()      | help()       | min()      | setattr()      |
| ------------- | ----------- | ------------ | ---------- | -------------- |
| all()         | dir()       | hex()        | next()     | slice()        |
| any()         | divmod()    | id()         | object()   | sorted()       |
| ascii()       | enumerate() | input()      | oct()      | staticmethod() |
| bin()         | eval()      | int()        | open()     | str()          |
| bool()        | exec()      | isinstance() | ord()      | sum()          |
| bytearray()   | filter()    | issubclass() | pow()      | super()        |
| bytes()       | float()     | iter()       | print()    | tuple()        |
| callable()    | format()    | len()        | property() | type()         |
| chr()         | frozenset() | list()       | range()    | vars()         |
| classmethod() | getattr()   | locals()     | repr()     | zip()          |
| compile()     | globals()   | map()        | reversed() | __import__()   |
| complex()     | hasattr()   | max()        | round()    |                |
| delattr()     | hash()      | memoryview() | set()      |                |

Resource by Python Foundation https://docs.python.org/3/library/functions.html

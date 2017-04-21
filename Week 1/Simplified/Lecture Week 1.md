# Lecture 1 by P' Kumamon
Copyright by P' Kumamon. For education purpose only

Follow me on GitHub! 
[https://github.com/sagelga](https://github.com/sagelga)

## Types of Values
Integer|Float|String|Boolean
:-:|:-:|:-:|:-:
int()|float()|str()|bool()
1,2,3|1,1.1,1.2|"Hello World"|True

### Type of value check
```python
var = "Hello"
type(var) # -> <class 'str'>
```

```python
var = "1234"
type(var) # -> <class 'str'>
```

```python
var = 1234
type(var) # -> <class 'int'>
```

```python
var = 1234.56
type(var) # -> <class 'float'>
```

```python
var = True
type(var) # -> <class 'bool'>
```

## Operators
Symbol|+|-|*|/|//|%|**
:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:
Name|Add|Subtract|Multiply|Divide|Floor Division|Mod|Exponent
Example|2+3|2-3|2*3|2/3|2//3|2&3|2**3
Results|5|-1|6|0.66666|0|2|8

## Logic Operator
Type|and|or
-|-|-
False False|False|False
False True|False|True
True False|False|True
True True|True|True

Type|not
-|-
False|True
True|False

## Order of Operations
Follows using PEMDAS rule

P|E|M|D|A|S
:-:|:-:|:-:|:-:|:-:|:-:
Parenthesis|Exponential|Multiplication|Division|Addition|Sutraction
()|**|*|/|+|-

## String Operation
```python
text = "Hello"
text2 = "World"
print(text + text2) # -> "HelloWorld"
```

```python
text = "Hello"
text2 = "World"
print(text, text2) # -> "Hello World"
```

### String with integer
```python
text = "Hello"
print(text * 5) # -> "HelloHelloHelloHelloHello"
```

```python
text = "Hello"
text2 = "World"
print(text + text2 + 5) # -> ERROR (You cannot add string with a integer type)


# so try to use this instead 
text = "Hello"
text2 = "World"
print(text + text2 + str(5)) # -> HelloWorld5
```

## Basic I/O

### print() Function
```python
text = "Hello"
print(text + "World") # -> HelloWorld
```

```python
text = 12
print(text, "World") # -> 12 World
```

```python
text = "Hello"
text2 = "World"
print(text + text2, sep=",") # -> Hello,World
```

```python
text = "Hello"
text2 = "World"
print(text + text2, end="!") # -> HelloWorld!
```

### input() Function
```python
var_x = input() # var_x is now a string type.
```

```python
var_x = int(input()) # Converts Float/Integer/String to Integer
```

```python
var_x = float(input()) # Converts Float/Integer/String to Float
```

```python
var_x = str(input()) # Converts Float/Integer/String to String
```

## Comments and DocString

Use 3 " to make it as multiple line comments (DocString)
```python
"""This is a docstring"""
```

Use # to make it as single line comment
```python
# this is one line comment
```

## ASCII Special Characters

![ASCII Table](http://www.asciitable.com/index/asciifull.gif)

## Module Import

Always import the library as a global variable (before any functions)

It will reduce your time to import over and over again
```python
import math
def kumamon():
	print(math.pi())
kumamon()
```

## Module list and how to use

### Basic Module List

They are inside this link
[https://docs.python.org/3.6/library/functions.html](https://docs.python.org/3.6/library/functions.html)

### Math Modules List

They are inside this link
[https://docs.python.org/3.6/library/math.html](https://docs.python.org/3.6/library/math.html)


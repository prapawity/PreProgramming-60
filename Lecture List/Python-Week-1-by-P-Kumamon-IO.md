# Python Week 1 by P’ Kumamon (I/O)

Copyright by P' Kumamon IT14.
For education purpose only

Follow me on GitHub!
[https://github.com/sagelga](https://github.com/sagelga)

----------
# Types of Values
| **Integer**
Number without decimal point | **Float**
Number with decimal point | **String**
Text | **Boolean**
Logic |
| ---------------------------------------- | ----------------------------------- | --------------- | ----------------- |
| int()                                    | float()                             | str()           | bool()            |
| -1 0 1                                   | 1.1 -2.1 3.555                      | "Hello World"   | True False        |


**Type of value check**

    var = "Hello"
    type(var) # -> <class 'str'>
    var = "1234"
    type(var) # -> <class 'str'>
    var = 1234
    type(var) # -> <class 'int'>
    var = 1234.56
    type(var) # -> <class 'float'>
    var = True
    type(var) # -> <class 'bool'>
# Operators

**Basic Operator**

| **Symbol**  | **+** | **-**    | *****    | **/**   | **//**         | **%** | ******   |
| ----------- | ----- | -------- | -------- | ------- | -------------- | ----- | -------- |
| **Name**    | Add   | Subtract | Multiply | Divide  | Floor Division | Mod   | Exponent |
| **Example** | 2+3   | 2-3      | 2*3      | 2/3     | 2//3           | 2&3   | 2**3     |
| **Results** | 5     | -1       | 6        | 0.66666 | 0              | 2     | 8        |

**Logic Operator**

| **Type**    | **AND (&&)** | **OR (||)** |
| ----------- | ------------ | ----------- |
| False False | False        | False       |
| False True  | False        | True        |
| True False  | False        | True        |
| True True   | True         | True        |

| **Type** | **NOT (!)** |
| -------- | ----------- |
| False    | True        |
| True     | False       |

**Combined Operator**

| **==**    | **!=**       | **<**     | **<=**                | **>**     | **>=**                |
| --------- | ------------ | --------- | --------------------- | --------- | --------------------- |
| Equals to | Not equal to | Less than | Less than or equal to | More than | More than or equal to |

## Order of Operations

Python is using PEMDAS rule. Do not use other mathematical rule to let Python compute
http://study.com/academy/lesson/what-is-pemdas-definition-rule-examples.html

| **P**           | **E**           | **M**              | **D**        | **A**        | **S**          |
| --------------- | --------------- | ------------------ | ------------ | ------------ | -------------- |
| **P**arenthesis | **E**xponential | **M**ultiplication | **D**ivision | **A**ddition | **S**utraction |
| ()              | **              | *                  | /            | +            | -              |

## String Operation
    text = "Hello"
    text2 = "World"
    print(text + text2) -> "HelloWorld"
    text = "Hello"
    text2 = "World"
    print(text, text2) -> "Hello World"

**String with integer**

    text = "Hello"
    print(text * 5) -> "HelloHelloHelloHelloHello"

    text = "Hello"
    text2 = "World"
    print(text + text2 + 5) -> ERROR (You cannot add string with a integer type)


    # so try to use this instead
    text = "Hello"
    text2 = "World"
    print(text + text2 + str(5)) -> HelloWorld5


## Basic I/O

**print() Function**

    text = "Hello"
    print(text + "World") -> HelloWorld
    text = 12
    print(text, "World") -> 12 World
    text = "Hello"
    text2 = "World"
    print(text + text2, sep=",") -> Hello,World
    text = "Hello"
    text2 = "World"
    print(text + text2, end="!") -> HelloWorld!

**input() Function**

    var_x = input() # var_x is now a string type.
    var_x = int(input()) # Converts Float/Integer/String to Integer
    var_x = float(input()) # Converts Float/Integer/String to Float
    var_x = str(input()) # Converts Float/Integer/String to String

**Things getting complicated**

    text = "Hello"
    num = 1234

    print(num+hello)
    # Returns error
    (string cannot be add with interger)

    print(str(num)+text)
    # Returns 1234Hello
    (they can be concatinate together because they are in the same value type)
## Comments and DocString

Use 3 " to make it as multiple line comments (DocString)

    """This is a docstring"""

Use # to make it as single line comment

    # this is one line comment


## Minimum and Maximum
    How to use:
    min(<argument 1>,<argument 2>)
    Returns the lowest number

    max(<argument 1>,<argument 2>)
    Returns the highest number

    ——————————————————————————————

    # Using 2 arguments
    var1 = 12
    var2 = 21
    return min(var1,var2)

    # Using 3 arguments
    var1 = 12
    var2 = 21
    var3 = 120
    return min(min(var1,var2),var3)

    # Using arguments from array
    var = [12,24]
    return min(var[0], var[1])


## Module Import

Always import the library as a global variable (before any functions)
It will reduce your time to import over and over again

    import math
    def kumamon():
        print(math.pi())
    kumamon()


## Module list and how to use

**Basic Module List**
They are inside this link
[https://docs.python.org/3.6/library/functions.html](https://docs.python.org/3.6/library/functions.html)

**Math Modules List**
+Python Extra (Math Library)

# Python Week 6 by P’ Kumamon (Lists + Tuples)

Copyright by P' Kumamon IT14.
For education purpose only

Follow me on GitHub!
[https://github.com/sagelga](https://github.com/sagelga)

----------
# Introduction to Arrays

Array is a set of related data. In Python we have two difference types of array called List and Tuples.

# Introduction to Lists

Like a string, a list is a sequence of values. In string, the value are characters; in a list, they can be any type. The values in a list are called **elements** or sometimes **items**.

There are several ways to create a new list; the simplest is enclose the elements in square brackets ([ and ])

**Create an array**

    kumamon = ['Kumamon', 'is', 'so', 'cute']
    numbers = [1, 2, 3, 4]
    blank = []
    initiate = list()

as visualized from kumamon

| **Value**          | Kumamon | is | so | cute |
| ------------------ | ------- | -- | -- | ---- |
| **Array Number**   | 0       | 1  | 2  | 3    |
| **Logical Number** | 1       | 2  | 3  | 4    |


then looked at numbers

| **Value**          | 1 | 2 | 3 | 4 |
| ------------------ | - | - | - | - |
| **Array Number**   | 0 | 1 | 2 | 3 |
| **Logical Number** | 1 | 2 | 3 | 4 |

# Adding More Elements

**Add using .append()**

    kumamon = [1,2,3,4]
    kumamon.append(5)

    # kumamon now equals to
    [1, 2, 3, 4, 5]

**Add using .split()**
+Python Week 3 by P’ Kumamon (Strings): Using-.split()

**Add from other array**

    text1 = ["Happy"]
    text2 = ["Kumamon"]
    return text1+text2

    # Returns
    ["Happy", "Kumamon"]
# Modifying Elements in Array

**Using .sort() or sorted()**

    kumamon = [1, 3, 4, 2, 5]
    kumamon.sort()

    # kumamon now equals to
    [1, 2, 3, 4, 5]

**Using reversed sort**

    kumamon = [1, 3, 4, 2, 5]
    kumamon.sort(reverse = True)

    # kumamon now equals to
    [5, 4, 3, 2, 1]

**Sort is from ASCII**

    kumamon = ['9', '1', 'a', 'A']
    kumamon = kumamon.sort()

    # kumamon now equals to
    ['1', '9', 'A', 'a']
# Using Elements in Array

**Using .pop()**
.pop() will print then remove that item

**Using array call**

    kumamon = ["Happy", "Funny", "Fat"]
    print(kumamon[1])

    # Returns "Funny"
# Remove Elements in Array

**Using .remove()**
.remove() will remove that element from the array


# Introduction to Tuples

Tuples is an array, with a catch. They **cannot be replaced, removed, modify** after being created.

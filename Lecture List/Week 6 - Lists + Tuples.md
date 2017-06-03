# Python Week 6 by P’ Kumamon (Lists + Tuples)

Copyright by P' Kumamon IT14.
For education purpose only

## Follow me on GitHub
![https://github.com/sagelga](https://www.dropbox.com/s/x5xk4trg3u82bcn/GitHub-Profile-Mobile.PNG?raw=1)

----------
# Introduction to Arrays
Array is a set of related data. In Python we have two difference types of array called List and Tuples.

# Introduction to Lists
Like a string, a list is a sequence of values. In string, the value are characters; in a list, they can be any type. The values in a list are called **elements** or sometimes **items**.

There are several ways to create a new list; the simplest is enclose the elements in square brackets ([ and ])

### Create an array
```python
kumamon = ['Kumamon', 'is', 'so', 'cute']
numbers = [1, 2, 3, 4]
blank = []
initiate = list()
```

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

# Adding More Elements to array
### Using .append()
```Python
kumamon = [1,2,3,4]
kumamon.append(5)

# kumamon now equals to
[1, 2, 3, 4, 5]
```

### Using .split()
```Python
How to use:
<variable name>.split("<separator you are using>")


text = "I am a happy Kumamon"
return text.split() # Returns array ['I', 'am', 'a', 'happy', 'Kumamon']

text = "I,am,a,happy,Kumamon"
return text.split(",") # Returns array ['I', 'am', 'a', 'happy', 'Kumamon']
```

### Add from other array
```python
text1 = ["Happy"]
text2 = ["Kumamon"]
return text1+text2

# Returns
["Happy", "Kumamon"]
```

# Modifying Elements in Array
### Using .sort() or sorted()
```python
kumamon = [1, 3, 4, 2, 5]
kumamon.sort()

# kumamon now equals to
[1, 2, 3, 4, 5]
```

### Using reversed sort
```Python
kumamon = [1, 3, 4, 2, 5]
kumamon.sort(reverse = True)

# kumamon now equals to
[5, 4, 3, 2, 1]
```

### Sort is from ASCII
```Python
kumamon = ['9', '1', 'a', 'A']
kumamon = kumamon.sort()

# kumamon now equals to
['1', '9', 'A', 'a']
```

# Using Elements in Array
### Using .pop()
.pop() will print then remove that item

### Using array call
```Python
kumamon = ["Happy", "Funny", "Fat"]
print(kumamon[1])

# Returns "Funny"
```

# Remove Elements in Array
### Using .remove()
.remove() will remove that element from the array

## Using .strip()
```Python
How to use:
<variable name>.strip("<character/text you want to remove>")
-> Returns the text that have been modified


text = "ABCDE"
return text.strip("A") # Returns "BCDE"

text = "ABCDEAAAA"
return text.strip("A") # Returns "BCDE"

text = "ABAACAABA"
return text.strip("AB") # Returns "C"
```

### Using .replace()
```Python
How to use:
<variable name>.replace(<text that you like to change>,<change into>)
-> Returns the text that have been modified


text = "Hello, my name is Kumamon"
return text.replace("Kumamon", "Rillakuma")
# Returns "Hello, my name is Rillakuma"
```

### Using .join()
```Python
How to use:
<separator you want to use>.join(<array variable>)
-> Return the new text that have been joined


text = ['I', 'am', 'a', 'happy', 'Kumamon']
print(" ".join(text)) # Prints out "I am a happy Kumamon"
```

---

# Introduction to Tuples
Tuples is an array, with a catch. They **cannot be replaced, removed, modify** after being created.

Syntactically, a tuple is a comma-separated list of values:
```Python
text = 'k', 'u', 'm', 'a', 'm', 'o', 'n'
```
Although it is not necessary, it is common to enclose tuples in parentheses:
```Python
text = ('k', 'u', 'm', 'a', 'm', 'o', 'n')
```
To create a tuple with a single element, you have to include a final comma:
```Python
t1 = 'a',
type(t1)
# Return <class 'tuple'>
```
A value in parentheses is not a tuple:
```Python
t2 = ('a')
type(t2)
# Return <class 'string'>
```
Another way to create a tuple is the build-in function tuple. With no argument, it creates an empty tuple:
```Python
t = tuple()
t
# Return ()
```

# Tuple assignment
It is often useful to swap the values of two variables. With conventional assignments, you have to use a temporary variable. For example, to swap a and b:
```Python
temp = a
a = b
b = temp
```
This solution is cumbersome; tuple assignment is more elegant:
```Python
a, b = b, a
```
The left side is a tuple of variables; the right side is a tuple of expressions. Each value is assigned to its respective variable. All the expressions on the right side are evaluated before any of the assignments.

The number of variables on the left and the number of values on the right have to be the same:
```Python
a, b = 1, 2, 3
# Return ValueError: too many values to unpack
```
More generally, the right side can be any kind of sequence (string, list or tuple). For example, to split an email address into a user name and a domain, you could write:
```Python
address = 'kumamon@kumamoto.me'
username, domain = address.split('@')
```
When you print out username and domain you will get:
```Python
print("Username :", username)
print("Domain :", domain)
# Returns
# Username : kumamon
# Domain : kumamoto.me
```
# Tuples as return values
Strictly speaking, a function can only return one value, but if the value is a tuple, the effect is the same as returning multiple values. For example, if you want to divide two integers and compute the quotient and remainder, it is inefficient to compute x/y and then x%y. It is better to compute them both at the same time.

The built-in function divmod takes two arguments and returns a tuple of two values, the quotient and remainder. You can store the result as a tuple:
```Python
result = divmod(7, 3)
print(result)
# Return (2, 1)
```
Or use tuple assignment to store the elements separately:
```Python
quotient, remainder = divmod(7, 3)
print("Quotient :", quotient)
print("Remainder :", remainder)
# Returns
# Quotient : 2
# Remainder : 1
```


# String to character stripping
```plain
Converge text (merge) -> .join()
Diverge text (separate) -> .split()

Replacing text (replace) -> .replace()
Stripping text (strip) -> .strip()
```

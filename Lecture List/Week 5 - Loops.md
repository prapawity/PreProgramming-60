# Python Week 5 by P’ Kumamon (Loops)

Copyright by P' Kumamon IT14.
For education purpose only

Follow me on GitHub!
[https://github.com/sagelga](https://github.com/sagelga)

----------
# Introduction to Loops
Q: Why do we need a loop?
A: It will simplify the use of coding and increse code quality

# Introduction to variable manipulator
### Using in
```python
How to use:
<text> in <text>

Example
"kumamon" in "kumamon is happy" # Returns True
"kumamoto" in "kumamon is happy" # Returns False
```
in is a tester that find the text within the text. Similarly to .find()

### Using range()
```python
How to use:
range(<stop>)
range(<start>, <stop>)

Example
range(10) -> 0,1,2,3,4,5,6,7,8,9
range(1,10) -> 1,2,3,4,5,6,7,8,9,10
```
range is a number array that continues the number as you like

# Introduction to For Loop
```python
How to use:
for <variable> in range(<stop>):
for <variable> in range(<start>,<stop>):

Example
for i in range(10):
    print(i, end=" ")

# Returns 0 1 2 3 4 5 6 7 8 9
```
"for i" is to start a loop. 'i' variable will be number consists of "in range(x,y)".

### For loop without range()
```python
for i in "Kumamon":
    print(i, end=" ")

# Returns "K u m a m o n"
```

### For loop using text array
```python
text = "Kumamon"
for i in range(len(text)):
    print(i, end=" ")

# Returns "K u m a m o n"
```

### For loop using array
```python
text = [1,2,3,4,5]
for i in range(len(text)):
    print(i, end=" ")

# Returns "1 2 3 4 5"
```

### Nested For loops
```python
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k)

# Returns
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
```

### Using For loops to call function
```python
def main():
    for i in range(2):
        for j in range(2):
            kumamon(i, j)

def kumamon(num1, num2):
    print(num1 + num2)

main()

# Returns
0
1
1
2
```

### Using for loops for n times
```python
for i in range(0,10):
    print(i, end=" ")

# Returns
0 1 2 3 4 5 6 7 8 9
```

### Applicate for loops with len()
```python
text = "1234567890"
for i in range(len(text)):
    print(i, end=" ")

# Returns
0 1 2 3 4 5 6 7 8 9
```

# Introduction to While Loop
```python
How to use:
while <arguments>:
    # Will runs this when the argument is true

Example:
count = 10
while count > 5:
    print("Hello")
    count--
```

### Infinite Loop
```python
while 1:
  print("This will go on and on forever....")

# Returns
This will go on and on forever....
This will go on and on forever....
This will go on and on forever....
...
...
...
# Programs will not end! Be aware!
```
### Work itself like FOR loops
```python
count = 10
while count != 0:
    print("Loop is now", count)
    count -= 1
```

# Loop types comparison
| Loop Type /
Sample Environment | **For**                                                          | **While**                                                   |
| ------------------------------ | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| Requires to start              | Length of loops                                                  | Argument that are true                                      |
| Loop Control                   | Controllable
(Using in range() or array)                         | Controllable
(Using break or making argument becomes false) |
| Stop when                      | - When they loop to the amount given
- When given break argument | - When argument is now false
- When given break argument    |
| Made for                       | Exact number of loops                                            | Exact way to stop the loops                                 |

# Using these to help
These can makes you get more of the loops.

| How to use   | **break**       | **continue**                 |
| ------------ | --------------- | ---------------------------- |
| **Benefits** | Stops the loop  | Reset the loop flow          |
| **For**      | Use as failsafe | Stop program from doing more |

### Using break()
```python
for i in range(10):
    print(i, end=" ")
    if i == 5:
        break

print("Loop is complete!")

# Returns
0 1 2 3 4 5 Loop is complete!
```
### Using continue()
```python
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")

print("Loop is complete!")

# Returns
0 1 2 3 4 6 7 8 9 Loop is complete!
```

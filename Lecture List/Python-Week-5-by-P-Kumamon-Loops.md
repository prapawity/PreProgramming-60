# Python Week 5 by P’ Kumamon (Loops)

# Table of Contents

**This is all contributed by P’ Kumamon. Enjoy.**

| **I/O**                            | **Functions**                            | **Strings**                            | **Condition**                            | **Loops**                            |
| ---------------------------------- | ---------------------------------------- | -------------------------------------- | ---------------------------------------- | ------------------------------------ |
| +Python Week 1 by P’ Kumamon (I/O) | +Python Week 2 by P’ Kumamon (Functions) | +Python Week 3 by P’ Kumamon (Strings) | +Python Week 4 by P’ Kumamon (Condition) | +Python Week 5 by P’ Kumamon (Loops) |

| **Lists and Tuples**                          | **Dict**                            | **Recursion**                            | **Minimal Code**                           | **Pylint Quality**                   |
| --------------------------------------------- | ----------------------------------- | ---------------------------------------- | ------------------------------------------ | ------------------------------------ |
| +Python Week 6 by P’ Kumamon (Lists + Tuples) | +Python Week 7 by P’ Kumamon (Dict) | +Python Week 8 by P’ Kumamon (Recursion) | +Python Extra by P’ Kumamon (Minimal Code) | +Python Extra by P’ Kumamon (PyLint) |

----------

**Please contribute these yourself naja. I hoped that you will find it useful one day…**

| Built-in Functions                 | Math Library                 | NumPy + MathPlotLib + SciPy + JuPyter |
| ---------------------------------- | ---------------------------- | ------------------------------------- |
| +Python Extra (Built-In Functions) | +Python Extra (Math Library) | +Python Extra (Data Visualization)    |

----------

Copyright by P' Kumamon IT14. 
For education purpose only

Follow me on GitHub! 
[https://github.com/sagelga](https://github.com/sagelga)

----------
# Introduction to Loops

Q: Why do we need a loop?
A: Your life is already a loop. You wake up, brush your teeth, and do some stuff. It goes on everyday. What about we make this loops be done by the power of compute?


# Introduction to variable manipulator

**Using in**

    How to use:
    <text> in <text>
    
    Example
    "kumamon" in "kumamon is happy" # Returns True 
    "kumamoto" in "kumamon is happy" # Returns False

**Using range()**

    How to use:
    range(<stop>)
    range(<start>, <stop>)
    
    Example
    range(10) -> 0,1,2,3,4,5,6,7,8,9
    range(1,10) -> 1,2,3,4,5,6,7,8,9,10
# Introduction to For Loop
    How to use:
    for <variable that will be use as counter> in range(<numeric number>)
    
    Example
    for i in range(10):
      print("Hello. This is the", i, "iteration") 
    
    # Returns
    Hello. This is the 0 iteration
    Hello. This is the 1 iteration
    Hello. This is the 2 iteration
    Hello. This is the 3 iteration
    Hello. This is the 4 iteration
    Hello. This is the 5 iteration
    Hello. This is the 6 iteration
    Hello. This is the 7 iteration
    Hello. This is the 8 iteration
    Hello. This is the 9 iteration

**For loop without range()**

    for i in "Kumamon":
      print(i, end=" ")
      
    # Returns
    K u m a m o n

**For loop using text array**

    text = "Kumamon"
    for i in range(len(text)):
      print(i, end=" ")
      
    # Returns
    K u m a m o n

**For loop using array**

    text = [1,2,3,4,5]
    for i in range(len(text)):
      print(i, end=" ")
    
    # Returns
    1 2 3 4 5 

**Nested For loops**

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

**Using For loops to call function**

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

**Using for loops for n times**

    for i in range(0,10):
      print(i, end=" ")
    
    # Returns
    0 1 2 3 4 5 6 7 8 9

**Applicate for loops with len()**

    text = "1234567890"
    for i in range(len(text)):
      print(i, end=" ")
    
    # Returns
    0 1 2 3 4 5 6 7 8 9 
# Introduction to While Loop
    How to use:
    while <arguments>:
      # Will runs this when the argument is true
      
    Example:
    count = 10
    while count > 5:
      print("Hello")
      count--

**Infinite Loop**

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

**Work itself like FOR loops**

    count = 10
    while count != 0:
      print("Loop is now", count)
      count -= 1


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

**Using break()**

    for i in range(10):
      print(i, end=" ")
      if i == 5:
        break
    print("Loop is complete!")
    
    # Returns 
    0 1 2 3 4 5 Loop is complete!

**Using continue()**

    for i in range(10):
      if i == 5:
        continue
      print(i, end=" ")
    print("Loop is complete!")
    
    # Returns
    0 1 2 3 4 6 7 8 9 Loop is complete!


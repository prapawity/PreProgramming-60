# Python Week 4 by P’ Kumamon (Condition)

Copyright by P' Kumamon IT14.
For education purpose only

Follow me on GitHub!
[https://github.com/sagelga](https://github.com/sagelga)

----------
# Introduction to condition flow

Condition flow makes the program think out of decision. Some decision is harder to make or some decision is complicate, Python has a cover for you.

# If statement

If statement will run when the argument is true.

    How to use:
    if <argument>:
      # This set of code will run when argument is true

    Example:
    kumamon = 12
    if kumamon > 10:
      print("Happy kumamon")

    Returns:
    "Happy kumamon"

**When If statement will not work**

    kumamon = 9
    if kumamon > 10:
      print("Heavy kumamon")

    Returns:


It returns nothing. Because the statement is now false

**Indentation on if statement**

    kumamon = 9
    if kumamon = 9 :
      print("Happy")
    print("Kumamon")

    # Returns
    Happy Kumamon

**If from variables**

    kumamon = 1
    if kumamon:
      print("Happy Kumamon")

    # Returns "Happy Kumamon"

**If from variables (cont)**

    kumamon = 10
    if kumamon:
      print("Happy Kumamon")

    # Returns "Happy Kumamon"
    --------------------------------------------
    kumamon = -1
    if kumamon:
      print("Happy Kumamon")

    # Returns "Happy Kumamon"

**If from variables (cont2)**

    kumamon = 0:
    if kumamon:
      print("Happy Kumamon")

    # Returns <none>
# If - Else statement

**Introduction to Else statement (Requires If statement)**

    kumamon = 9
    if kumamon > 10:
      print("Heavy kumamon")
    else:
      print("Cute kumamon")

    Returns:
    "Cute kumamon"

**Bound of Else to If**

    kumamon = 10
    if kumamon == 10:
      print("Happy Happy kumamon")
    if kumamon > 10:
      print("Heavy kumamon")
    else:
      print("Cute kumamon")

    Returns:
    "Happy Happy kumamon"
    "Cute kumamon"

**Else will not do when**

    kumamon = 10
    else:
      print("Happy Kumamon")

    # Returns Syntax Error
    (as they have no bound to if statement)
# If - Elif statement

If and elif is used together to make more decision than just a plain if statement.

**Introduction to Elif**

    kumamon = 10:
    if kumamon == 11:
      print("Happy Kumamon")
    elif kumamon == 10:
      print("Not Happy Kumamon")

    # Returns "Not Happy Kumamon

Elif statement is the else then if statement. It is the same as:

    kumamon = 10:
    if kumamon == 11:
      print("Happy Kumamon")
    else:
      if kumamon == 10:
        print("Not Happy Kumamon")

    # Returns "Not Happy Kumamon
# If - Elif - Else statement

You can pull the full power of Python by using these 3 statements

**Using in full potential**

    kumamon = 11
    if kumamon == 10:
      print("Happy Happy kumamon")
    elif kumamon > 10:
      print("Heavy kumamon")
    else: #This condition will run when kumamon < 10
      print("Cute kumamon")

    Returns:
    "Heavy kumamon"


# Nested control flow

Do anything you like, but beware of +Python Extra by P’ Kumamon (PyLint): 11.-Too-many-branch

**If Nested Flow**

    if kumamon > 5:
      if kumamon > 4:
        if kumamon > 3:
          if kumamon > 2:
            if kumamon > 1:
              print("Happy Happy Kumamon 1")
            print("Happy Happy Kumamon 2")
          print("Happy Happy Kumamon 3")
        print("Happy Happy Kumamon 4")
      print("Happy Happy Kumamon 5")

**More ultimate nested flow**

    if kumamon == 10:
      print("Happy Happy kumamon")
      if kumamon == 10:
        print("Happy Happy kumamon")
        if kumamon == 10:
          print("Happy Happy kumamon")
        elif kumamon > 10:
          print("Heavy kumamon")
        else:
          print("Cute kumamon")
      elif kumamon > 10:
        print("Heavy kumamon")
      else:
        print("Cute kumamon")
    elif kumamon > 10:
      print("Heavy kumamon")
    else:
      print("Cute kumamon")
      if kumamon == 10:
        print("Happy Happy kumamon")
      elif kumamon > 10:
        print("Heavy kumamon")
      else:
        print("Cute kumamon")

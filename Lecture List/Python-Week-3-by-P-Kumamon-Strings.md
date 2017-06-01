# “Python Week 3 by P’ Kumamon (Strings)

Copyright by P' Kumamon IT14.
For education purpose only

Follow me on GitHub!
[https://github.com/sagelga](https://github.com/sagelga)

----------
## YouTube video playlists
| **Part 1**                   | **Part 2**                   |
| ---------------------------- | ---------------------------- |
| https://youtu.be/2FV7yG0m-aU | https://youtu.be/Ds2XSKDZQ0s |

----------
# Strings index

How to remember how to use

    How to use:
    [start:stop:step]

    Start -> Start from what array number
    Stop -> Stop at what array number
    Step -> Skips every x array number

1-character printout

    var = "ABCD"
    print(var[0]) # Prints out "A" (A is in the 0th number array)

as visualized

| **Text**           | A | B | C | D |
| ------------------ | - | - | - | - |
| **Array Number**   | 0 | 1 | 2 | 3 |
| **Logical Number** | 1 | 2 | 3 | 4 |

Array Number always starts at 0 not 1!

**Inversed text printout**

    var = "ABCD"
    print(var[-1]) # Prints out "D" (D is the first one from the last)

**Overflow array**

    var = "ABCD"
    print(var[50]) # Returns error, as the 50th array number does not exist

**Multiple character printout**

    var = "ABCD"
    print(var[0:2])
    # Prints out "AB" (Start printing out from 0th to 1st array number

**Starts and Continue**

    var = "My name is Kumamon, and I love eating"
    print(var[4:])
    # Prints out "name is Kumamon, and I love eating" (Starting from 4th array number)

**Start from beginning to stop**

    var = "My name is Kumamon, and I love eating"
    print(var[:7])
    # Prints out "My name" (Starting from 0th array number to the 7th)

**Skips every**

    var = "ABABABAB"
    print(var[::2])
    # Prints out AAAA (Skips after logical number hits every 2, which is B)

**Inverse Skips every**

    var = "ABABABAB"
    print(var[::-2])
    # Prints out BBBB (Skips after logical number hits every -2, which is A)


----------
# Modifying Strings

NOTE: Please go take a look at Week 1. There is a few that you already know
+Python Week 1 by P’ Kumamon (I/O)

Variable Types and how to print like C

| **Use**      | %s     | %d      | %f    |
| ------------ | ------ | ------- | ----- |
| **To print** | String | Integer | Float |


**Doing it like C**

    var = "My name is Kumamon"
    print(">> %s <<" %var)
    # Prints out ">> My name is Kumamon <<"

**String Type Manipulation**

| Type      | %10s     | %-10s    | %.10s      | %-.10s     | %10.10s | %-10.-10s |
| --------- | -------- | -------- | ---------- | ---------- | ------- | --------- |
| For       | Aligning | Aligning | Cut String | Cut String | Both    | Both      |
| Alignment | Right    | Left     | Right      | Left       | Right   | Left      |

    text = "ABC"

    print("%4s" %text)
    # Prints out " ABC"

    print("%-4s" %text)
    # Prints out "ABC "

    print("%.2s" %text)
    # Prints out "AB"

    print("%-.2s" %text)
    # Prints out "AB"

    print("%5.2s" %text)
    # Prints out "   AB"

    print("%-5.2s" %text)
    # Prints out "AB   "


**Integer Type Manipulation**

| Type      | %10d     | %-10d    | %.10d      | %-.10d     | %10.10d | %-10.-10d | %0.10d                          |
| --------- | -------- | -------- | ---------- | ---------- | ------- | --------- | ------------------------------- |
| For       | Aligning | Aligning | Cut String | Cut String | Both    | Both      | Aligning                        |
| Alignment | Right    | Left     | Right      | Left       | Right   | Left      | Right
(Add 0 instead of space) |



    number = 12345

    print("%10d" %number)
    # Prints out "     12345"

    print("%-10d" %number)
    # Prints out "12345     "

    print("%.3d" %number)
    # Prints out "12345"

    print("%-.3d" %number)
    # Prints out "12345"

    print("%0.10d" %number)
    # Prints out 0000012345

**Float Type Manipulation**

| Type      | %10f     | %-10f    | %.10f      | %-.10f     | %10.10f | %-10.-10f |
| --------- | -------- | -------- | ---------- | ---------- | ------- | --------- |
| For       | Aligning | Aligning | Cut String | Cut String | Both    | Both      |
| Alignment | Right    | Left     | Right      | Left       | Right   | Left      |

    print("%10f" %number)
    # Prints out "123.456700"

    print("%-10f" %number)
    # Prints out "123.456700"

    print("%.2f" %number)
    # Prints out "123.46"

    print("%-.2f" %number)
    # Prints out "123.46"

    print("%10.3f" %number)
    # Prints out "   123.457"

    print("%-10.3f" %number)
    # Prints out "123.457   "
----------
# Strings to ASCII
http://www.asciitable.com/index/asciifull.gif


**String to ASCII (Decimal)**

    print(ord('A')) # Print out 65

**ASCII (Decimal) to String**

    print(chr(65)) # Print out 'A'

**Alters String ASCII**

    print(chr(65+1)) # Print out 'B'

**Referencing number from variable**

    var = 75
    print(chr(var)) # Print out 'K'

**Alters String ASCII from character**

    print(chr(ord('A')+1) # Print out 'B'


----------
# String to change case
    Convert character/text to lowercase -> .lower()
    Convert character/text to uppercase -> .upper()
    Convert character/text from lower to upper vice versa -> .swapcase()

    Check character/text is lowercase -> .islower()
    Check character/text is uppercase -> .isupper()
    Check character/text is a number -> .isdigit()
    Check character/text is an alphabet -> .isalpha()

**Using .lower()**

    text = "KUMAMON"
    text = "KuMaMoN"
    text = "kumamon"
    print(text.lower()) # All will print out "kumamon"

**Using .upper()**

    text = "KUMAMON"
    text = "KuMaMoN"
    text = "kumamon"
    print(text.upper()) # All will print out "KUMAMON"

**Using .swapcase()**

    text = "Kumamon"
    print(text.swapcase()) # Prints out "kUMAMON"

    text = "KuMaMoN"
    print(text.swapcase()) # Prints out "kUmAmOn"

******Using .isupper() & .islower()**

    How to use:
    <input variable>.islower()
    -> Returns True or False

    <input variable>.isupper()
    -> Returns True or False


    text = "K"
    return text.islower() # Returns false
    return text.isupper() # Returns true

    text = "k"
    return text.islower() # Returns true
    return text.isupper() # Returns false

**Using .isdigit() & .isalpha()**

    How to use:
    <input variable>.isdigit()
    -> Returns True or False

    <input variable>.isalpha()
    -> Returns True or False


    text = "12"
    return text.isdigit() # Returns true
    return text.isalpha() # Returns false

    text = "ABC"
    return text.isdigit() # Returns false
    return text.isalpha() # Returns true


----------
# String to character stripping
    Converge text (merge) -> .join()
    Diverge text (separate) -> .split()

    Replacing text (replace) -> .replace()
    Stripping text (strip) -> .strip()

**Using .split()**

    How to use:
    <variable name>.split("<separator you are using>")


    text = "I am a happy Kumamon"
    return text.split() # Returns array ['I', 'am', 'a', 'happy', 'Kumamon']

    text = "I,am,a,happy,Kumamon"
    return text.split(",") # Returns array ['I', 'am', 'a', 'happy', 'Kumamon']

**Using .join()**

    How to use:
    <separator you want to use>.join(<array variable>)
    -> Return the new text that have been joined


    text = ['I', 'am', 'a', 'happy', 'Kumamon']
    print(" ".join(text)) # Prints out "I am a happy Kumamon"

**Using .strip()**

    How to use:
    <variable name>.strip("<character/text you want to remove>")
    -> Returns the text that have been modified


    text = "ABCDE"
    return text.strip("A") # Returns "BCDE"

    text = "ABCDEAAAA"
    return text.strip("A") # Returns "BCDE"

    text = "ABAACAABA"
    return text.strip("AB") # Returns "C"

**Using .replace()**

    How to use:
    <variable name>.replace(<text that you like to change>,<change into>)
    -> Returns the text that have been modified


    text = "Hello, my name is Kumamon"
    return text.replace("Kumamon", "Rillakuma")
    # Returns "Hello, my name is Rillakuma"


----------
# String with array counts and find
    Finding character in text -> .find()
    Count character in text that satisfies search query -> .count()
    Finding text in array -> .index()

    Count all character in text -> len()

**Using .find()**

    How to use:
    <variable name>.find("<character/text you want to find>")
    -> Return as the lowest array number

    # 1 occurence character
    var = "ABCDE"
    return var.find("A") # Returns 0

    # 2 occurence character
    var = "ABCDEAAAAA"
    return var.find("A") # Returns 0

    # Non occurence character
    var = "ABCDE"
    return var.find("F") # Returns -1

    # Using more than 1 character
    var = "Kumamon is happy"
    return var.find("Kuma") # Returns 0

    # Using more than 1 character + 2 occurence
    var = "Kumamon is happy, Kumamon is happy"
    return var.find("Kuma") # Returns 0

**Using .count()**

    How to use:
    <variable name>.count("<character/text you want to count>")
    -> Returns the amount of character count.

    # 1 occurence character
    var = "ABCDE"
    return var.count("A") # Returns 1

    # 2 occurence character
    var = "ABCDEAAAAA"
    return var.count("A") # Returns 6

    # Non occurence character
    var = "ABCDE"
    return var.count("F") # Returns 0

    # Using more than 1 character
    var = "Kumamon is happy"
    return var.count("Kuma") # Returns 1

    # Using more than 1 character + 2 occurence
    var = "Kumamon is happy, Kumamon is happy"
    return var.count("Kuma") # Returns 2

**Using len()**

    How to use:
    len(<variable you want to count character>)
    Returns number of elements/character in array/text

    # Using to count strings
    return len("Kumamon") # Returns 7

    # Using to count strings in variable
    var = "Kumamon"
    return len(var) # Returns 7

    # Using to count elements in array
    var = [11,12,13,14,15]
    return len(var) # Retuns 5


# Strings to other base numeric number

**Using bin()**

    bin(<decimal integer>)
    # It is built in function
    # Returns the binary number (Base 2)
    https://docs.python.org/3/library/functions.html#bin

How to use bin()

    Example:
    print(bin(12345)) # Prints out 0b11000000111001

**Using hex()**

    hex(<decimal integer>)
    # It is built in function
    # Returns the hexadecimal number (Base 6)
    https://docs.python.org/3/library/functions.html#hex

How to use hex()

    Example:
    print(hex(12345)) # Prints out 0x3039

**Using oct()**

    oct(<decimal integer>)
    # It is a built in function
    # Returns the octadecimal (Base 8)
    https://docs.python.org/3/library/functions.html#oct

How to use oct()

    Example:
    print(oct(12345)) # Prints out 0o30071

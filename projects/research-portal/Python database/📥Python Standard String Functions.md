---
Creation Date: 9th Dec 2023
File Folder: 04_Capture
Link: "[[📥Strings Data type in Python]]"
tags: 
Status:
---
[[📥My Inputs]]

---
### Repetition
```python
str1 = "Python"
repeated = str1 * 3  # "PythonPythonPython"
print(repeated)
```

### Case Conversion

```python
str1 = "Hello World"
upper_str = str1.upper()  # "HELLO WORLD"
lower_str = str1.lower()  # "hello world"
print(upper_str)
print(lower_str)
```
### Remove White spaces

```python
# Removes white space from begining & end

str1 = "   Hello World   "
stripped_str = str1.strip()  # "Hello World"
print(stripped_str)
```

```python
mystr2 = " Hello Everyone "
x=mystr2.rstrip() # Removes all whitespaces at the end of the string
print(x)
```

```python
y=mystr2.lstrip() # Removes all whitespaces at the begining of the string
print(y)
```

```python
mystr2 = "*********Hello Everyone***********All the Best**********"
x=mystr2.strip('*') # Removes all '*' characters from begining & end of the string
print(x)
```

```python
mystr2 = "*********Hello Everyone***********All the Best**********"
x=mystr2.rstrip('*') # Removes all '*' characters at the end of the string
print(x)
```

```python
x=mystr2.lstrip('*') # Removes all '*' characters at the begining of the string
print(x)
```

### Replace 

```python
mystr2 = " Hello Everyone "
```

```python
x= mystr2.replace("He" , "Ho") #Replace substring "He" with "Ho"
print(x)
```

```python
y= mystr2.replace(" " , "") # Remove all whitespaces using replace function
print(y)
```

### Count
```python
mystr5 = "one two Three one two two three"
print(mystr5)
```

```python
x=mystr5.count("one") # Number of times substring "one" occurred in string.
print(x)
```

```python
x=mystr5.count("two") # Number of times substring "two" occurred in string
print(x)
```
### startswith and endswith

```python
x=mystr5.startswith("one") # Return boolean value True if string starts with "one"
print(x)
```


```python
x=mystr5.endswith("three") # Return boolean value True if string ends with "three"
print(x)
```

### Spilt String into substring

```python
mystr4 = "one two three four one two two three five five six seven six seven one"
print(mystr4)
```

```python
mylist = mystr4.split() # Split String into substrings mylist
print(mylist)
```

### String Alignment

```python
str2 = " WELCOME EVERYONE "
str2 = str2.center(100) # center align the string using a specific character
print(str2)
```

```python
str2 = " WELCOME EVERYONE "
str2 = str2.center(50,'*') # center align the string using a specific character
print(str2)

```

```python
str2 = " WELCOME EVERYONE "
str2 = str2.rjust(50) # # Right align the string using a specific character
print(str2)
```


```python
str2 = " WELCOME EVERYONE "
str2 = str2.rjust(50,'*') # Right align the string using a specific character
print(str2)

```
### find, and index

```python
str4 = "one two three four five six seven"
loc = str4.find("five") # Find the location of word 'five' in the string "str4"
print(loc)

```

```python
str4 = "one two three four five six seven"
loc = str4.index("five") # Find the location of word 'five' in the string "str4"
print(loc)

```

### String property

```python
mystr6 = '123456789'
print(mystr6.isalpha()) # returns True if all the characters in the text are letter
print(mystr6.isalnum()) # returns True if a string contains only letters or number
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9)
```

```python
mystr7 = 'ABCDEF'
print(mystr7.isupper()) # Returns True if all the characters are in upper case
print(mystr7.islower()) # Returns True if all the characters are in lower case
```

```python
str6 = "one two three four one"
loc = str6.rfind("one") # last occurrence of word 'one' in string "str6"
print(loc)
```

```python
loc = str6.rindex("one") # last occurrence of word 'one' in string "str6"
print(loc)
```

Using Escape Character

```python
#Using double quotes in the string is not allowed.
mystr = "My favourite TV Series is "Game of Thrones""
print(mystr)
```

```python
#Using escape character to allow illegal characters
mystr = "My favourite series is \"Game of Thrones\""
print(mystr)
```

Review

**`zfill()`**: Adds zeros at the beginning of the string until it reaches the specified length.

- Example: `"42".zfill(5)` returns `"00042"`.


1. **`isdigit()`**: Returns `True` if all characters in the string are digits, otherwise `False`.
    
    - Example: `"1234".isdigit()` returns `True`.
2. **`isspace()`**: Returns `True` if all characters in the string are whitespace, otherwise `False`.
    
    - Example: `" ".isspace()` returns `True`.

1. **`lstrip()`**: Removes leading (left-side) whitespaces.
    
    - Example: `" python".lstrip()` returns `"python"`.
2. **`rstrip()`**: Removes trailing (right-side) whitespaces.
    
    - Example: `"python ".rstrip()` returns `"python"`.
1. **`title()`**: Converts the first character of each word to uppercase and remaining characters to lowercase.
    
    - Example: `"python programming".title()` returns `"Python Programming"`.
2. **`swapcase()`**: Converts uppercase characters to lowercase and vice versa.
    
    - Example: `"PyThOn".swapcase()` returns `"pYtHoN"`.

**`capitalize()`**: Capitalizes the first character of a string and makes all other characters lowercase.

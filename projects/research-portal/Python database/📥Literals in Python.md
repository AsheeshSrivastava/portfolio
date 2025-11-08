---
Creation Date: 1st Dec 2023
File Folder: 02_Fleeting Note
aliases: 
tags:
  - 📥FleetingNote
Status: "#📥/🟨"
Category: Python Programming
Started: 1st Dec 2023
Finished: 
Rating: 
Link: 
Subject: Python Basics - Programming Components
---
Links: [[📥My Inputs]]

---
# ==📥Literals in Python==
---
- **Source:** [URL or location]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
- **Keywords:** [ ], [ ]
---
In Python, literals are data items that are constant values. They are the simplest form of expressing value in Python and are used to represent fixed values in your code. Python has various types of literals which can be broadly classified into the following categories:

1. **Numeric Literals**: These are immutable (unchangeable) numbers used directly in expressions. They can be of three types:
	   - **Integer (Base 10 or Decimal)**: These are the most common numerical literals and represent whole numbers in base 10 (the decimal system). Examples include `42`, `-7`, `2023`. They consist of digits from 0 to 9.
	   - **Binary (Base 2)**: Binary literals represent numbers in base 2, which means they only use the digits `0` and `1`. In Python, binary literals are prefixed with `0b` or `0B`. For example, the binary literal `0b101` represents the decimal number `5`.
	   - **Octal (Base 8)**: Octal literals are used to represent numbers in base 8, using digits from `0` to `7`. They are prefixed with `0o` or `0O` (zero followed by a lowercase or uppercase letter 'o'). For example, the octal literal `0o123` represents the decimal number `83`.
	   - **Hexadecimal (Base 16)**: Hexadecimal literals are used for base 16 numbers, employing digits from `0` to `9` and letters from `A` to `F` (or `a` to `f`). They are prefixed with `0x` or `0X`. For instance, the hexadecimal literal `0x1A3F` represents the decimal number `6719`.
	   - **Float**: Float literals represent real numbers, usually containing a decimal point. They can also be represented in scientific notation with an 'e' or 'E' indicating the power of 10. Examples include `3.14`, `-0.001`, and `1.5e2` (which is `150.0`).
	   - **Complex**: Complex number literals in Python have a real part and an imaginary part, with the imaginary part followed by a `j` or `J`. For example, `3+5j` represents a complex number with a real part of `3` and an imaginary part of `5`.

	Yes, binary, octal, and hexadecimal numbers are indeed literals in Python. They are just different ways to represent integer values using various number bases, and Python provides direct support for these formats. When you use these literals in your code, Python understands and processes them as integer values, but in the specified base.
2. **String Literals**: A string literal is a sequence of characters enclosed in quotes. Python supports both single (`'Hello'`) and double (`"World"`) quotes to represent string literals. Additionally, Python has triple-quoted strings (`'''` or `"""`) that can span multiple lines and include line breaks.
    
3. **Boolean Literals**: There are two Boolean literals in Python: `True` and `False`. They are used to represent the truth values in a logical expression.
    
4. **Special Literal - None**: In Python, `None` is a special literal used to denote the absence of a value or a null value. It's often used as a placeholder for optional or missing value.
    
5. **Collection Literals**: These are literals for different collection types in Python:
    
    - **List Literals**: Defined by square brackets `[]`, e.g., `[1, 2, 3]`.
    - **Tuple Literals**: Defined by parentheses `()`, e.g., `(1, 2, 3)`.
    - **Dictionary Literals**: Consist of key-value pairs enclosed in curly braces `{}`, e.g., `{'a': 1, 'b': 2}`.
    - **Set Literals**: Defined by curly braces `{}` with comma-separated values, e.g., `{1, 2, 3}`. However, an empty set must be defined with `set()`, as `{}` represents an empty dictionary.

In Python, literals and data types are related concepts but they serve different purposes:

1. **Literals**:
    
    - **Definition**: Literals are the raw data given in a variable or constant. They are the simplest form of expressing value in Python.
    - **Usage**: You use literals to represent values in your code. For example, when you write `5`, `"Hello"`, or `[1, 2, 3]`, you are directly using literals to denote an integer, a string, and a list, respectively.
    - **Types of Literals**: Python supports various types of literals like numeric (integer, float, complex), string, boolean, and collection literals (list, tuple, dictionary, set).
2. **Data Types**:
    
    - **Definition**: Data types are the classification or categorization of data items. They represent the kind of value that tells what operations can be performed on a particular data.
    - **Usage**: Data types are used to define how a programming language handles different literals or variables. When you declare a variable in Python, its data type determines what kind of operations you can perform on it and how it is stored.
    - **Common Data Types**: Python's common data types include integers (`int`), floating-point numbers (`float`), complex numbers (`complex`), strings (`str`), booleans (`bool`), and various collection types like lists (`list`), tuples (`tuple`), dictionaries (`dict`), and sets (`set`).

**Key Differences**:

- **Nature**: Literals are the actual values, while data types are the categories that these values belong to.
- **Role in Code**: A literal is a way to write a value directly in the code, whereas a data type is a conceptual classification that dictates how a programming language interprets these literals or variables.
- **Association**: Every literal belongs to a certain data type. For example, `123` is a literal of the data type `int`, and `"Python"` is a literal of the data type `str`.

Understanding the distinction between literals and data types is crucial in Python programming, as it helps in determining how data is stored, manipulated, and used in your programs.

### Complex numbers
- combination of real number and imaginary number

```python
c1 = 6 + 5j
```

```python
print(c1)
```

```python
# j = square root of -1
```

### Boolean literal

- True
- False


### Special Literal

None

```python
val1 = False
```

```python
val2 = True
```

```python
val3 = None
```

### Strings

- Sequence of characters enclosed within quotes ('', "", '''''', """""")

```python
s1 = 'Hello'
```

```python
name = "Mark"
```

```python
s2 = '''Welcome to Python'''
```

```python
s3 = """We are learning components of Python"""
```

```python
st1 = 'This is Python's class'
```

```python
st1 = "This is Python's class"
```

```python
print(st1)
```

```python
ver = 'Python3.10.3'
```

```python
st3 = "100"
```

```python
st4 = "Hello everyone
Python is fun"
```

```python
st4 = """Hello everyone
Python is fun"""
```

```python
print(st4)
```

---
# Context/Source/Trigger
- **Related to**: [[📥Python Basics]]
# Relevance:

- <mark style="background: #FFB86CA6;">Briefly state why this captured your interest or how it might be relevant to your goals or projects.</mark>
---
- Literals are a fundamental aspect of Python, and understanding them is essential for writing effective Python code.

- Understanding the distinction between literals and data types is crucial in Python programming, as it helps in determining how data is stored, manipulated, and used in your programs.
# Possible Actions
- [ ] Convert to Literature note
- [ ] Add to task list
- [ ] Link to existing notes

# Linked Resources
[[📥Python Programming Components]]

---

*Fleeting notes are temporary and should be reviewed regularly to migrate valuable insights to `Areas`, `Resource`, or `Projects`.*
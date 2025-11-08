---
title: Python Programming Components
Creation Date: 1st Dec 2023
File Folder: 01_Online Course
Category: Python Programming
tags:
  - "#📥LectureNotes"
Status: "#📥/🟩"
aliases: 
Link: "[[📥Python Basics]]"
Subject: Python Basics - Programming Components
Started: 30th Nov 2023
---
[[📥My Inputs]]
# ==Python Programming Components==
---
- **Source:** [URL or location pr Platform]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
 - Class Information
	- **Course Name**: 
	- **Instructor**: 
	- **Topic**:
- **Keywords:** [ ], [ ]
---
# Key Points
- Literals:: Data or value that is stored
<!--SR:!2023-12-09,3,252-->
<!--SR:!2023-12-09,3,252-->

```python
a= 100 # 100 is a literal
name = "Mark" # Mark is a literal 
```
# Detailed Notes

### Comments in Python
[[📥Comments in Python| Comments]] can be used to explain the code for more readability.
### Keywords and Identifiers in Python
#flashcards 
Keywords:: Keywords are the reserved words in Python and can’t be used as identifier.
<!--SR:!2023-12-08,2,230-->

These words are crucial to the language's syntax and structure. They are used to define the structure and layout of the Python language and cannot be used as identifiers, i.e., you cannot name your variables or functions with these words.

```python
import sys
import keyword
import operator
from datetime import datetime
import os
print(keyword.kwlist) # List of all Python Keywords
```

- Keywords in python:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

```python
len(keyword.kwlist) 
```

#flashcards 
Python contains keywords (number):: 35
<!--SR:!2023-12-20,14,290-->

#flashcards 
Identifiers:: name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another.
<!--SR:!2023-12-07,1,232-->

**Rules for Naming**:

- Identifiers can be a combination of letters in lowercase or uppercase (`a` to `z`, `A` to `Z`), digits (`0` to `9`), or an underscore `_`.
- An identifier cannot start with a digit.
- Keywords cannot be used as identifiers.
- Identifiers are case-sensitive (e.g., `myVar` and `myvar` are two different identifiers).
- Special symbols like `@`, `$`, `%` are not allowed in identifiers.

1. **Best Practices**:
    
    - Use descriptive names for better readability (e.g., `student_name` instead of `sn`).
    - Follow naming conventions like CamelCase for classes (e.g., `MyClass`) and lowercase with underscores for variables and functions (e.g., `my_variable`).

Understanding these basics is crucial as they form the foundation of writing syntactically correct and readable Python code.

### Statements in Python
#flashcards 
Statements in Python::  Instructions that a Python interpreter can execute.
<!--SR:!2023-12-07,1,232-->

```python
# Single line statement
p1 = 10 + 20
print(p1)
```

```python
# Single line statement
p2 = ['a', 'b', 'c', 'd']
print(p2)
```

```python
# Multiple line statement 
p3 = 20 + 30 \ 
     + 40 + 50 \ 
     + 70 + 80 
print(p3)
```

The error message you're seeing , "unexpected character after line continuation character," usually occurs when there is an unexpected character following the line continuation backslash (`\`). In your screenshot, it's not entirely clear what that character is, but common issues include:

- A space or some other invisible character after the `\` at the end of a line.
- An additional `+` sign after the `\` which is unnecessary and incorrect.

To fix this, make sure that:

- ==The backslash (`\`) is the last character on the line with nothing after it, not even a space==.
- Each subsequent line should start with an operator if the line is continuing an expression.

The corrected version of your code should look like this:
```python
# Multiple line statement
p3 = 20 + 30 \
     + 40 + 50 \
     + 70 + 80
print(p3)

```

```python
# Multiple line statement
p4 = ['a' ,
	  'b' , 
	  'c' , 
	  'd' ] 
print(p4)
```

### Indentation in Python
#flashcards 
Indentation in python refers to:: the spaces at the beginning of a code line.
<!--SR:!2023-12-09,3,252-->

It is very important as Python uses indentation to indicate a block of code. ==If the indentation is not correct we will end up with IndentationError error==.


```python
p = 10
if p == 10: 
	print ('P is equal to 10') # correct indentation
```

```python
# if indentation is skipped we will encounter "IndentationError: expected an inde 
p = 10
if p == 10:
print ('P is equal to 10')
```

```python
for i in range(0,5): 
	print(i) # correct indentation
```

```python
# if indentation is skipped we will encounter "IndentationError: expected an index
for i in range(0,5): 
print(i)
```

```python
# if indentation is skipped we will encounter "IndentationError: expected an inde 
for i in range(0,5): print(i) #correct indentation but less readable
```

```python
j=20 
for i in range(0,5):
	print(i) # inside the for loop 
print(j) # outside the for loop
```

### Docstrings in Python
#flashcards 
- Docstrings in python::  provide a convenient way of associating documentation with functions, classes, methods or modules.
<!--SR:!2023-12-07,1,232-->

- They appear right after the definition of a function, method, class, or module

```python
def square(num): 
	'''Square Function :- This function will return the square of a number''' 
	return num**2
```

```python
square(2)
```

```python
square.__doc__ # We can access the Docstring using __doc__ method
```

```python
def evenodd(num): 
	'''evenodd Function :- This function will test whether a numbr is Even or Odd '''
	if num % 2 == 0: 
		print("Even Number") 
	else:
		 print("Odd Number")
```

```python
evenodd(3)
```

The above snippet shows a Python function named `evenodd` which is designed to print "Even Number" if the number passed to it is even, and "Odd Number" if the number is odd. The function is called with the argument `3`, which correctly results in "Odd Number" being printed.

The `None` you see in the output is a result of the function not returning any value explicitly. In Python, if a function doesn't have a return statement, or if the return statement doesn't have an accompanying value, the function returns `None` by default. In many interactive Python environments, including Jupyter Notebooks and certain IDEs, `None` is printed out as the result of a function call if the function doesn't return anything other than `None`. However, if you were to run this code in a script file instead of an interactive environment, you would not see the `None` output.

To avoid seeing `None` in an interactive environment, you could include a return statement in your function that returns a value or simply `return None` explicitly, although this is not necessary and doesn't change the fact that `None` is the implicit return value.

```python
def evenodd(num):
    """evenodd Function :- This function will test whether a number is Even or Odd"""
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

result = evenodd(3)
print(result)

```

```python
evenodd.__doc__
```
#### Return vs Print in a function
Whether to use `return` or `print` directly in a function depends on the context of its use and what you're trying to achieve with the function:

1. **Using `return`:**
    
    - **Modularity:** When you want to use the result of the function elsewhere in your code, you should use `return`. This allows you to capture the output of the function in a variable and use it for further operations.
    - **Reusability:** Returning values makes your function more reusable in different contexts.
    - **Testing:** It's easier to write tests for functions that return values rather than print them.
    - **Control Flow:** You can decide later how to handle the returned value, whether it's printing it, logging it, or using it in conditional statements.
2. **Using `print`:**
    
    - **Simplicity:** For small scripts or when you're just writing a function to display information to the user and not to be used as part of a larger program, `print` is straightforward.
    - **Debugging:** Sometimes, `print` is used for debugging purposes, to show the state of variables or the flow of the program.

In summary, `return` is often considered better practice for functions that will be part of larger programs or libraries, while `print` might be used for simple scripts or debugging. It's best to use `return` when you want to maintain good modularity and reusability in your code.

### Variables
#flashcards 
- A [[📥Variables in Python| Variable]]: is a reserved memory location to store values.
- A variable is created the moment you first assign a value to it.
```python
q = 30
```

```python
id(q)
```

#flashcards 
id() function::: returns the “identity” of the object.
<!--SR:!2023-12-07,1,232!2023-12-09,3,252-->

- The identity of an object 
	- Is an integer 
	- Guaranteed to be unique 
	-  Constant for this object during its lifetime. 

```python
hex(id(q)) # Memory address of the variable
```
### [[📥Literals in Python|Literals]]

#flashcards 
Literals:: Data or value that is stored

```python
a= 100 # 100 is a literal
name = "Mark" # Mark is a literal 
```

### Constants  

In Python, constants are a type of variable whose value remains constant throughout the program. Once defined, their value should not be altered. While Python doesn't have built-in support for constants in the same way that some other languages do (like `const` in JavaScript or `final` in Java), you can create constants by convention.

Here are some key points about constants in Python:

1. **Naming Convention**: By convention, constants are usually defined with all uppercase letters and underscores separating words. For example, `MAX_SIZE` or `PI`.
    
2. **Declaration and Usage**: Constants are declared and used like any other variable. They are typically defined at the top of a Python file and meant to be used globally throughout the code. For example:

	```python
	MAX_CONNECTIONS = 50
	```
	
	```python
	GRAVITY = 9.8
	```
	
	```python
	print(GRAVITY)
	```

3. **Immutability**: Unlike true constants in some other languages, constants in Python can technically be changed. However, it's a strong convention not to alter them after they are set. This immutability is more of a guideline than a strict rule enforced by the language.
4. **Global Constants**: Constants are often used to define values that should remain unchanged throughout the execution of the program and have a global scope. This makes the code more readable and easier to maintain.
5. **Modules for Constants**: In larger programs, constants might be defined in a separate module or file and then imported where needed. This centralizes the constants, making them easier to manage.
    
	```python
	GRAVITY = 10
	```
	
	```python
	print(GRAVITY)
	```

Remember, the concept of constants in Python is more about using a convention to signal to other programmers that these values should not be changed, rather than any enforced immutability by the language itself.

### Expressions

What are expressions in python. How is to different from Statement. What is suites and block?
  
In Python, the concepts of expressions, statements, suites, and blocks are fundamental to understanding how the language structures and executes code. Here's a breakdown of each:
#### Expressions

- **Definition**: An expression in Python is a combination of values, variables, operators, and calls to functions that are evaluated and return a value. For example, `2 + 3`, `x * y`, and `my_function()` are all expressions. The evaluation of an expression always produces or returns a result value.
- **Characteristics**: Expressions need to be evaluated. If you type an expression on its own in a Python interpreter, it will show you the expression's value.
#### Statements

- **Definition**: A statement is an instruction that a Python interpreter can execute. While an expression is just a part of a statement, a statement does something. It might display a value, assign a value, or alter the flow of execution.
- **Differences from Expressions**:
    - **Purpose**: Statements do something; expressions evaluate to something.
    - **Examples**: An assignment like `x = 5` is a statement. A `while` loop or an `if` statement is also a statement. These do not evaluate to a value but rather perform an action or a series of actions.
    - **Completeness**: A statement is more complete than an expression. An expression can be part of a statement.
#### Suite

- **Definition**: In Python, a suite is a group of statements controlled by a clause. A suite can be a single line or a block of code. Suites are typically found in compound statements (statements that consist of one or more clauses).
- **Usage**: For example, in a `for` loop, the suite is the block of code that is executed repeatedly. It's often indented under the line with the `for` statement.
#### Block

- **Definition**: A block is a combination of all these statements and expressions. It is a piece of Python program text that is executed as a unit. The most common type of block is a compound statement, like what you see in `if`, `for`, `while`, and `try` statements.
- **Characteristics**: Blocks are defined by their indentation level, which follows Python's strict indentation rules. This means that all statements in a block are indented by the same amount.

To summarize:

- **Expressions** produce or calculate a value.
- **Statements** are the actual commands that the Python interpreter executes (like a command to do something).
- **Suites** are groups of statements under a control structure, like a loop or conditional.
- **Blocks** are larger structures, often consisting of multiple statements and expressions, defined by indentation in Python.

```python
# Expression examples
result = 3 + 5  # '3 + 5' is an expression
value = x * y   # 'x * y' is an expression, assuming x and y are defined

```

```python
# Statement examples
x = 10          # Assignment statement
print(x)        # Print statement (function call)

# Compound statement
if x > 5:       # 'if' statement
    print("x is greater than 5")  # This line is also a statement

```

```python
# Suite examples
if x < 15:
    y = x + 5   # This is a suite consisting of a single statement
    print(y)    # This is also part of the suite

```

```python
# Block example
for i in range(5):  # The for statement
    print(i)        # First line of the block
    if i % 2 == 0:  # Second line of the block, which is also a statement introducing another block
        print(f"{i} is even")  # Part of the inner block under the 'if' statement

```

What is the difference between Suite and Blocks?
	The terms "suite" and "block" in Python are closely related and sometimes used interchangeably, but they have specific meanings in the context of Python's syntax and structure. Here's a clarification of the difference between them:

- Suite

	- **Definition**: In Python, a suite refers to a group of individual statements, which is usually a part of a compound statement like `if`, `for`, `while`, etc. The suite represents the set of statements that are executed as part of the compound statement.
	- **Characteristics**:
	    - A suite is typically introduced by statements that end with a colon (`:`), such as `if`, `elif`, `else`, `for`, `while`, `try`, `except`, `with`, `def`, and `class`.
	    - The statements in a suite are usually written in a block of lines indented the same amount from the left.
		```python
		if condition:
	    # This is a suite
	    statement1
	    statement2
	
	```
-  Block

	- **Definition**: A block in Python refers to a group of code that is treated as a single unit. It is often a larger structure that can consist of multiple statements and expressions.
	- **Characteristics**:
	    - A block is defined by its indentation level, following Python's indentation rules.
	    - Blocks are essential in Python because the language uses indentation to define the scope and grouping of statements.
	    - Blocks can contain one or more suites, and they often represent the body of a function, loop, if statement, etc.

		```python
		# Block starting with the for statement
		for i in range(5):
		    # This is a suite inside the block
		    print(i)
		    if i % 2 == 0:
		        # This is another suite inside the block
		        print(f"{i} is even")
		
		```
# Action Items
- [ ] Review class recording
- [ ] Summarize key concepts
- [ ] Migrate relevant information to Areas/Resources/Projects

# References
- 

# Linked Notes
%%  tp.file.include("[Index of Related Notes]") %> %%
[[📥Python Basics]]
[[🗺️ 🐍 Python MOC]]
[[📥Python Introduction]]

---

*This note is initially captured under `Capture` and can be later moved to `Areas`, `Resource`, or `Projects`.*

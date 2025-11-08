---
Creation Date: 30th Nov 2023
File Folder: 02_Fleeting Note
aliases: 
tags:
  - 📥FleetingNote
Status: "#📥/🟨"
Category: Exams and Preperation
Started: 30th Nov 2023
Finished: 
Rating: 
Link: "[[🚧Python Module Exam]]"
Subject: Python
---
Links: [[📥My Inputs]]

---
# ==📥MCQs for Python Exam==
---
- **Source:** [ChatGpt-PyData Buddy]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
- **Keywords:** [ ], [ ]
---
### Comments in Python
#flashcards 
**Purpose of a comment in Python code**:: To explain the code and make it more readable
<!--SR:!2023-12-13,7,250-->
**Symbol for single-line comment**:: `#`
<!--SR:!2023-12-22,16,290-->
**How to write multi-line comments in Python**:: Enclosing the comment within triple quotes `'''` or `"""`
<!--SR:!2023-12-16,10,270-->
**True statement about comments in Python**:: Comments are used to document the purpose and functionality of the code.
<!--SR:!2023-12-17,11,270-->
**Why are comments useful for code maintenance in Python**:: They help in understanding the purpose and functionality of the code
<!--SR:!2023-12-12,6,250-->
**Recommended practice for writing comments in Python**:: Comments are best used for explaining tricky parts of the code where the reasoning might not be immediately obvious
<!--SR:!2023-12-15,9,250-->
### Python Keywords

Which of the following is a valid use of a Python keyword?
 - `class MyClass: pass`

	**Explanation**: Option C is the correct usage of the keyword `class` to define a new class. Options A, B, and D are incorrect as they attempt to assign values to keywords, which is not allowed in Python.

Which of the following is a valid use of Python keywords?
A) `import my_module` B) `return = "data"` C) `if(condition): pass` D) `True = 1`
 -  `import my_module`

	**Explanation**: Option A correctly uses the `import` keyword to import a module. Options B, C, and D misuse Python keywords, which is not allowed.

What is the output of the following Python code snippet?
```python
def check():
	return "Keyword Check" 
print(check)
```
A) `Keyword Check` B) `<function check at 0x...>` C) Syntax Error D) None

 - `<function check at 0x...>`

	**Explanation**: The code prints the memory address of the function `check`, not its return value, because the function is not called (`check()` would call it).

How many keywords are there in Python as of the latest version?
  - 35

### Python Identifiers, Statements, Docstrings, and Indentation

Which of the following is a valid Python identifier?
   - `variable_name`
	**Explanation**: Option B is a valid identifier as it follows the naming rules for Python identifiers. Option A is incorrect because identifiers cannot start with a digit. Option C uses a hyphen, which is not allowed. Option D is a Python keyword and cannot be used as an identifier.

Which of the following are valid Python identifiers? Select all that apply.

A) `_my_var` B) `1_variable` C) `variableOne` D) `for`

 - **Correct Answers**: A) `_my_var` and C) `variableOne`

	**Explanation**: A and C are valid identifiers. B starts with a digit, which is not allowed, and D is a Python keyword.

What is a primary rule to follow while naming identifiers in Python?
A) Identifiers must contain special characters like `@` or `#`. B) Identifiers can start with a digit. C) Identifiers must be descriptive and lengthy. D) Identifiers cannot be the same as a keyword.

  - **Correct Answer**: D) Identifiers cannot be the same as a keyword.

	**Explanation**: Identifiers cannot be keywords. They should also follow other rules, like not starting with a digit and not including special characters. They should be descriptive but not necessarily lengthy.

 Which of the following is NOT a valid identifier in Python?
a) `_myVariable1`  
b) `2ndVariable`  
c) `variable_name`  
d) `variableName`

  - Answer: b) `2ndVariable`

What is the correct way to handle line continuation in Python?
a) End the line with a comma `,`  
b) Use a semicolon `;` at the end of the line  
c) Place a backslash `\` at the end of the line  
d) Enclose the line in parentheses `()`

 -  Answer: c) Place a backslash `\` at the end of the line

What will happen if you skip indentation in a Python `if` statement?

a) The code will execute without any issues  
b) Python will automatically correct the indentation  
c) An `IndentationError` will occur  
d) The `if` condition will always evaluate to `True`

 - Answer: c) An `IndentationError` will occur


Which of the following is true about docstrings in Python?

a) They are comments used for code documentation  
b) They must be written at the beginning of a script  
c) They are used to improve the performance of functions  
d) They provide a convenient way of associating documentation with Python functions, classes, methods, or modules

 - Answer: d) They provide a convenient way of associating documentation with Python functions, classes, methods, or modules

What will be the output of the function `evenodd(3)`?

a) Even Number  
b) Odd Number  
c) 3  
d) None

 - Answer: b) Odd Number

In Python functions, what is the advantage of using `return` over `print`?

a) `return` displays the result to the user  
b) `return` allows the function output to be used elsewhere in the code  
c) There is no difference between `return` and `print`  
d) `print` is used for debugging, while `return` is not

 - Answer: b) `return` allows the function output to be used elsewhere in the code

### Constants, Expression, Statement, Suite and Block
#### Constants

1. **Which of the following is a convention for naming constants in Python?**
    
    - A. All lowercase letters
    - B. CamelCase notation
    - C. All uppercase letters
    - D. Starting with an underscore
    
    **Answer: C. All uppercase letters**
    
2. **In Python, constants are:**
    
    - A. Built-in types that cannot be changed
    - B. Defined using a specific keyword like `const` or `final`
    - C. Variables whose values should not be changed, as per convention
    - D. Automatically enforced by the Python interpreter
    
    **Answer: C. Variables whose values should not be changed, as per convention**
    
3. **Where are constants typically defined in a Python program?**
    
    - A. At the bottom of the Python file
    - B. Inside functions where they are used
    - C. At the top of the Python file
    - D. Inside a class definition
    
    **Answer: C. At the top of the Python file**
    

#### Suites

4. **In Python, what is a suite?**
    
    - A. A collection of libraries and modules
    - B. A single Python file
    - C. A group of statements controlled by a clause like `if`, `for`, etc.
    - D. A special function
    
    **Answer: C. A group of statements controlled by a clause like `if`, `for`, etc.**
    
5. **Which of the following is true about a suite in Python?**
    
    - A. It cannot contain other suites
    - B. It is defined by using parentheses
    - C. It is defined by the indentation level
    - D. It always consists of a single statement
    
    **Answer: C. It is defined by the indentation level**

**Consider the following code snippet. What does it represent in Python?**
```python
if x > 10:
    print("x is greater than 10")
    y = x - 5

```

- A. A function
- B. A suite
- C. A block
- D. An expression

**Answer: B. A suite**

#### Expressions

7. **What is an expression in Python?**
    
    - A. A piece of code that performs an action
    - B. A combination of values, variables, and operators that yields a result
    - C. A conditional statement like `if` or `while`
    - D. A definition of a function or class
    
    **Answer: B. A combination of values, variables, and operators that yields a result**
    
8. **Which of the following is an example of an expression in Python?**
    
    - A. `x = 5`
    - B. `print("Hello World")`
    - C. `3 + 4`
    - D. `def my_function():`
    
    **Answer: C. `3 + 4`**
    

#### Statements

9. **What defines a statement in Python?**
    
    - A. An instruction that Python can execute
    - B. A piece of code that returns a value
    - C. A comment in the code
    - D. A module import
    
    **Answer: A. An instruction that Python can execute**
    
10. **Which of the following is a statement in Python?**
    
    - A. `5 * 5`
    - B. `"Hello" + "World"`
    - C. `x = 10`
    - D. `len("Python")`
    
    **Answer: C. `x = 10`**
    

#### Suites and Blocks

11. **In Python, what differentiates a block from a suite?**
    
    - A. A block is a single line of code, while a suite is multiple lines
    - B. A block can contain multiple suites, but a suite cannot contain a block
    - C. A suite is used for error handling, whereas a block is not
    - D. A block is always inside a function, while a suite is not
    
    **Answer: B. A block can contain multiple suites, but a suite cannot contain a block**
    
12. **Consider the following code. What does it represent?**
```python
for i in range(3):
    print(i)
    if i == 1:
        print("One")
```
- A. A block
- B. An expression
- C. A statement
- D. A suite

**Answer: A. A block**

---
# Context/Source/Trigger
- **Related to**: 
[[🚧Python Module Exam]]
# Relevance:

- <mark style="background: #FFB86CA6;">Briefly state why this captured your interest or how it might be relevant to your goals or projects.</mark>
# Possible Actions
- [ ] Convert to Literature note
- [ ] Add to task list
- [ ] Link to existing notes

# Linked Resources

[[📥Comments in Python]]
---

*Fleeting notes are temporary and should be reviewed regularly to migrate valuable insights to `Areas`, `Resource`, or `Projects`.*
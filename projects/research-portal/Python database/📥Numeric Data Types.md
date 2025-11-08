---
Creation Date: 6th Dec 2023
File Folder: 02_Fleeting Note
aliases: 
tags:
  - 📥FleetingNote
Status: "#📥/🟨"
Category: Python Programming
Started: 6th Dec 2023
Finished: 
Rating: 
Link: "[[📥Python Basics]]"
Subject: Python Basics - Data Types
banner: https://files.oaiusercontent.com/file-tfHG6nFWvXOYKfbnXAPtZ15x?se=2123-10-29T19%3A03%3A03Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D8c859ba9-2c42-45fd-b160-d3c706e6e0f2.png&sig=r0%2B0WCgNWrA9jXXLfhESjQ61EzPFHxXcN0s9tXD8rVM%3D
---
Links: [[📥My Inputs]]

---
# ==📥Numeric Data Types==
---
- **Source:** [URL or location]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
- **Keywords:** [ ], [ ]
---
%% If possible subheadings should be in question  format %%
# Key Points


---
# Detailed Notes

Python, being a dynamically-typed language, offers a variety of data types. The main data types in Python are:

1. **Numeric Types:**
    
    - **int:** Integer, a whole number without a fractional part (e.g., 5, -3, 42).
    - **float:** Floating-point number, a number with a decimal point (e.g., 3.14, -0.001, 2.0).
    - **complex:** Complex number, a number with a real and imaginary part (e.g., 3 + 4j).


[[📥Importing in Python| Import]] (find the relevant information for importing here)

```python
import sys
import keyword
import operator
from datetime import datetime
import os
```

```python
val1 = 10 # Integer data type
print(val1)
print(type(val1)) # type of object
print(sys.getsizeof(val1)) # size of integer object in bytes 
print(val1, " is Integer?", isinstance(val1, int))
```

> [!note]- Understanding the given snippet
> print(val1): This line prints the value of the variable val1.
> 
> print(type(val1)): This line prints the type of the object that val1 refers to. The type() function in Python is used to determine the type of an object. For example, if val1 is an integer, this line will print <class 'int'>.
> 
> print(sys.getsizeof(val1)): This line prints the size of the object val1 in bytes. The sys.getsizeof() function from the sys module returns the size of an object in bytes. The size includes the space allocated for the object itself as well as any overhead for additional structures in Python's memory management. It's important to note that the size reported by getsizeof() might not always reflect the actual memory usage due to such overheads.
> 
> print(val1, " is Integer?", isinstance(val1, int)): This line checks whether val1 is an instance of the int class (i.e., whether it is an integer) and prints the result along with the value of val1. The isinstance() function is used to check if an object is an instance or subclass of a specified class. If val1 is an integer, isinstance(val1, int) will return True, otherwise False.
> 
> To summarize:
> 
> sys.getsizeof(object): Returns the size of the object in bytes, including its overhead.
> isinstance(object, class): Checks if the object is an instance of the specified class (or a subclass thereof).


```python
val2 = 92.78 # Float data type
print(val2)
print(type(val2)) # type of object
print(sys.getsizeof(val2)) # size of float object in bytes
print(val2, " is float?", isinstance(val2, float))
```

```python
val3 = 25 + 10j # Complex data type
print(val3)
print(type(val3)) # type of object
print(sys.getsizeof(val3)) # size of float object in bytes
print(val3, " is complex?", isinstance(val3, complex))
```

```python
sys.getsizeof(int()) # size of integer object in bytes 
```


---
# Context/Source/Trigger
- **Related to**: 

# Relevance:

- <mark style="background: #FFB86CA6;">Briefly state why this captured your interest or how it might be relevant to your goals or projects.</mark>
# Possible Actions
- [ ] Convert to Literature note
- [ ] Add to task list
- [ ] Link to existing notes

# Linked Resources
[[📥Data types in Python]]


---

*Fleeting notes are temporary and should be reviewed regularly to migrate valuable insights to `Areas`, `Resource`, or `Projects`.*
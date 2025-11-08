---
Creation Date: 7th Dec 2023
File Folder: 02_Fleeting Note
aliases: 
tags:
  - 📥FleetingNote
Status: "#📥/🟨"
Category: Python Programming
Started: 7th Dec 2023
Finished: 
Rating: 
Link: "[[📥Python Introduction]]"
Subject: Python Key Concepts
---
Links: [[📥My Inputs]]

---
# ==📥Immutable and Mutable Objects in python==
---
- **Source:** [URL or location]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
- **Keywords:** [ ], [ ]
---
%% If possible subheadings should be in question  format %%
# Key Points


---
# Detailed Notes
In Python, the terms "immutable" and "mutable" refer to the ability of an object's state or content to be changed after it has been created.

1. **Immutable**:
    
    - An immutable [[📥Object in a python|Object]] cannot be altered after it is created.
    - Any operation that seems to modify the object actually creates a new object with the modified content.
    - Common immutable types include `int`, `float`, `bool`, `str`, and `tuple`.
    - Immutable objects are often favored for their predictability and ease of use, especially in contexts where data integrity is critical.
    - Example: When you concatenate two strings, Python creates a new string with the combined content instead of modifying the original strings.
```python
str1 = "Hello"
str2 = str1 + ", World!"
# str1 remains "Hello", str2 is a new string "Hello, World!"
print(str1)
print(str2)
```

**Mutable**:

- A mutable [[📥Object in a python|Object]] can be changed after it is created.
- Operations that modify mutable objects do so by changing the object's state or contents, not by creating a new object (unless explicitly stated).
- Common mutable types include `list`, `dict`, `set`, and most custom objects (classes).
- Mutable objects are useful when you need an object to maintain a state or change over time, like a list that grows with new data.
- Example: Appending an item to a list changes the list in place.
```python
my_list = [1, 2, 3]
my_list.append(4)
# my_list is now [1, 2, 3, 4]
print(my_list)

```

- <u>Understanding whether a type is mutable or immutable is important for writing effective and bug-free code. It affects how you manage object state, how you pass objects to functions, and how you work with shared data structures. </u>

- Immutable objects provide safety from unintended side-effects, while mutable objects provide flexibility to modify data efficiently.


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
[[📥Object in a python]]
[[📥Strings Data type in Python]]

---

*Fleeting notes are temporary and should be reviewed regularly to migrate valuable insights to `Areas`, `Resource`, or `Projects`.*
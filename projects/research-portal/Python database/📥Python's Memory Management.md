---
Creation Date: 30th Nov 2023
File Folder: 02_Fleeting Note
aliases: 
tags:
  - 📥FleetingNote
Status: "#📥/⏹️"
Category: Python Programming
Started: 30th Nov 2023
Finished: 
Rating: 
Link: "[[📥Python Introduction]]"
Subject: Python Introduction -Memory Management
---
Links: [[📥My Inputs]]

---
# ==📥Python's Memory Management==
---
- **Source:** [URL or location]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
- **Keywords:** [ ], [ ]
---

![[Memory Management in Python.png]]

Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management. It also features dynamic name resolution(late binding) which binds methods and variable
names during program execution.

As we know, whenever we run any application it gets loaded into RAM and some memory gets allocated by OS for that application. Fig-1 shows the same. Now, Fig-2 shows the different area created in the allocated memory
for running the application.

- Code Area:- Code Area:- Fixed in size and code gets loaded in this area.

- Stack Area:- Stack Area:- It may grow or shrink dynamically and is responsible for the order in which method will be resolved. Also in this local variable reference are created.

- Heap Area:- Heap Area:- This also may grow or shrink dynamically and is responsible to store any object in Python. Here object get stored in random order. Every object which gets stored here will have a specific ID. 

	- [[📥Garbage Collection in Python| Garbage]] collector runs in heap area from time to time and destroys the object which are not having any reference.

- Variable area:- Variable area:- In This section variables are stored and they refer their corresponding object in heap area

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
[[📥Python Introduction]]
[[📥Garbage Collection in Python]]
[[📥MCQs for Python Exam]]
[[]]

---

*Fleeting notes are temporary and should be reviewed regularly to migrate valuable insights to `Areas`, `Resource`, or `Projects`.*
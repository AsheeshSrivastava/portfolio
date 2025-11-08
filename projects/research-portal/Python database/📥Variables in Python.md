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
Link: "[[📥Python Basics]]"
Subject: Python Basics - variables
---
Links: [[📥My Inputs]]

---
# ==📥Variables in Python==
---
- **Source:** [URL or location]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
- **Keywords:** [ ], [ ]
---
- A <font color="#f79646">Python variable</font>: is a reserved memory location to store values.
- A variable is created the moment you first assign a value to it.
```python
q = 30
```

```python
id(q)
```

#flashcards 
id() function::: returns the “identity” of the object.
<!--SR:!2023-12-07,1,230!2023-12-09,3,250-->

- The identity of an object 
	- Is an integer 
	- Guaranteed to be unique 
	-  Constant for this object during its lifetime. 

```python
hex(id(q)) # Memory address of the variable
```

```python
type(id(q))
```

```python
type(hex(id(q)))
```

```python
a = 20
b = 20
c = b
```

```python
a, type (a), hex(id(a))
```

```python
b, type (b), hex(id(b))
```

```python
c, type (c), hex(id(c))
```

![[variable memory location.png]]


```python
a = 20
a = a + 10 # Variable Overwriting
print(a)
```

#### Variable Assignment
```python
intvar = 10 # Integer variable
floatvar = 2.57 # Float Variable
strvar = "Python Language" # String variable

print(intvar)
print(floatvar)
print(strvar)

```

```python
intvar , floatvar , strvar = 10,2.57,"Python Language" # Using commas to separate
print(intvar)
print(floatvar)
print(strvar)

```

```python
p1 = p2 = p3 = p4 = 44 # All variables pointing to same value
print(p1,p2,p3,p4)
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


---

*Fleeting notes are temporary and should be reviewed regularly to migrate valuable insights to `Areas`, `Resource`, or `Projects`.*
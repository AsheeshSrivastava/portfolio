---
Creation Date: 29th Nov 2023
File Folder: 02_Fleeting Note
aliases: 
tags:
  - 📥FleetingNote
Status: "#📥/🟨"
Category: Python Programming
Started: 29th Nov 2023
Finished: 
Rating: 
Link: "[[📥Python Introduction]]"
Subject: Python
---
Links: [[📥My Inputs]]
- Allocate and deallocate the memory for 
# ==📥Memory Management in Python==
---
- **Source:** [URL or location]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
- **Keywords:** [ ], [ ]
---
### Memory Management in Python

- Allocate and deallocate the memory for effectively run the code
- Ineffiecient memory management may lead to slowness of the program

- In Python, memory management is taken care by Python Memory Manager (PMM) - automatically done in Python

Memory allocation

1. Static memory allocation
    - Memory is allocated at compile time
    - Stack is used
    - Memory cannot be re-used
    - int a = 10;
    
2. Dynamic memory allocation
    - Memory is allocated during runtime
    - Heap is used
    - Memory can be re-used
    - a = 10 # no need to declare a as int
    
- In Python, dynamic memory allocation is done. So, memory management is done during runtime.
PMM allocates the memory to an object and when that object is not needed, PMM automatically reclaims the memory for something else.


Stack: Memory allocation on continuous memory addresses/ locations

Heap: Memory allocation is random. Heap is a pile of memory.


PMM has:
- Object specific allocator: Allocate memory to the objects (int, string, float, ...)
- Raw memory allocator: It interacts with the OS to ensure that there is enough memory for allocation

When memory is allocated for running a program, different types of areas are created:
![[Memory Management.png]] 

#### Garbage collection

- deallocating the memory

Reference counting: It counts the number of times an object is referred.


```python
a = 1000
```

```python
id(a)
```

```python
b = 1000
```

```python
id(b)
```

```python
x = 1000
y = 1000
print(id(x))
print(id(y))
```

```python
x = 1000
id(x)
y = 1000
id(y)
```

```python
x = 1000
print(id(x))
y = 1000
id(y)
```

```python
c = a
```

```python
id(c)
```

```python
id(a)
```

```python
a = 500
```

```python
id(a)
```

```python
id(c)
```

```python
print(c)
```

```python
c = 600
```

```python
id(c)
```

```python
print(c)
```

When the reference count of a memory becomes 0, the PMM sees that and the object(value) is removed from that memory and the memory is re-claimed to be used for something else. This is called Garbage collection.

[[Garbage Collection.png]]

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
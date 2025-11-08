---
title: Python Introduction
Creation Date: 24th Nov 2023
File Folder: 01_Online Course
Category: Online Class
tags:
  - "#📥LectureNotes"
Status: "#🚧/🟩"
Subject: Core Python
Link: "[[🚧Python Module Exam]]"
---
[[📥My Inputs]]
# ==Python Introduction==
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
1. **Python's Nature**: Python is a general-purpose, high-level programming language.
2. **Ease of Learning**: Known for its simplicity and easy-to-learn syntax, making it a popular choice for beginners.
3. **Dual Nature**: Python is both a compiled and interpreted language, offering flexibility in its use.
4. **Dynamic Typing**: Python employs dynamic typing and memory management, enhancing its flexibility.
5. **Extensibility & Embeddability**: Python can be extended with code from other languages, and its own code can be embedded into code from other languages.
6. **Wide Library Support**: Known as 'batteries included', Python comes with extensive standard libraries.
7. **Community Support**: Benefits from a robust and active community, offering support for all levels of programmers.
8. **Educational Inclusion**: Python is now included in the CBSE 10th standard syllabus, reflecting its growing importance in education.

# Detailed Notes
#### Introduction to Programming and Operating Systems

- **Programming Language**: Defined as a set of predefined words used to create applications. Python fits into this as a language that simplifies programming tasks.
- **Operating System**: Acts as an intermediary between users and the computer hardware. Python's versatility allows it to run across different operating systems.

#### Memory in Computing

- **Types of Memory**: ==Python programs run in RAM (Volatile Memory, (RAM,cache))==, while secondary memory (Non-volatile(HDD, SSD)) is used for permanent storage.
- ==**Python's Memory Management**: Utilizes dynamic typing and a combination of reference counting and garbage collection.==
<!--SR:!2023-12-02,2,243!2023-12-04,3,243-->

#### Programming Language Types

- **Low-Level vs High-Level**: ==Python is a high-level language, closer to human language, and abstracts away much of the machine-level complexities.==
- **Compiled vs Interpreted**: ==Python code is first compiled into bytecode and then interpreted, making it both a compiled and interpreted language.==
<!--SR:!2023-12-02,2,243!2023-12-04,3,243-->

#### Python's Features

- **Simple & Expressive**: Python's syntax is straightforward, making it easy to write and maintain code.
- **Open Source & Freeware**: Accessible to everyone, with the ability to modify and redistribute the source code.
- **Portability**: Python code is portable and platform-independent.
- **Dynamically Typed**: Variables in Python are not bound to specific data types, offering more flexibility.
- **Garbage Collection**: Python handles memory management automatically.

#### Variants of Python

- Python has multiple implementations like CPython, Jython, PyPI, and Anaconda Python, each serving different purposes and environments.


## A Brief Introduction to Computer Memory

- **Types of Memory**:
    1. **Volatile Memory (Primary Memory)**: Temporary Storage (RAM, Cache, Register).
    2. **Non-volatile Memory (Secondary Memory)**: Permanent Storage (HDD, SDD, Floppy Disk, CD, Pen Drive).

## Types of Programming Languages

- **Low Level Programming Language**: Closer to the system, harder to learn and write, not ideal for large applications, non-portable, and less expressive (e.g., Machine Code, Assembly Code).
- **High Level Programming Language**: User-friendly, easier to learn and write, ideal for large applications, memory and security management handled by the compiler or VM, portable and expressive (e.g., C, C++, Java, Python).

## Source Code, Byte Code, and Machine Code in Python
#flashcards 
- **Source Code**::: Written to develop the application (Python `.py` files).
<!--SR:!2023-12-07,1,187!2023-12-11,5,243-->
- **Byte Code**::: Fixed set of instructions representing operations like arithmetic, comparison, memory-related operations, generated after compiling source code (Python `.pyc` files), system and platform independent.
<!--SR:!2023-12-08,2,203!2023-12-11,5,227-->
- **PVM**::: Python Virtual Machine with an Interpreter.
<!--SR:!2023-12-13,7,263!2023-12-13,7,263-->
- **Machine Code**::: Generated after interpretation of byte code, system and platform dependent.
<!--SR:!2023-12-08,2,203!2023-12-10,4,243-->

## Types of [[📥Errors in Python]]

- **[[Syntax Error]]** and **[[Indentation Error]]**: Caught at the compilation stage. (Compile time error)
- **[[Run-time Error]]**: Caught at the runtime or interpretation stage.

    - If there is a compile time error, Byte code will NOT be generated
    - During compilation, only syntax and indentation are checked
## Compiled vs. Interpreted Languages

- **Compiled Languages**: Need a compiler to translate code (Python, C, C++, Java).
- **Interpreted Languages**: Need an interpreter for translation (Perl, JavaScript, Python).

## Why Python is Both Compiled and Interpreted?

- Bridging the gap between portable programming languages and platform-independent languages.
- Source Code → Compiler → Byte Code → Interpreter or JIT Compiler → Machine Code → Output.
- ![[How python runs on our system.png]]
## Features of Python

1. **Simple & Easy to Learn**: Steeper learning curve compared to other languages.
2. **Most Expressive Language**: Less cluttered programs, faster execution, easy to debug and maintain.
3. **Freeware and Open Source**: Free to use, modifiable source code.
4. **Compiled and Interpreted**: Initially interpreted, later made both compiled and interpreted.
5. **Portable and Platform Independent**: Source code is portable, byte code is platform independent.
6. **Dynamically Typed Programming Language**: Uses objects, memory management through a reference model, no need to specify data types explicitly.
7. **Extensibility and Embeddability**: Extending code from other languages into Python, embedding Python code into other languages.
8. **Batteries Included**: Comes with a huge library support.
9. **Community Support**: Available for all levels of programmers.
10. **Educational Adoption**: Included in the CBSE 10th standard syllabus.

## [[📥Memory Management in Python]]

- Uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector.
- Dynamic name resolution (late binding) binds methods and variable names during program execution.
- Memory allocation managed by the Python Virtual Machine (PVM).

## Different Flavors of Python

#flashcards
**CPython**:: C implementation of Python.
<!--SR:!2023-12-12,6,250-->
**Jython**::Java implementation of Python.
<!--SR:!2023-12-14,8,250-->
**PyPI**:: Python implementation with JIT compiler.
<!--SR:!2023-12-10,4,210-->
**Ruby Python**:: implementation of Python.
<!--SR:!2023-12-08,2,230-->
**Stackless Python**:: For concurrency in Python.
<!--SR:!2023-12-08,2,190-->
**Anaconda Python**:: For handling and processing big data.
<!--SR:!2023-12-15,9,250-->

# Action Items
- [ ] Review class recording
- [ ] Summarize key concepts
- [ ] Migrate relevant information to Areas/Resources/Projects
- [ ] Combine the knowledge from [[1_Python Introduction]] to this document 🔼  📅 2023-12-04 

# References
- 

# Linked Notes
%%  tp.file.include("[Index of Related Notes]") %> %%

[[📥Python Basics]]

---

*This note is initially captured under `Capture` and can be later moved to `Areas`, `Resource`, or `Projects`.*

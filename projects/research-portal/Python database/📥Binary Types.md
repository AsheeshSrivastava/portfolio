---
Creation Date: 9th Dec 2023
File Folder: 04_Capture
tags: 
Link: "[[📥Data types in Python]]"
Status:
---
[[📥My Inputs]]

---

In the context of Python, binary types are not typically classified under "derived datatypes" like lists, tuples, sets, dictionaries, and frozen sets. Instead, they fall under a different category, often referred to as "binary sequence types" or simply "binary types". These include:

1. **Bytes (`bytes`)**: Immutable sequences of bytes.
2. **Byte Arrays (`bytearray`)**: Mutable sequences of bytes.
3. **Memory Views (`memoryview`)**: Objects that allow efficient access to another object’s binary or buffer data without copying it.

Derived datatypes, on the other hand, are more complex structures that are built from simpler datatypes and provide more advanced functionalities, like collections of multiple elements (lists, sets, etc.) or mappings (dictionaries).

Binary types are used for handling raw binary data, often in contexts like file processing, network communication, and other low-level operations. They are specialized tools for specific use cases, particularly when dealing with byte-oriented data.

# Detailed Notes

In Python, binary types refer to data types that are used to store binary data (data in a binary format, i.e., consisting of 0s and 1s). The binary types in Python are primarily used for working with binary data such as files, network connections, and other low-level operations. These types are:

1. **Bytes**:
    
    - The `bytes` type is an immutable sequence of bytes, which are 8-bit integers.
    - It is often used for raw binary data, fixed-length, and immutable byte arrays.
    - Example: `b'Hello'` represents a byte literal for the string "Hello".
2. **Bytearray**:
    
    - The `bytearray` type is similar to `bytes` but mutable, meaning it can be modified after creation.
    - It is used for the same purposes as bytes when mutability is required.
    - Example: `bytearray(b'Hello')` creates a mutable byte array.
3. **Memoryview**:
    
    - The `memoryview` type allows for the creation of a memory view object from a buffer, which is essentially a shared memory block for data storage.
    - It provides a way to access and manipulate the raw bytes of the buffer without copying the buffer's contents, thus optimizing memory usage and performance, especially when handling large binary data.
    - Example: `memoryview(bytearray('ABC', 'utf-8'))` creates a memory view object.

These binary types are considered derived or complex types because they extend the functionality of Python's basic types and allow for more advanced operations on binary data. They are particularly important in areas like file I/O (Input/Output), network communication, and data processing that involves working with raw binary or byte-oriented data.
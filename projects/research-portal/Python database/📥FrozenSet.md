---
Creation Date: 9th Dec 2023
File Folder: 
tags: 
Link: 
Title: Untitled
Status:
---
[[📥My Inputs]]

---

Frozen sets in Python are similar to sets, but they are immutable, meaning that once they are created, they cannot be modified. This includes adding or removing elements. Frozen sets are useful when you need to use a set in a context where a hashable type is required, like as a key in a dictionary.

You can convert various data types into a frozen set using the `frozenset()` function, as long as they are iterable. Here are some common data types that can be converted:

1. **Strings**: Each character in the string will become an element in the frozen set.
2. **Lists**: Each element in the list will become an element in the frozen set.
3. **Tuples**: Each element in the tuple will become an element in the frozen set.
4. **Sets**: The set will be converted into a frozen set with the same elements.
5. **Dictionaries**: The keys of the dictionary will become elements of the frozen set.

```python
# Converting a string
frozen_set_from_string = frozenset("hello")  # frozenset({'e', 'h', 'l', 'o'})

# Converting a list
frozen_set_from_list = frozenset([1, 2, 2, 3, 3])  # frozenset({1, 2, 3})

# Converting a tuple
frozen_set_from_tuple = frozenset((1, 2, 3))  # frozenset({1, 2, 3})

# Converting a set
regular_set = {1, 2, 3}
frozen_set_from_set = frozenset(regular_set)  # frozenset({1, 2, 3})

# Converting dictionary keys
dict_sample = {"a": 1, "b": 2}
frozen_set_from_dict = frozenset(dict_sample)  # frozenset({'a', 'b'})

```

> [!tip] It's important to note that while the frozen set itself is immutable, the elements contained within it must also be immutable for it to be hashable. This means that you cannot have lists or other sets as elements of a frozen set, but you can have tuples, strings, and other frozen sets.

Frozen sets are particularly useful in situations where you need a collection of unique, immutable elements that can be used as keys in a dictionary or stored in another set, and you want to ensure that this collection itself remains unchanged throughout the program.







---
# Linked Notes
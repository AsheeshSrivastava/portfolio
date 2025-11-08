---
Creation Date: 9th Dec 2023
File Folder: 
tags:
  - "#learnbay"
Link: 
Title: 📥Strings in Python note
Status: 
Category: Python Programming
Subject: Core Python
---
[[📥My Inputs]]
[[📥Strings Data type in Python]]

---

### Key Points: Strings in Python

1. **String Data Type**: Belongs to the text type category in Python.
2. **Creating Strings**: Can be done using single or double quotes.
3. **String Length**: Determined using the `len()` function.
4. **Indexing in Strings**: Uses square brackets `[]` for position referencing.
5. **String Slicing**: Follows the format `stringname[start: stop: stepsize]`.
6. **String Repetition**: Utilizes the `*` symbol for repetition.
7. **String Concatenation**: Performed using the `+` operator.
8. **Checking Membership**: Done using `in` and `not in` operators.
9. **Comparing Strings**: Uses relational operators like `>`, `<`, double quotes, etc.
10. **Removing Spaces**: Achieved with `rstrip()`, `lstrip()`, and `strip()` methods.
11. **Finding Substrings**: Employing methods like `find()`, `index()`, etc.
12. **Counting Substrings**: Uses the `count()` method.
13. **String Immutability**: Strings are immutable in Python.
14. **Replacing Substrings**: Done with the `replace()` method.
15. **Splitting and Joining Strings**: Utilizes `split()` and `join()` methods.
16. **Changing String Case**: Employing methods like `upper()`, `lower()`, `title()`, etc.
17. **Checking Starting/Ending of String**: Uses `startswith()` and `endswith()` methods.
18. **String Testing Methods**: Includes `isalnum()`, `isalpha()`, `isdigit()`, etc.
19. **Formatting Strings**: Done using the `format()` method.
20. **Working with Characters**: Involves indexing and slicing on strings.
21. **Sorting Strings**: Uses the `sort()` method and `sorted()` function.
22. **Searching in Strings**: Achieved through sequential or linear search techniques.
23. **Finding Number of Characters/Words**: Can be done without using `len()` function.
24. **Inserting Substrings**: Involves list manipulation due to string immutability.

### Detailed Notes

#### Strings in Python

- **Strings**: Group of characters used to represent text data like names, addresses, etc.
- **Creating Strings**: Assign characters to a variable enclosed in single or double quotes, e.g., `s1 = ‘Hello World’`, `s2 = "Hello World"`.
- **String Length**: The `len()` function provides the total number of characters, including spaces.
- **Indexing in Strings**: Access individual elements using index numbers, e.g., `str[0]` for the first element. Negative indexing refers to elements in reverse order.
- **String Slicing**: Extracts parts of strings using start, stop, and step size parameters.
- **Repeating Strings**: The `*` operator repeats strings a specified number of times.
- **Concatenating Strings**: The `+` operator joins strings end-to-end.
- <span style="background:#fff88f">**Membership Check**: Use `in` and `not in` for case-sensitive checks within strings.</span>
- **Comparing Strings**: Relational operators return Boolean values based on string comparison.
- **Removing Spaces**: Methods like `rstrip()`, `lstrip()`, and `strip()` remove unnecessary spaces.
- **Substring Location**: Methods like `find()`, `index()`, `rfind()`, and `rindex()` find substrings' locations.
- **Counting Substrings**: The `count()` method counts occurrences of a substring.
<span style="background:#fff88f">- **String Immutability**: Strings cannot be changed once created; any modification results in a new string.</span>
<span style="background:#fff88f">- **Replacing Substrings**: The `replace()` method substitutes parts of the string.</span>
<span style="background:#fff88f">- **Splitting/Joining Strings**: `split()` breaks strings into lists, and `join()` merges them back.</span>
<span style="background:#fff88f">- **Changing String Case**: Methods like `upper()`, `lower()`, `swapcase()`, and `title()` alter the case.</span>
<span style="background:#fff88f">- **Start/End Checking**: `startswith()` and `endswith()` methods check a string's beginning and ending.</span>
<span style="background:#fff88f">- **String Testing**: Methods like `isalnum()`, `isalpha()`, `isdigit()` test the nature of string characters.</span>
- **String Formatting**: The `format()` method presents strings in a clear manner.
<span style="background:#fff88f">- **Working with Characters**: Involves extracting individual elements from strings.</span>
<span style="background:#fff88f">- **Sorting Strings**: `sort()` and `sorted()` arrange strings in order.</span>
<span style="background:#fff88f">- **Searching in Strings**: Sequential search compares a target string with each string in a group.</span>
<span style="background:#fff88f">- **Character/Word Count**: A loop can count characters or words without using `len()`</span>.
<span style="background:#d3f8b6">- **Inserting Substrings**: Due to immutability, substrings are inserted using lists and then converted back to strings.</span>

---
# Linked Notes
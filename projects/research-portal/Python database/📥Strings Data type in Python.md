---
Creation Date: 6th Dec 2023
File Folder: 02_Fleeting Note
aliases: 
tags:
  - 📥FleetingNote
Status: "#📥/🟨"
Category: Python Proramming
Started: 6th Dec 2023
Finished: 
Rating: 
Link: 
Subject: Python Basics - Data Types
---
Links: [[📥My Inputs]]

---
# ==📥Strings Data type in Python==
---
- **Source:** [URL or location]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
- **Keywords:** [ ], [ ]
---
%% If possible subheadings should be in question  format %%
# Key Points


---
# Detailed Notes

### String Creation

```python
str1 = "HELLO PYTHON"
print(str1)
mystr = 'Hello World' # Define string using single quotes
print(mystr)
mystr = "Hello World" # Define string using double quotes
print(mystr)
mystr = '''Hello 
 World ''' # Define string using triple quotes
print(mystr)
mystr = """Hello
 World""" # Define string using triple quotes
print(mystr)
mystr = ('Happy '
 'Monday '
 'Everyone')
print(mystr)
mystr2 = 'Woohoo '
mystr2 = mystr2*5
print(mystr2)
print(len(mystr2)) # Length of string

```

### String Indexing

![[String Indexing.png]]

```python
str1
```

```python
str1[0] # First Character in string
```

```python
str1[len(str1)-1] # Last character in string using len function
```

```python
len(str1)-1
``` 

```python
len(str1)
```

```python
str1[-1] # Last character in string
```

```python
str1[6] #Fetch 7th element of the string
```

```python
str1[5]
```

Note: str1[5] is a space. In jupyter notebook it will give as → ‘ ’

```python
str1[len(str1)] # index error?
```

> [!question]+ Why output in the above snippet shows "index out of range"
> Because Indexing starts at zero from left to right, hence the last character in the string will always be len(str)-1.

```Python
str1[len(str1)-12] # First character in string using len function
```
#### String Slicing

- In Python, string slicing is used to extract a portion of a string. The syntax for slicing is `[start:stop]`, where `start` is the index of the first character you want to include in the slice, and `stop` is the index of the first character you do not want to include in the slice.

	The key point here is that the character at the `start` index is included, but the character at the `stop` index is not. This is what we mean when we say the `stop` index is exclusive.
	
	In your example, `str1[6:12]` means:
	
	- Start at index 6 (inclusive), and
	- Stop at index 12 (exclusive).
	
	The slice will include characters from the string `str1` starting from the character at index 6 up to, but not including, the character at index 12.
	
	Here's a breakdown:
	
	- Index 6: 7th character (since indices start at 0)
	- Index 7: 8th character
	- Index 8: 9th character
	- Index 9: 10th character
	- Index 10: 11th character
	- Index 11: 12th character
	- Index 12: Not included in the slice
	
	So, `str1[6:12]` retrieves characters from the 7th to the 12th character of `str1`. This exclusive nature of the stop index allows for more intuitive behavior when chaining or combining slices, as the end of one slice cleanly aligns with the start of the next.


> [!question]+ String Slicing -Fetch all the characters from 0 to 5

```python
str1[0:5] 
```

> [!question] String Slicing - Retreive all characters between 6 - 12
> 

```python
str1[6:12] # String slicing - Retreive all characters between 6 - 12
```

> [!question] str1[6:12] # String slicing - Retreive all characters between 6 - 12 How is index location exclusive here
> 
---

#### More on string slicing

##### Negative Indexing

In Python, negative indexing is used to access elements from the end of a sequence like a string. When you use negative indices in string slicing, the indexing starts from the end of the string, with `-1` being the index of the last character.

The slicing syntax `str1[-6:]` means:

- Start at the 6th character from the end of the string (`-6` index), and
- Continue to the end of the string (since there's no specified stop index).

So, this slice will include the last six characters of `str1`. Here's how it works:

1. `-6`: This is the starting index. It points to the 6th character from the end.
2. `:`: This indicates that we are taking a slice.
3. There's no stop index provided after the colon. In Python slicing, if the stop index is omitted, it means the slice goes all the way to the end of the string.

For example, if `str1` is `"Hello, World!"`, then `str1[-6:]` would result in `"World!"`, which are the last six characters of `str1`.


```python
str1[-4:] # Retreive last four characters of the string
```

```python
print(str1[-6:]) # Retreive last six characters of the string
print(str1[:4]) # Retreive first four characters of the string
print(str1[:6]) # Retreive first six characters of the string
```

### Update or Delete String

```python
str1
```

> [!warning] #Strings are immutable which means elements of a string cannot be chang ed once they have been assigned.





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
---
File Folder: 
tags:
  - 🗺️/MoC
Creation Date: 2nd Dec 2023
Area: "[[🚞My career shift towards Data Science]]"
Title: 🗺️ 🐍 Python MOC
Link: "[[🗺️Coding MoC]]"
Status: "#📥/⏹️"
---
[[🗺️My Map of Contents (MOCs)]]
## Overview
Brief description or notes about the topic: Python is high level programming language
## Key Resources
%% (add as many resources as needed) %%
[[python.pdf]]
## Subtopics
### Subtopic 1: 
- Brief description or key points

### Subtopic 2: 
- Brief description or key points

### Subtopic 3: 
- Brief description or key points
- ... (add as many subtopics as needed)

## Related Notes
%% (add as many related notes as needed) %%
```dataviewjs
dv.table(["File", "Subject", "Started", "Finished", "Tags"],
  dv.pages('"04_Capture"')
  .where(page => page.file.name != "📥My Inputs" &&
                 !page.file.path.includes("000_Templates") &&
                 !page.file.path.includes("001_Journals") &&
                 !page.file.path.includes("01_Project") &&
                 page.category == "Python Programming")
  .sort(p => p.started, 'desc')
  .map(page => [
    page.file.link,
    page.subject,
    page.started,
    page.finished,
    page.tags
    
  ])
);

// Add CSS to style the table
dv.el("style", `
  .dataview.table-view {
    width: 80% !important; /* Set the width as needed */
  }
  
  .dataview.table-view th,
  .dataview.table-view td {
    padding: 5px 10px; /* Adjust padding for spacing */
    word-break: break-word; /* Break words to prevent overflow */
    min-width: 100px; /* Minimum width for columns */
  }
  
  .dataview.table-view th {
    position: sticky;
    top: 0;
    background-color: #333; /* Adjust the color to match your theme */
    color: white;
  }
`);
```
## External Links
%% (add as many external links as needed) %%

# Python Exam Preparation - Kanban Board
## Basics
- [ ] Introduction to Python
- [ ] Basic Syntax
- [ ] Variables and Data Types
- [ ] Basic Operators
- [ ] Conditional Statements
- [ ] Loops

## Intermediate Concepts
- [ ] Functions
- [ ] Modules and Packages
- [ ] Exceptions Handling
- [ ] File Operations (Read, Write, Append)
- [ ] Lists, Tuples, and Dictionaries
- [ ] String Manipulation

## Advanced Topics
- [ ] Object-Oriented Programming
  - [ ] Classes and Objects
  - [ ] Inheritance
  - [ ] Polymorphism
  - [ ] Encapsulation
  - [ ] Method Overriding
- [ ] Iterators and Generators
- [ ] Decorators
- [ ] List Comprehensions

## Additional Concepts
- [ ] Memory Management
- [ ] Regular Expressions
- [ ] Database Interaction
- [ ] Error and Exception Handling
- [ ] Built-in Functions
- [ ] Advanced Data Structures

## Revision and Practice
- [ ] Practice Coding Problems
- [ ] Review Notes
- [ ] Sample Tests
- [ ] Time Management

## Final Preparation
- [ ] Review Key Topics
- [ ] Practice Previous Exam Papers
- [ ] Rest and Relaxation
- [ ] Exam Strategy

## Reflections and Personal Thoughts


---



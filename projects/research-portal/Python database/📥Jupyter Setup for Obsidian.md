---
Creation Date: 29th Nov 2023
File Folder: 02_Fleeting Note
aliases: 
tags:
  - 📥FleetingNote
Status: "#📥/🟨"
Category: Setup and Installation
Started: 29th Nov 2023
Finished: 
Rating: 
Link: 
Subject: Jupyter
---
Links: [[📥My Inputs]]

---
# ==📥Jupyter Setup for Obsidian==
---
- **Source:** [URL or location]
- **Last Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")`
- **Keywords:** [ ], [ ]
---
 -  A way to work with Jupyter notebooks in conjunction with Obsidian, which is a popular note-taking application that supports Markdown
- Here's a breakdown of the alternative setup suggested:

1. **Python Distribution and Jupyter Lab**: You are advised to set up a Python distribution on your computer. This typically involves installing Python and then using Python's package manager `pip` to install additional software.
    
2. **Jupytext**: Jupytext is a utility that allows you to synchronize Jupyter notebooks with Markdown documents. It can convert notebooks to Markdown and vice versa. This is particularly useful if you prefer to write in Markdown and still want to execute the code in a Jupyter environment.
    
3. **Running Jupyter Lab**: Once you have Jupyter Lab installed, you can start it by running `jupyter lab` from the command line in the root directory of your Obsidian vault. The "vault" is the folder where all your Obsidian notes are stored.
    
4. **Opening Markdown as a Notebook**: With Jupytext installed, you can open any Markdown file in Jupyter Lab and work with it as though it's a Jupyter notebook. This means that you can run code cells contained in the Markdown file.
    
5. **[[Pairing Notebooks with Markdown Files]]**: The setup also suggests "pairing" Markdown files with traditional Jupyter notebook files (`.ipynb` extension). This allows you to save the outputs of your code cells and keep them even if you close and reopen the notebook. This is done by creating a `jupytext.toml` configuration file in your vault's root directory with a specific line of code (`formats = "md,.ipynb//ipynb"`). When paired, a hidden `.ipynb` directory is created that contains the classic notebook files with the code outputs.
    
While this setup is robust, it does not allow you to run Jupyter notebooks directly within Obsidian. It seems to that integrating that functionality into Obsidian would require significant effort and isn't currently available.

**If you have Anaconda installed**, you do not need to set up a separate Python distribution because Anaconda is a complete Python distribution itself. Anaconda is particularly well-suited for data science and machine learning projects as it bundles a large number of scientific packages, including Jupyter Lab, making it a convenient choice for your needs.

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
[[📥About Anaconda]]

---

*Fleeting notes are temporary and should be reviewed regularly to migrate valuable insights to `Areas`, `Resource`, or `Projects`.*
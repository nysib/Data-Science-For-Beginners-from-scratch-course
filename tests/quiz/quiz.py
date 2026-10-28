"""Quiz 1 and Quiz 2 answers for the homework workflow and VSCode setup."""

# #### Quiz 1 — Homework Accept & Submit Workflow
#
#
# Video: https://youtu.be/hW_7hodGxVU
#
# 1) How do you know a homework assignment has arrived?
# **Answer: In GitHub Desktop I click "Fetch origin". If new homework has arrived, the button changes to "Pull origin" - there are new commits on GitHub. After pulling, the new commit appears in the History tab. [11:19]**
#
# 2) How do you accept/take a homework?
# **Answer: In GitHub Desktop: click "Fetch origin", then "Pull origin". If I have local changes in the same file, GitHub Desktop offers "Stash changes": I stash my changes, the homework is pulled, and then I restore my changes from "Stashed Changes" with the "Restore" button. [11:19]**
#
# 3) What is the History button for, and what functions appear when you right-click a commit?
# **Answer: The History button shows the list of all past commits - who changed what and when. Right-clicking a commit opens a menu with options like Create branch from commit, Checkout commit, Revert changes, Copy SHA, and View on GitHub.**
#
# 3.1) Where do you get the link to a commit? Where do you send it?
# **Answer: History -> "Copy SHA" (or "View on GitHub" to get the URL), or by opening the commit on GitHub and copying the page link.**
#
# 4) What is a log file?
# **Answer: What was completed during a lesson: what was learned, progress.**
#
# 4.1) When do you need to push it?
# **Answer: When the lesson completed.**
#
# 5) What is an interpreter?
# **Answer: An interpreter is a program that reads code and executes it line by line, immediately. Python is a language; CPython and PyPy are examples of interpreters that run Python code.**
#
# 6) Where can you select the interpreter?
# **Answer: In Cursor, via "Select Kernel" (for notebooks) or the interpreter selector in the bottom status bar.**
#
# 7) What is a module?
# **Answer: python file with scripts, functions, classes**
#
# 8) How do you create and send a commit?
# **Answer: I stage changes, write a commit message describing what changed, create the commit, then push it to GitHub (in GitHub Desktop: summary + "Commit to branch", then "Push origin").**
#
# 9) How do you check that a commit was sent and is on GitHub?
# **Answer: in repository on github check the commit history / branch see if commit appears there. In GitHub (locally), the "Push" button shows nothing pending once it's synced**
#
# 10) Which command shows that the code did not pass error checks?
# **Answer: `pre-commit run --all-files` - it runs all the checks and shows the failed ones as `Failed` (red output in the terminal). pre-commit also runs automatically on every commit.**
#
# 10.1) List the linters used to check code and give a brief description of each.
# **Answer:**
# - **pylint** - a full static analyzer: finds errors, code smells, naming and style problems, unused variables and imports.
# - **pydocstyle** - checks docstrings (presence and formatting) against PEP 257.
# - **codespell** - finds common spelling mistakes in code, comments and text.
# - **flake8** - checks PEP 8 style (line length, spacing, indentation) and simple logical errors.
# - **mypy** - static type checker: verifies type hints and reports type mismatches.
#
# 11) How do you find out which specific linter failed the check?
# **Answer: Terminal output**
#
# 12) Does the Pylint linter see markdown?
# **Answer: no**
#
# 13) Can the cell number in the terminal and the cell number in Cursor differ? In what case?
# **Answer: can be different, if markdown is used (skips markdown)**
#
# 14) Where do you see the cell number in Cursor?
# **Answer: bottom of the Cursor window (status bar) - shows current cell number**
#
# 15) In what format is the .ipynb sent to GitHub? And what about JSON here?
# **Answer: json format - [VIDEO 1:01]**
#
# 16) Where do you see which cell has the error?
# **Answer: right below the cell that produced error**
#
# 17) How do you launch the terminal?
# **Answer: Terminal menu -> New Terminal**
#
# 18) What is a linter?
# **Answer: a tool that analyzes python code for errors, problems, even bad practices**
#
# 19) On which website do you paste the error code if the error is related to pylint?
# **Answer: pylint.readthedocs.io**
#
# 20) The pydocstyle section in most cases closes automatically after fixing errors — in which linter?
# **Answer: pylint - after fixing the pylint docstring errors (e.g. `missing-module-docstring`), the pydocstyle section usually passes too. [7:02]**
#
# 21) What is a module description? Should it reflect information about what is in the module?
# **Answer: a docstring at the top of a module file describing what the module contains and what it does**
#
# 21.1) Which git command starts a programmer's morning?
# **Answer: git pull**
#
# 22) After making changes to files, the "open in Cursor" button disappears in GitHub Desktop — how else can you open Cursor from GitHub Desktop?
# **Answer: Repository menu -> Open in Cursor**
#
# 23) What is stash? (General explanation of the concept)
# **Answer: a way to temporarily save uncommitted changes without committing them**
#
# 23.1) How do you save a stash? (git command / button in Cursor)
# **Answer: A stash is a buffer where you temporarily hide changes (e.g. to accept a pull). Save it with git stash or git stash push -m "NAME_STASH". In Cursor: Source Control → "..." → Stash.**
#
# 23.2) How do you restore a stash? (git command)
# **Answer: git stash pop**
#
# 23.3) The difference between stash and commit. When is it better to save changes in a stash, and when to commit?
# **Answer: A commit is a permanent saved point in history; a stash is a temporary shelf for unfinished work.**
#
# 23.4) How do you view the list of saved stashes? (git command)
# **Answer: git stash list**
#
# 23.5) How do you delete a stash? (commands for deleting individual stashes or all at once)
# **Answer: git stash drop stash@{n} - single one; git stash clear - delete all**
#
# 23.6) Practical examples of using stash. (Brief scenarios where stash helps)
# **Answer: people working on the same file;  realized that working on the wrong branch — stash, switch branch, pop.**
#
# 24) Where do you see that there is a conflict in files?
# **Answer: Conflict sections are marked directly in the file with conflict markers (<<<<<<<, =======, >>>>>>>) and highlighted by the editor. GitHub Desktop/Cursor also marks the file as conflicted.**
#
# 24.1) When does it appear?
# **Answer: changes are happening in the same lines of code and GitHub can't merge them**
#
# 25) How do you resolve a conflict in files?
# **Answer: In the conflicted file, choose which version to keep (yours, theirs, or both), remove the conflict markers, save, then commit.**
#
# 26) Write the correct statement: green is what came from GitHub and blue is local changes, OR blue is what came from GitHub and green is local changes?
# **Answer: green is what came from GitHub and blue is local changes**
#
# 27) If we work in one file, can you accept a pull and then hide your changes in a stash?
# **Answer: Yes. I hide my uncommitted changes in a stash first, then accept the pull, then restore the stash (`git stash pop`).**
#
# 27.1) What can happen when you restore a stash after accepting a pull?
# **Answer: A conflict**
#
# 28) How many ways of resolving conflicts were shown in the video? Write the NUMBER and list the methods.
# **Answer: 4 ways: Accept Current Change, Accept Incoming Change, Accept Both Changes, and editing the result manually and then clicking "Resolve in Merge Editor". [12:50]**
#
# 29) What does the "complete merge" button do?
# **Answer: It marks the conflicts in the file as resolved and finishes the merge locally (the merge commit is created in the local repository). GitHub is not involved at this step.**
#
# 30) Which chat should you write to if you still have questions?
# **Answer: "Help Me"**
#
# 31) What is FORK? Why is it done?
# **Answer: A fork is a personal copy of another user's repository in my own GitHub account. It lets me make changes independently and later propose them back via a Pull Request.**
#
# 32) How do you download a forked repository to your local computer?
# **Answer: clone it in GitHub Desktop: File -> Clone repository -> pick up fork; or git clone command**
#
# 33) With what probability were your errors already solved? And who solved them?
# **Answer: With a probability of 90% - they were already solved by the course author and other students. The solutions can be found in the "Help Me" chat (Ctrl+F by the error code, e.g. D100). [9:40]**
#
# 34) How do you create a file in VS Code?
# **Answer: click New File (or right-click -> New File), name it, press Enter.**
#
# 35) Should the log file be filled in at the end of each lesson?
# **Answer: yes**
#
#
#
# #### Additional Questions
#
# 1) Which command converts an .ipynb file to .py?
# **Answer: `jupytext --to py filename.ipynb`**
#
# 2) What is a package manager? Do you use conda or pip? Which is better for data science?
# **Answer: A package manager is a tool that installs, updates, and manages libraries and their dependencies automatically. The two main Python ones are pip (installs from PyPI) and conda (installs packages and manages environments). I use pip for now. For data science, conda is often preferred because it handles complex scientific and compiled dependencies and environments well, while pip is lighter and has the widest package selection.**
#
# 3) Why is the .py extension better than .ipynb?
# **Answer: A .py file is plain text, so it works cleanly with git (clear diffs), linters, and pre-commit checks. An .ipynb file is JSON under the hood (it stores output, metadata, and execution counts), which makes diffs messy and reviews harder. .py is also what is used for real modules and production code.**
#
# 4) What is PEP8?
# **Answer: PEP 8 is the official Python style guide — a set of conventions for writing readable, consistent code (naming, indentation, spacing, line length). "PEP" stands for Python Enhancement Proposal.**
#
# 4.1) Do linters check for PEP8 compliance?
# **Answer: Yes. Tools such as flake8, pycodestyle, and partially pylint check code style and report PEP 8 violations.**
#
# 4.2) What notation is used for creating variables?
# **Answer: snake_case — all lowercase words separated by underscores (e.g. user_name, total_count).**
#
# 4.3) Can a variable consist of a single letter, for example the underscore "_"?
# **Answer: Yes - a single underscore "_" is a valid variable name, as is any single letter like x or i.**
#
# 4.4) Why and where do we use the underscore "_"?
# **Answer: As a throwaway variable for values we don't need (e.g. for _ in range(5):), to signal that the value is intentionally ignored. It is also used as a separator in number literals (1_000_000) and as a prefix for "internal" names (_helper).**
#
# 4.5) Per PEP8, is a single-letter variable allowed?
# **Answer: PEP 8 allows them but advises against ambiguous single characters - it specifically warns against lowercase "l", uppercase "O", and "I" because they look like 1 and 0. Short names like i or j are acceptable in small scopes such as loops, but descriptive names are preferred.**
#
#
#

# #### Quiz 2 — VSCode setup, line wrapping, linters, working with cells
#
# Video: https://youtu.be/Si9MfV8uJ-0
#
# 1) How do you enable autosave in Cursor?
# **Answer: File menu -> Auto Save (toggle on), or set "files.autoSave": "afterDelay" in Settings.[0:11]**
#
# 2) How do you set up line wrapping?
# **Answer: View -> Word Wrap, Alt+Z, or set "editor.wordWrap": "on"[0:30]**
#
# 3) How many characters per line does PEP8 allow?
# **Answer: 79 characters for code lines (72 for comments and docstrings).**
#
# 4) What line-break methods are shown in the video?
# **Answer: Six methods are shown: backslash continuation, triple quotes, a list joined with join(), parentheses for implicit string concatenation, f-strings inside parentheses, and the + operator. The runnable examples are in the code cells below.**
#
# 4.1) Backslash (\\) continuation
# **Answer: a backslash at the end of a line tells Python that the statement continues on the next line, so the two strings are joined into one.**
#
# 4.2) Triple quotes (''' or \"\"\")
# **Answer: line breaks are preserved literally.**
#
# 4.3) List of strings joined with join()
# **Answer: items joined by newlines.**
#
# 4.4) Parentheses for line continuation
# **Answer: the strings inside the parentheses are joined automatically into one.**
#
# 4.5) f-strings with parentheses
# **Answer: the variable values are inserted into the string.**
#
# 4.6) String concatenation with +
# **Answer: two strings explicitly joined with +**
#
# 5) Where is the "problems" button for error checking?
# **Answer: In the bottom status bar (error/warning icons), or View -> Problems (Ctrl+Shift+M). It lists errors and warnings across open files by linter type.[4:48]**
#
# 6) Where is the Git client in Cursor? How do you commit? How do you accept homework?
# **Answer: The Source Control panel in the left sidebar (branch icon). To commit: stage the changed files, type a message (a note of what was changed), then click the Commit button (the checkmark), or use the dropdown next to it to pick a specific commit command. To accept homework: pull the latest changes from GitHub.[6:28]**
#
# 7) What is Git? Is it local? Can you view history and return to any commit?
# **Answer: Git is a version control system. It is local (stored in the .git folder), it tracks the full history of file changes, and I can return to any earlier commit.**
#
# 8) How do you insert an image in markdown?
# **Answer: `![alt text](path/to/image.png)` - or an HTML img tag for more control over size. [7:58]**
#
# 9) Where do you see line length in Cursor?
# **Answer: In the bottom status bar - it shows "Ln X, Col Y" (the line and column of the cursor). Col starts at 1, so with the cursor at the end of a line of N characters the status bar shows Col N+1: the Col value is one more than the number of characters. A ruler can also be set via editor.rulers (e.g. 79) to mark the PEP8 limit.**
#
# 10) How do you change a cell type from Python to markdown?
# **Answer: Select the cell, press Esc then M (command mode), or use the cell type dropdown.**
#
# 11) How do you run all cells at once in Jupyter?
# **Answer: Use the "Run All" button in the notebook toolbar. [8:29]**
#
# 12) How do you resize an image in Jupyter? Do you need HTML?
# **Answer: Yes - use an HTML img tag in a markdown cell, e.g. <img src="image.png" width="300">. [8:10]**
#
# 13) Which hotkey runs a cell and moves to the next one?
# **Answer: Shift+Enter runs the cell and moves to the next (Ctrl+Enter runs in place). [8:42]**
#
# 14) How do you turn on line numbers in Jupyter cells?
# **Answer: Press L in command mode, or use the command palette "Show Cell Line Numbers". [9:02]**
#
# 15) What is "Go To"? Why is it useful? How do you jump to an error cell?
# **Answer: "Go To" lets me jump straight to a specific line or cell instead of scrolling, which is useful in long notebooks. When a cell has errors, I can click the error in the traceback and it jumps to that cell. [9:44]**
#
# 16) How do you clear the output of cells that already ran?
# **Answer: Use "Clear All Outputs" from the notebook toolbar. [10:50]**
#
# 17) How do you work in several files at once in Cursor? What is SPLIT?
# **Answer: Open multiple tabs and use Split Editor to view files side by side (split icon, top right, or Ctrl+\\). SPLIT divides the editor into panes. [10:55]**
#
# 18) Which shortcut hides the left sidebar?
# **Answer: Ctrl+B toggles the left sidebar.**
#
# 19) Is the "two sheets" button our local files?
# **Answer: Currently opened projects/files.**
#
# 20) Which error appeared in the traceback when running all cells - DICT or LIST?
# **Answer: NameError: name 'Dict' is not defined**
#
# 21) Did you review the two reference links (Telegram post: https://t.me/c/1937296927/832/19307 and markdown cheatsheet: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)?
# **Answer: I reviewed both. The markdown cheatsheet is a useful reference for syntax and I am using it while writing these answers.**
#
# 22) What is validation?
# **Answer: Checking that data or input meets the expected rules/format (type, range, structure) before it is used.**
#
# 23) What is an error traceback?
# **Answer: It's the error report Python shows when something breaks — it points to the line that failed and the type of error. I read it from the bottom up.**
#
# 24) What does "the interpreter disconnected" mean?
# **Answer: The kernel the notebook was using stopped, so cells won't run until I reconnect or pick a kernel again.**

# #### Line-break examples for questions 4.1-4.6

# 4.1 backslash continuation
# black replaces backslashes with parentheses, so formatting is kept as is here
# fmt: off
string_continued = "This is a long string that we want to " \
    "split across multiple lines."
# fmt: on
print(string_continued)

# 4.2 triple quotes
multi_line_string = """This is a string that spans
multiple lines. You can write freely
and it will keep the line breaks."""
print(multi_line_string)

# 4.3 list + join
strings = [
    "This is the first line.",
    "This is the second line.",
    "This is the third line.",
]
result = "\n".join(strings)
print(result)

# 4.4 parentheses continuation
long_string = (
    "This is a very long string that I would like to continue on the next line, "
    "and the parentheses let Python join both parts into one string."
)
print(long_string)

# 4.5 f-strings with parentheses
letter_a = 5
letter_b = 6
product_ab = letter_a * letter_b
message = (
    f"When {letter_a} is multiplied by {letter_b}, "
    f"the result is {product_ab}, and both f-strings are joined into one line."
)
print(message)

# 4.6 concatenation with +
string_part1 = "This is the first part, "
string_part2 = "and this is the second part."
full_string = string_part1 + string_part2
print(full_string)

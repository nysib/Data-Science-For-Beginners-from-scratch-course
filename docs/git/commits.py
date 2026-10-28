"""Answers about commit types and Conventional Commits examples."""

# # Conventional Commits
#
# ### Question 1. Describe in your own words the purpose of each of these commit types.
#
# - **feat** — adds a new feature or functionality to the project
# - **fix** — fixes a bug in existing code
# - **docs** — changes only to documentation (README, comments, docstrings)
# - **style** — formatting changes (indentation, spaces, semicolons) that don't affect logic
# - **refactor** — restructuring code without changing its behavior or fixing a bug
# - **test** — adding or correcting tests
# - **build** — changes to the build system or external dependencies
# - **ci** — changes to CI configuration files and scripts
# - **perf** — a code change that improves performance
# - **chore** — routine maintenance tasks that don't touch source or tests

# ### Question 2. Imagine that you fixed a bug in a function that rounds numbers incorrectly. Make a fictional commit and write a message for it in accordance with Conventional Commits (using the type fix).
#
# ```bash
# git commit -m "fix: correct rounding logic in number formatting function" -m "The function rounded 2.5 down to 2 instead of up to 3. Updated to apply standard half-up rounding."
# ```

# ### Question 3. Adding new functionality: suppose you implemented a new generateReport function in the project. Make a fictional commit with the type feat, reflecting the addition of this functionality.
#
# ```bash
# git commit -m "feat: add generateReport function" -m "Implements report generation that aggregates project data and outputs a formatted summary."
# ```

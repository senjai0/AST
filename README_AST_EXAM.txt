AST_EXAM.py README
===================

Purpose
-------
This script demonstrates how Python code is parsed into an Abstract Syntax Tree (AST) using the built-in `ast` module. It analyzes several Python constructs and prints both the AST dump and a brief translation evaluation.

What it covers
--------------
1. For loops
2. Generator functions
3. Complex conditional statements
4. Complex arithmetic operations

Features
--------
- Uses `ast.parse(code)` to create the AST
- Prints the AST structure with `ast.dump(tree, indent=4)`
- Evaluates node counts, node types, and tree depth
- Explains how language constructs map to AST nodes

Usage
-----
1. Open a terminal in the `c:\Users\arboi\.vscode\Programming Languages` folder.
2. Run:

   python AST_EXAM.py

3. Review the printed output to see the AST dump and translation analysis for each example.

Notes
-----
- The script is intended for learning how Python source is represented in AST form.
- It is a static analysis example and does not modify source code.

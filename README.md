# POPL-Project-Group-Super-Cool

## Team Members
- Lauren Bissey
- Sam Byerly
- Sam Hirner
- Jasper Holland

## Project Description
### Project Goal
The goal of this assignment is to implement a grammar, specifically a context-free grammar in ANTLR, to parse the Python programming language for some version 3.x.
The parser does not need to be a complete parser of the Python language, as that would be incredibly comprehenzive, but should capture key structures of the language.
The output of the parser is a tree.
### Expected Features
- Valid Data Types
    - integers
    - floats
    - arrays
    - booleans
    - strings
- Arithmetric operators (+, -, *, /, %)
- Assignment operators (=, +=, -=, *=, /=)
- if-elif-else blocks
- Conditional statements (<, <=, >, >=, !=, and, or, not)
- while loops
- for loops
- Nested structures
- Comments (single line and multiple lines)

## Parser Requirements
- Uses ANTLR4 and requires language to compile CFG
- Dependencies to run CFG on Python code
    - Connect ANTLR to file to be parsed with Python
    - Need Python3 installed
    - Uses antlr4 library in python
        - pip install antlr4

## Running Instructions
- Compiles the CFG in ANTLR
    - antlr4 -Dlanguage=Python3 PythonParser.g4
- Run the scipt to run CFG on Python file to be parsed
    - python3 PythonParserTest.py

## Video Demonstration
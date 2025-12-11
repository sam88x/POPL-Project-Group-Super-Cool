# POPL-Project-Group-Super-Cool

## Team Members
- Lauren Bissey
- Sam Byerly
- Sam Hirner
- Jasper Holland

## Project Description
### Project Goal
The goal of this assignment is to implement a grammar, specifically a context-free grammar in ANTLR, to parse the Python programming language for some version 3.x.
The parser does not need to be a complete parser of the Python language, as that would be incredibly comprehensive, but should capture key structures of the language.
The output of the parser is a parse tree.
### Supported Features
- Valid Data Types
    - integers
    - floats
    - arrays
    - booleans
    - strings
- Arithmetic operators (+, -, *, /, %)
- Assignment operators (=, +=, -=, *=, /=)
- if-elif-else blocks
- Conditional statements (<, <=, >, >=, !=, and, or, not)
- while loops
- for loops
- Nested structures
- Comments (single line and multiple lines)

## Parser Requirements
- Uses ANTLR4 and requires language to compile CFG
- Parser targets Python 3.x
- Dependencies to run CFG on Python code:
    - Need Java installed for ANTLR
    - Need Python3 installed
    - Uses antlr4 library in python
        -  `pip install antlr4`
- Dependency to create abstract syntax tree vizualization from input
    - Install GraphViz
        - `winget install Graphviz.Graphviz` (for windows)

## Running Instructions
- Change the file path on line 75 of PythonParserTest.py to the name of the file you wish to parse. Currently, the project_deliverable_3.py file is being parsed:
    - `... open("project_deliverable_3.py", "r") ...`
- Compile the CFG in ANTLR
    - `antlr4 -Dlanguage=Python3 PythonParser.g4`
- Run the scipt to run CFG on Python file to be parsed
    - `python3 PythonParserTest.py`
- To create tree visualization, run GraphViz on the dot file
    - `& "C:\Program Files\Graphviz\bin\dot.exe" -Tpng tree.dot -o tree.png` (for windows)
    - You should adapt the path to dot.exe for your machine if it is installed in a differnt place

## Video Demonstration
[![Video Demonstration](https://www.youtube.com/embed/we-n8IovgD0?si=_s0aq4FQeh3wITw4)](https://www.youtube.com/embed/we-n8IovgD0?si=_s0aq4FQeh3wITw4)


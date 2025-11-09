# antlr4 -Dlanguage=Python3 PythonParser.g4

from antlr4 import *
from PythonParserLexer import PythonParserLexer
from PythonParserParser import PythonParserParser

def test_parser(code_string):
    try:
        input_stream = InputStream(code_string)
        lexer = PythonParserLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        
        parser = PythonParserParser(token_stream)
        tree = parser.start()
        
        if parser.getNumberOfSyntaxErrors() > 0:
            print(f"FAILED: {code_string[:50]}...")
            return False
        else:
            print(f"PASSED: {code_string[:50]}...")
            print(f"   Tree: {tree.toStringTree(recog=parser)}")
            return True
            
    except Exception as e:
        print(f"ERROR: {code_string[:50]}...")
        print(f"   {str(e)}")
        return False

# Test script
with open("project_deliverable_1.py", "r") as f:
    test = f.read()
print(test)

test_parser(test)

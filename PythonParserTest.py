# antlr4 -Dlanguage=Python3 PythonParser.g4

from antlr4 import *
from PythonParserLexer import PythonParserLexer
from PythonParserParser import PythonParserParser

def test_parser(code_string):
    #DEBUG FOR SYMBOLIC NAME INDEXES; UNCOMMENT IF DEBUGING LEXER RULE REMOVALS
    # print("Parser literalNames (sample around INDENT):")
    # for i, lit in enumerate(getattr(PythonParserParser, "literalNames", [])):
    #     if i >= 0 and i < 70:   # print a chunk; adjust upper bound as needed
    #         print(i, lit)
    # print("Parser symbolicNames (sample):")
    # for i, sym in enumerate(getattr(PythonParserParser, "symbolicNames", [])):
    #     if i >= 0 and i < 70:
    #         print(i, sym)

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
        print(type(e))
        return False

# Test script
with open("project_deliverable_3.py", "r") as f:
    test = f.read()

test_parser(test)

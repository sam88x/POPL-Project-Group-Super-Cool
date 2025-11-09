# Generated from PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParserParser import PythonParserParser
else:
    from PythonParserParser import PythonParserParser

# This class defines a complete listener for a parse tree produced by PythonParserParser.
class PythonParserListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParserParser#start.
    def enterStart(self, ctx:PythonParserParser.StartContext):
        pass

    # Exit a parse tree produced by PythonParserParser#start.
    def exitStart(self, ctx:PythonParserParser.StartContext):
        pass


    # Enter a parse tree produced by PythonParserParser#statement.
    def enterStatement(self, ctx:PythonParserParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#statement.
    def exitStatement(self, ctx:PythonParserParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#arithmetic.
    def enterArithmetic(self, ctx:PythonParserParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by PythonParserParser#arithmetic.
    def exitArithmetic(self, ctx:PythonParserParser.ArithmeticContext):
        pass



del PythonParserParser
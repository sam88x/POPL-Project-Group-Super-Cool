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


    # Enter a parse tree produced by PythonParserParser#block.
    def enterBlock(self, ctx:PythonParserParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonParserParser#block.
    def exitBlock(self, ctx:PythonParserParser.BlockContext):
        pass


    # Enter a parse tree produced by PythonParserParser#statement.
    def enterStatement(self, ctx:PythonParserParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#statement.
    def exitStatement(self, ctx:PythonParserParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#while_loop.
    def enterWhile_loop(self, ctx:PythonParserParser.While_loopContext):
        pass

    # Exit a parse tree produced by PythonParserParser#while_loop.
    def exitWhile_loop(self, ctx:PythonParserParser.While_loopContext):
        pass


    # Enter a parse tree produced by PythonParserParser#if_else_block.
    def enterIf_else_block(self, ctx:PythonParserParser.If_else_blockContext):
        pass

    # Exit a parse tree produced by PythonParserParser#if_else_block.
    def exitIf_else_block(self, ctx:PythonParserParser.If_else_blockContext):
        pass


    # Enter a parse tree produced by PythonParserParser#conditional.
    def enterConditional(self, ctx:PythonParserParser.ConditionalContext):
        pass

    # Exit a parse tree produced by PythonParserParser#conditional.
    def exitConditional(self, ctx:PythonParserParser.ConditionalContext):
        pass


    # Enter a parse tree produced by PythonParserParser#relational.
    def enterRelational(self, ctx:PythonParserParser.RelationalContext):
        pass

    # Exit a parse tree produced by PythonParserParser#relational.
    def exitRelational(self, ctx:PythonParserParser.RelationalContext):
        pass


    # Enter a parse tree produced by PythonParserParser#assignment.
    def enterAssignment(self, ctx:PythonParserParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonParserParser#assignment.
    def exitAssignment(self, ctx:PythonParserParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonParserParser#arithmetic.
    def enterArithmetic(self, ctx:PythonParserParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by PythonParserParser#arithmetic.
    def exitArithmetic(self, ctx:PythonParserParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by PythonParserParser#expression.
    def enterExpression(self, ctx:PythonParserParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonParserParser#expression.
    def exitExpression(self, ctx:PythonParserParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonParserParser#array.
    def enterArray(self, ctx:PythonParserParser.ArrayContext):
        pass

    # Exit a parse tree produced by PythonParserParser#array.
    def exitArray(self, ctx:PythonParserParser.ArrayContext):
        pass



del PythonParserParser
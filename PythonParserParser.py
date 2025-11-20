# Generated from PythonParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,158,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,
        0,1,1,1,1,3,1,44,8,1,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,2,1,2,
        1,2,5,2,56,8,2,10,2,12,2,59,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,
        68,8,3,1,3,3,3,71,8,3,1,4,1,4,1,4,1,4,3,4,77,8,4,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,105,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        3,9,114,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,5,9,131,8,9,10,9,12,9,134,9,9,1,10,1,10,1,10,1,10,1,10,1,
        10,3,10,142,8,10,1,11,1,11,1,11,1,11,5,11,148,8,11,10,11,12,11,151,
        9,11,1,11,3,11,154,8,11,1,11,1,11,1,11,0,1,18,12,0,2,4,6,8,10,12,
        14,16,18,20,22,0,0,171,0,27,1,0,0,0,2,43,1,0,0,0,4,45,1,0,0,0,6,
        62,1,0,0,0,8,76,1,0,0,0,10,78,1,0,0,0,12,83,1,0,0,0,14,87,1,0,0,
        0,16,104,1,0,0,0,18,113,1,0,0,0,20,141,1,0,0,0,22,143,1,0,0,0,24,
        26,5,26,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,
        0,0,28,35,1,0,0,0,29,27,1,0,0,0,30,31,3,2,1,0,31,32,5,26,0,0,32,
        34,1,0,0,0,33,30,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,
        0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,3,2,1,0,39,40,5,0,0,1,40,1,1,
        0,0,0,41,44,3,16,8,0,42,44,3,6,3,0,43,41,1,0,0,0,43,42,1,0,0,0,44,
        3,1,0,0,0,45,49,5,1,0,0,46,48,5,26,0,0,47,46,1,0,0,0,48,51,1,0,0,
        0,49,47,1,0,0,0,49,50,1,0,0,0,50,57,1,0,0,0,51,49,1,0,0,0,52,53,
        3,2,1,0,53,54,5,26,0,0,54,56,1,0,0,0,55,52,1,0,0,0,56,59,1,0,0,0,
        57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,3,
        2,1,0,61,5,1,0,0,0,62,63,5,20,0,0,63,64,3,14,7,0,64,65,5,2,0,0,65,
        67,3,4,2,0,66,68,3,8,4,0,67,66,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,
        0,69,71,3,12,6,0,70,69,1,0,0,0,70,71,1,0,0,0,71,7,1,0,0,0,72,77,
        3,10,5,0,73,74,3,10,5,0,74,75,3,8,4,0,75,77,1,0,0,0,76,72,1,0,0,
        0,76,73,1,0,0,0,77,9,1,0,0,0,78,79,5,21,0,0,79,80,3,14,7,0,80,81,
        5,2,0,0,81,82,3,4,2,0,82,11,1,0,0,0,83,84,5,22,0,0,84,85,5,2,0,0,
        85,86,3,4,2,0,86,13,1,0,0,0,87,88,5,3,0,0,88,15,1,0,0,0,89,90,5,
        28,0,0,90,91,5,4,0,0,91,105,3,20,10,0,92,93,5,28,0,0,93,94,5,5,0,
        0,94,105,3,18,9,0,95,96,5,28,0,0,96,97,5,6,0,0,97,105,3,18,9,0,98,
        99,5,28,0,0,99,100,5,7,0,0,100,105,3,18,9,0,101,102,5,28,0,0,102,
        103,5,8,0,0,103,105,3,18,9,0,104,89,1,0,0,0,104,92,1,0,0,0,104,95,
        1,0,0,0,104,98,1,0,0,0,104,101,1,0,0,0,105,17,1,0,0,0,106,107,6,
        9,-1,0,107,108,5,9,0,0,108,109,3,18,9,0,109,110,5,10,0,0,110,114,
        1,0,0,0,111,114,5,28,0,0,112,114,5,29,0,0,113,106,1,0,0,0,113,111,
        1,0,0,0,113,112,1,0,0,0,114,132,1,0,0,0,115,116,10,7,0,0,116,117,
        5,11,0,0,117,131,3,18,9,8,118,119,10,6,0,0,119,120,5,12,0,0,120,
        131,3,18,9,7,121,122,10,5,0,0,122,123,5,13,0,0,123,131,3,18,9,6,
        124,125,10,4,0,0,125,126,5,14,0,0,126,131,3,18,9,5,127,128,10,3,
        0,0,128,129,5,15,0,0,129,131,3,18,9,4,130,115,1,0,0,0,130,118,1,
        0,0,0,130,121,1,0,0,0,130,124,1,0,0,0,130,127,1,0,0,0,131,134,1,
        0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,19,1,0,0,0,134,132,1,0,
        0,0,135,142,3,18,9,0,136,142,5,28,0,0,137,142,5,29,0,0,138,142,5,
        19,0,0,139,142,5,27,0,0,140,142,3,22,11,0,141,135,1,0,0,0,141,136,
        1,0,0,0,141,137,1,0,0,0,141,138,1,0,0,0,141,139,1,0,0,0,141,140,
        1,0,0,0,142,21,1,0,0,0,143,153,5,16,0,0,144,145,3,20,10,0,145,146,
        5,17,0,0,146,148,1,0,0,0,147,144,1,0,0,0,148,151,1,0,0,0,149,147,
        1,0,0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,149,1,0,0,0,152,154,
        3,20,10,0,153,149,1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,156,
        5,18,0,0,156,23,1,0,0,0,15,27,35,43,49,57,67,70,76,104,113,130,132,
        141,149,153
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\t'", "':'", "'test == test'", "'='", 
                     "'+='", "'-='", "'*='", "'/='", "'('", "')'", "'*'", 
                     "'/'", "'%'", "'+'", "'-'", "'['", "','", "']'", "<INVALID>", 
                     "'if'", "'elif'", "'else'", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BOOLEAN", 
                      "IF", "ELIF", "ELSE", "AND", "OR", "NOT", "NEWLINE", 
                      "STRING", "VARIABLE", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_if_else_block = 3
    RULE_elif_blocks = 4
    RULE_elif_block = 5
    RULE_else_block = 6
    RULE_conditional = 7
    RULE_assignment = 8
    RULE_arithmetic = 9
    RULE_expression = 10
    RULE_array = 11

    ruleNames =  [ "start", "statement", "block", "if_else_block", "elif_blocks", 
                   "elif_block", "else_block", "conditional", "assignment", 
                   "arithmetic", "expression", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    BOOLEAN=19
    IF=20
    ELIF=21
    ELSE=22
    AND=23
    OR=24
    NOT=25
    NEWLINE=26
    STRING=27
    VARIABLE=28
    NUMBER=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StatementContext,i)


        def EOF(self):
            return self.getToken(PythonParserParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.NEWLINE)
            else:
                return self.getToken(PythonParserParser.NEWLINE, i)

        def getRuleIndex(self):
            return PythonParserParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = PythonParserParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 24
                self.match(PythonParserParser.NEWLINE)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30
                    self.statement()
                    self.state = 31
                    self.match(PythonParserParser.NEWLINE) 
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 38
            self.statement()
            self.state = 39
            self.match(PythonParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PythonParserParser.AssignmentContext,0)


        def if_else_block(self):
            return self.getTypedRuleContext(PythonParserParser.If_else_blockContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PythonParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.assignment()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.if_else_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.NEWLINE)
            else:
                return self.getToken(PythonParserParser.NEWLINE, i)

        def getRuleIndex(self):
            return PythonParserParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = PythonParserParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(PythonParserParser.T__0)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 46
                self.match(PythonParserParser.NEWLINE)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 52
                    self.statement()
                    self.state = 53
                    self.match(PythonParserParser.NEWLINE) 
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 60
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_else_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PythonParserParser.IF, 0)

        def conditional(self):
            return self.getTypedRuleContext(PythonParserParser.ConditionalContext,0)


        def block(self):
            return self.getTypedRuleContext(PythonParserParser.BlockContext,0)


        def elif_blocks(self):
            return self.getTypedRuleContext(PythonParserParser.Elif_blocksContext,0)


        def else_block(self):
            return self.getTypedRuleContext(PythonParserParser.Else_blockContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_if_else_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_else_block" ):
                listener.enterIf_else_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_else_block" ):
                listener.exitIf_else_block(self)




    def if_else_block(self):

        localctx = PythonParserParser.If_else_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(PythonParserParser.IF)
            self.state = 63
            self.conditional()
            self.state = 64
            self.match(PythonParserParser.T__1)
            self.state = 65
            self.block()
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 66
                self.elif_blocks()


            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 69
                self.else_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_blocksContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_block(self):
            return self.getTypedRuleContext(PythonParserParser.Elif_blockContext,0)


        def elif_blocks(self):
            return self.getTypedRuleContext(PythonParserParser.Elif_blocksContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_elif_blocks

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_blocks" ):
                listener.enterElif_blocks(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_blocks" ):
                listener.exitElif_blocks(self)




    def elif_blocks(self):

        localctx = PythonParserParser.Elif_blocksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elif_blocks)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.elif_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.elif_block()
                self.state = 74
                self.elif_blocks()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(PythonParserParser.ELIF, 0)

        def conditional(self):
            return self.getTypedRuleContext(PythonParserParser.ConditionalContext,0)


        def block(self):
            return self.getTypedRuleContext(PythonParserParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_elif_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_block" ):
                listener.enterElif_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_block" ):
                listener.exitElif_block(self)




    def elif_block(self):

        localctx = PythonParserParser.Elif_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elif_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(PythonParserParser.ELIF)
            self.state = 79
            self.conditional()
            self.state = 80
            self.match(PythonParserParser.T__1)
            self.state = 81
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(PythonParserParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(PythonParserParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_else_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_block" ):
                listener.enterElse_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_block" ):
                listener.exitElse_block(self)




    def else_block(self):

        localctx = PythonParserParser.Else_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(PythonParserParser.ELSE)
            self.state = 84
            self.match(PythonParserParser.T__1)
            self.state = 85
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParserParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = PythonParserParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(PythonParserParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(PythonParserParser.VARIABLE, 0)

        def expression(self):
            return self.getTypedRuleContext(PythonParserParser.ExpressionContext,0)


        def arithmetic(self):
            return self.getTypedRuleContext(PythonParserParser.ArithmeticContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PythonParserParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(PythonParserParser.VARIABLE)
                self.state = 90
                self.match(PythonParserParser.T__3)
                self.state = 91
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(PythonParserParser.VARIABLE)
                self.state = 93
                self.match(PythonParserParser.T__4)
                self.state = 94
                self.arithmetic(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.match(PythonParserParser.VARIABLE)
                self.state = 96
                self.match(PythonParserParser.T__5)
                self.state = 97
                self.arithmetic(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.match(PythonParserParser.VARIABLE)
                self.state = 99
                self.match(PythonParserParser.T__6)
                self.state = 100
                self.arithmetic(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.match(PythonParserParser.VARIABLE)
                self.state = 102
                self.match(PythonParserParser.T__7)
                self.state = 103
                self.arithmetic(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ArithmeticContext,i)


        def VARIABLE(self):
            return self.getToken(PythonParserParser.VARIABLE, 0)

        def NUMBER(self):
            return self.getToken(PythonParserParser.NUMBER, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)



    def arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParserParser.ArithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 107
                self.match(PythonParserParser.T__8)
                self.state = 108
                self.arithmetic(0)
                self.state = 109
                self.match(PythonParserParser.T__9)
                pass
            elif token in [28]:
                self.state = 111
                self.match(PythonParserParser.VARIABLE)
                pass
            elif token in [29]:
                self.state = 112
                self.match(PythonParserParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 130
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 115
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 116
                        self.match(PythonParserParser.T__10)
                        self.state = 117
                        self.arithmetic(8)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 118
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 119
                        self.match(PythonParserParser.T__11)
                        self.state = 120
                        self.arithmetic(7)
                        pass

                    elif la_ == 3:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 121
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 122
                        self.match(PythonParserParser.T__12)
                        self.state = 123
                        self.arithmetic(6)
                        pass

                    elif la_ == 4:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 124
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 125
                        self.match(PythonParserParser.T__13)
                        self.state = 126
                        self.arithmetic(5)
                        pass

                    elif la_ == 5:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 127
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 128
                        self.match(PythonParserParser.T__14)
                        self.state = 129
                        self.arithmetic(4)
                        pass

             
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self):
            return self.getTypedRuleContext(PythonParserParser.ArithmeticContext,0)


        def VARIABLE(self):
            return self.getToken(PythonParserParser.VARIABLE, 0)

        def NUMBER(self):
            return self.getToken(PythonParserParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(PythonParserParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(PythonParserParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(PythonParserParser.ArrayContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PythonParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.arithmetic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(PythonParserParser.VARIABLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.match(PythonParserParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.match(PythonParserParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.match(PythonParserParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 140
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PythonParserParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = PythonParserParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(PythonParserParser.T__15)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 940114432) != 0):
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 144
                        self.expression()
                        self.state = 145
                        self.match(PythonParserParser.T__16) 
                    self.state = 151
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                self.state = 152
                self.expression()


            self.state = 155
            self.match(PythonParserParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.arithmetic_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_sempred(self, localctx:ArithmeticContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         





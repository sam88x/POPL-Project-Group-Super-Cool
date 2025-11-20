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
        4,1,35,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,0,5,0,36,8,0,10,0,12,0,39,9,0,
        1,0,1,0,1,0,1,1,1,1,3,1,46,8,1,1,2,1,2,5,2,50,8,2,10,2,12,2,53,9,
        2,1,2,1,2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,3,3,70,8,3,1,3,3,3,73,8,3,1,4,1,4,1,4,1,4,3,4,79,8,4,1,5,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,3,7,103,8,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,111,8,
        7,10,7,12,7,114,9,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,133,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,142,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,5,10,159,8,10,10,10,12,10,162,9,10,
        1,11,1,11,1,11,1,11,1,11,1,11,3,11,170,8,11,1,12,1,12,1,12,1,12,
        5,12,176,8,12,10,12,12,12,179,9,12,1,12,3,12,182,8,12,1,12,1,12,
        1,12,0,2,14,20,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,1,1,0,5,10,
        204,0,29,1,0,0,0,2,45,1,0,0,0,4,47,1,0,0,0,6,64,1,0,0,0,8,78,1,0,
        0,0,10,80,1,0,0,0,12,85,1,0,0,0,14,102,1,0,0,0,16,115,1,0,0,0,18,
        132,1,0,0,0,20,141,1,0,0,0,22,169,1,0,0,0,24,171,1,0,0,0,26,28,5,
        31,0,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,
        37,1,0,0,0,31,29,1,0,0,0,32,33,3,2,1,0,33,34,5,31,0,0,34,36,1,0,
        0,0,35,32,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,
        1,0,0,0,39,37,1,0,0,0,40,41,3,2,1,0,41,42,5,0,0,1,42,1,1,0,0,0,43,
        46,3,18,9,0,44,46,3,6,3,0,45,43,1,0,0,0,45,44,1,0,0,0,46,3,1,0,0,
        0,47,51,5,1,0,0,48,50,5,31,0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,
        1,0,0,0,51,52,1,0,0,0,52,59,1,0,0,0,53,51,1,0,0,0,54,55,3,2,1,0,
        55,56,5,31,0,0,56,58,1,0,0,0,57,54,1,0,0,0,58,61,1,0,0,0,59,57,1,
        0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,3,2,1,0,63,
        5,1,0,0,0,64,65,5,25,0,0,65,66,3,14,7,0,66,67,5,2,0,0,67,69,3,4,
        2,0,68,70,3,8,4,0,69,68,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,73,
        3,12,6,0,72,71,1,0,0,0,72,73,1,0,0,0,73,7,1,0,0,0,74,79,3,10,5,0,
        75,76,3,10,5,0,76,77,3,8,4,0,77,79,1,0,0,0,78,74,1,0,0,0,78,75,1,
        0,0,0,79,9,1,0,0,0,80,81,5,26,0,0,81,82,3,14,7,0,82,83,5,2,0,0,83,
        84,3,4,2,0,84,11,1,0,0,0,85,86,5,27,0,0,86,87,5,2,0,0,87,88,3,4,
        2,0,88,13,1,0,0,0,89,90,6,7,-1,0,90,91,5,3,0,0,91,92,3,14,7,0,92,
        93,5,4,0,0,93,103,1,0,0,0,94,95,5,30,0,0,95,103,3,14,7,6,96,97,3,
        20,10,0,97,98,3,16,8,0,98,99,3,20,10,0,99,103,1,0,0,0,100,103,5,
        24,0,0,101,103,3,20,10,0,102,89,1,0,0,0,102,94,1,0,0,0,102,96,1,
        0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,112,1,0,0,0,104,105,10,
        5,0,0,105,106,5,28,0,0,106,111,3,14,7,6,107,108,10,4,0,0,108,109,
        5,29,0,0,109,111,3,14,7,5,110,104,1,0,0,0,110,107,1,0,0,0,111,114,
        1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,15,1,0,0,0,114,112,1,
        0,0,0,115,116,7,0,0,0,116,17,1,0,0,0,117,118,5,33,0,0,118,119,5,
        11,0,0,119,133,3,22,11,0,120,121,5,33,0,0,121,122,5,12,0,0,122,133,
        3,20,10,0,123,124,5,33,0,0,124,125,5,13,0,0,125,133,3,20,10,0,126,
        127,5,33,0,0,127,128,5,14,0,0,128,133,3,20,10,0,129,130,5,33,0,0,
        130,131,5,15,0,0,131,133,3,20,10,0,132,117,1,0,0,0,132,120,1,0,0,
        0,132,123,1,0,0,0,132,126,1,0,0,0,132,129,1,0,0,0,133,19,1,0,0,0,
        134,135,6,10,-1,0,135,136,5,3,0,0,136,137,3,20,10,0,137,138,5,4,
        0,0,138,142,1,0,0,0,139,142,5,33,0,0,140,142,5,34,0,0,141,134,1,
        0,0,0,141,139,1,0,0,0,141,140,1,0,0,0,142,160,1,0,0,0,143,144,10,
        7,0,0,144,145,5,16,0,0,145,159,3,20,10,8,146,147,10,6,0,0,147,148,
        5,17,0,0,148,159,3,20,10,7,149,150,10,5,0,0,150,151,5,18,0,0,151,
        159,3,20,10,6,152,153,10,4,0,0,153,154,5,19,0,0,154,159,3,20,10,
        5,155,156,10,3,0,0,156,157,5,20,0,0,157,159,3,20,10,4,158,143,1,
        0,0,0,158,146,1,0,0,0,158,149,1,0,0,0,158,152,1,0,0,0,158,155,1,
        0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,21,1,0,
        0,0,162,160,1,0,0,0,163,170,3,20,10,0,164,170,5,33,0,0,165,170,5,
        34,0,0,166,170,5,24,0,0,167,170,5,32,0,0,168,170,3,24,12,0,169,163,
        1,0,0,0,169,164,1,0,0,0,169,165,1,0,0,0,169,166,1,0,0,0,169,167,
        1,0,0,0,169,168,1,0,0,0,170,23,1,0,0,0,171,181,5,21,0,0,172,173,
        3,22,11,0,173,174,5,22,0,0,174,176,1,0,0,0,175,172,1,0,0,0,176,179,
        1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,177,
        1,0,0,0,180,182,3,22,11,0,181,177,1,0,0,0,181,182,1,0,0,0,182,183,
        1,0,0,0,183,184,5,23,0,0,184,25,1,0,0,0,18,29,37,45,51,59,69,72,
        78,102,110,112,132,141,158,160,169,177,181
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\t'", "':'", "'('", "')'", "'<'", "'<='", 
                     "'>'", "'>='", "'=='", "'!='", "'='", "'+='", "'-='", 
                     "'*='", "'/='", "'*'", "'/'", "'%'", "'+'", "'-'", 
                     "'['", "','", "']'", "<INVALID>", "'if'", "'elif'", 
                     "'else'", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOLEAN", "IF", "ELIF", "ELSE", "AND", "OR", "NOT", 
                      "NEWLINE", "STRING", "VARIABLE", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_if_else_block = 3
    RULE_elif_blocks = 4
    RULE_elif_block = 5
    RULE_else_block = 6
    RULE_conditional = 7
    RULE_relational = 8
    RULE_assignment = 9
    RULE_arithmetic = 10
    RULE_expression = 11
    RULE_array = 12

    ruleNames =  [ "start", "statement", "block", "if_else_block", "elif_blocks", 
                   "elif_block", "else_block", "conditional", "relational", 
                   "assignment", "arithmetic", "expression", "array" ]

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
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    BOOLEAN=24
    IF=25
    ELIF=26
    ELSE=27
    AND=28
    OR=29
    NOT=30
    NEWLINE=31
    STRING=32
    VARIABLE=33
    NUMBER=34
    WS=35

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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 26
                self.match(PythonParserParser.NEWLINE)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 32
                    self.statement()
                    self.state = 33
                    self.match(PythonParserParser.NEWLINE) 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 40
            self.statement()
            self.state = 41
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
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.assignment()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
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
            self.state = 47
            self.match(PythonParserParser.T__0)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 48
                self.match(PythonParserParser.NEWLINE)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 54
                    self.statement()
                    self.state = 55
                    self.match(PythonParserParser.NEWLINE) 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 62
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
            self.state = 64
            self.match(PythonParserParser.IF)
            self.state = 65
            self.conditional(0)
            self.state = 66
            self.match(PythonParserParser.T__1)
            self.state = 67
            self.block()
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 68
                self.elif_blocks()


            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 71
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
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.elif_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.elif_block()
                self.state = 76
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
            self.state = 80
            self.match(PythonParserParser.ELIF)
            self.state = 81
            self.conditional(0)
            self.state = 82
            self.match(PythonParserParser.T__1)
            self.state = 83
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
            self.state = 85
            self.match(PythonParserParser.ELSE)
            self.state = 86
            self.match(PythonParserParser.T__1)
            self.state = 87
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

        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ConditionalContext,i)


        def NOT(self):
            return self.getToken(PythonParserParser.NOT, 0)

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ArithmeticContext,i)


        def relational(self):
            return self.getTypedRuleContext(PythonParserParser.RelationalContext,0)


        def BOOLEAN(self):
            return self.getToken(PythonParserParser.BOOLEAN, 0)

        def AND(self):
            return self.getToken(PythonParserParser.AND, 0)

        def OR(self):
            return self.getToken(PythonParserParser.OR, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)



    def conditional(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParserParser.ConditionalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_conditional, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 90
                self.match(PythonParserParser.T__2)
                self.state = 91
                self.conditional(0)
                self.state = 92
                self.match(PythonParserParser.T__3)
                pass

            elif la_ == 2:
                self.state = 94
                self.match(PythonParserParser.NOT)
                self.state = 95
                self.conditional(6)
                pass

            elif la_ == 3:
                self.state = 96
                self.arithmetic(0)
                self.state = 97
                self.relational()
                self.state = 98
                self.arithmetic(0)
                pass

            elif la_ == 4:
                self.state = 100
                self.match(PythonParserParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.state = 101
                self.arithmetic(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 104
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 105
                        self.match(PythonParserParser.AND)
                        self.state = 106
                        self.conditional(6)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 107
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 108
                        self.match(PythonParserParser.OR)
                        self.state = 109
                        self.conditional(5)
                        pass

             
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParserParser.RULE_relational

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)




    def relational(self):

        localctx = PythonParserParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(PythonParserParser.VARIABLE)
                self.state = 118
                self.match(PythonParserParser.T__10)
                self.state = 119
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(PythonParserParser.VARIABLE)
                self.state = 121
                self.match(PythonParserParser.T__11)
                self.state = 122
                self.arithmetic(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(PythonParserParser.VARIABLE)
                self.state = 124
                self.match(PythonParserParser.T__12)
                self.state = 125
                self.arithmetic(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.match(PythonParserParser.VARIABLE)
                self.state = 127
                self.match(PythonParserParser.T__13)
                self.state = 128
                self.arithmetic(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.match(PythonParserParser.VARIABLE)
                self.state = 130
                self.match(PythonParserParser.T__14)
                self.state = 131
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 135
                self.match(PythonParserParser.T__2)
                self.state = 136
                self.arithmetic(0)
                self.state = 137
                self.match(PythonParserParser.T__3)
                pass
            elif token in [33]:
                self.state = 139
                self.match(PythonParserParser.VARIABLE)
                pass
            elif token in [34]:
                self.state = 140
                self.match(PythonParserParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 158
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 143
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 144
                        self.match(PythonParserParser.T__15)
                        self.state = 145
                        self.arithmetic(8)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 146
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 147
                        self.match(PythonParserParser.T__16)
                        self.state = 148
                        self.arithmetic(7)
                        pass

                    elif la_ == 3:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 149
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 150
                        self.match(PythonParserParser.T__17)
                        self.state = 151
                        self.arithmetic(6)
                        pass

                    elif la_ == 4:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 152
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 153
                        self.match(PythonParserParser.T__18)
                        self.state = 154
                        self.arithmetic(5)
                        pass

                    elif la_ == 5:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 155
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 156
                        self.match(PythonParserParser.T__19)
                        self.state = 157
                        self.arithmetic(4)
                        pass

             
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.arithmetic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(PythonParserParser.VARIABLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(PythonParserParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.match(PythonParserParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.match(PythonParserParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 168
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
        self.enterRule(localctx, 24, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(PythonParserParser.T__20)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30083645448) != 0):
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 172
                        self.expression()
                        self.state = 173
                        self.match(PythonParserParser.T__21) 
                    self.state = 179
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                self.state = 180
                self.expression()


            self.state = 183
            self.match(PythonParserParser.T__22)
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
        self._predicates[7] = self.conditional_sempred
        self._predicates[10] = self.arithmetic_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def conditional_sempred(self, localctx:ConditionalContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def arithmetic_sempred(self, localctx:ArithmeticContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         





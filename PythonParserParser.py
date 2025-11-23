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
        4,1,36,185,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,4,0,31,8,0,11,0,12,0,32,5,0,35,8,0,10,0,12,0,38,9,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,2,
        1,2,1,2,3,2,56,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,4,1,4,1,4,1,
        4,1,4,3,4,85,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,3,5,100,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,108,8,5,10,5,12,5,111,
        9,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,130,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,141,
        8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        5,8,158,8,8,10,8,12,8,161,9,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,169,8,
        9,1,10,1,10,1,10,1,10,5,10,175,8,10,10,10,12,10,178,9,10,1,10,3,
        10,181,8,10,1,10,1,10,1,10,0,2,10,16,11,0,2,4,6,8,10,12,14,16,18,
        20,0,1,1,0,5,10,206,0,25,1,0,0,0,2,42,1,0,0,0,4,55,1,0,0,0,6,57,
        1,0,0,0,8,62,1,0,0,0,10,99,1,0,0,0,12,112,1,0,0,0,14,129,1,0,0,0,
        16,140,1,0,0,0,18,168,1,0,0,0,20,170,1,0,0,0,22,24,5,32,0,0,23,22,
        1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,36,1,0,0,0,
        27,25,1,0,0,0,28,30,3,4,2,0,29,31,5,32,0,0,30,29,1,0,0,0,31,32,1,
        0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,28,1,0,0,0,35,
        38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,
        0,39,40,3,4,2,0,40,41,5,0,0,1,41,1,1,0,0,0,42,43,5,1,0,0,43,49,3,
        4,2,0,44,45,5,32,0,0,45,46,5,1,0,0,46,48,3,4,2,0,47,44,1,0,0,0,48,
        51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,3,1,0,0,0,51,49,1,0,0,
        0,52,56,3,14,7,0,53,56,3,8,4,0,54,56,3,6,3,0,55,52,1,0,0,0,55,53,
        1,0,0,0,55,54,1,0,0,0,56,5,1,0,0,0,57,58,5,31,0,0,58,59,3,10,5,0,
        59,60,5,2,0,0,60,61,3,2,1,0,61,7,1,0,0,0,62,63,5,25,0,0,63,64,3,
        10,5,0,64,65,5,2,0,0,65,66,5,32,0,0,66,76,3,2,1,0,67,68,5,32,0,0,
        68,69,5,26,0,0,69,70,3,10,5,0,70,71,5,2,0,0,71,72,5,32,0,0,72,73,
        3,2,1,0,73,75,1,0,0,0,74,67,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,
        76,77,1,0,0,0,77,84,1,0,0,0,78,76,1,0,0,0,79,80,5,32,0,0,80,81,5,
        27,0,0,81,82,5,2,0,0,82,83,5,32,0,0,83,85,3,2,1,0,84,79,1,0,0,0,
        84,85,1,0,0,0,85,9,1,0,0,0,86,87,6,5,-1,0,87,88,5,3,0,0,88,89,3,
        10,5,0,89,90,5,4,0,0,90,100,1,0,0,0,91,92,5,30,0,0,92,100,3,10,5,
        6,93,94,3,16,8,0,94,95,3,12,6,0,95,96,3,16,8,0,96,100,1,0,0,0,97,
        100,5,24,0,0,98,100,3,16,8,0,99,86,1,0,0,0,99,91,1,0,0,0,99,93,1,
        0,0,0,99,97,1,0,0,0,99,98,1,0,0,0,100,109,1,0,0,0,101,102,10,5,0,
        0,102,103,5,28,0,0,103,108,3,10,5,6,104,105,10,4,0,0,105,106,5,29,
        0,0,106,108,3,10,5,5,107,101,1,0,0,0,107,104,1,0,0,0,108,111,1,0,
        0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,11,1,0,0,0,111,109,1,0,0,
        0,112,113,7,0,0,0,113,13,1,0,0,0,114,115,5,34,0,0,115,116,5,11,0,
        0,116,130,3,18,9,0,117,118,5,34,0,0,118,119,5,12,0,0,119,130,3,16,
        8,0,120,121,5,34,0,0,121,122,5,13,0,0,122,130,3,16,8,0,123,124,5,
        34,0,0,124,125,5,14,0,0,125,130,3,16,8,0,126,127,5,34,0,0,127,128,
        5,15,0,0,128,130,3,16,8,0,129,114,1,0,0,0,129,117,1,0,0,0,129,120,
        1,0,0,0,129,123,1,0,0,0,129,126,1,0,0,0,130,15,1,0,0,0,131,132,6,
        8,-1,0,132,133,5,3,0,0,133,134,3,16,8,0,134,135,5,4,0,0,135,141,
        1,0,0,0,136,137,5,16,0,0,137,141,3,16,8,8,138,141,5,34,0,0,139,141,
        5,35,0,0,140,131,1,0,0,0,140,136,1,0,0,0,140,138,1,0,0,0,140,139,
        1,0,0,0,141,159,1,0,0,0,142,143,10,7,0,0,143,144,5,17,0,0,144,158,
        3,16,8,8,145,146,10,6,0,0,146,147,5,18,0,0,147,158,3,16,8,7,148,
        149,10,5,0,0,149,150,5,19,0,0,150,158,3,16,8,6,151,152,10,4,0,0,
        152,153,5,20,0,0,153,158,3,16,8,5,154,155,10,3,0,0,155,156,5,16,
        0,0,156,158,3,16,8,4,157,142,1,0,0,0,157,145,1,0,0,0,157,148,1,0,
        0,0,157,151,1,0,0,0,157,154,1,0,0,0,158,161,1,0,0,0,159,157,1,0,
        0,0,159,160,1,0,0,0,160,17,1,0,0,0,161,159,1,0,0,0,162,169,3,16,
        8,0,163,169,5,34,0,0,164,169,5,35,0,0,165,169,5,24,0,0,166,169,5,
        33,0,0,167,169,3,20,10,0,168,162,1,0,0,0,168,163,1,0,0,0,168,164,
        1,0,0,0,168,165,1,0,0,0,168,166,1,0,0,0,168,167,1,0,0,0,169,19,1,
        0,0,0,170,180,5,21,0,0,171,172,3,18,9,0,172,173,5,22,0,0,173,175,
        1,0,0,0,174,171,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,
        1,0,0,0,177,179,1,0,0,0,178,176,1,0,0,0,179,181,3,18,9,0,180,176,
        1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,5,23,0,0,183,21,
        1,0,0,0,17,25,32,36,49,55,76,84,99,107,109,129,140,157,159,168,176,
        180
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\t'", "':'", "'('", "')'", "'<'", "'<='", 
                     "'>'", "'>='", "'=='", "'!='", "'='", "'+='", "'-='", 
                     "'*='", "'/='", "'-'", "'*'", "'/'", "'%'", "'+'", 
                     "'['", "','", "']'", "<INVALID>", "'if'", "'elif'", 
                     "'else'", "'and'", "'or'", "'not'", "'while'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOLEAN", "IF", "ELIF", "ELSE", "AND", "OR", "NOT", 
                      "WHILE", "NEWLINE", "STRING", "VARIABLE", "NUMBER", 
                      "WS" ]

    RULE_start = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_while_loop = 3
    RULE_if_else_block = 4
    RULE_conditional = 5
    RULE_relational = 6
    RULE_assignment = 7
    RULE_arithmetic = 8
    RULE_expression = 9
    RULE_array = 10

    ruleNames =  [ "start", "block", "statement", "while_loop", "if_else_block", 
                   "conditional", "relational", "assignment", "arithmetic", 
                   "expression", "array" ]

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
    WHILE=31
    NEWLINE=32
    STRING=33
    VARIABLE=34
    NUMBER=35
    WS=36

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 22
                self.match(PythonParserParser.NEWLINE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 28
                    self.statement()
                    self.state = 30 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 29
                        self.match(PythonParserParser.NEWLINE)
                        self.state = 32 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==32):
                            break
             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 39
            self.statement()
            self.state = 40
            self.match(PythonParserParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(PythonParserParser.T__0)
            self.state = 43
            self.statement()
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 44
                    self.match(PythonParserParser.NEWLINE)
                    self.state = 45
                    self.match(PythonParserParser.T__0)
                    self.state = 46
                    self.statement() 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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


        def while_loop(self):
            return self.getTypedRuleContext(PythonParserParser.While_loopContext,0)


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
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.assignment()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.if_else_block()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.while_loop()
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


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(PythonParserParser.WHILE, 0)

        def conditional(self):
            return self.getTypedRuleContext(PythonParserParser.ConditionalContext,0)


        def block(self):
            return self.getTypedRuleContext(PythonParserParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)




    def while_loop(self):

        localctx = PythonParserParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(PythonParserParser.WHILE)
            self.state = 58
            self.conditional(0)
            self.state = 59
            self.match(PythonParserParser.T__1)
            self.state = 60
            self.block()
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

        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ConditionalContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.NEWLINE)
            else:
                return self.getToken(PythonParserParser.NEWLINE, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.BlockContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.BlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.ELIF)
            else:
                return self.getToken(PythonParserParser.ELIF, i)

        def ELSE(self):
            return self.getToken(PythonParserParser.ELSE, 0)

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
        self.enterRule(localctx, 8, self.RULE_if_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(PythonParserParser.IF)
            self.state = 63
            self.conditional(0)
            self.state = 64
            self.match(PythonParserParser.T__1)
            self.state = 65
            self.match(PythonParserParser.NEWLINE)
            self.state = 66
            self.block()
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 67
                    self.match(PythonParserParser.NEWLINE)
                    self.state = 68
                    self.match(PythonParserParser.ELIF)
                    self.state = 69
                    self.conditional(0)
                    self.state = 70
                    self.match(PythonParserParser.T__1)
                    self.state = 71
                    self.match(PythonParserParser.NEWLINE)
                    self.state = 72
                    self.block() 
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(PythonParserParser.NEWLINE)
                self.state = 80
                self.match(PythonParserParser.ELSE)
                self.state = 81
                self.match(PythonParserParser.T__1)
                self.state = 82
                self.match(PythonParserParser.NEWLINE)
                self.state = 83
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_conditional, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 87
                self.match(PythonParserParser.T__2)
                self.state = 88
                self.conditional(0)
                self.state = 89
                self.match(PythonParserParser.T__3)
                pass

            elif la_ == 2:
                self.state = 91
                self.match(PythonParserParser.NOT)
                self.state = 92
                self.conditional(6)
                pass

            elif la_ == 3:
                self.state = 93
                self.arithmetic(0)
                self.state = 94
                self.relational()
                self.state = 95
                self.arithmetic(0)
                pass

            elif la_ == 4:
                self.state = 97
                self.match(PythonParserParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.state = 98
                self.arithmetic(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 107
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 101
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 102
                        self.match(PythonParserParser.AND)
                        self.state = 103
                        self.conditional(6)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 104
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 105
                        self.match(PythonParserParser.OR)
                        self.state = 106
                        self.conditional(5)
                        pass

             
                self.state = 111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
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
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(PythonParserParser.VARIABLE)
                self.state = 115
                self.match(PythonParserParser.T__10)
                self.state = 116
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(PythonParserParser.VARIABLE)
                self.state = 118
                self.match(PythonParserParser.T__11)
                self.state = 119
                self.arithmetic(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.match(PythonParserParser.VARIABLE)
                self.state = 121
                self.match(PythonParserParser.T__12)
                self.state = 122
                self.arithmetic(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(PythonParserParser.VARIABLE)
                self.state = 124
                self.match(PythonParserParser.T__13)
                self.state = 125
                self.arithmetic(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.match(PythonParserParser.VARIABLE)
                self.state = 127
                self.match(PythonParserParser.T__14)
                self.state = 128
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 132
                self.match(PythonParserParser.T__2)
                self.state = 133
                self.arithmetic(0)
                self.state = 134
                self.match(PythonParserParser.T__3)
                pass
            elif token in [16]:
                self.state = 136
                self.match(PythonParserParser.T__15)
                self.state = 137
                self.arithmetic(8)
                pass
            elif token in [34]:
                self.state = 138
                self.match(PythonParserParser.VARIABLE)
                pass
            elif token in [35]:
                self.state = 139
                self.match(PythonParserParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 157
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 142
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 143
                        self.match(PythonParserParser.T__16)
                        self.state = 144
                        self.arithmetic(8)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 145
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 146
                        self.match(PythonParserParser.T__17)
                        self.state = 147
                        self.arithmetic(7)
                        pass

                    elif la_ == 3:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 148
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 149
                        self.match(PythonParserParser.T__18)
                        self.state = 150
                        self.arithmetic(6)
                        pass

                    elif la_ == 4:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 151
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 152
                        self.match(PythonParserParser.T__19)
                        self.state = 153
                        self.arithmetic(5)
                        pass

                    elif la_ == 5:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 154
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 155
                        self.match(PythonParserParser.T__15)
                        self.state = 156
                        self.arithmetic(4)
                        pass

             
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.arithmetic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(PythonParserParser.VARIABLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(PythonParserParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(PythonParserParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.match(PythonParserParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
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
        self.enterRule(localctx, 20, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(PythonParserParser.T__20)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60148482056) != 0):
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 171
                        self.expression()
                        self.state = 172
                        self.match(PythonParserParser.T__21) 
                    self.state = 178
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                self.state = 179
                self.expression()


            self.state = 182
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
        self._predicates[5] = self.conditional_sempred
        self._predicates[8] = self.arithmetic_sempred
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
         





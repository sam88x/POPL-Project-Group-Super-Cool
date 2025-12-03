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
        4,1,39,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,4,0,33,8,0,11,0,12,0,34,5,0,37,8,0,10,0,12,
        0,40,9,0,1,0,1,0,1,0,1,1,4,1,46,8,1,11,1,12,1,47,1,1,1,1,1,1,4,1,
        53,8,1,11,1,12,1,54,1,1,5,1,58,8,1,10,1,12,1,61,9,1,1,2,1,2,1,2,
        1,2,3,2,67,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,95,8,5,
        10,5,12,5,98,9,5,1,5,1,5,1,5,1,5,1,5,3,5,105,8,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,120,8,6,1,6,1,6,1,6,1,6,
        1,6,1,6,5,6,128,8,6,10,6,12,6,131,9,6,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,150,8,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,161,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,178,8,9,10,9,12,9,181,9,9,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,189,8,10,1,11,1,11,1,11,1,11,
        5,11,195,8,11,10,11,12,11,198,9,11,1,11,3,11,201,8,11,1,11,1,11,
        1,11,0,2,12,18,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,1,0,5,10,228,
        0,27,1,0,0,0,2,45,1,0,0,0,4,66,1,0,0,0,6,68,1,0,0,0,8,74,1,0,0,0,
        10,82,1,0,0,0,12,119,1,0,0,0,14,132,1,0,0,0,16,149,1,0,0,0,18,160,
        1,0,0,0,20,188,1,0,0,0,22,190,1,0,0,0,24,26,5,34,0,0,25,24,1,0,0,
        0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,38,1,0,0,0,29,27,
        1,0,0,0,30,32,3,4,2,0,31,33,5,34,0,0,32,31,1,0,0,0,33,34,1,0,0,0,
        34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,30,1,0,0,0,37,40,1,
        0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,
        42,3,4,2,0,42,43,5,0,0,1,43,1,1,0,0,0,44,46,5,1,0,0,45,44,1,0,0,
        0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,59,
        3,4,2,0,50,52,5,34,0,0,51,53,5,1,0,0,52,51,1,0,0,0,53,54,1,0,0,0,
        54,52,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,58,3,4,2,0,57,50,1,
        0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,3,1,0,0,0,61,
        59,1,0,0,0,62,67,3,16,8,0,63,67,3,10,5,0,64,67,3,6,3,0,65,67,3,8,
        4,0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,5,
        1,0,0,0,68,69,5,31,0,0,69,70,3,12,6,0,70,71,5,2,0,0,71,72,5,34,0,
        0,72,73,3,2,1,0,73,7,1,0,0,0,74,75,5,32,0,0,75,76,5,36,0,0,76,77,
        5,33,0,0,77,78,3,20,10,0,78,79,5,2,0,0,79,80,5,34,0,0,80,81,3,2,
        1,0,81,9,1,0,0,0,82,83,5,25,0,0,83,84,3,12,6,0,84,85,5,2,0,0,85,
        86,5,34,0,0,86,96,3,2,1,0,87,88,5,34,0,0,88,89,5,26,0,0,89,90,3,
        12,6,0,90,91,5,2,0,0,91,92,5,34,0,0,92,93,3,2,1,0,93,95,1,0,0,0,
        94,87,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,104,1,
        0,0,0,98,96,1,0,0,0,99,100,5,34,0,0,100,101,5,27,0,0,101,102,5,2,
        0,0,102,103,5,34,0,0,103,105,3,2,1,0,104,99,1,0,0,0,104,105,1,0,
        0,0,105,11,1,0,0,0,106,107,6,6,-1,0,107,108,5,3,0,0,108,109,3,12,
        6,0,109,110,5,4,0,0,110,120,1,0,0,0,111,112,5,30,0,0,112,120,3,12,
        6,6,113,114,3,18,9,0,114,115,3,14,7,0,115,116,3,18,9,0,116,120,1,
        0,0,0,117,120,5,24,0,0,118,120,3,18,9,0,119,106,1,0,0,0,119,111,
        1,0,0,0,119,113,1,0,0,0,119,117,1,0,0,0,119,118,1,0,0,0,120,129,
        1,0,0,0,121,122,10,5,0,0,122,123,5,28,0,0,123,128,3,12,6,6,124,125,
        10,4,0,0,125,126,5,29,0,0,126,128,3,12,6,5,127,121,1,0,0,0,127,124,
        1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,13,1,
        0,0,0,131,129,1,0,0,0,132,133,7,0,0,0,133,15,1,0,0,0,134,135,5,36,
        0,0,135,136,5,11,0,0,136,150,3,20,10,0,137,138,5,36,0,0,138,139,
        5,12,0,0,139,150,3,18,9,0,140,141,5,36,0,0,141,142,5,13,0,0,142,
        150,3,18,9,0,143,144,5,36,0,0,144,145,5,14,0,0,145,150,3,18,9,0,
        146,147,5,36,0,0,147,148,5,15,0,0,148,150,3,18,9,0,149,134,1,0,0,
        0,149,137,1,0,0,0,149,140,1,0,0,0,149,143,1,0,0,0,149,146,1,0,0,
        0,150,17,1,0,0,0,151,152,6,9,-1,0,152,153,5,3,0,0,153,154,3,18,9,
        0,154,155,5,4,0,0,155,161,1,0,0,0,156,157,5,16,0,0,157,161,3,18,
        9,8,158,161,5,36,0,0,159,161,5,37,0,0,160,151,1,0,0,0,160,156,1,
        0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,179,1,0,0,0,162,163,10,
        7,0,0,163,164,5,17,0,0,164,178,3,18,9,8,165,166,10,6,0,0,166,167,
        5,18,0,0,167,178,3,18,9,7,168,169,10,5,0,0,169,170,5,19,0,0,170,
        178,3,18,9,6,171,172,10,4,0,0,172,173,5,20,0,0,173,178,3,18,9,5,
        174,175,10,3,0,0,175,176,5,16,0,0,176,178,3,18,9,4,177,162,1,0,0,
        0,177,165,1,0,0,0,177,168,1,0,0,0,177,171,1,0,0,0,177,174,1,0,0,
        0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,19,1,0,0,0,
        181,179,1,0,0,0,182,189,3,18,9,0,183,189,5,36,0,0,184,189,5,37,0,
        0,185,189,5,24,0,0,186,189,5,35,0,0,187,189,3,22,11,0,188,182,1,
        0,0,0,188,183,1,0,0,0,188,184,1,0,0,0,188,185,1,0,0,0,188,186,1,
        0,0,0,188,187,1,0,0,0,189,21,1,0,0,0,190,200,5,21,0,0,191,192,3,
        20,10,0,192,193,5,22,0,0,193,195,1,0,0,0,194,191,1,0,0,0,195,198,
        1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,196,
        1,0,0,0,199,201,3,20,10,0,200,196,1,0,0,0,200,201,1,0,0,0,201,202,
        1,0,0,0,202,203,5,23,0,0,203,23,1,0,0,0,19,27,34,38,47,54,59,66,
        96,104,119,127,129,149,160,177,179,188,196,200
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
                     "'else'", "'and'", "'or'", "'not'", "'while'", "'for'", 
                     "'in'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOLEAN", "IF", "ELIF", "ELSE", "AND", "OR", "NOT", 
                      "WHILE", "FOR", "IN", "NEWLINE", "STRING", "VARIABLE", 
                      "NUMBER", "WS", "COMMENT" ]

    RULE_start = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_while_loop = 3
    RULE_for_loop = 4
    RULE_if_else_block = 5
    RULE_conditional = 6
    RULE_relational = 7
    RULE_assignment = 8
    RULE_arithmetic = 9
    RULE_expression = 10
    RULE_array = 11

    ruleNames =  [ "start", "block", "statement", "while_loop", "for_loop", 
                   "if_else_block", "conditional", "relational", "assignment", 
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
    FOR=32
    IN=33
    NEWLINE=34
    STRING=35
    VARIABLE=36
    NUMBER=37
    WS=38
    COMMENT=39

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
            while _la==34:
                self.state = 24
                self.match(PythonParserParser.NEWLINE)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30
                    self.statement()
                    self.state = 32 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 31
                        self.match(PythonParserParser.NEWLINE)
                        self.state = 34 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==34):
                            break
             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 41
            self.statement()
            self.state = 42
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.match(PythonParserParser.T__0)
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 49
            self.statement()
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self.match(PythonParserParser.NEWLINE)
                    self.state = 52 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 51
                        self.match(PythonParserParser.T__0)
                        self.state = 54 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==1):
                            break

                    self.state = 56
                    self.statement() 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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


        def for_loop(self):
            return self.getTypedRuleContext(PythonParserParser.For_loopContext,0)


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
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.assignment()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.if_else_block()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.while_loop()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.for_loop()
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


        def NEWLINE(self):
            return self.getToken(PythonParserParser.NEWLINE, 0)

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
            self.state = 68
            self.match(PythonParserParser.WHILE)
            self.state = 69
            self.conditional(0)
            self.state = 70
            self.match(PythonParserParser.T__1)
            self.state = 71
            self.match(PythonParserParser.NEWLINE)
            self.state = 72
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(PythonParserParser.FOR, 0)

        def VARIABLE(self):
            return self.getToken(PythonParserParser.VARIABLE, 0)

        def IN(self):
            return self.getToken(PythonParserParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(PythonParserParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(PythonParserParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(PythonParserParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)




    def for_loop(self):

        localctx = PythonParserParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(PythonParserParser.FOR)
            self.state = 75
            self.match(PythonParserParser.VARIABLE)
            self.state = 76
            self.match(PythonParserParser.IN)
            self.state = 77
            self.expression()
            self.state = 78
            self.match(PythonParserParser.T__1)
            self.state = 79
            self.match(PythonParserParser.NEWLINE)
            self.state = 80
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
        self.enterRule(localctx, 10, self.RULE_if_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(PythonParserParser.IF)
            self.state = 83
            self.conditional(0)
            self.state = 84
            self.match(PythonParserParser.T__1)
            self.state = 85
            self.match(PythonParserParser.NEWLINE)
            self.state = 86
            self.block()
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 87
                    self.match(PythonParserParser.NEWLINE)
                    self.state = 88
                    self.match(PythonParserParser.ELIF)
                    self.state = 89
                    self.conditional(0)
                    self.state = 90
                    self.match(PythonParserParser.T__1)
                    self.state = 91
                    self.match(PythonParserParser.NEWLINE)
                    self.state = 92
                    self.block() 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 99
                self.match(PythonParserParser.NEWLINE)
                self.state = 100
                self.match(PythonParserParser.ELSE)
                self.state = 101
                self.match(PythonParserParser.T__1)
                self.state = 102
                self.match(PythonParserParser.NEWLINE)
                self.state = 103
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_conditional, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 107
                self.match(PythonParserParser.T__2)
                self.state = 108
                self.conditional(0)
                self.state = 109
                self.match(PythonParserParser.T__3)
                pass

            elif la_ == 2:
                self.state = 111
                self.match(PythonParserParser.NOT)
                self.state = 112
                self.conditional(6)
                pass

            elif la_ == 3:
                self.state = 113
                self.arithmetic(0)
                self.state = 114
                self.relational()
                self.state = 115
                self.arithmetic(0)
                pass

            elif la_ == 4:
                self.state = 117
                self.match(PythonParserParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.state = 118
                self.arithmetic(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 127
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 121
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 122
                        self.match(PythonParserParser.AND)
                        self.state = 123
                        self.conditional(6)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 124
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 125
                        self.match(PythonParserParser.OR)
                        self.state = 126
                        self.conditional(5)
                        pass

             
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
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
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(PythonParserParser.VARIABLE)
                self.state = 135
                self.match(PythonParserParser.T__10)
                self.state = 136
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(PythonParserParser.VARIABLE)
                self.state = 138
                self.match(PythonParserParser.T__11)
                self.state = 139
                self.arithmetic(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(PythonParserParser.VARIABLE)
                self.state = 141
                self.match(PythonParserParser.T__12)
                self.state = 142
                self.arithmetic(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.match(PythonParserParser.VARIABLE)
                self.state = 144
                self.match(PythonParserParser.T__13)
                self.state = 145
                self.arithmetic(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 146
                self.match(PythonParserParser.VARIABLE)
                self.state = 147
                self.match(PythonParserParser.T__14)
                self.state = 148
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
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 152
                self.match(PythonParserParser.T__2)
                self.state = 153
                self.arithmetic(0)
                self.state = 154
                self.match(PythonParserParser.T__3)
                pass
            elif token in [16]:
                self.state = 156
                self.match(PythonParserParser.T__15)
                self.state = 157
                self.arithmetic(8)
                pass
            elif token in [36]:
                self.state = 158
                self.match(PythonParserParser.VARIABLE)
                pass
            elif token in [37]:
                self.state = 159
                self.match(PythonParserParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 177
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 162
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 163
                        self.match(PythonParserParser.T__16)
                        self.state = 164
                        self.arithmetic(8)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 165
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 166
                        self.match(PythonParserParser.T__17)
                        self.state = 167
                        self.arithmetic(7)
                        pass

                    elif la_ == 3:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 168
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 169
                        self.match(PythonParserParser.T__18)
                        self.state = 170
                        self.arithmetic(6)
                        pass

                    elif la_ == 4:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 171
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 172
                        self.match(PythonParserParser.T__19)
                        self.state = 173
                        self.arithmetic(5)
                        pass

                    elif la_ == 5:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 174
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 175
                        self.match(PythonParserParser.T__15)
                        self.state = 176
                        self.arithmetic(4)
                        pass

             
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.arithmetic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.match(PythonParserParser.VARIABLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.match(PythonParserParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.match(PythonParserParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                self.match(PythonParserParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 187
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
            self.state = 190
            self.match(PythonParserParser.T__20)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 240537108488) != 0):
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 191
                        self.expression()
                        self.state = 192
                        self.match(PythonParserParser.T__21) 
                    self.state = 198
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                self.state = 199
                self.expression()


            self.state = 202
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
        self._predicates[6] = self.conditional_sempred
        self._predicates[9] = self.arithmetic_sempred
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
         





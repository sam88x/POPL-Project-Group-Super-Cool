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
        4,1,16,59,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,28,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,54,8,2,10,2,12,2,57,9,2,1,
        2,0,1,4,3,0,2,4,0,0,67,0,6,1,0,0,0,2,27,1,0,0,0,4,36,1,0,0,0,6,7,
        3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,5,13,0,0,10,11,5,1,0,0,11,28,
        3,4,2,0,12,13,5,13,0,0,13,14,5,1,0,0,14,28,5,15,0,0,15,16,5,13,0,
        0,16,17,5,2,0,0,17,28,3,4,2,0,18,19,5,13,0,0,19,20,5,3,0,0,20,28,
        3,4,2,0,21,22,5,13,0,0,22,23,5,4,0,0,23,28,3,4,2,0,24,25,5,13,0,
        0,25,26,5,5,0,0,26,28,3,4,2,0,27,9,1,0,0,0,27,12,1,0,0,0,27,15,1,
        0,0,0,27,18,1,0,0,0,27,21,1,0,0,0,27,24,1,0,0,0,28,3,1,0,0,0,29,
        30,6,2,-1,0,30,31,5,6,0,0,31,32,3,4,2,0,32,33,5,7,0,0,33,37,1,0,
        0,0,34,37,5,13,0,0,35,37,5,14,0,0,36,29,1,0,0,0,36,34,1,0,0,0,36,
        35,1,0,0,0,37,55,1,0,0,0,38,39,10,7,0,0,39,40,5,8,0,0,40,54,3,4,
        2,8,41,42,10,6,0,0,42,43,5,9,0,0,43,54,3,4,2,7,44,45,10,5,0,0,45,
        46,5,10,0,0,46,54,3,4,2,6,47,48,10,4,0,0,48,49,5,11,0,0,49,54,3,
        4,2,5,50,51,10,3,0,0,51,52,5,12,0,0,52,54,3,4,2,4,53,38,1,0,0,0,
        53,41,1,0,0,0,53,44,1,0,0,0,53,47,1,0,0,0,53,50,1,0,0,0,54,57,1,
        0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,5,1,0,0,0,57,55,1,0,0,0,4,27,
        36,53,55
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'('", "')'", "'*'", "'/'", "'%'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VARIABLE", "NUMBER", "BOOLEAN", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_arithmetic = 2

    ruleNames =  [ "start", "statement", "arithmetic" ]

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
    VARIABLE=13
    NUMBER=14
    BOOLEAN=15
    WS=16

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

        def statement(self):
            return self.getTypedRuleContext(PythonParserParser.StatementContext,0)


        def EOF(self):
            return self.getToken(PythonParserParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.statement()
            self.state = 7
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

        def VARIABLE(self):
            return self.getToken(PythonParserParser.VARIABLE, 0)

        def arithmetic(self):
            return self.getTypedRuleContext(PythonParserParser.ArithmeticContext,0)


        def BOOLEAN(self):
            return self.getToken(PythonParserParser.BOOLEAN, 0)

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
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self.match(PythonParserParser.VARIABLE)
                self.state = 10
                self.match(PythonParserParser.T__0)
                self.state = 11
                self.arithmetic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(PythonParserParser.VARIABLE)
                self.state = 13
                self.match(PythonParserParser.T__0)
                self.state = 14
                self.match(PythonParserParser.BOOLEAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(PythonParserParser.VARIABLE)
                self.state = 16
                self.match(PythonParserParser.T__1)
                self.state = 17
                self.arithmetic(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 18
                self.match(PythonParserParser.VARIABLE)
                self.state = 19
                self.match(PythonParserParser.T__2)
                self.state = 20
                self.arithmetic(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 21
                self.match(PythonParserParser.VARIABLE)
                self.state = 22
                self.match(PythonParserParser.T__3)
                self.state = 23
                self.arithmetic(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 24
                self.match(PythonParserParser.VARIABLE)
                self.state = 25
                self.match(PythonParserParser.T__4)
                self.state = 26
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 30
                self.match(PythonParserParser.T__5)
                self.state = 31
                self.arithmetic(0)
                self.state = 32
                self.match(PythonParserParser.T__6)
                pass
            elif token in [13]:
                self.state = 34
                self.match(PythonParserParser.VARIABLE)
                pass
            elif token in [14]:
                self.state = 35
                self.match(PythonParserParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 38
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 39
                        self.match(PythonParserParser.T__7)
                        self.state = 40
                        self.arithmetic(8)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 41
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 42
                        self.match(PythonParserParser.T__8)
                        self.state = 43
                        self.arithmetic(7)
                        pass

                    elif la_ == 3:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 44
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 45
                        self.match(PythonParserParser.T__9)
                        self.state = 46
                        self.arithmetic(6)
                        pass

                    elif la_ == 4:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 47
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 48
                        self.match(PythonParserParser.T__10)
                        self.state = 49
                        self.arithmetic(5)
                        pass

                    elif la_ == 5:
                        localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 50
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 51
                        self.match(PythonParserParser.T__11)
                        self.state = 52
                        self.arithmetic(4)
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.arithmetic_sempred
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
         





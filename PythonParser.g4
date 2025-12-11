grammar PythonParser;

@lexer::header {
from antlr4 import *
from antlr4.Token import CommonToken
}

@lexer::members {
def _ensure_init(self):
    if not hasattr(self, 'indent_stack'):
        self.indent_stack = [0]
        self.token_queue = []
        #These name indexes are their indexes in a list of defined lexer rules
        #this means these indexes only map to the correct token to make
        #when every token is captured by a lexer rule. Therefore you can't
        #make use literals that aren't captured by a lexer rule; it will break
        #this indent code
        self.INDENT_ID = self.symbolicNames.index("INDENT")
        self.DEDENT_ID = self.symbolicNames.index("DEDENT")
        self.NEWLINE_ID = self.symbolicNames.index("NEWLINE")
        print("******SAM DEBUG SETUP*******\n\nINDENT id=",self.INDENT_ID)
        print("DEDENT id=",self.DEDENT_ID)
        print("NEWLINE id=",self.NEWLINE_ID)
        

def nextToken(self):
    self._ensure_init()
    
    if self.token_queue:
        t = self.token_queue.pop(0)
        self._token = t
        return t
        
    t = super().nextToken()
    
    if t.type == Token.EOF:
        # If we have open indentation blocks
        if len(self.indent_stack) > 1:
            if self._token and self._token.type != self.NEWLINE_ID and self._token.type != self.DEDENT_ID:
                nl_token = self.create_token(self.NEWLINE_ID, "\n")
                self.token_queue.append(nl_token)
            
            while len(self.indent_stack) > 1:
                self.indent_stack.pop()
                dedent = self.create_token(self.DEDENT_ID, "DEDENT")
                self.token_queue.append(dedent)
            
            self.token_queue.append(t)
            return self.token_queue.pop(0)
            
    self._token = t
    return t

def create_token(self, type_val, text):
    t = CommonToken(type=type_val)
    t.channel = Token.DEFAULT_CHANNEL
    t.text = text
    t.line = self.line
    t.column = self.column
    return t

def handle_newline(self):
    self._ensure_init()
    txt = self.text
    spaces = txt.lstrip('\r\n')
    indent = 0
    for char in spaces:
        if char == '\t': 
            indent += 4
        elif char == ' ': 
            indent += 1
    previous = self.indent_stack[-1]
    
    if indent > previous:
        self.indent_stack.append(indent)
        #print("\n******SAM DEBUG*******\nINDENT id=",self.INDENT_ID)
        t = self.create_token(self.INDENT_ID, "INDENT")
        self.token_queue.append(t)
    elif indent < previous:
        while indent < self.indent_stack[-1]:
            self.indent_stack.pop()
            #print("\n******SAM DEBUG*******\nDEDENT id=",self.DEDENT_ID)

            t = self.create_token(self.DEDENT_ID, "DEDENT")
            self.token_queue.append(t)
        if indent != self.indent_stack[-1]:
            print(f"Indentation Error: mismatch. Expected {self.indent_stack[-1]}, got {indent}")
}

start: (statement | NEWLINE)* EOF;

statement: assignment NEWLINE | if_else_block | while_loop | for_loop;

block: INDENT statement+ DEDENT;

while_loop: WHILE conditional ':' NEWLINE block;

for_loop: FOR VARIABLE IN (range_func | VARIABLE) ':' NEWLINE block;

if_else_block: IF conditional ':' NEWLINE block
    (ELIF conditional ':' NEWLINE block)*
    (ELSE ':' NEWLINE block)?;

conditional: LPAREN conditional RPAREN
    | NOT conditional
    | conditional AND conditional
    | conditional OR conditional
    | arithmetic relational arithmetic
    | BOOLEAN
    | arithmetic;

relational: LESS | LESSEQ | GREATER | GREATEREQ | EQ | NOTEQ;

assignment: VARIABLE ASSIGN expression
    | VARIABLE PLUSASSIGN arithmetic
    | VARIABLE MINUSASSIGN arithmetic
    | VARIABLE MULTASSIGN arithmetic
    | VARIABLE DIVASSIGN arithmetic;

range_func: RANGE LPAREN NUMBER COMMA NUMBER  RPAREN;

arithmetic: LPAREN arithmetic RPAREN
    | MINUS arithmetic
    | arithmetic MULT arithmetic 
    | arithmetic DIV arithmetic
    | arithmetic MOD arithmetic
    | arithmetic PLUS arithmetic
    | arithmetic MINUS arithmetic
    | VARIABLE | NUMBER;

expression: arithmetic | VARIABLE | NUMBER | BOOLEAN | STRING | array;

array: LBRACK ((expression COMMA)* expression)? RBRACK;

//must caputure all literals with lexer rules (see comment in lexer:members for info)
BOOLEAN: 'True' | 'False';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
AND: 'and';
OR: 'or';
NOT: 'not';
WHILE: 'while';
FOR: 'for';
IN: 'in';

COLON:':';
LESS: '<';
LESSEQ: '<=';
GREATER: '>';
GREATEREQ: '>=';
EQ: '==';
NOTEQ: '!=';
ASSIGN: '=';
PLUSASSIGN: '+=';
MINUSASSIGN: '-=';
MULTASSIGN: '*=';
DIVASSIGN: '/=';

LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
RANGE: 'range';

NEWLINE: ('\r'? '\n' | '\r')+ [ \t]* { self.handle_newline() };

STRING: '"' (~["\\\r\n] | '\\' .)* '"'
      | '\'' (~['\\\r\n] | '\\' .)* '\'';

VARIABLE: [A-Za-z_][A-Za-z_0-9]*;
NUMBER: [0-9]+('.'[0-9]+)?;

WS : [ ]+ -> skip ;

COMMENT : ('#' ~[\r\n]* | '\'\'\'' .*? '\'\'\'') -> skip ;

INDENT : '.___INDENT' -> skip;
DEDENT : '.___DEDENT' -> skip;
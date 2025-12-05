grammar PythonParser;

tokens { INDENT, DEDENT }

@lexer::members {
    # Stack, levels of indentation
    self.indents = []

    # Pending tokens (nextToken overridden, indents/dedents added to this)
    self.tokens = []

    # nextToken override for injecting INDENT/DEDENT
    def nextToken(self):
        from PythonParserParser import PythonParserParser
        from antlr4.Token import CommonToken
        
        if self.tokens:
            token = self.tokens.pop(0)
            print(f"Injected token: {token.type} ('{token.text}') @ line {token.line}")
            return token
        else:
            token = super().nextToken()
            
            print(f"Normal token: {token.type} ('{token.text}') @ line {token.line}")
            
            # Inject any pending DEDENT tokens at EOF
            if token.type == Token.EOF:
                while len(self.indents) > 0:
                    self.indents.pop()
                    dedentToken = CommonToken(
                        type=PythonParserParser.DEDENT
                    )
                    dedentToken.line = self.line
                    dedentToken.column = self.column

                    dedentToken.text = "DEDENT"

                    self.tokens.append(dedentToken)
                    print(self.tokens)
                if self.tokens:
                    return self.tokens.pop()
            return token

}

//start: (statement | NEWLINE)* EOF;
start: NEWLINE* (statement NEWLINE+)* statement EOF;
//start: NEWLINE* statement EOF;

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


NEWLINE: '\n'+ ('\t')* {
    from PythonParserParser import PythonParserParser
    from antlr4.Token import CommonToken


    text = self.text
    tabCount = text.count("\t")

    currentIndentLevel = 0
    if self.indents: 
        currentIndentLevel = self.indents[-1]


    if (tabCount == currentIndentLevel):
        # No indent/dedent, just newline

        print(self.line, self.indents)
        pass

    elif (tabCount > currentIndentLevel):
        # Indent
        self.indents.append(tabCount)
        print(self.line, self.indents)
        # indentToken = self._factory.create(PythonParserParser.INDENT, "")
        indentToken = CommonToken(
            type=PythonParserParser.INDENT
        )
        indentToken.line = self.line
        indentToken.column = self.column

        indentToken.text = "INDENT"

        self.tokens.append(indentToken)

    else:
        while (len(self.indents) > 0 and self.indents[-1] > tabCount):
            self.indents.pop()
            # dedentToken = self._factory.create(PythonParserParser.DEDENT, "")
            dedentToken = CommonToken(
                type=PythonParserParser.DEDENT
            )
            dedentToken.line = self.line
            dedentToken.column = self.column

            dedentToken.text = "DEDENT"

            self.tokens.append(dedentToken)
        print(self.line, self.indents)
        newlineToken = CommonToken(
            type=PythonParserParser.NEWLINE
        )
        newlineToken.line = self.line
        newlineToken.column = self.column

        #self.tokens.append(newlineToken)
        while (self.tokens):
            self.nextToken()
};


STRING: '"' (~('\n'| '\r' | '"') | '\\"')* '"'
    | '\'' (~('\n'| '\r' | '"') | '\\"')* '\'';

/* Need to prevent keywords?? */

VARIABLE: [A-Za-z_][A-Za-z_0-9]*;
NUMBER: [0-9]+('.'[0-9]+)?;

block: INDENT statement (NEWLINE statement)* DEDENT;
statement: assignment | if_else_block | while_loop | for_loop;

while_loop: WHILE conditional ':' NEWLINE block;

for_loop: FOR VARIABLE IN expression ':' NEWLINE block;

if_else_block: IF conditional ':' NEWLINE block
    (NEWLINE ELIF conditional ':' NEWLINE block)*
    (NEWLINE ELSE ':' NEWLINE block)?;

conditional: '(' conditional ')'
    | NOT conditional
    | conditional AND conditional
    | conditional OR conditional
    | arithmetic relational arithmetic
    | BOOLEAN
    | arithmetic;

relational: '<' | '<=' | '>' | '>=' | '==' | '!=';

assignment: VARIABLE '=' expression
    | VARIABLE '+=' arithmetic
    | VARIABLE '-=' arithmetic
    | VARIABLE '*=' arithmetic
    | VARIABLE '/=' arithmetic;

arithmetic: '(' arithmetic ')'
    | '-' arithmetic
    | arithmetic '*' arithmetic 
    | arithmetic '/' arithmetic
    | arithmetic '%' arithmetic
    | arithmetic '+' arithmetic
    | arithmetic '-' arithmetic
    | VARIABLE | NUMBER;

expression: arithmetic | VARIABLE | NUMBER | BOOLEAN | STRING | array;

array: '[' ((expression ',')* expression)? ']';

WS : [ \r]+ -> skip ;

COMMENT : (('#' ~[\n\r]*) |( '\'\'\'' .*? '\'\'\'')) -> skip ;
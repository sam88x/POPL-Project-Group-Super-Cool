grammar PythonParser;

start: NEWLINE* (statement NEWLINE)* statement EOF;

BOOLEAN: 'True' | 'False';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
AND: 'and';
OR: 'or';
NOT: 'not';
NEWLINE: '\n'+;
STRING: '"' (~('\n'| '\r' | '"') | '\\"')* '"'
    | '\'' (~('\n'| '\r' | '"') | '\\"')* '\'';

/* Need to prevent keywords?? */

VARIABLE: [A-Za-z_][A-Za-z_0-9]*;
NUMBER: [0-9]+('.'[0-9]+)?;

statement: assignment | if_else_block;
block: '\t' NEWLINE* (statement NEWLINE)* statement;

if_else_block: IF conditional ':' block elif_blocks? else_block?;
elif_blocks: elif_block | elif_block elif_blocks;
elif_block: ELIF conditional ':' block;
else_block: ELSE ':' block;

conditional: 'test == test';

assignment: VARIABLE '=' expression
    | VARIABLE '+=' arithmetic
    | VARIABLE '-=' arithmetic
    | VARIABLE '*=' arithmetic
    | VARIABLE '/=' arithmetic;

arithmetic: '(' arithmetic ')'
    | arithmetic '*' arithmetic 
    | arithmetic '/' arithmetic
    | arithmetic '%' arithmetic
    | arithmetic '+' arithmetic
    | arithmetic '-' arithmetic
    | VARIABLE | NUMBER;

expression: arithmetic | VARIABLE | NUMBER | BOOLEAN | STRING | array;

array: '[' ((expression ',')* expression)? ']';

WS : [ \r]+ -> skip ;

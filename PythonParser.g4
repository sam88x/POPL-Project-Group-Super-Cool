grammar PythonParser;

start: NEWLINE* (statement NEWLINE)* statement EOF;

VARIABLE: [A-Za-z_][A-Za-z_0-9]*;
NUMBER: [0-9]+('.'[0-9]+)?;
BOOLEAN: 'True' | 'False';
NEWLINE: '\n'+;
STRING: '"' (~('\n'| '\r' | '"') | '\\"')* '"'
    | '\'' (~('\n'| '\r' | '"') | '\\"')* '\'';

/* Need to prevent keywords?? */


statement: assignment | if_else_block;
block: '\t' NEWLINE* (statement NEWLINE)* statement;

if_else_block: 'if' conditional ':' block elif_blocks? else_block?;
elif_blocks: elif_block | elif_block elif_blocks;
elif_block: 'elif' conditional ':' block;
else_block: 'else' ':' block;

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

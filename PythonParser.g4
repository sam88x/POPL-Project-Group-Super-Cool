grammar PythonParser;

start: NEWLINE* (statement NEWLINE)* statement EOF;

VARIABLE: [A-Za-z_][A-Za-z_0-9]*;
NUMBER: [0-9]+('.'[0-9]+)?;
BOOLEAN: 'True' | 'False';
NEWLINE: '\n'+;
STRING: '"' (~('\n'| '\r' | '"') | '\\"')* '"'
    | '\'' (~('\n'| '\r' | '"') | '\\"')* '\'';

/* Need to prevent keywords?? */


statement: assignment;

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

WS : [ \t\r]+ -> skip ;

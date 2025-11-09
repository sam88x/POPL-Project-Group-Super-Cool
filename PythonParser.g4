grammar PythonParser;

start: statement EOF;

VARIABLE: [A-Za-z_][A-Za-z_0-9]*;
NUMBER: [0-9]+('.'[0-9]+)?;
BOOLEAN: 'True' | 'False';
/* STRING: '';  Need to implement */
/* ARRAY: ''; Need to implement */

/* Need to prevent keywords?? */

statement: VARIABLE '=' arithmetic
    | VARIABLE '=' BOOLEAN
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

WS : [ \t\r]+ -> skip ;

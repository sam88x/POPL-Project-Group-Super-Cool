grammar PythonParser;

start: NEWLINE* (statement NEWLINE+)* statement EOF;

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
NEWLINE: '\n';
STRING: '"' (~('\n'| '\r' | '"') | '\\"')* '"'
    | '\'' (~('\n'| '\r' | '"') | '\\"')* '\'';

/* Need to prevent keywords?? */

VARIABLE: [A-Za-z_][A-Za-z_0-9]*;
NUMBER: [0-9]+('.'[0-9]+)?;

block: ('\t')+ statement (NEWLINE ('\t')+ statement)*;
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
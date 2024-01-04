import ply.lex as lex
import ply.yacc as yacc

output_file = "inputTranslated.c"
input_kotlin = "input.kt"


reserved = {
    'fun': 'FUN',
    'Int': 'TYPE',
    'Float': 'TYPE',
    'Double': 'TYPE',
    'String': 'TYPE',
    'return': 'RETURN',
    'var': 'VAR',
    'while': 'WHILE',
    'for': 'FOR',
    'if': 'IF',
    'else': 'ELSE'
}

tokens = ('ID', 'NEWLINE', 'COMMENT', 'BLOCKCOMMENT', 'INT', 'NUMBER', 'FLOATNUMBER', 'SSTRING',
          'DOT', 'COLON', 'COMA', 'TRUE', 'FUN', 'FALSE', 'FOR', 'WHILE',
          'IF', 'ELSE', 'TYPE', 'ARRAYTYPE', 'VAR', 'RETURN', 'IN',
          'ASSIGNOP', 'ASSIGN', 'ARITHMOP', 'LOGICOP', 'COMPOP', 'INCRDECR', 'ORBRACKET',
          'CRBRACKET', 'OBRACE', 'CBRACE',
          )

t_NEWLINE = r'\n'
t_COMMENT = r'//.*'
t_BLOCKCOMMENT = r'/\*(.|\n)*?\*/'
t_NUMBER = r'\d+'
t_FLOATNUMBER = r'\d+\.\d+'
t_SSTRING = r"'([^'\\]|\\.)*'"
t_DOT = r'\.'
t_COLON = r':'
t_COMA = r','
t_TRUE = r'true'
t_FUN = r'fun'
t_FALSE = r'false'
t_FOR = r'for'
t_WHILE = r'while'
t_IF = r'if'
t_ELSE = r'else'
t_TYPE = r'Int|String|Float|Double'
t_ARRAYTYPE = r'Array\<(' + '|'.join(['Int', 'String', 'Float', 'Double']) + r')\>'
t_VAR = r'var'
t_RETURN = r'return'
t_IN = r'in'
t_ASSIGNOP = r'[-+*/%]='
t_ASSIGN = r'='
t_ARITHMOP = r'[-+*/%]'
t_LOGICOP = r'&&|\|\|'
t_COMPOP = r'==|!=|<=|>=|<|>'
t_INCRDECR = r'\+\+|\-\-'
t_ORBRACKET = r'\('
t_CRBRACKET = r'\)'
t_OBRACE = r'{'
t_CBRACE = r'}'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# Omit whitespace
t_ignore = ' \t'


def t_error(t):
    print(f'Nierozpoznany znak: {t.value[0]}')
    t.lexer.skip(1)


# Kotlin to C grammar
def p_start(p):
    '''start : functions'''
    output = "#include <stdio.h>\n"
    if p[1] is not None:
        output += p[1]
    output_f.write(output + "\n")


def p_functions(p):
    '''functions : FUN function_header body functions
        | empty'''
    if len(p) > 2:
        p[0] = p[2] + '\n' + p[3] + "\n" + p[4]
    else:
        p[0] = p[1]


def p_function_header(p):
    '''function_header : ID ORBRACKET function_variables CRBRACKET COLON TYPE
        | ID ORBRACKET function_variables CRBRACKET'''
    if len(p) == 7:
        tmp = p[6].lower()
        if tmp == 'string':
            tmp = 'char[] '
        p[0] = tmp + " " + p[1] + " (" + p[3] + ")"
    else:
        p[0] = "void " + p[1] + " (" + p[3] + ")"


def p_function_variables(p):
    '''function_variables : ID COLON TYPE
        | ID COLON TYPE COMA function_variables
        | empty'''
    if len(p) < 2:
        p[0] = ""
    else:
        tmp = p[3].lower()
        if tmp == 'string':
            tmp = 'char[] '
        if len(p) == 4:
            p[0] = tmp + " " + p[1]
        else:
            p[0] = tmp + " " + p[1] + ", " + p[5]


def p_function_args(p):
    '''function_args : run_function
        | value
        | ID
        | value COMA function_args
        | empty'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + " " + p[3]


def p_body(p):
    '''body : OBRACE NEWLINE actual_body CBRACE'''
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_actual_body(p):
    '''actual_body : return_line
        | statement
        | statement actual_body
        | empty'''
    if len(p) == 3:
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[1]


def p_return_line(p):
    '''return_line : RETURN expression
        | RETURN run_function
        | RETURN value NEWLINE
        | RETURN ID NEWLINE
        | empty'''
    if len(p) == 4:
        p[0] = p[1] + " " + p[2] + ";" + p[3]
    elif len(p) == 3:
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[1]


def p_statement(p):
    '''statement : expression
        | var_assign
        | while_loop
        | run_function
        | if_sentence'''
    p[0] = p[1]


def p_expression(p):
    '''expression : ID ARITHMOP ID NEWLINE
        | ID INCRDECR NEWLINE'''
    if len(p) == 5:
        print("Expression")
        print(p[1] + p[2] + p[3] + p[4])
        p[0] = p[1] + p[2] + p[3] + ";" + p[4]
    if len(p) == 4:
        p[0] = p[1] + p[2] + ";" + p[3]


def p_var_assign(p):
    '''var_assign : VAR ID COLON TYPE ASSIGN value
    | var_assign NEWLINE'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        tmp = p[4].lower()
        if tmp == 'string':
            tmp = 'char[] '
        p[0] = tmp + " " + p[2] + " " + p[5] + " " + p[6] + ";"


def p_run_function(p):
    '''run_function : ID ORBRACKET function_args CRBRACKET
    | ID ORBRACKET function_args CRBRACKET NEWLINE'''
    if len(p) == 6:
        p[0] = p[1] + p[2] + p[3] + p[4] + ";" + p[5]
    else:
        p[0] = p[1] + p[2] + p[3] + p[4]


def p_if_sentence(p):
    '''if_sentence : IF ORBRACKET bool_expression CRBRACKET body NEWLINE
        | if_sentence else_sentence'''
    if len(p) == 7:
        p[0] = p[1] + " " + p[2] + p[3] + p[4] + p[5] + p[6]
    else:
        p[0] = p[1] + " " + p[2]


def p_else_sentence(p):
    '''else_sentence : ELSE body NEWLINE'''
    p[0] = p[1] + " " + p[2] + p[3]


def p_while_loop(p):
    '''while_loop : WHILE ORBRACKET bool_expression CRBRACKET body NEWLINE'''
    p[0] = p[1] + " " + p[2] + p[3] + p[4] + p[5] + p[6]


def p_bool_expression(p):
    '''bool_expression : bool_expression and_or bool_expression
                | ORBRACKET bool_expression CRBRACKET
                | ID COMPOP ID
                | value COMPOP value
                | value COMPOP ID
                | ID COMPOP value
                | TRUE
                | FALSE'''
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3]


def p_and_or(p):
    '''and_or : LOGICOP'''
    p[0] = p[1]


def p_value(p):
    '''value : FLOATNUMBER
    | NUMBER
    | SSTRING
    | TRUE
    | FALSE
    | empty'''
    p[0] = p[1]


def p_empty(p):
    'empty :'
    p[0] = ""


def p_error(p):
    print(parser.token())
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")


lexer = lex.lex()
parser = yacc.yacc()

f = open(input_kotlin, "rt")
output_f = open(output_file, "wt")
lines = f.read()
# print tokens
lexer.input(lines)
for tok in lexer:
    print(tok)
parser.parse(lines)
f.close()

output_f.close()


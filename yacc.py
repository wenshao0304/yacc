import ply.yacc as yacc
import sys
import ply.lex as lex

tokens = (
    'NAME', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN', 'POWER','RAD'
    )

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_POWER   = r'\^'
t_RAD     = r'\*\*'

t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %s"  % t.value)
        t.value = 0
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

lexer.input('10+2*5/(2+5)/2')

while True:
    tok = lexer.token()
    if not tok:
        break     
    print(tok)
      
    
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]
    
def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1] 

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]
    
def p_term_factor(p):
    'term : factor'
    p[0] = p[1] 
    
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]
    
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
    
def p_expression_power(p): 
    'expression : expression POWER term'
    p[0] = p[1] ** p[3]
    
def p_expression_rad(p):
    'expression : expression RAD term'
    p[0] = p[1] ** (1./p[3])
    
def p_error(p):
    print("Syntax error in input!")
    
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
        





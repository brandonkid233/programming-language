import lexer

#define token types
RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'
SPECIAL  = 'SPECIAL'
HEX = 'HEX'
ARGS = 'ARGS'

#token regex
token_exprs = [
    (r'[ \n\t]+',                    None),
    (r'#[^\n]*',                     None),
    (r'print',                       RESERVED),
    (r'\=',                          RESERVED),
    (r'\(',                          RESERVED),
    (r'\)',                          RESERVED),
    (r';',                           RESERVED),
    (r'\+',                          RESERVED),
    (r'-',                           RESERVED),
    (r'\*',                          RESERVED),
    (r'/',                           RESERVED),
    (r'<=',                          RESERVED),
    (r'<',                           RESERVED),
    (r'>=',                          RESERVED),
    (r'>',                           RESERVED),
    (r'=',                           RESERVED),
    (r'!=',                          RESERVED),
    (r'and',                         RESERVED),
    (r'or',                          RESERVED),
    (r'not',                         RESERVED),
    (r'if',                          RESERVED),
    (r'then',                        RESERVED),
    (r'else',                        RESERVED),
    (r'while',                       RESERVED),
    (r'do',                          RESERVED),
    (r'end',                         RESERVED),
    (r'def',                         RESERVED),
    (r'return',                      RESERVED),
    (r'stop',                        SPECIAL),
    (r'over',                        SPECIAL),
    (r'[0-9]+',                      INT),
    (r'[0-9,a-f]+',                  HEX),
    (r'_?[A-Za-z][A-Za-z0-9_]*',     ID),
]

def lang_lex(characters):
    return lexer.lex(characters, token_exprs)
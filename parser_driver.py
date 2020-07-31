import sys
from parser_test import *
from parser_test import aexp
from lang_lexer import lang_lex

# use parser if is not imported
if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('usage: %s filename parsername' % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = lang_lex(characters)
    parser = globals()[sys.argv[2]]()
    result = parser(tokens, 0)
    print(result)
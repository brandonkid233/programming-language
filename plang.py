import os
import sys
from parser_test import *
from parser_test import lang_parse
import random
from lexer import *
from lang_lexer import *

def usage():
    print('Usage: plang.py filename\n')
def ide():
    env = {}
    final = ''
    while 1:
        command = input('>> ')
        if(command=='vars'):
            print(env)
        elif(command.lower()=='run'):
            name = 'temp.'+ str(random.randint(0,9999))+'.lang'
            temp = open(name,'w+')
            temp.write(final)
            temp.close()
            text = open(name).read()
            command = 'python3 "'+__file__+'" '+name
            os.system(command)
            os.remove(name)
            final = ''
        else:
            final += command + '\n'
def run(text,context='main',env={}):
    from lang_lexer import lang_lex
    from parser_test import lang_parse
    env['_inner_code'] = text
    tokens = lang_lex(text)
    parse_result = lang_parse(tokens)
    if not parse_result:
        sys.stderr.write(f'Parse error in {context}!\n')
        return env
    ast = parse_result.value
    ast.eval(env)
    return env
if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        #ide()
        sys.exit(1)
    filename = sys.argv[1]
    text = open(filename).read()
    """tokens = lang_lex(text)
    parse_result = lang_parse(tokens)
    if not parse_result:
        sys.stderr.write('Parse error!\n')
        sys.exit(1)
    ast = parse_result.value
    env = {}
    ast.eval(env)

    sys.stdout.write('Final variable values:\n')"""
    env = run(text)
    for name in env:
        if(name=='_inner_code' or name=='exit'):
            continue
        sys.stdout.write('%s: %s\n' % (name, env[name]))
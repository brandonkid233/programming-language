#run code
def run(text,context='goto',env={}):
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
# handle vars
class var_handlers:
    # handle prints
    def handle_print(self,env):
        _print = env.get('_print',None)
        if(_print!=None):
            out = ''
            new = []
            temp = ''
            for i in str(_print):
                if(len(temp)>=3):
                    new.append(int(temp))
                    temp = i
                    continue
                temp += i
            new.append(int(temp))
            for i in new:
                out += chr(i)
            print(out)
            del env['_print']
        return env
    #raw  number print 
    def handle_raw_print(self,env):
        _raw_print = env.get('_raw_print',None)
        if(_raw_print!=None):
            print(str(_raw_print))
            del env['_raw_print']
        return env
    def handle_goto(self,env):
        if('goto' in env):
            goto = env['goto']
            new = env['_inner_code'].split('\n')
            x = 0
            new2 = []
            for i in new:
                if(x>=goto):
                    new2.append(i)
                x+=1
                pass
            new = ''
            for i in new2:
                new += i +'\n'
            new = new [:-1]
            del env['goto']
            env = run(new,'goto',env)
        return env
    #handle the prints and goto
    def handle_special_vars(self,env):
        env = self.handle_print(env)
        env = self.handle_raw_print(env)
        env = self.handle_goto(env)
        return env
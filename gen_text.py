#gen the str -> int
def genText(inp):
    out = ''
    new = []
    for i in str(inp):
        new.append(i)
        temp = str(ord(i))
        while 1:
            if(len(temp)<3):
                temp='0'+temp
            else:
                break
        out+=temp
    return out
# only open ui if it is not imported
if __name__ == '__main__':
    while 1:
        inp = input('text to convert: ')
        out = genText(inp)
        print("print that by adding: `_print = "+str(out)+";` to your file on the place you want it to print")
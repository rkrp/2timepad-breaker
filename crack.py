#!/usr/bin/python

import re
from sys import argv
from orig import strxor

#Load dictionary for validation
with open('/usr/share/dict/cracklib-small', 'r') as fp:
    wordlist = fp.read().split('\n')


def isprintable(inp):
    words = inp.split(' ')
    if len(words) == 1:
        return False

    for word in words:
        word = word.strip()
        if len(word) >= 4 and word in wordlist:
            return True
    return False

def main():
    #Ciphertext to be cracked
    ct = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904".decode('hex')
    
    #Loading the other ciphertexts encrypted with the same key
    with open('inputs', 'r') as fp:
        cts = fp.read().split('\n')

    text = argv[1]      #Guessed part of the text

    num = 0
    for case_t in cts:
        if not case_t:
            continue

        num += 1
        print 'Case', num, ':'
        case_t = case_t.decode('hex')
        c1c2 = strxor(ct, case_t)
        for i in range(len(c1c2)):
            res = strxor(text, c1c2[i:i+len(text)])
            if isprintable(res):
                print i, res
        print
        

if __name__ == '__main__':
    main()

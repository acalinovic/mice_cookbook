import re
import time
chars = 0
words = 0
with open('/home/boris/Téléchargements/Eva.txt') as f:
    line = f.readline()
    while len(line) > 0 and line != '':
        line = f.readline()
        line = re.sub(r'[0-9][0-9]/[0-9][0-9]/[0-9][0-9] à [0-9][0-9]:[0-9][0-9].*:', '', line)
        chars += len(line)
        words += len(line.split(' '))
        print(line)
    print('symboles: ' + str(chars))
    print('mots: ' + str(words))

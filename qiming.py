﻿from urllib import request
from itertools import permutations as perm
import re

def pinyin():
    """return a list of pinyin"""
    url = r'http://www.cidianwang.com/pinyin/'
    html = request.urlopen(url).read().decode('latin-1')
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd2 in position 249: invalid continuation byte
    # UnicodeDecodeError: 'gb2312' codec can't decode byte 0xa8 in position 23486: illegal multibyte sequence
    pinyin = [i[6:][:-1] for i in re.findall('lank">[a-z].*?<', s)]

    with open('qiming.md', 'w', encoding='utf-8') as f:
        f.write('[Pinyin](http://www.cidianwang.com/pinyin/)')
        write('---\n')
        for i in range(len(pinyin)):
            f.write(''.join(pinyin[i]).capitalize())
            if (i+1)%10 == 0:
                f.write('\n\n')
            else:
                f.write(' ')
    
    return pinyin


url = 'https://github.com/okxy/qiming/blob/master/Pinyin.md'
try:
    s = request.urlopen(url).read().decode('utf-8')
except:
    pass

ss = re.findall('：.*?<',s)
sss = [i[1:][:-1].split('\u3000') for i in ss]
pinyin2 = set([j for i in sss for j in i])
print(len(pinyin2), 'pinyin')

with open('qiming.txt', 'w', encoding='utf-8') as f:
    n = 0
    for i in perm(pinyin2, 2):
        n += 1
        f.write(''.join(i).capitalize())
        if n%10 == 0:
            f.write('\n\n')
        else:
            f.write(' ')

print('finished.')    
print(n,'names')

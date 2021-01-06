'''
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Требуется найти количество подстрок в этой строке.
'''

import hashlib

def my_hash(value):
    letter=26
    index=0
    size=10000

    for i,char in enumerate(value):
        index+=(ord(char)-ord('a')+1)*letter**i

    hashlib.sha1(value.encode('utf-8')).hexdigest()

    return index%size

s="buddy"
slog=[]
s_t=set()
i=0
i1=0
len_s=len(s)

under_string=set()
while i<=len_s:
    i1=0
    while i1<=len_s:
        s_t.add(my_hash(s[i:i1]))
        i1+=1
    i += 1
    if i<len_s:
        s_t.add(my_hash(s[i]))

print(f'Количество подстрок {len(s_t)-2} в строке: {s}')

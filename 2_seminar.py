##1

#n = [int(_) for _ in input().split()]
#c = n[0]
#nums = n[1:]
#s = ((1+c)/2) * c
#print(int(s-sum(nums)))
#


##2

# vvod = input().split()
# n = int(vvod[0])
# text = vvod[1]
# ans = []
# x = ''
# for i in range(len(text)):
#     if len(x) != n:
#         x = text[i] + x
#     else:
#         ans.append(x)
#         x = ''
#         x = text[i] + x
# ans.append(x)
# print(*ans, sep='')



##3


#def is_mirrored_string(s):
#    mirrored_pairs = {'3': 'E', 'E': '3', 'L': 'J', 'J': 'L', '2': 'S', 'S': '2', '5': 'Z', 'Z': '5'}
#    return any(c in mirrored_pairs for c in s)
#
#n = input()
#alp1 = '3L25'
#alp2 = 'EJSZ'
#mirs = 'AHIMOTUVWXY18'
#if n[::-1] == n:
#    flag = True
#    for i in n:
#        if i in mirs:
#            flag = True
#        else:
#            flag = False
#            break
#    if flag:
#        print(n + ' is a regular palindrome')
#    else:
#        print(n + ' is a mirrored palindrome')
#else:
#    for i in n:
#        if i not in alp1 and i not in alp2 and i not in mirs:
#            print(n + ' is not a palindrome')
#            break
#    if len(n) % 2 == 0:
#        n1 = n[:len(n)//2]
#        n2 = n[len(n)//2:]
#        n1 = n1[::-1]
#        for i in range(len(n)//2):
#    if is_mirrored_string(n):
#        print(n + ' is a Mirrored string')
#    else:
#        print(n + ' is not a palindrome')


##4


#n = input()
#print(''.join([n[i+1]+n[i] for i in range(0, len(n), 2) if len(n)%2==0]))
#print(''.join([n[i+1]+n[i] for i in range(0, len(n)-1, 2) if len(n)%2!=0]) + str(*[n[-1] for _ in range(1) if len(n)%2!=0]))


##5

#n = input()
#print(n[-1] + ''.join([n[i] for i in range(len(n) - 1)]))


##6

#n = input().split()
#temp = 0
#for i in n:
#    if n.count(i) == 1 and i != temp:
#        print(i)
#        temp = i


##7


#n = input().split()
#M = 0
#count = 0
#for i in n:
#    if n.count(i) > count:
#        count = n.count(i)
#        M = i
#print(M)


##8

#n = int(input())
#spis = [int(i) for i in input().split()]
#for i in spis:
#    above = len([x for x in spis if x > i])
#    below = len([x for x in spis if x < i])
#    eq = spis.count(i)
#    if eq % 2 == 0 and abs(above-below) == 0 or eq % 2 == 0 and abs(above-below) == 1:
#        print(f'{i} is a median')
#        break
#    elif eq % 2 != 0 and abs(above-below) == 0:
#        print(f'{i} is a median')
#        break



##9

#import re
#with open('example.txt', 'r') as f:
#    text = f.read()
#text = re.split(r'[.?!]', text)
#ans = [x for x in text if x !='']
#print(len(ans))



##10

#import re
#with open('input.txt', 'r') as f:
#    text = f.read()
#glas = 'уеыаоэяиюё'
#wrong = 'еюяё'
#zamena = {'е': 'э', 'я': 'а', 'ё': 'о', 'ю': 'у'}
#text = text.split()
#ans = []
#for i in text:
#    n = re.split(r'[бвгджзйклмнпрстфхцчшщьъ]', i)
#    if i[0] not in glas:
#        for k in n:
#            if k[0] in wrong:
#                x = zamena.get(k[0], 0)
#            else:
#                x = k[0]
#            k = k[0] + f'с{x}' + k[1:]
#            ans.append(k)
#    else:
#        ans.append(n[0])
#        for k in n[1:]:
#            if k[0] in wrong:
#                x = zamena.get(k[0], 0)
#            else:
#                x = k[0]
#            k = k[0] + f'с{x}' + k[1:]
#            ans.append(k)
#print(*ans)

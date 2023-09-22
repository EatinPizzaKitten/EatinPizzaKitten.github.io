##  1  ##

#def fibo(n):
#    temp = [1, 1]
#    for i in range(3, n+1):
#        x = sum(temp)
#        temp[0] = temp[1]
#        temp[1] = x
#    return temp[1]
#print(fibo(int(input())))


##  2  ##

#def prost(n):
#    mnoz = []
#    for i in range(2, n):
#        while n % i == 0:
#            mnoz.append(i)
#            n //= i
#            mnoz.append('*')
#    return ''.join(str(_) for _ in mnoz[:-1])
#print(prost(int(input())))


##  3  ##

#def NOD(one, two):
#    while one != 0 and two != 0:
#        if one >= two:
#            one %= two
#        else:
#            two %= one
#    return one or two
#a, b = map(int, input().split())
#nod = NOD(a, b)
#for i in range(a):
#    j = (nod - b*i)/a
#    if j == int(j):
#        print(int(j), i, nod, sep=' ')
#        break


##  4  ##

#def triangle(size, x):
#    if size % 2 != 0:
#        h = size // 2 + 1
#        for i in range(1, h+1):
#            print(x*i)
#        for i in range(h-1, 0, -1):
#            print(x*i)
#    else:
#        h = size // 2
#        for i in range(1, h + 1):
#            print(x*i)
#        for i in range(h, 0, -1):
#            print(x*i)
#    return ''
#a, b = map(str, input().split())
#print(triangle(int(a), b))


##  5  ##
#
#import numpy as np
#n, m = map(int, input().split())
#ar = np.zeros((n, m))
#x = 0
#y = 0
#dx = 1
#dy = 0
#for i in range(n*m):
#    ar[y][x] = i
#    if ar[(x + dx) % n][(y + dy) % m]:
#        dx, dy = dy, -dx
#    x += dx
#    y += dy
#print(ar)
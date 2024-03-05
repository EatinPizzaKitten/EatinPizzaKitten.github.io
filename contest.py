###   2   ###

#a, b = map(int, input().split())
#x = 0
#while True:
#    if (a+x) % b == 0 and (b+x) % a == 0:
#        print(x)
#        break
#    else:
#        x += 1


###  Супер  ###


#a, b = map(int, input().split())
#def ssim(x, y):
#    if x % 2 == 0 or y % 2 == 0:
#        return 0
#    else:
#        return 1 + 4 * ssim(x // 2, y // 2)
#print(ssim(a,b))


###   Патрик   ###

#n = int(input())
#l = [int(_) for _ in input().split()]
#l.reverse()
#x = 0
#s = 0
#for i in l:
#    if i >= x:
#        x = i
#    else:
#        s += x - i
#print(s)



###   Космос   ###

#from math import factorial
#n, m = map(int, input().split())
#Comb = (factorial(n))/(6 * factorial(n-3))
#pairs = []
#for i in range(m):
#    pairs.append(list(input().split()))
#for i in range(len(pairs)-1):
#    for j in pairs[i+1:]:
#        if str(pairs[i][0]) == str(j[0]) and str(pairs[i][1]) == str(j[1]) or str(pairs[i][0]) == str(j[1]) and str(pairs[i][1]) == str(j[0]):
#            pairs[i] = 0
#            break
#new = []
#for i in pairs:
#    if i != 0:
#        x = sorted(i)
#        new.append(str(x[0] + x[1]))
#count = 0
#for i in range(1, n-1):
#    for j in range(i+1, n):
#        for k in range(j+1, n+1):
#            if str(i) + str(j) in new or str(j) + str(k) in new or str(i) + str(k) in new:
#                count += 0
#            else:
#                count += 1
#
#print(count)


###   Жокир))   ###

#banks = [int(_) for _ in input().split()]
#nulls = [0]*len(banks)
#if len(banks) == 1:
#    print(banks[0])
#else:
#    nulls[0] = banks[0]
#    nulls[1] = max(nulls[0], banks[1])
#for i in range(2, len(banks)):
#  nulls[i] = max(banks[i] + nulls[i - 2], nulls[i - 1]);
#print(nulls[-1])

###   Крош   ###

#n, k = map(int, input().split())
#negr = [int(_) for _ in input().split()]
#ans = 0
#for i in range(2**n):
#    j = i ^ k
#    if negr[i] + negr[j] > ans:
#        ans = negr[i] + negr[j]
#print(ans)


###   Строки   ###

t = int(input())
t = int(input())
for i in range(t):
    x = [int(_) for _ in input().split()]
    n, k = x[0], x[1]
    print(fibo(n)[k-1])
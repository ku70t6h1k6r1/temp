# coding: UTF-8

dic = {}
dic[0] = 0.234
dic[4] = 0.142
dic[5] = -0.654
dic[2] = -0.986
dic[10] = -0.114
dic = sorted(dic.items(), key=lambda x: x[0])
a = []
for fac in dic:
    a.append(fac[1])

print a

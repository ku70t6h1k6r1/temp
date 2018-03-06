# coding: UTF-8
import math
import random
import numpy as np
from scipy import stats

# ソフトマックス関数
def softmax(a, t = 1):
    temp = np.empty(len(a))

    for i in range(len(a)):
        temp[i] = math.exp(a[i]/t)

    return temp / temp.sum()

# カテゴリカル分布（歪んだサイコロ）
def dice(pkIn):
    xk = np.arange(len(pkIn))
    pk = (pkIn)
    custm = stats.rv_discrete(name='custm', values=(xk, pk))
    return (custm.rvs(size=1))[0]


#SQLで管理した方がよさげ

rythmIndex = {}
rythmIndex['on1'] = 0
rythmIndex['on2'] = 1
rythmIndex['on4'] = 2
rythmIndex['on8'] = 3
rythmIndex['on16'] = 4
rythmIndex['off1'] = 5
rythmIndex['off2'] = 6
rythmIndex['off4'] = 7
rythmIndex['off8'] = 8
rythmIndex['off16'] = 9

# out / loop loop + out = 1 順番大切
rythmWeight = np.array([ 
softmax([0.5,0.5])
,softmax([0.4,0.5])
,softmax([0.5,0.5])
,softmax([0.4,0.5])
,softmax([0.5,0.5])
,softmax([0.6,0.5])
,softmax([0.5,0.5])
,softmax([0.6,0.5])
,softmax([0.5,0.5])
,softmax([0.6,0.5])
,softmax([0.5,0.5])
])

parentRythmWeight = np.array(softmax([3,4,5,6,3,5,3,5,6,2])) # sum = 1 
print parentRythmWeight

rythmLine = []

noteDuration = dice(parentRythmWeight)
rythmLine.append(noteDuration)

for i in range(4):
    loopFlg = dice(np.ravel(rythmWeight[noteDuration,]))
    print np.ravel(rythmWeight[noteDuration,:])
    print loopFlg
    if loopFlg > 0 :
        rythmLine.append(noteDuration)
    else:
        noteDuration = dice(parentRythmWeight)
        rythmLine.append(noteDuration)

print rythmLine



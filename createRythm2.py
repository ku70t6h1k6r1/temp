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
#ON
rythmIndex[0] = [1,0,0,0 ,0,0,0,0 ,0,0,0,0 ,0,0,0,0 ]
rythmIndex[1] = [1,0,0,0 ,0,0,0,0 ]
rythmIndex[2] = [1,0,0,0 ]
rythmIndex[3] = [1,0 ]
rythmIndex[4] = [1]
#OFF
rythmIndex[5] = [-1,0,0,0 ,0,0,0,0 ,0,0,0,0 ,0,0,0,0 ]
rythmIndex[6] = [-1,0,0,0 ,0,0,0,0 ]
rythmIndex[7] = [-1,0,0,0 ]
rythmIndex[8] = [-1,0 ]
rythmIndex[9] = [-1]

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

parentRythmWeight = np.array(softmax([3,4,5,6,3,1,1,1.5,1.5,1])) # sum = 1 


noteDuration = dice(parentRythmWeight)
rythmLine = np.array(rythmIndex[noteDuration])

while len(rythmLine) <= 16 * 4:
    loopFlg = dice(np.ravel(rythmWeight[noteDuration,]))
    if loopFlg > 0 :
        rythmLine = np.r_[rythmLine,rythmIndex[noteDuration]]
    else:
        noteDuration = dice(parentRythmWeight)
        rythmLine = np.r_[rythmLine,rythmIndex[noteDuration]]

print rythmLine



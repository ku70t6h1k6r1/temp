# coding: UTF-8
import math
import random
import numpy as np
import createForm as form
from scipy import stats
np.set_printoptions(threshold=np.inf)

def dice(pkIn):
    # カテゴリカル分布（歪んだサイコロ）
    xk = np.arange(len(pkIn))
    pk = (pkIn)
    custm = stats.rv_discrete(name='custm', values=(xk, pk))
    return (custm.rvs(size=1))[0]

# シグモイド関数
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))  # GAIN設定したほうが良い


# ソフトマックス関数
def softmax(a, t = 1):
    temp = np.empty(len(a))

    for i in range(len(a)):
        temp[i] = math.exp(a[i]/t)

    return temp / temp.sum()

def create():
    rehC = form.create(4,4,0)
    rehA = form.create(8,2,0)
    melody = np.r_[rehA, rehC]
    return melody

def pickUpAccent(melody):
    output = np.zeros(0)
    oneBar = np.zeros(len(melody))

    # minimum beat length sixteen-beat and then 16
    for j in range(len(melody)/16):
        for i in range(16):
            if melody[16*j + i] != -1:
                oneBar[16*j + i] = oneBar[16*j + i]  + 1
    output = np.r_[output, softmax(oneBar)] #ランダム性はコントロールできる。
    return output

def pickUpSecAccent(melody):
    output = np.zeros(0)
    oneBar = np.zeros(16)

    # minimum beat length sixteen-beat and then 16
    for j in range(len(melody)/16):
        for i in range(16):
            if melody[j*16 + i] != -1:
                oneBar[i] = oneBar[i]  + 1
        if j % 4 == 3: #リズムの一塊によって変更する
            output = np.r_[output, softmax(oneBar), softmax(oneBar), softmax(oneBar), softmax(oneBar)] #ランダム性はコントロールできる。*3でいけないのか。
            oneBar = np.zeros(16)
    return output

def merge(pickUpAccent_o, pickUpSecAccent_o, temp):
    merge =  pickUpAccent_o * pickUpSecAccent_o

    output = np.zeros(0)
    oneBar = np.zeros(16)

    # minimum beat length sixteen-beat and then 16
    for j in range(len(merge)/16):
        for i in range(16):
            oneBar[i] = merge[j*16 + i]
        output = np.r_[output, softmax(oneBar, t = temp)] #ランダム性はコントロールできる。0.0005
        oneBar = np.zeros(16)
    return output


#print "#############"
#melody = create()
#merge(pickUpAccent(melody), pickUpSecAccent(melody))

# coding: UTF-8
import math
import random
import numpy as np
from scipy import stats

# ソフトマックス関数
def softmax(a):
    temp = np.empty(len(a))

    for i in range(len(a)):
        temp[i] = math.exp(a[i])

    return temp / temp.sum()

def dice(pkIn):
    # カテゴリカル分布（歪んだサイコロ）
    xk = np.arange(len(pkIn))
    pk = (pkIn)
    custm = stats.rv_discrete(name='custm', values=(xk, pk))
    return (custm.rvs(size=1))[0]

class CreateMelody:
    def __init__(self):
        self.pitchWeight = np.array(softmax([5.5, 1.5, 5, 1.5, 5, 5, 1.5, 5.1, 1.5, 5, 1.5, 5]))

    def create(self,note_n):
        melody = []

        for i in range(note_n):
            melody.append(dice(self.pitchWeight))
        return melody

    def translateMelody(self,melody):
        output = []
        oneNote = np.zeros(12)
        for i in range(8):
            if melody[i] < 12 :
                oneNote[melody[i]] = oneNote[melody[i]]  + 1
        output = softmax(oneNote)
        return output

def Create(note_n):
    notes = CreateMelody()
    return notes.create(note_n)

#test
#print Create(10)

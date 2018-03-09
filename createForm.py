# -*- coding: utf-8 -*-
import createRythm2 as rythm
import createMelody as pitch
import numpy as np

#rehC
def create(bars_n, n, lastNote):
    reh_rythm = rythm.Create(bars_n)
    reh_pitch = pitch.Create(bars_n*16)
    rev_reh_rythm = reh_rythm[::-1]
    rev_reh_pitch  = reh_pitch[::-1]

    onsetIndex = np.where(rev_reh_rythm == 1)
    firstDoIndex = np.min(np.where(rev_reh_pitch == lastNote))

    reh_melody = np.full(bars_n*16, -1)

    j = 0
    onsetIndex = list(onsetIndex[0])
    for i in onsetIndex:
        reh_melody[i] = rev_reh_pitch[firstDoIndex + j] #足りない時の対応
        j += 1

    melody = reh_melody[::-1]
    for i in range(n - 1 ):
        melody = np.r_[melody,reh_melody[::-1]]

    return melody

#rehC = create(4,4,0)
#rehA = create(8,2,7)
#song = np.r_[rehA, rehC]
#print song


#rehC_rythm = np.r_[rehC_rythm, rehC_rythm]
#rehC_rythm = np.r_[rehC_rythm, rehC_rythm]

#rehB
#rehB_rythm = rythm.Create(8)
#rehB_rythm = np.r_[rehB_rythm, rehB_rythm]

#rehA
#rehA_rythm = rythm.Create(4)
#rehA_rythm = np.r_[rehA_rythm, rehA_rythm]

# -*- coding: utf-8 -*-
import createRythm2 as rythm
import createMelody as pitch
import numpy as np

#rehC
rehC_rythm = rythm.Create(4)
rehC_pitch = pitch.Create(4*16)


rehC_rythm = np.r_[rehC_rythm, rehC_rythm]
rehC_rythm = np.r_[rehC_rythm, rehC_rythm]

#rehB
rehB_rythm = rythm.Create(8)
rehB_rythm = np.r_[rehB_rythm, rehB_rythm]

#rehA
rehA_rythm = rythm.Create(4)
rehA_rythm = np.r_[rehA_rythm, rehA_rythm]

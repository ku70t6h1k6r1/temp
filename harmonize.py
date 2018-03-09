# coding: UTF-8
import math
import random
import numpy as np
import createForm as form
from scipy import stats

# シグモイド関数
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))  # GAIN設定したほうが良い


# ソフトマックス関数
def softmax(a):
    temp = np.empty(len(a))

    for i in range(len(a)):
        temp[i] = math.exp(a[i])

    return temp / temp.sum()


# ニューロン
class Neuron:
    input_sum = 0.0
    output = 0.0

    def setInput(self, inp):
        self.input_sum += inp

    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return self.output

    def reset(self):
        self.input_sum = 0.0
        self.output = 0.0


# ニューラルネットワーク
class NeuralNetwork:
    # リスト初期値
    w_im = []
    w_om = []
    input_layer = []
    middle_layer = []
    output_layer = []

    inputBP_layer = []
    middleBP_layer = []
    outputBP_layer = []

    def initialize(self, in_n, middle_n, out_n):
        self.in_n = in_n
        self.middle_n = middle_n
        self.out_n = out_n

        # 重み初期値
        self.w_im = [[0.0] * self.middle_n for i in range(self.in_n + 1)]
        self.w_mo = [[0.0] * self.out_n for i in range(self.middle_n + 1)]
        self.resetW()

        # 各層の初期値
        self.input_layer = [0.0] * self.in_n
        self.input_layer.append(1.0)

        for iMID in range(self.middle_n):
            self.middle_layer.append(Neuron())
        self.middle_layer.append(1.0)

        for iOUT in range(self.out_n):
            self.output_layer.append(Neuron())

        # BP用
        for iMID in range(self.middle_n):
            self.middleBP_layer.append(Neuron())

        for iOUT in range(self.out_n):
            self.outputBP_layer.append(Neuron())

    # ----重み初期値設定
    def resetW(self):
        self.w_im = np.loadtxt("out_im.csv", delimiter=",")
        self.w_mo = np.loadtxt("out_mo.csv", delimiter=",")

    # 実行
    def commit(self, input_data):
        # 各層のリセット
        for iIN in range(self.in_n):
            self.input_layer[iIN] = input_data[iIN]

        for iMID in range(self.middle_n):
            self.middle_layer[iMID].reset()

        for iOUT in range(self.out_n):
            self.output_layer[iOUT].reset()

        # 入力層→中間層
        for iIN in range(self.in_n + 1):
            for iMID in range(self.middle_n):
                self.middle_layer[iMID].setInput(self.input_layer[iIN] * self.w_im[iIN][iMID])

        # 中間層→出力層

        for iMID in range(self.middle_n):
            for iOUT in range(self.out_n):
                self.output_layer[iOUT].setInput(self.middle_layer[iMID].getOutput() * self.w_mo[iMID][iOUT])

        for iOUT in range(self.out_n):
            self.output_layer[iOUT].setInput(self.middle_layer[self.middle_n] * self.w_mo[self.middle_n][iOUT])
            self.output_layer[iOUT].getOutput()

        return self.output_layer

#コード
class Chord:
    IM7 = [0,4,7,11]
    I7 = [0,4,7,10]
    Isus4M7 = [0,5,7,11]
    Isus47 = [0,5,9,10]
    Im7 = [0,3,7,10]
    ImM7 = [0,3,7,11]
    Imb57= [0,3,6,10]
    Idim7 = [0,3,6,9]

    chordTones = []

    def convertNote(notes,num):
        outputNotes = []
        for i in range(len(notes)):
            if notes[i] + num > 11:
                outputNotes.append(notes[i] + num - 12)
            else:
                outputNotes.append(notes[i] + num)
        return outputNotes

    for i in range(12):
        tempChordTones = []
        tempChordTones.append(convertNote(IM7,i))
        tempChordTones.append(convertNote(I7,i))
        tempChordTones.append(convertNote(Isus4M7,i))
        tempChordTones.append(convertNote(Isus47,i))
        tempChordTones.append(convertNote(Im7,i))
        tempChordTones.append(convertNote(ImM7,i))
        tempChordTones.append(convertNote(Imb57,i))
        tempChordTones.append(convertNote(Idim7,i))
        chordTones.append(tempChordTones)

    def output(self):
        return self.chordTones

class CreateMelody:

    def create(self):
        rehC = form.create(4,4,0)
        rehA = form.create(8,2,7)
        melody = np.r_[rehA, rehC]
        return melody

    def translateMelody(self,melody):
        output = []
        oneNote = np.zeros(12)
        # minimum beat length sixteen-beat and then 16
        for i in range(8):
            if melody[i] != -1:
                oneNote[melody[i]] = oneNote[melody[i]]  + 1
        output = softmax(oneNote)
        return output

    def chord(self,chords):
        chordNo = chords.argmax()
        chordIndex = chordNo % 8
        root = int(chordNo % 8)
        # only root note returned
        return root
#テスト実行

harmonizeNW = NeuralNetwork()
NeuralNetwork.initialize(harmonizeNW , 12, 8, 96)
NeuralNetwork.resetW(harmonizeNW)

melodyObj = CreateMelody()
melody = melodyObj.create()
chords = np.full(len(melody)/8, -1)

for i in range(len(melody)/8):
    melodyForMachine = melodyObj.translateMelody(melody[i*8 : (i+1)*8])
    tempOutputLayer = harmonizeNW.commit(melodyForMachine)
    outputLayer = np.zeros(96)
    for j in range(96):
        outputLayer[j] = tempOutputLayer[j].output
    chords[i] = melodyObj.chord(outputLayer)

print melody
print chords

####
#midiout
import pygame.midi
from time import sleep

pygame.init()
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
output_id = pygame.midi.get_default_output_id()
print("input MIDI:%d" % input_id)
print("output MIDI:%d" % output_id)
input = pygame.midi.Input(input_id)
o = pygame.midi.Output(output_id)

print ("starting")
print ("full midi_events:[[[status,data1,data2,data3],timestamp],...]")

i = 0
note_past = 60
note_past_bs = 60

o.set_instrument(4,0)
o.set_instrument(4,1)
for note in melody:
    if note != -1 :
        o.note_off(note_past, 60, 0)
        o.note_on(note + 60,int(np.random.normal(45,15)),0)
        note_past = note + 60
    if i % 8 == 0:
        o.note_off(note_past_bs,60, 1)
        o.note_on(chords[int(i/8)] + 48, int(np.random.normal(45,8)), 1)
        note_past_bs = chords[int(i/8)] + 48
    i += 1
    sleep(0.25)
o.note_on(60 ,60,0)
o.note_on(48, 40, 1)
sleep(4)

input.close()
o.close()
pygame.midi.quit()
pygame.quit()
exit()

# coding: UTF-8
import math
import random


# シグモイド関数
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a)) #GAIN設定したほうが良い

#

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
    # 重み
    #w_im = [[0.496, 0.512], [-0.501, 0.998], [0.498, -0.502]]    #[中間層ノードの数(without Bias)]×入力層ノードの数(with bias)
    #w_mo = [0.121, -0.4996, 0.200]    #[出力層ノードの数]×中間層ノードの数
    #[接続元ノードpreのINDEX(with Bias)][接続先ノードpostのINDEX(without Bias)]
    
    #リスト初期値
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
        
        #重み初期値
        self.w_im = [[0.0] * self.middle_n for i in range(self.in_n + 1 )]
        self.w_mo = [[0.0] * self.out_n for i in range(self.middle_n + 1 )]
        self.resetW()
        
        #各層の初期値
        self.input_layer = [0.0] * self.in_n
        self.input_layer.append(1.0)
        
        for iMID in range (self.middle_n):
            self.middle_layer.append(Neuron())
        self.middle_layer.append(1.0)

        for iOUT in range (self.out_n):
            self.output_layer.append(Neuron())

        #BP用
        for iMID in range (self.middle_n):
            self.middleBP_layer.append(Neuron())

        for iOUT in range (self.out_n):
            self.outputBP_layer.append(Neuron())

    # ----重み初期値設定
    def resetW(self):
        for post in range(self.middle_n):
            for pre in range(self.in_n + 1):
                self.w_im[pre][post] = random.uniform(-1,1)
        for post in range(self.out_n):
            for pre in range(self.middle_n + 1):
                self.w_mo[pre][post] = random.uniform(-1,1)

    # 実行
    def commit(self, input_data):
        # 各層のリセット
        for iIN in range (self.in_n):
            self.input_layer[iIN] = input_data[iIN]

        for iMID in range (self.middle_n):
            self.middle_layer[iMID].reset()

        for iOUT in range (self.out_n):
            self.output_layer[iOUT].reset()

        # 入力層→中間層
        for iIN in range (self.in_n + 1):
            for iMID in range (self.middle_n):
                self.middle_layer[iMID].setInput(self.input_layer[iIN] * self.w_im[iIN][iMID])

        # 中間層→出力層
        
        for iMID in range (self.middle_n ):
            for iOUT in range (self.out_n):
                self.output_layer[iOUT].setInput(self.middle_layer[iMID].getOutput() * self.w_mo[iMID][iOUT])

        for iOUT in range (self.out_n):
            self.output_layer[iOUT].setInput(self.middle_layer[self.middle_n] * self.w_mo[self.middle_n][iOUT])
            self.output_layer[iOUT].getOutput()

        return self.output_layer

    def learn(self, inputData, outputData)
        # 各層のリセット
        for iMID in range (self.middle_n):
            self.middleBP_layer[iMID].reset()

        for iOUT in range (self.out_n):
            self.outputBP_layer[iOUT].reset()

        #NW出力
        nwResult = self.commit(inputData)
        nwOutputData = [] #0-1
        for i in range(self.out_n):
            nwOutputData.append(nwResult[i].output)
        
        #学習係数
        k = 0.3

        #BPようにメソッド作ったほうがよいのでは
        #出力層→
        for iOUT in range(self.out_n):
            self.outputBP_layer[iOUT].setInput(1.0 - nwResult[iOUT]) * nwResult[iOUT] * 2 * ( nwResult[iOUT] - outputData[iOUT] ) 
            #delta_w_mo = (outputData[iOUT] - nwResult[iOUT]) * nwResult[iOUT] * (1.0 - nwResult[iOUT]) * 2

        #中間層
        for iMID in range(self.middle_n):
            for iOUT in range(self.out_n):
                self.middleBP_layer[iMID].setInput(self.outputBP_layer[iOUT].input_sum)
            self.middleBP_layer[iMID].output = self.middleBP_layer[iMID].input_sum * ( 1 - self.middle_layer[iMID].output ) * self.middle_layer[iMID].output

        #出力層→中間層
        for post in range(self.out_n):
            for pre in range(self.middle_n):
                self.w_mo[pre][post] -= k * self.outputBP_layer[post].output *  self.middle_layer[pre].output
        
        #中間層→入力層
        for post in range(self.middle_n):
            for pre in range(self.in_n):
                self.w_im[pre][post] -= k * self.middleBP_layer[post].output *  self.input_layer[pre].output #self.input_layer[pre].output多分sigmoidじゃない
        
#テスト実行
inputData = [-700, 8.9, 0.9, 0.65, 0.3, 0.3, -0.7, 8.9, 0.9, 0.65,10]


testNW = NeuralNetwork()
NeuralNetwork.initialize(testNW, 11, 7, 6)
NeuralNetwork.resetW(testNW)

testOut = testNW.commit(inputData)





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

    def learn(self, inputData, outputData):
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
            print nwResult[i].output

        #学習係数
        k = 0.8

        #BPようにメソッド作ったほうがよいのでは
        #出力層
        for iOUT in range(self.out_n):
            self.outputBP_layer[iOUT].setInput( (1.0 -  nwOutputData[iOUT] ) *  nwOutputData[iOUT] * 2.0 * ( nwOutputData[iOUT] - outputData[iOUT] ) )


        #中間層
        for iMID in range(self.middle_n):
            for iOUT in range(self.out_n):
                self.middleBP_layer[iMID].setInput(self.outputBP_layer[iOUT].input_sum * self.w_mo[iMID][iOUT]) 
            self.middleBP_layer[iMID].output = self.middleBP_layer[iMID].input_sum * ( 1.0 - self.middle_layer[iMID].output ) * self.middle_layer[iMID].output

        #出力層→中間層
        for post in range(self.out_n):
            for pre in range(self.middle_n):
                self.w_mo[pre][post] -= k * self.outputBP_layer[post].input_sum  *  self.middle_layer[pre].output
        
        #中間層→入力層
        for post in range(self.middle_n):
            for pre in range(self.in_n):
                self.w_im[pre][post] -= k * self.middleBP_layer[post].output *  self.input_layer[pre] 
                #self.input_layer[pre].output sigmoidじゃない Neuron()じゃない
                
        return self
        
#テスト実行

testNW = NeuralNetwork()
NeuralNetwork.initialize(testNW, 3, 10, 3)

for i in range(20000):
    i1 = random.uniform(0,1)
    i2 = random.uniform(0,1)
    i3 = random.uniform(0,1)
    
    inputData = [i1, i2, i3]
    outputData = [i1*0.5, i2*0.5, i3*0.5]
    print "###################"
    NeuralNetwork.learn(testNW ,inputData, outputData)

print "#TEST##################"
NeuralNetwork.learn(testNW ,[0,0.4,0.4], [0,0.2,0.2])
print "#TEST##################"
NeuralNetwork.learn(testNW ,[0.4,0.6,0.3], [0.2,0.3,0.15])


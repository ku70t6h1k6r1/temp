# encoding: utf-8
require 'matrix'

#a = Matrix[[2,1,3,4],[3,2,5,2],[3,4,1,-1],[-1,-3,1,3]]
#a = Matrix[[3,1],[2,2]]
a = Matrix[[-1,2],[3,4]]

A = a
#V = a.eigensystem.v
V = a.eigensystem.eigenvectors
W = a.eigensystem.v_inv
#D = a.eigensystem.d
D = a.eigensystem.eigenvalues 

i = 0
puts D[i]
puts A * V[i]
puts D[i] * V[i]

# encoding: utf-8
require 'matrix'

a = Matrix[[0,1],[-0.5,-1.5]]



A = a
V = a.eigensystem.v
W = a.eigensystem.v_inv
D = a.eigensystem.d
u = a.eigensystem.eigenvectors 

#puts W
#puts "# WA = DW ########"
#puts W * A
#puts D * W

#correct
#puts D[0,0] * u[0]
#puts A * u[0]

ut = Matrix[u[0]]
puts ut * A.t
puts ut * D[0,0]


#puts A
#puts V
#puts W
#puts D




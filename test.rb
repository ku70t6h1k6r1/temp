# encoding: utf-8
require 'matrix'

a = Matrix[[2,1],[-0.5,-1.5]]
x =Vector[1.958489222, 0.584487374]


A = a
V = a.eigensystem.v
W = a.eigensystem.v_inv
D = a.eigensystem.d

#puts W
#puts "# WA = DW ########"
#puts W * A
#puts D * W

puts A.eigensystem.eigenvectors 
puts 1.85 * A

#puts A
#puts V
#puts W
#puts D

#puts x
#puts x * A


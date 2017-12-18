require 'matrix'

class Matrix
  def []=(i,j,x)
    @rows[i][j]=x
  end
end

#a = Matrix.zero(2)
#a[0,0] = 2
#a[0,1] = 1
#a[1,0] = 1
#a[1,1] = 2

#puts a.lup.solve([2, 3])[0].to_f

mtxN = 8

cnt = 64

b = Matrix.zero(mtxN)
b = b 

b[0,2] = Rational(1, 3) 
b[0,3] = Rational(1, 3) 
b[0,7] = Rational(1, 3) 

b[1,3] = Rational(1, 2) 
b[1,7] = Rational(1, 2) 

b[2,0] = Rational(1, 1)

b[3,0] = Rational(1, 3) 
b[3,5] = Rational(1, 3) 
b[3,7] = Rational(1, 3) 

b[4,0] = Rational(1, 6) 
b[4,1] = Rational(1, 6)
b[4,2] = Rational(1, 6)
b[4,3] = Rational(1, 6)
b[4,6] = Rational(1, 6)
b[4,7] = Rational(1, 6)

b[5,0] = Rational(1, 3)
b[5,4] = Rational(1, 3)
b[5,7] = Rational(1, 3)

b[6,0] = Rational(1, 2)
b[6,7] = Rational(1, 2)

b[7,5] = Rational(1, 1)

#a 4,9 (1,-4) (1,1)
a = Matrix.zero(2)
a[0,0] = 8
a[0,1] = 1
a[1,0] = 4
a[1,1] = 5


#if mtxN^2 == cnt then

	v, d, v_inv = b.eigensystem.eigenvalues
	#puts b.eigensystem.eigenvalues
	
	a = b
	b = b.t

	V = b.eigensystem.v
	W  = b.eigensystem.v_inv
	Wt = W.t
	A = b
	D = b.eigensystem.d
	u = b.eigensystem.eigenvectors
	ut = Matrix[u[0]]

#	W = a.eigensystem.v_inv
#	Wt = W.t
#	A = a
#	D = a.eigensystem.d
	
	#DW = WA
	#puts D
	#puts D * W
	#puts W * A
	
	#AV = VD
	#puts D
	#puts A * V
	#puts  V * D
	
	#W.inv = V
	

	puts a
	puts "###########"
	puts D[0,0]
	puts ut * a
	puts ut #* D[0,0]

	
#end


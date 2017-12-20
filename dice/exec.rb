require 'matrix'

class Dice
	def shake(array)
		array = ( Vector.elements(array)  / array.inject(:+) ).to_a
		random = Random.new.rand(1e8)/1e8.to_f
		
		sumVal = 0.0
		i =  0
		array.each do |val|
			sumVal = val + sumVal
			if val  > random then
				break
			else
				i += 1
			end
		end
		
		return i
	end
end

a = [1,1,2]

dice = Dice.new
puts dice.shake(a)


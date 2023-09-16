# Demonstrate Currying of composition of function

# currying method
def convert(b, c, d):
	def a(x):
		return b(c(d(x)))
	return a
	
def daystohour(time):
	return time * 24
	
def hourstominutes(time):
	return time * 60
	
def minutestoseconds(time):
	return time * 60
	
if __name__ == '__main__':
	transform = convert(minutestoseconds, hourstominutes, daystohour)
    # convert days to seconds
	e = transform(2)
	print(e)
	

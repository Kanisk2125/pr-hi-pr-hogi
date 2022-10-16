import cmath
num=eval(input('enter a number : '))
num_sqrt = cmath.sqrt(num)
print('the square root of a number is :{1:0.3f}+ {2:0.3f}j '.format(num,num_sqrt.real, num_sqrt.imag))

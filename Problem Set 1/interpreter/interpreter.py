exp = input("Expression: ")

x, y, z = exp.split(" ")
x = float (x)
z = float (z)

if y == '+':
    print( float( x + z ) )
elif y == '-':
    print( float( x - z ) )
elif y == '*':
    print( float( x * z ) )
elif y == '/' and 'z' != 0:
    print( float( x / z ) )

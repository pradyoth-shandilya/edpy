from sympy import *
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

xhat = "x\u0302"
yhat = "y\u0302"
zhat = "z\u0302"
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
def gradient(printn=1):
	check = 0
	start = "\033[1m"
	end = "\033[0;0m"
	print("This is the gradient evaluator of polynomial fields. Use the following instructions to evaluate the gradient...")
	#exnum = input("Enter the number of expressions seperated by '+' symbols")
	#Enter expressions in the form of coefficient, symbol and power in that order and enter the word 'end' to terminate
	#the expression
	symexpr = input("Enter expression\n")
	print(' ')
	expr = sympify(symexpr)
	a = diff(expr,x,1)
	#Uncomment the following lines to get colored outputs
	#astr = "("+str(a)+")" + color.BOLD + color.RED + xhat + color.END + color.END
	astr = "("+str(a)+")" + xhat
	b = diff(expr,y,1)
	#bstr = "("+str(b)+")" + color.BOLD + color.BLUE + yhat + color.END + color.END
	bstr = "("+str(b)+")" + yhat
	c = diff(expr,z,1)
	#cstr = "("+str(c)+")" + color.BOLD + color.YELLOW + zhat + color.END + color.END
	cstr = "("+str(c)+")" + zhat
	gexpr = astr + " + " + bstr + " + " + cstr
	grad = "\u2207r\u0302 = " + astr + " + " + bstr + " + " + cstr
	if printn==0:
		print(grad)
	#return gradient
	#grad = Add('(',a,b,c)
	#print(grad)

def divergence():
	print("This is the divergence evaluator. Use the following instructions to evaluate the divergence...")
	xcomp = input("Enter the " + xhat+ " component\n")
	xcomp = sympify(xcomp)
	ycomp = input("Enter the " + yhat+ " component\n")
	ycomp = sympify(ycomp)
	zcomp = input("Enter the " + zhat+ " component\n")
	zcomp = sympify(zcomp)
	print("The vector whose divergence is to be evaulated is\n")
	print("("+str(xcomp)+")"+xhat+" + ("+str(ycomp)+")"+yhat+" + ("+str(zcomp)+")"+zhat)
	p_xd = diff(xcomp,x,1)#Partial derivative wrt x
	p_yd = diff(ycomp,y,1)#Partial derivative wrt y
	p_zd = diff(zcomp,z,1)#Partial derivative wrt z
	print("\u2207 . r\u0302 = (" + str(p_xd) + ") + (" + str(p_yd) + ") + (" + str(p_zd) + ")\n")


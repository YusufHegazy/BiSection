import sympy as sp
from math import *
import texttable as tt

print("""

███╗   ██╗██╗   ██╗███╗   ███╗    ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
████╗  ██║██║   ██║████╗ ████║    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║██╔████╔██║    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
██║╚██╗██║██║   ██║██║╚██╔╝██║    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                  
                                                                By: Yusuf Hegazy                                                                                                                             
""")
   

def func(expr, x): #evaluates a func., args: func, x substitute
    return eval(expr)


def dfunc(expr): #derivative of func in terms of x, args: func
    x = sp.Symbol('x')
    symfnu = str(sp.diff(func(expr, x)))
    return symfnu

def dfuncsub(expr, x): #evaluates the derivative of a func., args: func to deriv, x sub.
    return func(dfunc(expr), x)


def bisection_input():
    input_expr = str(input("function: "))
    input_exprn = input_expr.replace("^","**").lower()
    a_input = float(input("+ve: "))
    b_input = float(input("-ve: "))
    approx = float(input("approxiamtion:"))
    bisection(input_exprn,a_input,b_input,approx)

def bisection(expr, af,bf,tol):
    tablebisec = tt.Texttable()
    titles = ['a', 'b', 'xi', 'f(xi)']
    tablebisec.header(titles)
    tablebisec.set_precision(10)
    
    a_list = []
    b_list = []
    xi_list = []
    fxi_list = []
    a = af
    b = bf
    xi = (a+b)/2
    a_list.append(a)
    b_list.append(b)
    xi_list.append(xi)
    fxi_list.append(func(expr,xi))
    while (abs(b-a)>tol):
        if (func(expr,xi) < 0):
            b = xi
        else:
            a = xi
        xi = (a+b)/2
        a_list.append(a)
        b_list.append(b)
        xi_list.append(xi)
        fxi_list.append(func(expr,xi))

    for row in zip(a_list,b_list,xi_list,fxi_list):
        tablebisec.add_row(row)

    
    s = tablebisec.draw()
    print(s)
   


def newtonform(xn, fxn, dfxn):
        return xn - fxn/dfxn
    
def newton_method_input(): #just to use it to trigger
    fn = str(input("function: "))
    fns = fn.replace("^","**").lower()
    xnod = float(input("x0 = "))
    tole = float(input("approximation: "))
    newton_method(fns, xnod, tole)
    
def newton_method(expr, xn, tol):   #all the work is done here
    
    tablenewton = tt.Texttable()
    titles = ['i', 'x_i-1', 'x_i', 'tolerance']
    tablenewton.header(titles)
    tablenewton.set_precision(10)
    
    xnode_list = []
    oldxnode_list = []
    tol_list= []
    i_list = []
    i = 1
    fnsubxn = func(expr, xn)
    dfnsubxn = dfuncsub(expr, xn)
    old_xnode = 0
    xnode = newtonform(xn, fnsubxn, dfnsubxn)
    xnode_list.append(xnode)
    oldxnode_list.append(old_xnode)
    tol_list.append(abs(xnode-old_xnode))
    i_list.append(i)
    while( abs(xnode-old_xnode)> tol):
        old_xnode = xnode
        fnsubxn = func(expr, xnode)
        dfnsubxn = dfuncsub(expr, xnode)
        xnode = newtonform(xnode, fnsubxn, dfnsubxn)
        i+=1
        xnode_list.append(xnode)
        oldxnode_list.append(old_xnode)
        tol_list.append(abs(xnode-old_xnode))
        i_list.append(i)
        
        
    for row in zip(i_list,oldxnode_list,xnode_list,tol_list):
        tablenewton.add_row(row)
        
    s = tablenewton.draw()
    return print(s)



def secantform(xn,oldxn, fxn, oldfxn):
    return xn - (fxn*(xn-oldxn))/(fxn-oldfxn)

def secant_method_input(): #just to use it with other methods
    fn = str(input("function: "))
    fns = fn.replace("^","**").lower()
    xnod = float(input("x0 = "))
    oldxnod = float(input("x1 = "))
    tole = float(input("approximation: "))
    secant_method(fns, xnod, oldxnod, tole)

def secant_method(expr, oldoldxn, oldxn, tol):   #all the work is done here
    tablesecant = tt.Texttable()
    titles = ['i', 'x_i-2', 'x_i-1', 'x_i', 'tolerance']
    tablesecant.header(titles)
    tablesecant.set_precision(10)
    
    xnode_list = []
    oldxnode_list = []
    oldoldxnode_list = []
    tol_list= []
    i_list = []
    i = 2
    old_xnode = oldxn
    oldold_xnode = oldoldxn
    fnsuboldxn = func(expr, oldxn)
    fnsuboldoldxn = func(expr, oldoldxn)
    xnode = secantform(old_xnode, oldold_xnode, fnsuboldxn, fnsuboldoldxn)
    
    xnode_list.append(xnode)
    oldxnode_list.append(old_xnode)
    oldoldxnode_list.append(oldold_xnode)
    tol_list.append(abs(xnode-old_xnode))
    i_list.append(i)
    
    while( abs(xnode-old_xnode)> tol):
        oldold_xnode = old_xnode
        old_xnode = xnode
        
        fnsuboldxn = func(expr, old_xnode)
        fnsuboldoldxn = func(expr, oldold_xnode)

        xnode = secantform(old_xnode, oldold_xnode, fnsuboldxn, fnsuboldoldxn)
        
        i+=1
        xnode_list.append(xnode)
        oldxnode_list.append(old_xnode)
        oldoldxnode_list.append(oldold_xnode)
        tol_list.append(abs(xnode-old_xnode))
        i_list.append(i)
        
        
    for row in zip(i_list,oldoldxnode_list,oldxnode_list,xnode_list,tol_list):
        tablesecant.add_row(row)
        
    s = tablesecant.draw()
    return print(s)

instructionss = """

------------------------------------------------------------------------------
        ^ --> power operator
        * --> multiplication operator

        you must always use "*" to multiply numbers, for example: ab = a*b
        use the power operator "^" to raise a power, example: x^2


        functions available:
        ------------------------------------
        exp(x)	Returns e**x
        expm1(x)	Returns e^x - 1
        log(x, base)	Returns the logarithm of x to the base (defaults to e)
        log1p(x)	Returns the natural logarithm of 1+x
        log2(x)	Returns the base-2 logarithm of x
        log10(x)	Returns the base-10 logarithm of x
        pow(x, y)	Returns x raised to the power y
        sqrt(x)	Returns the square root of x
        acos(x)	Returns the arc cosine of x
        asin(x)	Returns the arc sine of x
        atan(x)	Returns the arc tangent of x
        atan2(y, x)	Returns atan(y / x)
        cos(x)	Returns the cosine of x
        hypot(x, y)	Returns the Euclidean norm, sqrt(x*x + y*y)
        sin(x)	Returns the sine of x
        tan(x)	Returns the tangent of x
        degrees(x)	Converts angle x from radians to degrees
        radians(x)	Converts angle x from degrees to radians
        acosh(x)	Returns the inverse hyperbolic cosine of x
        asinh(x)	Returns the inverse hyperbolic sine of x
        atanh(x)	Returns the inverse hyperbolic tangent of x
        cosh(x)	Returns the hyperbolic cosine of x
        sinh(x)	Returns the hyperbolic cosine of x
        tanh(x)	Returns the hyperbolic tangent of x
        erf(x)	Returns the error function at x
        erfc(x)	Returns the complementary error function at x
        gamma(x)	Returns the Gamma function at x
        lgamma(x)	Returns the natural logarithm of the absolute value of the Gamma function at x
        pi	Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...)
        e	mathematical constant e (2.71828...)
        ---------------------------------------------
"""

def run():
    print("""
+---------------------------------+
|Please choose a Numerical Method:|
|                                 |
|    [1] Bisection Method         |
|    [2] Newtons's Method         |
|    [3] Secant Method            |
|    [4] View Instructions        |
|    [5] Exit Program             |
+---------------------------------+
""")
          
    method_no = int(input())
          
    if(method_no == 1):
        bisection_input()
        run()
    elif(method_no == 2):
        newton_method_input()
        run()
    elif(method_no == 3):
        secant_method_input()
        run()
    elif(method_no == 4):
        print(instructionss)
        run()
    elif(method_no == 5):
        quit()
    
run()
    

import math

def swap(a,b):
    print(b,a,sep=",")

def c_to_f(c):
    return c*9/5+32

def hex_area(s):
    s = (3*math.sqrt(3)*s)/2
    print( f"{s:.2f}" )

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    swap(3,4)

    hex_area(3)
    hex_area(10)
    hex_area(1)

    print( c_to_f(-40) )
    print( c_to_f(0) )
    print( c_to_f(10) )

    print( is_leap(1600) )
    print( is_leap(1700) )
    print( is_leap(2000) )
    print( is_leap(2100) )
    print( is_leap(1996) )
    print( is_leap(2004) )
    print( is_leap(2005) )
    print( is_leap(2006) )


import sys 
from p2total import total

a = int( sys.argv[1] )
if a == 1:
    total( ["a", "b", "c"], [3,2,1] )
    
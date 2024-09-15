def total( items, prices ):
    return sum(prices)


items = ["Apple", "Banana", "Carrot"]
prices = [3,5,7]
for i in range( len(items) ):
    print( items[i], prices[i] )
print( "Total =", total(items, prices) )

# if - statementsler

var1=10
var2=20

if (var1>var2):
    print("condition one is correct")
elif(var1==var2):
    print("condition second is corret")
elif(var1<var2):
    print("condition third is corret")
else:
    print("condition for is corret")

liste=[1,2,3,4,5,7]



value=3
if value in liste:
    print("the condition is corret = {} ".format(value))
else:
    print("not including this number")



dictin={"onur":41,"ilyas":51,"görkem":61}
keys = dictin.keys()
if "onur" in keys:
    print("corrret")
else:
    print("not corret")


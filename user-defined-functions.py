# user defined functions

var1=20
var2=50
output=((((var1+var2)*50)/100.0)*var1/var2)
#print(output)


def my_first_func(var1,var2):
    """ 
    Bu benim ilk User defined functionum
    """
    output2=((((var1+var2)*50)/100.0)*var1/var2)
    return output2


print(my_first_func(10,20))
print(my_first_func(20,50))
print(my_first_func(100,30))

# return etmeden fonksiyon yazdirma
def deneme1():
    print("bu benim ikinci denemem")

deneme1()
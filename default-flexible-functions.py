# default and flexible functions
 
# cember cevre uzunlugu = 2*pi*r

def cember_cevre_hesapla(r,pi=3.14):
    """
    cember cevresi hesapla
    input(parametre): r, pi
    output=cemberin cevresi
    """
    output=2*pi*r
    return output

print(cember_cevre_hesapla(2))


# flexible

def hesapla(boy,kilo):
    output=boy+kilo
    return output

print(hesapla(175,128))



def hesapla(boy,kilo,*args):
    print(len(args))
    output=(boy+kilo)*args[0]
    return output

print(hesapla(1,2,5,10,42))




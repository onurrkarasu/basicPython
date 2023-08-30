#yas=26
#isim="onur"
#soyisim="karasu"


def bilgilerim(yas,isim,soyisim,*args,ayakno=45):
   print("İsim  ",isim,"  yasi: ",yas, "  ayak no ",ayakno)
   print(type(isim), "  ",type(soyisim), "  ",type(ayakno))
   print(float(yas))
   output=args[0]*yas


bilgilerim(26,"onur","karasu",45,24,24)



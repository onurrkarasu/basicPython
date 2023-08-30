# 1640. yil = 17 yüzyıl
# 109 . yil = 2 yüzyil
# 2000. yil = 20 yüzyill


def year2Century(year):
    """
    from year to Century
    """
    str_year=str(year)

    if(len(str_year)<3):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"): #100, 200 ,300 
            return int(str_year[0])
        else:                   #190, 250, 450
            return int(str_year[0])+1
    else:           # 1750 , 1700, 1805
            if(str_year[2:4]=="00"):   # 1700, 1800, 1900
                 return int(str_year[:2])
            else:       # 1705, 1645, 1258
                 return int(str_year[:2])+1

print(year2Century(1500))
print(year2Century(1501))



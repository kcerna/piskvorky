from tah import tah

def tah_hrace (pole, pozice):

    if pozice < 0:
        #print('Pozice nemuze mit zapornou hodnotu! Zkus jeste ')
        raise ValueError('Pozice nemuze mit zapornou hodnotu! Zkus jeste ')
        return
    elif pozice > 19:
        #print('Je to prilis velke cislo drz se rozmezi 0 az 19! Zkus jeste ')
        raise ValueError('Je to prilis velke cislo drz se rozmezi 0 az 19! Zkus jeste ')
        return
    elif pole[int(pozice)] != '-':
        #print('Tato pozice je obsazena! Zkus jeste ')
        raise ValueError('Tato pozice je obsazena! Zkus jeste ')
        return
    else:
        return(tah(pole, pozice,'X'))
        #exit()




#while True:


#    try:
        #v_pozice = int(input('Zadej pozici kam to chces dat, musi byt mezi 0 a 19 = '))

        #v_pole = input('Zadej pole, musi mit jenom 20 symbolu = ')

#        tah_hrace(pole, pozice)

#    except ValueError:
#        True

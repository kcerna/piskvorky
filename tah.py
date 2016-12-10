def tah (pole, cislo_policka, symbol):

    v_result = pole[:int(cislo_policka)] + symbol + pole[int(cislo_policka) + 1:]

    return(v_result)



#v_pole = input('Zadej cele pole, musi mit 20 symbolu! ')
#v_cislo_policka = input('Zadej cislo policka ')
#v_symbol = input('Zadej symbol ')

#tah(v_pole, v_cislo_policka, v_symbol)

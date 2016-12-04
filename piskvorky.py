#from zamen import zamen
import random
#from tah import tah
#from tah_hrace import tah_hrace
#from tah_pocitace import tah_pocitace
#from vyhodnot import vyhodnot
import sys
from termcolor import colored, cprint
from colored import fore, back, style


def vyhodnot(herni_pole):

    herni_pole = str.upper(herni_pole)

    if 'XXX' in herni_pole:
        return('X')

    elif '000' in herni_pole:
        return('0')

    elif '-' not in herni_pole:
        return('!')

    else:
        return(herni_pole)




def tah (pole, cislo_policka, symbol):

    v_result = pole[:int(cislo_policka)] + symbol + pole[int(cislo_policka) + 1:]

    return(v_result)



#from tah import tah

def tah_hrace (pole, pozice):
    print("Cisla poli: 01234567890123456789")
    print("                      1111111111")

    if pozice < 0:
        #print(back.RED + style.BOLD + 'Pozice nemuze mit zapornou hodnotu! Zkus jeste ' + style.RESET)
        raise ValueError('Pozice nemuze mit zapornou hodnotu! Zkus jeste ')
        return
    elif pozice > 19:
        print('Je to prilis velke cislo drz se rozmezi 0 az 19! Zkus jeste ')
        raise ValueError('Je to prilis velke cislo drz se rozmezi 0 az 19! Zkus jeste ')
        return
    elif pole[int(pozice)] != '-':
        print('Tato pozice je obsazena! Zkus jeste ')
        raise ValueError('Tato pozice je obsazena! Zkus jeste ')
        return
    else:
        return(tah(pole, pozice,'X'))


def tah_pocitace(pole):


    #Am I a winner?

    v_v_pole = pole.replace('0-0','000')

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()

    v_v_pole = pole.replace('-00','000')

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()

    v_v_pole = pole.replace('00-','000')

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()



    #analyze X

    v_v_pole = pole.replace('X-X','X0X')

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()

    v_v_pole = pole.replace('-X','0X')

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()

    v_v_pole = pole.replace('X-','X0')

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()



    if 'X' in pole:
        v_position0 = pole.index('X')

        if v_position0 in (0,19):
            if pole[int(v_position0+1)] == '-':

                return(pole[:v_position0+1] + '0' + pole[v_position0+2:])
                #return('1')
                exit()

            else:
              if pole[int(v_position0-1)] == '-' and v_position0-1 >=0:

                return(pole[:v_position0-1] + '0' + pole[v_position0+1:])
                #return('2')
                exit()



    #analyze possibility
    if '0' in pole:

        v_position0 = pole.index('0')


        if pole[int(v_position0-1)] == '-':
            return(pole[:v_position0-1] + '0' + pole[v_position0:])
            #return('3')
            exit()

        elif pole[int(v_position0+1)] == '0':

            if v_position0+2 == '-':

                return(pole[:v_position0+1] + '00' + pole[v_position0+1:])
            #    return('4')
                exit()
        else:
            True


    #we are looking for emty position
    while True:
        cislo_policka = random.randrange(len(pole))

        if pole[cislo_policka] == '-':
            return(tah(pole, cislo_policka, '0'))
            exit()


def piskvorky1d():


    i = 0
    v_pole = '-'*20

    while i <20:

        try:
            v_pozice = int(input('Zadej pozici kam to chces dat, musi byt mezi 0 a 19 = '))

            v_pole = tah_hrace(v_pole, v_pozice)

            print(v_pole)

        except ValueError:
            True

        else:
            v_pole = tah_pocitace(v_pole)

            print(v_pole)

            i = i + 1

            v_vyhodnot_res = vyhodnot(v_pole)

            if v_vyhodnot_res in ('X', '0', '!'):
                print(v_vyhodnot_res)
                exit()



piskvorky1d()

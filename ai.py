from zamen import zamen
import random
from tah import tah

def tah_pocitace(pole):


    #Am I a winner


    v_v_pole = pole.replace('0-0','000',1)

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()

    v_v_pole = pole.replace('-00','000',1)

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')s
        exit()

    v_v_pole = pole.replace('00-','000',1)

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()



    #analyze X

    v_v_pole = pole.replace('X-X','X0X',1)

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()

    v_v_pole = pole.replace('-X','0X',1)

    if v_v_pole != pole:
        return(v_v_pole)
        #return('7')
        exit()

    v_v_pole = pole.replace('X-','X0',1)

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


        #else:

        #cislo_policka = random.randrange(len(pole))

        #if pole[cislo_policka] == '-':
        #    return tah(pole, cislo_policka, '0')

    #    if 'XX' in pole:
    #        return(pole[:v_position0+2] + '0' + pole[v_position0+3:])

#v_v = input('Zadej pole ')

#print(tah_pocitace(v_v))

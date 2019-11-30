import random

class LottoNumerot():
    def __init__(self):
        print("LottoNumerot instance luotu!")
        self.arvotut_numerot = []
        self.pelaajan_numerot = []

    def arvo_numerot(self):
        print("Arvon numeroita...")
        laskuri = 1
        while laskuri <= 7:
            numero = random.randint(1, 41)
            if (numero in self.arvotut_numerot):
                pass
            else:
                self.arvotut_numerot.append(numero)
                laskuri += 1

        self.arvotut_numerot.sort()
        print(self.arvotut_numerot)


    def kysy_numerot(self):
        print("Pelaajan numerot...")
        laskuri = 1
        while laskuri <= 7:
            numero = int(input('Kirjoita lottonumero: '))
            if(numero in self.pelaajan_numerot):
                print('Annoit jo aikaisemmin tuon numeron! Anna uusi!\n')
            elif(numero > 0 and numero < 41):
                self.pelaajan_numerot.append(numero)
                laskuri += 1
            else:
                print("Lottonumerot ovat 1-40. Kirjoita uusi numero!\n")

        self.pelaajan_numerot.sort()
        print(self.pelaajan_numerot)


    def tarkista_numerot(self):
        print("Tarkistan numeroita...")
        oikein_list = []
        for element in self.arvotut_numerot:
            if element in self.pelaajan_numerot:
                oikein_list.append(element)

        print("Sinulla oli %d oikein!" % len(oikein_list))



l = LottoNumerot()
l.arvo_numerot()
l.kysy_numerot()
l.tarkista_numerot()


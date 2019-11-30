#
# Kirjasto / Library
#

class Asiakas:
    def __init__(self, name):
        self.name = name
        self.laina = []

    def lainaa_kirja(self, kirja):
        if kirja.status == 0: # jos kirja on kirjastossa
            if len(kirja.varaaja) > 0:
                if self == kirja.varaaja[0]:
                    self.laina.append(kirja)
                    kirja.status = 1 # lainassa
                    kirja.vapauta_varauksesta(self)
                    print(self.name + "  on lainannut kirjan " + kirja.nimi)
                else:
                    print("kirja on varattu toiselle")
            else:    
                self.laina.append(kirja)
                kirja.status = 1 # lainassa
                print(self.name + "  on lainannut kirjan " + kirja.nimi)
        else:
            print("Kirja on lainassa.")
        
    def palauta_kirja(self, kirja):
        if kirja in self.laina:
            self.laina.remove(kirja)
            kirja.status = 0 # kirjastossa
            print(self.name + "  on palauttanut kirjan " + kirja.nimi)


class Kirja:
    def __init__(self, nimi, tekija):
        self.nimi = nimi
        self.tekija = tekija
        self.status = 0 # kirjastossa
        # self.varattu = False
        self.varaaja = []
        
    def laita_varaukseen(self, asiakas):
        # self.varattu = True
        if asiakas not in self.varaaja:
            self.varaaja.append(asiakas)

    def vapauta_varauksesta(self, asiakas):
        # self.varattu = False
        if asiakas in self.varaaja:
            self.varaaja.remove(asiakas)


arosusi = Kirja("Arosusi", "Herman Hesse")
kolmemuskettisoturia = Kirja("Kolme musketti soturia", "Aleksandre Dumas")
seitsemanveljesta = Kirja("Seitsemän veljestä", "Aleksis Kivi")

sari = Asiakas("Sari")
sari.lainaa_kirja(arosusi)
sari.palauta_kirja(arosusi)

janne = Asiakas("Janne")
# arosusi.laita_varaukseen(janne)
# arosusi.laita_varaukseen(sari)
# sari.lainaa_kirja(arosusi)
# janne.lainaa_kirja(arosusi)
# sari.lainaa_kirja(arosusi)
# janne.palauta_kirja(arosusi)
sari.lainaa_kirja(arosusi)
sari.lainaa_kirja(seitsemanveljesta)

asiakaslista = {sari.name : sari, janne.name : janne}
kirjalista = {arosusi.nimi : arosusi, seitsemanveljesta.nimi : seitsemanveljesta}
  
lopetus = False
while lopetus == False:
    print( "1. Anna asiakkaan nimi (Sari tai Janne)")
    print( "2. Näytä asiakkaan lainat")
    print( "3. Lainaa kirja")
    print( "4. Palauta kirja")
    print( "5. Varaa kirja")
    print( "6. Poista varaus kirjasta")
    print( "7. Näytä asiakkaan kirjojen varaukset")
    print( "8. Lopeta")
    
    valinta = input()
    if valinta == "1":     
        print("Menu 1 on valittu")
        print("Anna asiakkaan nimi")
        asnimi = str(input())
        asiakas = asiakaslista[asnimi]
    if valinta == "2":
        print("Menu 2 on valittu")
        print(asiakas.name + "n lainat ovat: ")
        for iter in asiakas.laina:
            print(iter.nimi)
    if valinta == "3":
        print("Menu 3 on valittu")
        print("Anna lainattavan kirjan nimi: ")
        lainattava = input()
        asiakas.lainaa_kirja(kirjalista[lainattava])
    if valinta == "4":
        print("Menu 4 on valittu")
        print("Anna palautettavan kirjan nimi: ")
        palautettava = input()
        asiakas.palauta_kirja(kirjalista[palautettava])
    if valinta == "5":
        print("Menu 5 on valittu")
        print("Anna varattavan kirjan nimi: ")
        varattava = input()
        kirjalista[varattava].laita_varaukseen(asiakas)
    if valinta == "6":
        print("Menu 6 on valittu")
        print("Anna varatun kirjan nimi, jonka varaus perutaan: ")
        varattu = input()
        kirjalista[varattu].vapauta_varauksesta(asiakas)
    if valinta == "7":
        print("Menu 7 on valittu")
        print(asiakas.name + "n varaukset ovat: ")
        for key, kirja in kirjalista.items():
            for iter in kirja.varaaja:
                if iter.name == asiakas.name:
                    print(kirja.nimi)
    if valinta == "8":
        print("Lopetus")
        lopetus = True

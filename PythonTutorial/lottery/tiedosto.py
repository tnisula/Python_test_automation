#
#    File exercise
#

# Importoidut modulit
import json

# avaa tiedosto
# lue tiedostosta
try:
    f = open("pythondata.json")
    jsonstring = f.read()
except:
    print("Tiedoston avaus / luku failaa!")
else:
    print("Tiedosto avattu ja luettu")
    print(jsonstring)
finally:
    f.close()
	
olio = json.loads(jsonstring)

# muutetaan tietoa
lista = olio["avain"]
lista[0]["nimi"] = "Pekka"
olio["avain"][0]["nimi"] = "Simo"
print(lista)

# tallenna tiedosto
jsonstring = json.dumps(olio)
try:
    f = open("pythondata.json", "w")
    f.write(jsonstring)
except:
    print("Tiedoston tallennus failaa!")
finally:
    f.close()


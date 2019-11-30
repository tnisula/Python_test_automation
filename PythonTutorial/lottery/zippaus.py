import glob
import zipfile

tiedostot = glob.glob("*.py")
print(tiedostot)

with zipfile.ZipFile("tiistai.zip", "w") as myzip:
    for iter in tiedostot:
        myzip.write(iter)
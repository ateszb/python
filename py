# 1. A karakterek_szama(fname)       függvény visszatér a fájlban levő karakterek számával. ('\n karakterekkel eggyütt')
# 2. A szavak_szama(fname)           függvény visszatér a fname) fájlban levő szavak számával.
# 3. A sorok_szama(fname)            függvény visszatér a  fájlban levő sorok számával.
# 4. Az r_betuk_szama(fname)         függvény visszatér a  fájlban levő 'r' betük számával.
# 5. A lorem_szavak_szama(fname)     függvény visszatér a  fájlban levő "lorem" szavak számával.
# 6. A legritkabb_karakter(fname)    függvény visszatér a  fájlban legritkábban előforduló karakterrel.
# 7. A leghosszabb_sor_hossza(fname) függvény visszatér a  fájlban levő leghosszabb sor hosszával.

# 1
def karakterek_szama(fname):
    with open(fname) as f:
        return len(f.read())
# 2
def szavak_szama(fname):
    with open(fname) as f:
        return len(f.read().split())
# 3        
def sorok_szama(fname):
    with open(fname) as f:
        return len(f.readlines())
# 4
def r_betuk_szama(fname):
    with open(fname) as f:
        return f.read().count('r')
# 5
def lorem_szavak_szama(fname):
    with open(fname) as f:
        return f.read().count('lorem')

# 6
def leggyakoribb_karakter(fname):
    with open(fname) as f:
        stat = dict()
        for betu in f.read():
            stat[betu] = stat.get(betu, 0) + 1
        print(stat)
        return max(stat, key=stat.get)
# 7
def leghosszabb_sor_hossza(fname):
    with open(fname) as f:
        return len(  max(f.readlines(), key=len )  )

'''
Európa, Python_3. feladatsor
9 részfeladat 18 pont

A feladat kezdetekor, majd minden feladat során futtatni kell a unit teszteket.
(pipa a baloldali menüsávon, majd a kék Run tests gomb megnyomása)
A feladat beadásához a képernyő jobb felső részén a SUBMIT gombot kell megnyomni.
A main.py fájlt nem szabad módosítani.
A feladat megoldása során az eu.py fájlban kell létrehozni a kért Eu osztályt és a függvényeket.

Feladatok: 

1. Osztály létrehozása Eu: néven az eu.py fájlban
2. A forrast_beolvas_feldolgoz_listaval_visszater(fname) függvény létrehozása az eu.py fájlban. Bemenő paraméter a fájl neve.
3. A tagallamok_szama_2018(lista) függvény létrehozása az eu.py fájlban.
4. A csatlakozasok_szama_az_evben(lista) függvény létrehozása az eu.py fájlban.
5. A csatlakozasok_szama_a_honapban(lista) függvény létrehozása az eu.py fájlban.
6. Az orszag_csatlakozasi_datuma(lista) függvény létrehozása az eu.py fájlban.
7. Az utoljara_csatlakozott_orszag(lista) függvény létrehozása az eu.py fájlban.
8. A legtobb_csatlakozas_honapja(lista) függvény létrehozása az eu.py fájlban.
9. A tagallamok_szama_az_adott_evben(lista) függvény létrehozása az eu.py fájlban.
'''



#1. Az Eu osztály létrehozása:
class Eu:
  def __init__(self,sor):
    orszag, datum = sor.strip().split(";")
    self.orszag = orszag
    self.datum  = datum
    self.ev     = int(datum[ : 4])
    self.honap  = int(datum[5: 7])
    self.nap    = int(datum[8:10])
      
# -------------------------------------------------------
# 2. Forrast beolvas, feldolgoz listaval visszater. Bemenő paraméter a fájl neve.
def forrast_beolvas_feldolgoz_listaval_visszater(fname):
    with open(fname,"r",encoding="utf8") as f:
        return [ Eu(sor) for sor in f ]
          
# -------------------------------------------------------
# 3. A tagállamok száma 2018-ban a BREXIT előtt, tehát Az Egyesült királyság még tag.
def tagallamok_szama_2018(lista):
    return len(lista)

#--------------------------------------------------------

# 4. 
def csatlakozasok_szama_az_evben(lista, ev):
    return len( [sor for sor in lista if sor.ev == ev] )
    
#--------------------------------------------------------

# 5.
def csatlakozasok_szama_a_honapban(lista, honap):
    return sum( [1 for sor in lista if sor.honap == honap] )
   
#--------------------------------------------------------

# 6. 
def orszag_csatlakozasi_datuma(lista, orszag):
    datum = [sor.datum for sor in lista if sor.orszag == orszag]
    if datum:
        return datum[0]
    else:
        return None
    
#--------------------------------------------------------
# 7.
def utoljara_csatlakozott_orszag(lista):
    return max(lista, key=lambda x: x.datum).orszag

#--------------------------------------------------------

# 8.
def legtobb_csatlakozas_honapja(lista):
    honapok = dict()
    for sor in lista:
        honapok[sor.honap] = honapok.get(sor.honap, 0) + 1
    return max(honapok, key=honapok.get)

#--------------------------------------------------------

# 9.
def tagallamok_szama_az_adott_evben(lista, ev):
    evek = dict()
    for sor in lista:
        if sor.ev <= ev:
            evek[sor.ev] = evek.get(sor.ev, 0) + 1
    return sum(evek.values())

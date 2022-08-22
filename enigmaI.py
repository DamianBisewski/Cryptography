
#Here the Stecker is implemented. The przewodySteckerbrett variable is a dictionary where letters are swapped.
class Steckerbrett:
    def __init__(self, przewodySteckerbrett):
        self.przewodySteckerbrett = przewodySteckerbrett

    def zamien(self, wartoscWejsciowa):
        if wartoscWejsciowa in self.przewodySteckerbrett:
            return self.przewodySteckerbrett[wartoscWejsciowa]
        else:
            return wartoscWejsciowa

#This is the rotor. The wiring is implemented as three dictionaries, according to EnigmaI's wiring in all the three rotors.
class Wirnik:
    przewody = [{
        "A":"E", "B":"K", "C":"M", "D":"F", "E":"L", "F":"G", "G":"D", "H":"Q",
        "I":"V", "J":"Z", "K":"N", "L":"T", "M":"O", "N":"W", "O":"Y", "P":"H",
        "Q":"X", "R":"U", "S":"S", "T":"P", "U":"A", "V":"I", "W":"B", "X":"R",
        "Y":"C", "Z":"J"}, {
        "A":"A", "B":"J", "C":"D", "D":"K", "E":"S", "F":"I", "G":"R", "H":"U",
        "I":"X", "J":"B", "K":"L", "L":"H", "M":"W", "N":"T", "O":"M", "P":"C",
        "Q":"Q", "R":"G", "S":"Z", "T":"N", "U":"P", "V":"Y", "W":"F", "X":"V",
        "Y":"O", "Z":"E"}, {
        "A":"B", "B":"D", "C":"F", "D":"H", "E":"J", "F":"L", "G":"C", "H":"P",
        "I":"R", "J":"T", "K":"X", "L":"V", "M":"Z", "N":"N", "O":"Y", "P":"E",
        "Q":"I", "R":"W", "S":"G", "T":"A", "U":"K", "V":"M", "W":"U", "X":"S",
        "Y":"Q", "Z":"O"
        }
    ]
    def __init__(self, nrWirnika):
        self.wirnikMapowanie = self.przewody[nrWirnika-1]
        self.wirnikMapowanieOdwrotne = {v: k for k, v in self.wirnikMapowanie.items()}
    def wirnikZastapienie(self, wartoscWejsciowa):    #Here the letters are substituted according to the rotors' wiring.
        return self.wirnikMapowanie[wartoscWejsciowa]
    def wirnikZastapienieOdwrotne(self, wartoscWejsciowa):    #The letters are substituted again after having passed through the reflector
        return self.wirnikMapowanieOdwrotne[wartoscWejsciowa]

class ZestWirnikow:     #The set of three rotors
    alfabet = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
    def __init__(self, off1, off2, off3):       #The offsets and rotors are initialized
        self.wirnikStep0 = off1
        self.wirnikStep1 = off2
        self.wirnikStep2 = off3
        self.wirnikA = Wirnik(1)
        self.wirnikB = Wirnik(2)
        self.wirnikC = Wirnik(3)
    def zakodujWirniki(self, literaWejsciowa):          #The letters are substituted during moving inside rotors
        self.wirnikStep2 += 1
        literaWejsciowa = self.inputTlumacz(literaWejsciowa, self.wirnikStep2)
        self.outputC = self.outputTlumacz(self.wirnikC.wirnikZastapienie(literaWejsciowa), self.wirnikStep2)
        self.outputC = self.inputTlumacz(self.outputC, self.wirnikStep1)
        self.outputB = self.outputTlumacz(self.wirnikB.wirnikZastapienie(self.outputC), self.wirnikStep1)
        self.outputB = self.inputTlumacz(self.outputB, self.wirnikStep0)
        self.outputA = self.outputTlumacz(self.wirnikA.wirnikZastapienie(self.outputB), self.wirnikStep0)
        return self.outputA
    def zakodujWirnikiOdwrotnie(self, literaWejsciowa):
        literaWejsciowa = self.inputTlumacz(literaWejsciowa, self.wirnikStep0)
        self.outputA = self.outputTlumacz(self.wirnikA.wirnikZastapienieOdwrotne(literaWejsciowa), self.wirnikStep0)
        self.outputA = self.inputTlumacz(self.outputA, self.wirnikStep1)
        self.outputB = self.outputTlumacz(self.wirnikB.wirnikZastapienieOdwrotne(self.outputA), self.wirnikStep1)
        self.outputB = self.inputTlumacz(self.outputB, self.wirnikStep2)
        self.outputC = self.outputTlumacz(self.wirnikC.wirnikZastapienieOdwrotne(self.outputB), self.wirnikStep2)
        return self.outputC
    def outputTlumacz(self, wartoscWejsciowa, step):        #In these functions the rotors are moved in order with offsets
        index = self.alfabet.index(wartoscWejsciowa) - step
        while index < 0:
            index += 26
        return self.alfabet[index]
    def inputTlumacz(self, wartoscWejsciowa, step):
        index = self.alfabet.index(wartoscWejsciowa) + step
        while index > 25:
            index -= 26
        return self.alfabet[index]

class Reflektor:        #The reflector. After going through three rotors we come here. The letters are moved through the reflector and go back to the rotors in inverted rotor order.
    przewody = {
    "B": {
        "A":"Y", "B":"R", "C":"U", "D":"H", "E":"Q", "F":"S", "G":"L", "H":"D",
        "I":"P", "J":"X", "K":"N", "L":"G", "M":"O", "N":"K", "O":"M", "P":"I",
        "Q":"E", "R":"B", "S":"F", "T":"Z", "U":"C", "V":"W", "W":"V", "X":"J",
        "Y":"A", "Z":"T"},
    "C": {
        "A":"F", "B":"V", "C":"P", "D":"J", "E":"I", "F":"A", "G":"O", "H":"Y",
        "I":"E", "J":"D", "K":"R", "L":"Z", "M":"X", "N":"W", "O":"G", "P":"C",
        "Q":"T", "R":"K", "S":"U", "T":"Q", "U":"S", "V":"B", "W":"N", "X":"M",
        "Y":"H", "Z":"L"}}
    def __init__(self, reflektorTyp):
        self.reflektorSlownik = self.przewody[reflektorTyp]
    def odwroc(self, wartoscWejsciowa):
        return self.reflektorSlownik[wartoscWejsciowa]

class Enigma:         #the Enigma machine with the rotors, reflector and Steckerbrett.
    def __init__(self, zamiany, off1, off2, off3, reflektor):
        self.zestwirnikow1 = ZestWirnikow(off1, off2, off3)
        self.reflektor1 = Reflektor(reflektor)
        self.stecker1 = Steckerbrett(zamiany)

    def encrypt(self, wartoscWejsciowa):   #Encryption
        wartoscWejsciowa = wartoscWejsciowa.upper()
        wartoscWejsciowa = self.stecker1.zamien(wartoscWejsciowa)
        self.przed = self.zestwirnikow1.zakodujWirniki(wartoscWejsciowa)
        self.po = self.reflektor1.odwroc(self.przed)
        return self.stecker1.zamien(self.zestwirnikow1.zakodujWirnikiOdwrotnie(self.po))

zamiany = dict()        #the input - what pairs in Steckerbrett
liczbapar = int(input("Podaj liczbe par liter do zamiany, maksymalnie 13: "))
litery = set()
for i in range(0, liczbapar):
    a = input("Podaj pierwsza litere: ")
    b = input("Podaj druga litere: ")
    if a in litery:
        print("Ta litera juz jest w zamianach")
    else:
        if b in litery:
            print("Ta litera juz jest w zamianach")
        else:
            zamiany[a] = b
            zamiany[b] = a
            litery.add(a)
            litery.add(b)
plain = input("Podaj tekst do zakodowania: ")    #The text we want to encode
a = int(input("Podaj offset pierwszego wirnika (od 0 do 25): "))   #the rotor offsets
b = int(input("Podaj offset drugiego wirnika (od 0 do 25): "))
c = int(input("Podaj offset trzeciego wirnika (od 0 do 25): "))
refl = input("Podaj rodzaj reflektora (B lub C): ")       #the reflector type
if refl != "B" and refl != "C":
    print("Nie istnieje taki typ reflektora")
else:                          #if rotor offsets outside 0-25 range we do modulo on them
    if a < 0 or a > 25:
        a = a%26
    if b < 0 or b > 25:
        b = b%26
    if c < 0 or c > 25:
        c = c%26
    enigma1 = Enigma(zamiany, a, b, c, refl)         #encryption of the given text
    encr = ""
    for i in range(len(plain)):
        encr = encr + enigma1.encrypt(plain[i])
    print(encr)                                  #encrypted text printed
    enigma2 = Enigma(zamiany, a, b, c, refl)     #decryption
    decr = ""
    for i in range(len(encr)):
        decr = decr + enigma2.encrypt(encr[i])    #as Enigma is reversible decryption is basically encryption of the encrypted text with the same reflector, Steckerbrett and rotor offsets
    print(decr)

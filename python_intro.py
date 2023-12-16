print("Hello, Django girls")
if 3 > 2: print("It works!")
if 5 > 2: print("5 ist wirklich größer als 2")
else: print("5 ist nicht größer als 2")
name = "Sonja"
if name == "Ola":
    print("Hey Ola")
elif name == "Sonja": 
    print("Hey Sonja!")
else: 
    print("Hey anonymus!")        
volume = 57
if volume < 20:
    print("Das ist etwas leise.")
elif 20 <= volume < 40:
    print("Das ist gut für Hintergrund-Musik.")
elif 40 <= volume < 60:
    print("Perfect, ich kann alle Details hören.")
elif 60 <= volume < 80:
    print("Gut für Partys.")
elif 80 <= volume < 100:
    print("Etwas laut!")
else:
    print("Mir tun die Ohren etwas weh! : (")
if volume < 20 or volume > 80:
    volume = 50
    print("So ist es besser!")  
def hallo():
    print("Halli-hallo!")
    print("Wie geht`s?") 
hallo()    
def hallo(name):
    if name == "Ola":
        print("Hallo Ola!")
    elif name == "Sonja":
        print("Hallo Sonja!")
    else:
        print("Hallo Unbekannte(r)!")
hallo("Ola")
hallo("Sonja")
hallo("Charlotte")
def hallo(name):
    print("Hallo " + name + "!")
hallo("Rachel")
girls = ["Rachel", "Monica", "Phoebe", "Ola", "You"]
for name in girls:
    hallo(name)
    print("Nächstes Mädchen")
for i in range(1, 6):
    print(i)    

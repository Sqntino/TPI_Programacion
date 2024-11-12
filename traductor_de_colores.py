#Seleccionar idioma al que desea traducir
ingles = 1
frances = 2
italiano = 3
portugues = 4

#Listas de colores en los distintos idiomas
colores_ingles = ["red", "blue", "yellow", "black", "white", "brown", "grey", "green", "orange", "purpple", "pink"]
colores_frances = ["rouge", "bleu", "jaune", "noir", "blanc", "marron", "gris", "vert", "orange", "violet", "rose"]
colores_italiano = ["rosso", "blu", "giallo", "nero", "bianco", "marrone", "grigio", "verde", "arancione", "viola", "rosa"]
colores_portugues = ["vermelho", "azul", "amarelo", "preto", "branco", "marrom", "cinza", "verde", "laranja", "roxo", "rosa"]

#Seleccion de idioma
print("Idioma a traducir: \n\n-Ingles:1\n-Frances:2\n-Italiano:3\n-Portugues:4")
print()
idioma = int(input("Escriba el numero correspondiente al idioma que desea traducir: "))
print()

#En caso de que un idioma no este disponible
while idioma <= 0 or idioma > 4: 
    idioma = int(input("Esta opción no está en la lista, ingrese un número disponible: "))

#Eleccion de colores
if idioma == ingles:
    print("Usted ha seleccionado el idioma inglés")
    print()
    print("0:rojo\n1:azul\n2:amarillo\n3:negro\n4:blanco\n5:marron\n6:gris\n7:verde\n8:naranja\n9:purpura\n10:rosa")
    print()
    color = int(input("Escriba el numero del color que desea traducir: "))
    while color <= 0 or color >10:
        color = int(input("El color no esta disponible, ingrese un color que se encuentre en la lista: "))
    print()
    print(colores_ingles[color])
    
elif idioma == frances:
    print("Usted ha seleccionado el idioma francés")
    print("0:rojo\n1:azul\n2:amarillo\n3:negro\n4:blanco\n5:marron\n6:gris\n7:verde\n8:naranja\n9:purpura\n10:rosa")
    color = int(input("Escriba el numero del color que desea traducir: "))
    while color <= 0 or color > 10:
        color = int(input("El color no esta disponible, ingrese un color que se encuentre en la lista: "))
    print()
    print(colores_frances[color])

elif idioma == italiano:
    print("Usted ha seleccionado el idioma italiano")
    print("0:rojo\n1:azul\n2:amarillo\n3:negro\n4:blanco\n5:marron\n6:gris\n7:verde\n8:naranja\n9:purpura\n10:rosa")
    color = int(input("Escriba el numero del color que desea traducir: "))
    while color <= 0 or color > 10:
        color = int(input("El color no esta disponible, ingrese un color que se encuentre en la lista: "))
    print()
    print(colores_italiano[color])
    
elif idioma == portugues:
    print("Usted ha seleccionado el idioma portugues")
    print("0:rojo\n1:azul\n2:amarillo\n3:negro\n4:blanco\n5:marron\n6:gris\n7:verde\n8:naranja\n9:purpura\n10:rosa")
    color = int(input("Escriba el numero del color que desea traducir: "))
    while color <= 0 or color > 10:
        color = int(input("El color no esta disponible, ingrese un color que se encuentre en la lista: "))
    print()
    print(colores_portugues[color])

print()
print("GENIAL! sigue aprendiendo los colores en muchos idiomas con este juego!")
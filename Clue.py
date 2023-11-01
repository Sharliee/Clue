import json
import random
respuestas_correctas=0

def elegir_testimonio(buscar,tipo):
    global respuestas_correctas
    equivocado="No dedujiste correctamente"
    correcto="Dedujiste correctamente"
    if tipo == 0:
        if buscar == 1:
            return testimonio1
        if buscar == 2:
            return testimonio2
        if buscar == 3:
            return testimonio3
        if buscar == 4:
            return testimonio4
        if buscar == 5:
            return sospechoso
        if buscar == 6:
            return lugar
        if buscar == 7:
            return arma
    else:
        if buscar in (1,2,3,4):
            return equivocado
        if buscar in (5,6,7):
            respuestas_correctas=respuestas_correctas+1
            return correcto

def cargar_base_de_datos(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data  

def buscar(sospechosos,revisar,tipo):
    revisar=int(revisar)-1
    if 0 <= revisar < len(sospechosos):
        objetivo=sospechosos[revisar]
        if objetivo in testimonios:
            print(elegir_testimonio(testimonios[objetivo],tipo))
        y=1
        return y
    else:
        print("\nInsertar el numero de la opcion\n")
        y=0
        return y

def investigar_personaje():
    y=0
    sospechosos=list(personajes.keys())
    
    while y==0:
        revisar=input("\nSelecciona un sospechoso a interrogar: \n1. Carlos Riveramelo\n2. Aldo Estrada\n3. Olaf Mendoza\n4. Sergio Fernandez\n5. Antonio Chong\n\nTu elección:")
        y=buscar(sospechosos,revisar,0)
    
def investigar_locacion():
    y=0
    sospechosos=list(locaciones.keys())
    
    while y==0:
        revisar=input("\nSelecciona un lugar a investigar: \n1. Estudio de grabación\n2. Sala de ensayo\n3. Dormitorios\n4. Piscina\n5. Cochera\n\nTu elección:")
        y=buscar(sospechosos,revisar,0)
    
    
def investigar_arma():
    y=0
    sospechosos=list(armas.keys())
    
    while y==0:
        revisar=input("\nSelecciona un instrumento a inspeccionar: \\n1. Tuba\n2. Acordeón\n3. Trompeta\n4. Clarinete\n5. Tarola\n\nTu elección:")
        y=buscar(sospechosos,revisar,0)
    

def alazar_borrar_personaje(numero):
    borrar=random.choice(list(personajes2.keys()))
    del informacion2["evidencia"][0]["personajes"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_locacion(numero):
    borrar=random.choice(list(locaciones2.keys()))
    del informacion2["evidencia"][1]["locaciones"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_arma(numero):
    borrar=random.choice(list(armas2.keys()))
    del informacion2["evidencia"][2]["armas"][borrar]
    testimonios[borrar]=numero
    return borrar

informacion: dict = cargar_base_de_datos('clue_base_de_datos.json')

#informacion 2 se va a terminar borrando
informacion2: dict = cargar_base_de_datos('clue_base_de_datos.json')


#Se cambio un valor de cada categoria a True para denotar el asesino, el lugar y el arma#
personajes = informacion['evidencia'][0]['personajes']
asesino = random.choice(list(personajes.keys()))
informacion["evidencia"][0]["personajes"][asesino] = True    

locaciones = informacion['evidencia'][1]['locaciones']
escena_crimen = random.choice(list(locaciones.keys()))
informacion["evidencia"][1]["locaciones"][escena_crimen] = True    

armas = informacion['evidencia'][2]['armas']
arma_homicida = random.choice(list(armas.keys()))
informacion["evidencia"][2]["armas"][arma_homicida] = True    
##


#Se crean los testimonios de los inocentes, y la informacion del culpable, el arma y el lugar#
testimonios={}

personajes2 = informacion2['evidencia'][0]['personajes']
locaciones2 = informacion2['evidencia'][1]['locaciones']
armas2 = informacion2['evidencia'][2]['armas']

sospechoso="\n"+asesino+" no se presentó a hacer testimonio.\n"
testimonios[asesino]=5
lugar="\nNadie recuerda haber estado en "+escena_crimen+"\n"
testimonios[escena_crimen]=6
arma="\nNadie recuerda haber visto o usado el/la "+arma_homicida+"\n"
testimonios[arma_homicida]=7
final_resultado="\n"+asesino+" mato al Ing. Gutierrez usando "+arma_homicida+" en la/el "+escena_crimen+"\n"

del informacion2["evidencia"][0]["personajes"][asesino]
del informacion2["evidencia"][1]["locaciones"][escena_crimen]
del informacion2["evidencia"][2]["armas"][arma_homicida]

testimonio1= "\n"+alazar_borrar_personaje(1)+" estaba en "+alazar_borrar_locacion(1)+" usando "+alazar_borrar_arma(1)+"\n"
testimonio2= "\n"+alazar_borrar_personaje(2)+" estaba en "+alazar_borrar_locacion(2)+" usando "+alazar_borrar_arma(2)+"\n"
testimonio3= "\n"+alazar_borrar_personaje(3)+" estaba en "+alazar_borrar_locacion(3)+" usando "+alazar_borrar_arma(3)+"\n"
testimonio4= "\n"+alazar_borrar_personaje(4)+" estaba en "+alazar_borrar_locacion(4)+" usando "+alazar_borrar_arma(4)+"\n"
##


print("¡Oh, no! ¡Ha habido un asesinato en las inmediaciones del famoso grupo musical 'La Arrolladora del Ingeniero Gutierrez'. \n")
print("Es sabido que la victima, Isaac Gutiérrez, se ganó muchos enemigos cuando alcanzó el éxito.\n")
print("Ayuda a encontrar al asesino interrogando a los integrantes de la banda, para así descrubir quién fue, dónde lo hizo y qué utilizó para hacerlo.")
print("Tienes 5 intentos para investigar a la persona, arma o locación. Una vez usados tus intentos, deberás decidir tus opciones.\n")

x=5

while x!=0:
    a_investigar= input("Quedan "+str(x)+" intentos\nSelecciona que quieres investigar\n 1. Integrante\n 2. Locacion\n 3. Instrumento\n\nTu elección:")
    
    switch = {
        '1': investigar_personaje,
        '2': investigar_locacion,
        '3': investigar_arma
    }
    
    if a_investigar in switch:
        switch[a_investigar]()
        x=x-1
    else:
        print("Opción no válida")
        
print("\nYa no tienes más intentos. Ahora, usa tus habilidades detectivezcas de deducción para elegir al culpable, su arma y el lugar del asesinto\n")

y=0

while y==0:
    final_culpable=input("Elige un culpable: \n1. Carlos Riveramelo\n2. Aldo Estrada\n3. Olaf Mendoza\n4. Sergio Fernandez\n5. Antonio Chong\n")
    y=buscar(list(personajes.keys()),final_culpable,1)
    
y=0
while y==0:
    final_lugar=input("Elige el lugar del asesinato: \n1. Estudio de grabación\n2. Sala de ensayo\n3. Dormitorios\n4. Piscina\n5. Cochera\n")
    y=buscar(list(locaciones.keys()),final_lugar,1)
    
y=0
while y==0:
    final_arma=input("Elige el instrumento homicida: \n1. Tuba\n2. Acordeón\n3. Trompeta\n4. Clarinete\n5. Tarola\n")
    y=buscar(list(armas.keys()),final_arma,1)
   
print("\n"+final_resultado+"\n")
print("Deduciste "+str(respuestas_correctas)+" parte(s) del asesinato")
if respuestas_correctas == 3:
    print("\n¡Felicidades! has resuelto el asesinato. ")
else:
    print("\nLo sentimos, no has logrado dar con el asesino.")
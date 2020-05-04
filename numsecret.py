import random
import json
import datetime

secret = random.randint(1, 30)
intentos = 0
numeros_fallos = []

usuario = input("Introduce tu nombre de usuario: ")

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Puntuaciones Totales almacenadas: " + str(score_list))

# sort score list by attempts
lista_ordenada = sorted(score_list, key=lambda s: s["intentos"])[:3]
# sort dict list by key

for score_dict in lista_ordenada:
    puntuacion_txt = "El Jugador {0} tiene {1} intentos con fecha: {2}, nºsecreto: {3}, erroneos: {4}".format(score_dict.get("jugador"),
                                                                                                         str(score_dict.get("intentos")),
                                                                                                         score_dict.get("date"),
                                                                                                         score_dict.get("num_secreto"),
                                                                                                         score_dict.get("fallos"))

    print(puntuacion_txt)

while True:
    num_usuario = int(input("Introduzca el numero secreto (Entre 1 y 30)"))
    intentos += 1

    if num_usuario == secret:
        score_list.append({"intentos": intentos, "date": str(datetime.datetime.now()), "jugador": usuario,
                           "fallos": numeros_fallos , "num_secreto": secret})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Enhorabuena acertaste el numero secreto: " + str(secret))
        print("Numero de intentoss: " + str(intentos))

        break

    elif num_usuario > secret:
        print("El numero introducido no es correcto... Prueba con un numero mas pequeño")

    elif num_usuario < secret:
        print("El numero introducido no es correcto... Prueba con un numero mas grande")

    numeros_fallos.append(num_usuario)
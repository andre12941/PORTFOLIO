#Contador de partidadas dardo

#Lista de jugadores


print ("Bienvenido al juego de dardos, por favor ingrese el nombre de los jugadores")
player1_name = input("Nombre del jugador 1: ")
player2_name = input("Nombre del jugador 2: ")
player3_name = input("Nombre del jugador 3: ")
player4_name = input("Nombre del jugador 4: ")

# variable que poseen los jugadores, intentos y puntos obtenidos en cada ronda
puntuacion1 = ["puntos1"+"puntos2"+"puntos3"+"puntos4"+"puntos5"+"puntos6"+"puntos7"+"puntos8"+"puntos9"]
puntuacion2 = ["puntos1"+"puntos2"+"puntos3"+"puntos4"+"puntos5"+"puntos6"+"puntos7"+"puntos8"+"puntos9"]         
puntuacion3 = ["puntos1"+"puntos2"+"puntos3"+"puntos4"+"puntos5"+"puntos6"+"puntos7"+"puntos8"+"puntos9"] 
puntuacion4 = ["puntos1"+"puntos2"+"puntos3"+"puntos4"+"puntos5"+"puntos6"+"puntos7"+"puntos8"+"puntos9"] 
puntuacionfija = 121

player1 = {"nombre": player1_name, "intentos": 3, "puntaje":puntuacion1}
player2 = {"nombre": player1_name, "intentos": 3, "puntaje":puntuacion2}
player3 = {"nombre": player1_name, "intentos": 3, "puntaje":puntuacion3}
player4 = {"nombre": player1_name, "intentos": 3, "puntaje":puntuacion4}

players = [player1,player2,player3,player4]



print ("El juego consiste en lanzar 3 dardos por jugador, el jugador que tenga la mayor puntuación gana la partida")

print  ("Comenzoro el juego...")


#primera ronda
    
#puntos primer jugador
print ("Ahora es el turno del jugador {} ".format(player1_name) + " por lo tanto sera el primero en lanzar los dardos")
if player1["intentos"] > 0:
             
    puntos = int(input("Introduce la puntuación obtenida por " + player1_name + ":  "))
    player1["puntos1"]= puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player1_name, player1["puntos1"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player1_name + ":  "))
if puntos <= 121:
    player1["puntos2"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player1_name, player1["puntos2"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player1_name + ":  "))
if puntos <= 121:
    player1["puntos3"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player1_name, player1["puntos3"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player1_name,player1["puntos1"] 
                                                            + player1["puntos2"] + 
                                                            player1["puntos3"]))

#puntos segundo jugador

print ("Ahora es el turno del jugador {}".format(player2_name) + " por lo tanto sera el segundo en lanzar los dardos")
if player2["intentos"] > 0:
    puntos = int(input("Introduce la puntuación obtenida por " + player2_name + ": "))
    player2["puntos1"] = puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player2_name, player2["puntos1"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player2_name + " : "))
if puntos <= 121:
        player2["puntos2"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player2_name, player2["puntos2"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player2_name + ":  "))
if puntos <= 121:
        player2["puntos3"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player2_name, player2["puntos3"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player2_name,player2["puntos1"] 
                                                            + player2["puntos2"] + 
                                                            player2["puntos3"]))

#puntos tercer jugador

print ("Ahora es el turno del jugador {}".format(player3_name) + " por lo tanto sera el tercero en lanzar los dardos")
if player3["intentos"] > 0:
    puntos = int(input("Introduce la puntuación obtenida por " + player3_name + ": "))
    player3["puntos1"] = puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player3_name, player3["puntos1"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player3_name + ": "))
if puntos <= 121:
    player3["puntos2"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player3_name, player3["puntos2"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player3_name + ": "))
if puntos <= 121:
    player3["puntos3"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player3_name, player3["puntos3"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player3_name,player3["puntos1"] 
                                                                            + player3["puntos2"] + 
                                                                            player3["puntos3"]))

#puntos cuarto jugador

print ("Ahora es el turno del jugador {}".format(player4_name) + " por lo tanto sera el cuarto en lanzar los dardos")
if player4["intentos"] > 0:
    puntos = int(input("Introduce la puntuación obtenida por " + player4_name + ": "))
    player4["puntos1"] = puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player4_name, player4["puntos1"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player4_name + ":  "))
if puntos <= 121:
        player4["puntos2"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player4_name, player4["puntos2"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player4_name + ":  "))
if puntos <= 121:
        player4["puntos3"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player4_name, player4["puntos3"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player4_name, player4["puntos1"] 
                                                            + player4["puntos2"] + 
                                                            player4["puntos3"]))
    
    
print (" Los jugadores han terminado de lanzar los dardos en la primera ronda, y su puntuación final es la siguiente: " 
       + " \n El jugador " + player1_name + "  ha obtenido un total de " + str(121 - (player1["puntos1"] + player1["puntos2"] + player1["puntos3"])) + " puntos, " 
       + " \n El jugador " + player2_name + "  ha obtenido un total de " + str(121 - (player2["puntos1"] + player2["puntos2"] + player2["puntos3"])) + " puntos, " 
       + " \n El jugador " + player3_name + "  ha obtenido un total de " + str(121 - (player3["puntos1"] + player3["puntos2"] + player3["puntos3"])) + " puntos, y " 
       + " \n El jugador " + player4_name + "  ha obtenido un total de " + str(121 - (player4["puntos1"] + player4["puntos2"] + player4["puntos3"])) + " puntos.")

# fin de la inicializacion

puntuacion1 = puntuacionfija - (player1["puntos1"] + player1["puntos2"] + player1["puntos3"])
puntuacion2 = puntuacionfija - (player2["puntos1"] + player2["puntos2"] + player2["puntos3"])
puntuacion3 = puntuacionfija - (player3["puntos1"] + player3["puntos2"] + player3["puntos3"])
puntuacion4 = puntuacionfija - (player4["puntos1"] + player4["puntos2"] + player4["puntos3"])


while puntuacion1 <= 0 or puntuacion2 <= 0 or puntuacion3 <= 0 or puntuacion4 <= 0: 
    if puntuacion1 <= 0 : 
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player1_name,puntuacion1) + "fin de la partida" )  
        break  
    elif  puntuacion2 <= 0:
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player2_name,puntuacion2) + "fin de la partida" )
        break
    elif  puntuacion3 <= 0:
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player3_name,puntuacion3) + "fin de la partida" )
        break
    elif  puntuacion4 <= 0:
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player4_name,puntuacion4) + "fin de la partida" )
        break
    elif (puntuacion1 > 0 or puntuacion2 > 0 or puntuacion3 > 0 or puntuacion4 > 0):
        print ("Seguimos con la siguiente ronda ya que ningun jugado ha llegado a 0")
        break
#Segunda Ronda
#puntos primer jugador

print ("Ahora es el turno del jugador {} ".format(player1_name) + " por lo tanto sera el primero en lanzar los dardos")
if player1["intentos"] > 0:
        
    puntos = int(input("Introduce la puntuación obtenida por " + player1_name + ":  "))
player1["puntos4"]= puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player1_name, player1["puntos4"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player1_name + ":  "))
if puntos <= 121:
    player1["puntos5"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player1_name, player1["puntos5"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player1_name + ":  "))
if puntos <= 121:
    player1["puntos6"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player1_name, player1["puntos6"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player1_name,player1["puntos4"] 
                                                                                + player1["puntos5"] + 
                                                                                player1["puntos6"]))

#puntos segundo jugador

print ("Ahora es el turno del jugador {}".format(player2_name) + " por lo tanto sera el segundo en lanzar los dardos")
if player2["intentos"] > 0:
    puntos = int(input("Introduce la puntuación obtenida por " + player2_name + ": "))
    player2["puntos4"] = puntos

    print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player2_name, player2["puntos4"]) + " le quedan 2 intentos")
    puntos = int(input("introduce la puntuación obtenida por " + player2_name + " : "))
if puntos <= 121:
    player2["puntos5"] = puntos
    print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player2_name, player2["puntos5"]) + " le quedan 1 intentos")
    puntos = int(input ("introduce la puntuación obtenida por " + player2_name + ":  "))
if puntos <= 121:
    player2["puntos6"] = puntos

    print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player2_name, player2["puntos6"]) + " le quedan 0 intentos")   

    print ("Los puntos obtenidos por el jugador {} son {}".format(player2_name,player2["puntos4"] 
                                                                                    + player2["puntos5"] + 
                                                                                    player2["puntos6"]))

#puntos tercer jugador

print ("Ahora es el turno del jugador {}".format(player3_name) + " por lo tanto sera el tercero en lanzar los dardos")

if player3["intentos"] > 0:
    puntos = int(input("Introduce la puntuación obtenida por " + player3_name + ": "))
    player3["puntos4"] = puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player3_name, player3["puntos4"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player3_name + ": "))
if  puntos <= 121:
    player3["puntos5"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player3_name, player3["puntos5"]) + " le quedan 1 intentos")

puntos = int(input ("introduce la puntuación obtenida por " + player3_name + ": "))

if puntos <= 121:
    player3["puntos6"] = puntos
    print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player3_name, player3["puntos6"]) + " le quedan 0 intentos")   
    print ("Los puntos obtenidos por el jugador {} son {}".format(player3_name,player3["puntos4"] 
                                                                            + player3["puntos5"] + 
                                                                                                    player3["puntos6"]))

#puntos cuarto jugador

print ("Ahora es el turno del jugador {}".format(player4_name) + " por lo tanto sera el cuarto en lanzar los dardos")
if player4["intentos"] > 0:
    puntos = int(input("Introduce la puntuación obtenida por " + player4_name + ": "))
    player4["puntos4"] = puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player4_name, player4["puntos4"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player4_name + ":  "))
if puntos <= 121:
        player4["puntos5"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player4_name, player4["puntos5"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player4_name + ":  "))
if puntos <= 121:
        player4["puntos6"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player4_name, player4["puntos6"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player4_name, player4["puntos4"] 
                                                            + player4["puntos5"] + 
                                                            player4["puntos6"]))
    
    
print (" Los jugadores han terminado de lanzar los dardos en la primera ronda, y su puntuación final es la siguiente: " 
    + " \n El jugador " + player1_name + "  ha obtenido un total de " + str(121 - (player1["puntos1"] + player1["puntos2"] + player1["puntos3"] + player1["puntos4"] + player1["puntos5"] + player1["puntos6"])) + " puntos, " 
    + " \n El jugador " + player2_name + "  ha obtenido un total de " + str(121 - (player2["puntos1"] + player2["puntos2"] + player2["puntos3"] + player2["puntos4"] + player2["puntos5"] + player2["puntos6"])) + " puntos, " 
    + " \n El jugador " + player3_name + "  ha obtenido un total de " + str(121 - (player3["puntos1"] + player3["puntos2"] + player3["puntos3"] + player3["puntos4"] + player3["puntos5"] + player3["puntos6"])) + " puntos, y " 
    + " \n El jugador " + player4_name + "  ha obtenido un total de " + str(121 - (player4["puntos1"] + player4["puntos2"] + player4["puntos3"] + player4["puntos4"] + player4["puntos5"] + player4["puntos6"])) + " puntos.")
    

puntuacion1 = puntuacionfija - (player1["puntos1"] + player1["puntos2"] + player1["puntos3"] + player1["puntos4"] + player1["puntos5"] + player1["puntos6"])
puntuacion2 = puntuacionfija - (player2["puntos1"] + player2["puntos2"] + player2["puntos3"] + player2["puntos4"] + player2["puntos5"] + player2["puntos6"])
puntuacion3 = puntuacionfija - (player3["puntos1"] + player3["puntos2"] + player3["puntos3"] + player3["puntos4"] + player3["puntos5"] + player3["puntos6"])
puntuacion4 = puntuacionfija - (player4["puntos1"] + player4["puntos2"] + player4["puntos3"] + player4["puntos4"] + player4["puntos5"] + player4["puntos6"])    

while puntuacion1 <= 0 or puntuacion2 <= 0 or puntuacion3 <= 0 or puntuacion4 <= 0 :
    if puntuacion1 <= 0 : 
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player1_name,puntuacion1) + "fin de la partida" )  
        break   
    elif  puntuacion2 <= 0:
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player2_name,puntuacion2) + "fin de la partida" )
        break
    elif  puntuacion3 <= 0:
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player3_name,puntuacion3) + "fin de la partida" )
        break
    elif  puntuacion4 <= 0:
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player4_name,puntuacion4) + "fin de la partida" )
        break
    else:  
        print ("Seguimos con la siguinete ronda, ninguno de los jugadores a llegado a los 0 puntos")
                                    

#Tercera Ronda
#puntos primer jugador
print ("Ahora es el turno del jugador {} ".format(player1_name) + " por lo tanto sera el primero en lanzar los dardos")
if player1["intentos"] > 0:
        
    puntos = int(input("Introduce la puntuación obtenida por " + player1_name + ":  "))
player1["puntos7"]= puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player1_name, player1["puntos7"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player1_name + ":  "))
if puntos <= 121:
    player1["puntos8"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player1_name, player1["puntos8"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player1_name + ":  "))
if puntos <= 121:
    player1["puntos9"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player1_name, player1["puntos9"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player1_name,player1["puntos7"] 
                                                        + player1["puntos8"] + 
                                                        player1["puntos9"]))

#puntos segundo jugador

print ("Ahora es el turno del jugador {}".format(player2_name) + " por lo tanto sera el segundo en lanzar los dardos")
if player2["intentos"] > 0:
    puntos = int(input("Introduce la puntuación obtenida por " + player2_name + ": "))
player2["puntos7"] = puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player2_name, player2["puntos7"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player2_name + " : "))
if puntos <= 121:
        player2["puntos8"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player2_name, player2["puntos8"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player2_name + ":  "))
if puntos <= 121:
        player2["puntos9"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player2_name, player2["puntos9"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player2_name,player2["puntos7"] 
                                                            + player2["puntos8"] + 
                                                            player2["puntos9"]))

#puntos tercer jugador

print ("Ahora es el turno del jugador {}".format(player3_name) + " por lo tanto sera el tercero en lanzar los dardos")
if player3["intentos"] > 0:
    puntos = int(input("Introduce la puntuación obtenida por " + player3_name + ": "))
    player3["puntos7"] = puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player3_name, player3["puntos7"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player3_name + ": "))
if puntos <= 121:
    player3["puntos8"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player3_name, player3["puntos8"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player3_name + ": "))
if puntos <= 121:
    player3["puntos9"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player3_name, player3["puntos9"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player3_name,player3["puntos7"] 
                                                                            + player3["puntos8"] + 
                                                                            player3["puntos9"]))

#puntos cuarto jugador

print ("Ahora es el turno del jugador {}".format(player4_name) + " por lo tanto sera el cuarto en lanzar los dardos")
if player4["intentos"] > 0:
    puntos = int(input("Introduce la puntuación obtenida por " + player4_name + ": "))
    player4["puntos7"] = puntos

print  ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player4_name, player4["puntos7"]) + " le quedan 2 intentos")
puntos = int(input("introduce la puntuación obtenida por " + player4_name + ":  "))
if puntos <= 121:
        player4["puntos8"] = puntos
print ("El jugador {} ha lanzado el dardo y ha obtenido una puntuación de {}".format(player4_name, player4["puntos8"]) + " le quedan 1 intentos")
puntos = int(input ("introduce la puntuación obtenida por " + player4_name + ":  "))
if puntos <= 121:
        player4["puntos9"] = puntos

print ("El jugador {} ha lanzado los dardos y ha obtenido una puntuación de {}".format(player4_name, player4["puntos9"]) + " le quedan 0 intentos")   

print ("Los puntos obtenidos por el jugador {} son {}".format(player4_name, player4["puntos7"] 
                                                            + player4["puntos8"] + 
                                                            player4["puntos9"]))
    
    
print (" Los jugadores han terminado de lanzar los dardos en la primera ronda, y su puntuación final es la siguiente: " 
    + " \n El jugador " + player1_name + "  ha obtenido un total de " + str(121 - (player1["puntos1"] + player1["puntos2"] + player1["puntos3"] + player1["puntos4"] + player1["puntos5"] + player1["puntos6"] + player1["puntos7"] + player1 ["puntos8"] + player1["puntos9"])) + " puntos, " 
    + " \n El jugador " + player2_name + "  ha obtenido un total de " + str(121 - (player2["puntos1"] + player2["puntos2"] + player2["puntos3"] + player2["puntos4"] + player2["puntos5"] + player2["puntos6"] + player2["puntos7"] + player2 ["puntos8"] + player2["puntos9"])) + " puntos, " 
    + " \n El jugador " + player3_name + "  ha obtenido un total de " + str(121 - (player3["puntos1"] + player3["puntos2"] + player3["puntos3"] + player3["puntos4"] + player3["puntos5"] + player3["puntos6"] + player3["puntos7"] + player3 ["puntos8"] + player3["puntos9"])) + " puntos, y " 
    + " \n El jugador " + player4_name + "  ha obtenido un total de " + str(121 - (player4["puntos1"] + player4["puntos2"] + player4["puntos3"] + player4["puntos4"] + player4["puntos5"] + player4["puntos6"] + player4["puntos7"] + player4 ["puntos8"] + player4["puntos9"])) + " puntos.")
    

puntuacion1 = puntuacionfija - (player1["puntos1"] + player1["puntos2"] + player1["puntos3"] + player1["puntos4"] + player1["puntos5"] + player1["puntos6"] + player1["puntos7"] + player1 ["puntos8"] + player1["puntos9"])
puntuacion2 = puntuacionfija - (player2["puntos1"] + player2["puntos2"] + player2["puntos3"] + player2["puntos4"] + player2["puntos5"] + player2["puntos6"] + player2["puntos7"] + player2 ["puntos8"] + player2["puntos9"])
puntuacion3 = puntuacionfija - (player3["puntos1"] + player3["puntos2"] + player3["puntos3"] + player3["puntos4"] + player3["puntos5"] + player3["puntos6"] + player3["puntos7"] + player3 ["puntos8"] + player3["puntos9"])
puntuacion4 = puntuacionfija - (player4["puntos1"] + player4["puntos2"] + player4["puntos3"] + player4["puntos4"] + player4["puntos5"] + player4["puntos6"] + player4["puntos7"] + player4 ["puntos8"] + player4["puntos9"])

while puntuacion1 <= 0 or puntuacion2 <= 0 or puntuacion3 <= 0 or puntuacion4 <= 0 :
    if puntuacion1 <= 0 : 
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player1_name,puntuacion1) + "fin de la partida" )  
        break   
    elif  puntuacion2 <= 0:
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player2_name,puntuacion2) + "fin de la partida" )
        break
    elif  puntuacion3 <= 0:
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player3_name,puntuacion3) + "fin de la partida" )
        break
    elif  puntuacion4 <= 0:
        print ("El jugador {} ha ganado la partida con una puntuacion de {} ".format(player4_name,puntuacion4) + "fin de la partida" )
        break
    else:  
        print ("FIN DE LAS RONDAS")


#FIN DEL JUEGO

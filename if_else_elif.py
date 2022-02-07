# Problema 1
print("¡Cadete! reporte la situacion actual")
i = input("¿Se acerca un asteroide? Y/N:  ")
if i == "Y" or i == "y":
    velocidad = int(input("¿A qué velocidad se aproxima?  "))
    tamaño = int(input("¿Cual es su tamaño?  "))
    if velocidad >= 25:
        print("Cadete, envíe el siguiente mensaje a la tierra: ¡Alerta! ¡Un asteroide se acerca a velocidades peligrosas!")
    elif velocidad >= 20 and velocidad < 25 and tamaño < 25:
        print("Cadete, envíe el siguiente mensaje a la tierra: Look up! ¡Hay una luz mágica en el cielo!")
    elif velocidad >= 25 and tamaño >= 25:
        print("Cadete, envíe el siguiente mensaje a la tierra: ¡Código rojo! ¡Un asteroíde muy peligroso viene a la tierra!")
    elif velocidad < 25 and tamaño > 25:
        print("Es un gran asteroide, pero se desviará porque tiene poca velocidad")
    else:
        print("Es una velocidad y tamaño menor, el asteroide desaparecerá y no es un peligro")
else:
    print("Gracias cadete, continúe su guardia")
    
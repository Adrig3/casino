# Se importan todas las funciones y tablas necesarias.
import random
import time
from databases import base_datos_dados, base_estadisticas_dados

# Se declara la variable salir con valor inicial False para así ejecutar el bucle hasta que el usuario salga.
salir = False

'''
La función genera dos valores aleatorios entre 1 y 6 representando
las caras de un dado y los almacena en variables, después llama a una
función para dibujarlos en pantalla y registra los datos en el diccionario
de estadísticas y en la tabla destinada a calcular la media.
'''
def tirar_dados():
    valor_dado_1 = random.randint(1,6)
    valor_dado_2 = random.randint(1,6)
    print("\nSe están lanzando los dados...\n")
    time.sleep(1)
    dibujar_dados(valor_dado_1,valor_dado_2)
    registrar_dados(valor_dado_1,valor_dado_2)
    añadir_estadisticas(valor_dado_1,valor_dado_2)

# La función toma dos variables y muestra por pantalla el dibujo de un dado con su valor.
def dibujar_dados(a,b):
    print(" ---       ---")
    print(f"| {a} |     | {b} |")
    print(" ---       ---")

# La función registra los datos en la tabla base_datos_datos.
def registrar_dados(a,b):
     base_datos_dados.append((a,b))

'''
La función primero declara la variable suma_dados en la cual suma
todos los resultados que hayan salido en los dados (registrados en la tabla
base_datos_dados) usando bucles for i.

Luego se declara la variable tiradas_totales que toma la longitud de la misma
tabla para así saber cuántas veces se han tirado los dados (2 dados = 1 tirada)

En caso de que no se hayan tirado dados, se muestra que no se puede calcular
la media ya que no se puede dividir por 0, en otro caso se calcula la media y
se muestra por pantalla.
'''
def media():

    suma_dados = sum(dado for pareja in base_datos_dados for dado in pareja)
    tiradas_totales = len(base_datos_dados)

    if suma_dados == 0:
         print("\nNo se han tirado dados.\n")
    else:
        media = suma_dados / tiradas_totales
        print(f"\nDe las {len(base_datos_dados)} tiradas, la media ha sido: {media}\n")

# La función suma uno al diccionario base_estadisticas_dados en base al número que haya salido en los dados
def añadir_estadisticas(a,b):
     base_estadisticas_dados[str(a)] += 1
     base_estadisticas_dados[str(b)] += 1

'''
La función primero le asigna a la variable total_tiradas la suma de la base
de estadísticas para saber cuántas veces se han tirado los dados y
posteriormente se abre un bucle for que calcula el porcentaje de aparición
de cada número de los dados, en caso de que no se hayan tirado dados se asigna
0 como porcentaje.
'''
def mostrar_estadisticas():
    total_tiradas = sum(base_estadisticas_dados.values())
    print("\nEstas son las estadísticas para cada número:\n")
    for i, j in base_estadisticas_dados.items():
        if total_tiradas > 0:
            porcentaje = (j / total_tiradas * 100) 
        else:
             porcentaje = 0
        print(f"El {i} ha salido {j} veces del total. Un {porcentaje}%.")
    print("")

# La función le muestra ayuda al usuario
def ayuda():
     print("\nPara interactuar con el programa, escribe una de las opciones listadas en el menú\n")
     
# La función muestra un menú con todas las opciones posibles y ejecuta la función asignada a la opción elegida.
def menu():
        global salir
        while salir != True:
            print("=== BIENVENIDO AL CASINO, PRUEBE SU SUERTE EN LOS DADOS ===")
            print("Opciones:                                                 |")
            print("(S) Salir                                                 ♠")
            print("(T) Tirar                                                 ♥")
            print("(M) Media aritmética                                      ♦")
            print("(E) Estadísticas de números                               ♣")
            print("(H) Muestra ayuda sobre el programa                       |")
            print("===========================================================")
            user_input = input("Seleccione una opción: ")

            match user_input:
                case "M" | "m":
                      media()
                case "T" | "t":
                      tirar_dados()
                case "E" | "e":
                      mostrar_estadisticas()
                case "S" | "s":
                      salir = True
                case "H" | "h":
                      ayuda()
                case _:
                    print("\nERROR: Opción inválida, selecciona una opción del menú.\n")


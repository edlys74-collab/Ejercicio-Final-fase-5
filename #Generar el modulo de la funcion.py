#Generar el modulo de la funcion
def contador_de_peliculas(matriz, nota_minima, año_minimo):
    
    conteo = 0
    for pelicula in matriz:
        nota = pelicula[1]
        año = pelicula[2]
        
        if nota >= nota_minima and año >= año_minimo:
            conteo += 1
            
    return conteo

#Matriz datos
peliculas = [
    ["Crepusculo", 5.2, 2008, "Romance"],
    ["Cincuenta sombras de Grey", 4.1, 2015, "Romance"],
    ["Harry Potter", 7.8, 2001, "Fantasia"],
    ["Rapidos y Furiosos", 6.5, 2010, "Accion"],
    ["Piratas del Caribe", 7.3, 2003, "Aventura"],
    ["Terremoto_falla_de_san_andres", 6.1, 2015, "Accion"],
    ["No_te_preocupes_cariño", 4.8, 2016, "Suspenso"]
]

print("Videoteca de peliculas")

#Ahora bucle para pedir al usuario  el año minimo
while True:
    try:
        filtro_año_minimo = int(input("Ingrese el año mínimo para filtrar las películas: "))
        if 1900 <= filtro_año_minimo <= 2026:
            break 
        else:
            print("Por favor, ingrese un año válido entre 1900 y 2026.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero para el año mínimo.")
        
#Ahora bucle para pedir al usuario la nota minima
while True:
    try:
        filtro_nota_minima = float(input("Ingrese la nota mínima para filtrar las películas: "))
        if 0 <= filtro_nota_minima <= 10:
            break 
        else:
            print("Por favor, ingrese una nota válida entre 0 y 10.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido para la nota mínima.")
        
#Llamar a la funcion
resultado = contador_de_peliculas(peliculas, filtro_nota_minima, filtro_año_minimo)

print(f"El número de películas que cumplen con los criterios es: {resultado}")  
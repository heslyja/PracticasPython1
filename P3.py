# Programa para calcular el capital obtenido de una inversión cada año

# Solicitar al usuario la cantidad a invertir, el interés anual y el número de años
cantidad_invertida = float(input("¿Cantidad a invertir?: "))  # Se convierte la entrada a flotante
interes_anual = float(input("¿Interés porcentual anual?: "))  # Se convierte la entrada a flotante
años = int(input("¿Años?: "))  # Se convierte la entrada a entero

# Calcular y mostrar el capital obtenido cada año
for año in range(1, años + 1):
    # Calcular el capital obtenido usando la fórmula del interés compuesto
    capital_obtenido = cantidad_invertida * (1 + interes_anual / 100) ** año
    # Imprimir el capital obtenido al final de cada año
    print(f"Capital tras {año} {'año' if año == 1 else 'años'}: {capital_obtenido:.2f}")


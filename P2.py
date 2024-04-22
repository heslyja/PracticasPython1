# Programa para convertir una cantidad N a monedas de $20, $10, $5 y $1

# Solicitar al usuario la cantidad a convertir
cantidad = int(input("Cantidad a Convertir: "))

# Inicializar el conteo de monedas para cada denominación
monedas_20 = cantidad // 20  # Calcular cuántas monedas de $20 se necesitan
cantidad %= 20  # Actualizar la cantidad restante después de quitar las monedas de $20

monedas_10 = cantidad // 10  # Calcular cuántas monedas de $10 se necesitan
cantidad %= 10  # Actualizar la cantidad restante después de quitar las monedas de $10

monedas_5 = cantidad // 5  # Calcular cuántas monedas de $5 se necesitan
cantidad %= 5  # Actualizar la cantidad restante después de quitar las monedas de $5

monedas_1 = cantidad  # La cantidad restante son monedas de $1

# Imprimir el resultado
print(f"Monedas de $20: {monedas_20}")
print(f"Monedas de $10: {monedas_10}")
print(f"Monedas de $5: {monedas_5}")
print(f"Monedas de $1: {monedas_1}")

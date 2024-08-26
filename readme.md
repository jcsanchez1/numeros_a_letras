# Cantidad a Letras

Este proyecto proporciona una función en Python para convertir cantidades numéricas a su representación en letras en español. Es especialmente útil para generar recibos, facturas, o cualquier documento financiero donde se requiera la cantidad escrita en palabras.

## Características

- Convierte números del 0 al 999,999,999.99
- Maneja correctamente casos especiales como "cien"
- Incluye manejo de centavos
- Proporciona un mensaje de error para cantidades fuera de rango

## Instalación

Clone este repositorio o descargue el archivo `cantidad_a_letras.py`.

```bash
git clone https://github.com/tu-usuario/cantidad-a-letras.git
```

## Uso

```python
from cantidad_a_letras import cantidad_a_letras

print(cantidad_a_letras(1234.56))
# Salida: Mil doscientos treinta y cuatro con cincuenta y seis centavos

print(cantidad_a_letras(1000000))
# Salida: Un millón exactos
```

## Ejemplos

```python
print(cantidad_a_letras(0))  # Cero exactos
print(cantidad_a_letras(1))  # Uno exactos
print(cantidad_a_letras(21))  # Veintiuno exactos
print(cantidad_a_letras(100))  # Cien exactos
print(cantidad_a_letras(118))  # Ciento dieciocho exactos
print(cantidad_a_letras(1000))  # Mil exactos
print(cantidad_a_letras(1234.56))  # Mil doscientos treinta y cuatro con cincuenta y seis centavos
print(cantidad_a_letras(1000000))  # Un millón exactos
print(cantidad_a_letras(-5678.90))  # Menos cinco mil seiscientos setenta y ocho con noventa centavos
print(cantidad_a_letras(123456789.34))  # Ciento veintitrés millones cuatrocientos cincuenta y seis mil setecientos ochenta y nueve con treinta y cuatro centavos
print(cantidad_a_letras(1000000000))  # Error: Cantidad fuera de rango
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue primero para discutir lo que le gustaría cambiar.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)

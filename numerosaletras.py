def cantidad_a_letras(cantidad):
    """Convierte una cantidad numérica a su representación en letras.

    Args:
    cantidad (float): La cantidad a convertir (máximo 999,999,999.99).

    Returns:
    str: La cantidad en letras.
    """
    unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    decenas = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
    especiales = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']

    def convertir_grupo(n):
        if n == 0:
            return ''
        elif n == 100:
            return 'cien'
        elif n <= 9:
            return unidades[n]
        elif n <= 19:
            return especiales[n - 10]
        elif n <= 99:
            d, u = divmod(n, 10)
            if u == 0:
                return decenas[d]
            elif d == 2:
                return 'veinti' + unidades[u]
            else:
                return decenas[d] + ' y ' + unidades[u]
        else:
            c, r = divmod(n, 100)
            if r == 0:
                return centenas[c]
            else:
                return centenas[c] + ' ' + convertir_grupo(r)

    def procesar_parte_entera(n):
        if n == 0:
            return 'cero'
        
        grupos = []
        while n > 0:
            grupos.append(n % 1000)
            n //= 1000
        
        nombres_grupos = ['', 'mil', 'millones']
        resultado = []
        
        for i, grupo in enumerate(grupos):
            if grupo > 0:
                if i == 1 and grupo == 1:
                    resultado.append('mil')
                elif i == 2 and grupo == 1:
                    resultado.append('un millón')
                else:
                    if i == 2:
                        resultado.append(convertir_grupo(grupo) + ' millones')
                    else:
                        resultado.append(convertir_grupo(grupo) + (' ' + nombres_grupos[i] if i > 0 else ''))
        
        return ' '.join(resultado[::-1]).strip()

    # Manejar números negativos
    if cantidad < 0:
        return "menos " + cantidad_a_letras(abs(cantidad))

    # Limitar a 999,999,999.99
    if cantidad > 999999999.99:
        return "Error: Cantidad fuera de rango"

    # Separar parte entera y decimal
    parte_entera = int(cantidad)
    parte_decimal = int(round((cantidad - parte_entera) * 100))

    resultado = procesar_parte_entera(parte_entera)

    # Convertir parte decimal a letras
    if parte_decimal > 0:
        resultado += ' con ' + convertir_grupo(parte_decimal) + ' centavo' + ('s' if parte_decimal != 1 else '')
    else:
        resultado += ' exactos'

    return resultado.capitalize()

# Pruebas
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
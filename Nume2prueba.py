# Función para validar los datos del trabajador
def validar_datos(nombre, sueldo_base, horas_extras):
    # Verificar si el nombre está vacío o tiene más de 30 caracteres
    if not nombre or len(nombre) > 30:
        print("Error: Por favor, ingrese el nombre con un máximo de 30 caracteres.")
        return False  # Devolver False si hay un error en los datos del trabajador

    # Verificar si el sueldo base es menor o igual a cero o si las horas extras son negativas
    if sueldo_base <= 0 or horas_extras < 0:
        print("Error: Por favor, ingrese valores válidos para el sueldo base y las horas extras.")
        return False  # Devolver False si hay un error en los datos del trabajador
    
    return True  # Devolver True si los datos del trabajador son válidos

# Función para calcular la liquidación del trabajador
def calcular_liquidacion(sueldo_base, horas_extras):
    # Calcular el pago por horas extras, total de ingresos, descuentos y sueldo neto
    pago_horas_extras = horas_extras * (sueldo_base / 160) * 1.5
    total_ingresos = sueldo_base + pago_horas_extras
    descuento_fonasa = total_ingresos * 0.07
    descuento_afp = total_ingresos * 0.10
    sueldo_neto = total_ingresos - (descuento_fonasa + descuento_afp)
    
    return pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto

# Función para mostrar la liquidación del trabajador por pantalla
def mostrar_liquidacion(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    # Mostrar los detalles de la liquidación por pantalla
    print("\nLiquidación de Sueldo")
    print("===========")
    print(f"Nombre del trabajador: {nombre}")
    print(f"Sueldo base: ${sueldo_base:.0f}")
    print(f"Pago por horas extras: ${pago_horas_extras:.0f}")
    print(f"Total de ingresos: ${total_ingresos:.0f}")
    print(f"Descuento por FONASA (7%): ${descuento_fonasa:.0f}")
    print(f"Descuento por AFP (10%): ${descuento_afp:.0f}")
    print(f"Sueldo neto a pagar: ${sueldo_neto:.0f}")
    print("========")

# Función para generar un archivo con la liquidación del trabajador
def generar_archivo_liquidacion(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    # Crear el nombre del archivo y escribir los detalles de la liquidación en él
    nombre_archivo = f"liquidacion_{nombre.replace(' ', '_')}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Liquidación de Sueldo\n")
        archivo.write("==========\n")
        archivo.write(f"Nombre del trabajador: {nombre}\n")
        archivo.write(f"Sueldo base: ${sueldo_base:.0f}\n")
        archivo.write(f"Pago por horas extras: ${pago_horas_extras:.0f}\n")
        archivo.write(f"Total de ingresos: ${total_ingresos:.0f}\n")
        archivo.write(f"Descuento por FONASA (7%): ${descuento_fonasa:.0f}\n")
        archivo.write(f"Descuento por AFP (10%): ${descuento_afp:.0f}\n")
        archivo.write(f"Sueldo neto a pagar: ${sueldo_neto:.0f}\n")
        archivo.write("==========\n")
    print(f"Archivo generado: {nombre_archivo}")

# Función principal del programa
def main():
    while True:
        # Solicitar al usuario los datos del trabajador
        nombre = input("Ingrese el nombre del trabajador: ").strip()
        try:
            sueldo_base = float(input("Ingrese el sueldo base: ").strip())
            horas_extras = float(input("Ingrese el número de horas extras trabajadas: ").strip())
    
        except ValueError:
            print("Error: El sueldo base y las horas extras deben ser valores numéricos positivos.")
            continue

        # Verificar si los datos del trabajador son válidos
        if not validar_datos(nombre, sueldo_base, horas_extras):
            continue

        # Calcular la liquidación del trabajador
        pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto = calcular_liquidacion(sueldo_base, horas_extras)

        # Mostrar la liquidación del trabajador por pantalla
        mostrar_liquidacion(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)

        # Generar un archivo con la liquidación del trabajador
        generar_archivo_liquidacion(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)

        # Preguntar al usuario si desea calcular otra liquidación
        otra = input("\n¿Desea calcular otra liquidación? (s/n): ").strip().lower()
        if otra != 's':
            break

# Ejecutar la función principal si el script se realiza.
if __name__ == "__main__":
    main()

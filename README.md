# Evidencia1_EDyP
Taller Mecanico

import datetime
import re

# Define una expresión regular para validar fechas
patron_fecha = r"^\d{1,2}-\d{2}-\d{4}$"

# Inicializa listas para almacenar notas y notas canceladas
notas = []
notas_canceladas = []

# Inicializa el contador de folios
folios_contador = 0

while True:
    print("\n1. Registrar una nota.")
    print("2. Consultas y reportes.")
    print("3. Cancelar una nota.")
    print("4. Recuperar nota.")
    print("5. Salir\n")
    
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        folios_contador += 1
        while True:
            nombre_cliente = input("Nombre del cliente: ")
            if not nombre_cliente.strip():
                print("El nombre del cliente no puede estar en blanco. Intente de nuevo.")
                continue
            else:
                break

        while True:
            fecha_actual = datetime.datetime.now()
            fecha_ingresada_str = input(f"Fecha de la nota (dd-mm-aaaa) [Fecha actual: {fecha_actual.strftime('%d-%m-%Y')}]: ")
            if not fecha_ingresada_str:
                fecha_ingresada_str = fecha_actual.strftime('%d-%m-%Y')
            if not re.match(patron_fecha, fecha_ingresada_str):
                print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa.")
                continue
            try:
                fecha_ingresada = datetime.datetime.strptime(fecha_ingresada_str, "%d-%m-%Y")
            except Exception:
                print("La fecha no es válida. Intente de nuevo.")
                continue
            if fecha_ingresada > fecha_actual:
                print("La fecha no puede ser posterior a la fecha actual del sistema.")
                continue
            else:
                break

        nota = {
            'folio': folios_contador,
            'fecha': fecha_ingresada,
            'cliente': nombre_cliente,
            'monto_a_pagar': 0.0,
            'detalle': [],
            'estado': True
        }

        while True:
            nombre_servicio = input("Nombre del servicio: ")
            if not nombre_servicio.strip():
                print("El nombre del servicio no puede estar en blanco. Intente de nuevo.")
                continue

            while True:
                costo_servicio_str = input("Costo del servicio: ")
                if not costo_servicio_str.strip():
                    print("El costo del servicio no puede estar en blanco. Intente de nuevo.")
                    continue
                try:
                    costo_servicio = float(costo_servicio_str)
                    if costo_servicio <= 0:
                        print("El costo debe ser mayor a 0 pesos.")
                        continue
                except ValueError:
                    print("El costo debe ser un número válido.")
                    continue
                break

            nota['detalle'].append((nombre_servicio, costo_servicio))
            nota['monto_a_pagar'] += costo_servicio

            agregar_mas_servicios = input("¿Agregar otro servicio? (s/n): ").lower()
            if agregar_mas_servicios != "s":
                break

        notas.append(nota)
        print(f"\nFolio asignado: {folios_contador}")
        print(f"Nombre: {nombre_cliente}")
        print(f"Fecha: {fecha_ingresada.strftime('%d-%m-%Y')}")
        print("Detalles: ")
        for servicio, costo in nota['detalle']:
            print(f"Servicio: {servicio} ----> Costo: {costo:.2f}")
        print(f"Monto total a pagar: {nota['monto_a_pagar']:.2f}")

    elif opcion == "2":
        print("\n1. Consultar por período.")
        print("2. Consultar por folio.")
        opcion_consulta = input("\nIngrese una opción de consulta: ")

        if opcion_consulta == "1":
            while True:
                fecha_inicial_str = input("Fecha inicial (dd-mm-aaaa): ")
                if not re.match(patron_fecha, fecha_inicial_str):
                    print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa.")
                    continue
                try:
                    fecha_inicial = datetime.datetime.strptime(fecha_inicial_str, "%d-%m-%Y")
                except Exception:
                    print("La fecha no es válida. Intente de nuevo.")
                    continue
                break

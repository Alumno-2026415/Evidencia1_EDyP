import datetime

patrón_fecha = r"^\d{1,2}\d{2}-\d{2}-\d{4}$"

notas = []
notas_canceladas = []

folios_contador = 0

while True:
    print("1. Registrar una nota.\n2. Consultas y reportes.\n3. Cancelar una nota.\n4. Recuperar nota.\n5. Salir")
    
    opcion = input("Ingrese una opción:\n")
    
    if opcion == "1":
        folios_contador += 1
        while True:
            nombre_cliente = input("Nombre del cliente:\n")
            if not nombre_cliente.strip():
                print("El folio no puede estar en blanco. Intente de nuevo.")
                continue
            else:
                break

        while True:
            fecha_actual = datetime.datetime.now()
            fecha_ingresada_str = input("Fecha de la nota (dd-mm-aaaa):\n")
            if not fecha_ingresada_str:
                fecha_ingresada_str = fecha_actual.strftime('%d-%m-%Y')
                if not re.match(patron_fecha, fecha_ingresada_str):
                    print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa.")
                continue
            try:
                fecha_ingresada = datetime.datetime.strftime(fecha_ingresada_str, "%d-%m-%Y")
            except Exception:
                print("La fecha no es válida. Intente de nuevo.")
                continue
            if fecha_ingresada > fecha_actual:
                print("La fecha no puede ser posterior a la fecha actual del sistema.")
                continue
            else:
                break
        
        nota = {
            "folio": folios_contador,
            "fecha": fecha_ingresada,
            "cliente": cliente,
            "monto_a_pagar": 0.0,
            "detalle": [],
            "estado": True
        }
        
        while True:
            nombre_servicio = input("Nombre del servicio: ")
            if not nombre_servicio.strip():
                print("El nombre del servicio no puede estar en blanco. Intente de nuevo")
                continue

        while True:
            costo_servicio_str = input("Costo del servicio: ")
            if not costo_servicio_str.strip():
                print("El costo no puede estar en blanco. Intente de nuevo")
                continue
            try:
                costo_servicio = float(costo_servicio_str)
                if costo_servicio <= 0:
                    print("El costo debe ser mayor a 0 pesos.")
                    continue
            except ValueError:
                print("El cosot debe tener un número válido")
                continue
            break
            
            costo_servicio = float(costo_servicio)
            
            if input("¿Agregar otro servicio? (s/n): ").lower() != "s":
                break
            
        notas.append(nota)
        print(f"\nFolio asignado: {folios_contador}")
        print(f"Nombre: {nombre_cliente}")
        print(f"Fecha: {fecha_ingresada.strftime('%d-%m-%Y')}")
        print("Detalles: ")
        for servicio, costo in nota['detalle']:
            print(f"Servicio: {servicio} ----> Costo: {costo:.2f}")
        print(f"Monto total a pagar: {nota['monto_a_pagar']:.2f}")
        print(f"Folio asignado: {folios_contador}")
    
    elif opcion == "2":
        print("1. Consultar por período.\n2. Consultar por folio.")
        consulta_opcion = input("Ingrese una opción de consulta:\n")
        
        if consulta_opcion == "1":
            while True:
                fecha_inicial_str = input("Fecha inicial (dd-mm-aaaa): ")
                if not re.match(patron_fecha, fecha_inicial_str):
                    print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa: ")
                    continue
                try:
                    fecha_final_str = input("Fecha final (dd-mm-aaaa): ")
                except Exception:
                    print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa.")
                    continue
                try:
                    fecha_inicial = datetime.datetime.strptime(fecha_inicial_str, "%d-%m-%Y")
                except Exception:
                    print("La fecha no es válida. Intente de nuevo")
                    continue
                break

            while True:
                fecha_final = datetime.datetime.strptime(fecha_final_str, "%d-%m-%Y")
                if not re.match(patro_fecha, fecha_final_str):
                    print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa.")
                    continue
                try:
                    fecha_final = datetime.datetime.strptime(fecha_final_str, "%d-%m-%Y")
                except Exception:
                    print("La fecha no es válida. Intente de nuevo.")
                    continue
                break
            
            notas_en_periodo = [nota for nota in notas if fecha_inicial <= nota['fecha'] <= fecha_final and nota['estado']]
            if notas_en_periodo:
                print("\nNotas encontradas en el periodo:")
                print("-" * 50)
                for nota in notas_en_periodo:
                    print(f"\nFolio: {nota['folio']}\tCliente: {nota['Cliente'].strftime('%d-%m-%Y')}")
                    print(f"Monto: {nota['monto_a_pagar']:.2f}")
            else:
                print("Fin de las notas")
            else:
                print("\nNo se encontraron notas en el periodo especificado.")
                
            for nota in notas:
                if nota['fecha']>=fecha_inicial and nota['fecha']<= fecha_final and nota['estado']:
                    notas_en_periodo.append(nota)
                    
            if notas_en_periodo:
                
                print('\nNotas encontradas en el período:')
                print("-"*50)
                
                for nota in notas_en_periodo:
                    
                    print(f"Folio: {nota['folio']}\t Cliente: {nota['cliente']}\t Fecha: {nota['fecha'].strftime('%d-%m-%Y')}")
                    for servicio,costo in nota['detalle']:
                        print(f' Servicio: {servicio}-----> Costo: {costo:.2f}')
                    print(f'Monto: {nota["monto_a_pagar"]:.2f}')
                    print("-"*50)
                else:
                    print('Fin de las notas')
            else:
                print('\nNo se encontraron notas en el período especificado')
                
        elif opcion == "2":
            pass
                
                 
            
                
    
            
            
        
        

import datetime
fecha_actual = datetime.date.today()
dia_actual = fecha_actual.day
mes_actual = fecha_actual.month
año_actual = fecha_actual.year
tupla_actual = (dia_actual, mes_actual, año_actual)
opcion = 0
clave_cliente = 0
clave_sala = 0
clave_registro = 0
#fechaExistente = False

def menu():
    opc = int(input("Menú Principal\n" +
                    "Seleccione la opcion que guste:\n"+
                    "1.- Registrar la reservación de una sala\n" +
                    "2.- Editar el nombre de un evento reservado\n" +
                    "3.- Consultar reservaciones\n" +
                    "4.- Registrar un nuevo cliente\n" +
                    "5.- Registrar una sala\n" +
                    "6.- Finalizar\n"))
    return opc
 
sala= []
clientes= []
eventos = []

while opcion !=6:
    opcion = menu()
    if opcion == 1:        
        if sala:
            clienteRegistrado = False            
            clave=int(input('Ingrese su ID: '))
            for elementoCliente in clientes:
                if clave ==elementoCliente[0]:
                    clienteRegistrado = True
                    break
                
                
                
#                 for validacionID in range(3):#len(elementoCliente)):        
#                     if clave == elementoCliente[0]:            
#                         clienteRegistrado = True
#                         break
#                     else:                
#                         break
                    
            if clienteRegistrado:
                print("Registrar la reservación de una sala para un evento\n")
                while True:
                    salaExistente = False
                    nombre_evento = input("Ingrese el nombre del evento: ") 
                    if nombre_evento != "": 
                        disponible = True 
                        cve_sala=int(input("Ingrese la clave de la sala del evento: ")) 
                        for revisionSala in sala:
                            for revisionClaveSala in range(len(revisionSala)):
                                if cve_sala == revisionSala[0]:
                                    salaExistente = True                                    
                                    break
                                
                        if salaExistente:                    
                            for Lista in eventos: 
                                if disponible: 
                                    for claveIteracion in range(len(Lista)): 
                                        if cve_sala == Lista[3]: 
                                            disponible = False 
                                            break
                                else: 
                                    break
                                
                            if disponible: 
                                print("Continue con el registro") 
                                horario_evento = input("Ingrese el horario del evento que desee (1.-MATUTINO, 2.-VESPERTINO, 3.-NOCTURNO): ")                     
                                
                                while True:
                                    fecha_reservada = input("Ingrese la fecha que desea reservar (dd/mm/aaaa): ")
                                    fecha_reservada = datetime.datetime.strptime(fecha_reservada,"%d/%m/%Y").date()
                                    dia_reservado = fecha_reservada.day
                                    mes_reservado = fecha_reservada.month
                                    año_reservado = fecha_reservada.year

                                    dia_valido = dia_reservado - dia_actual

                                    tupla_reservacion = (dia_reservado, mes_reservado, año_reservado)
                                    
                                    if dia_valido <= 1:
                                        print("Para reservar una fecha debe hacerlo con 2 dias de anticipación")
                                    else:
                                        if tupla_reservacion > tupla_actual:
                                            clave_registro += 1 
                                            print("Su reservación a sido éxitosa") 
                                            eventos.append((clave, clave_registro, nombre_evento, cve_sala, horario_evento, tupla_reservacion)) 
                                            break
                                        else:
                                            print("Para reservar una fecha debe hacerlo con 2 dias de anticipación")
                                        
                                break
                            else: 
                                print("ERROR! La sala ya ha sido registrada")                                
                        else:
                            print("ERROR! No existe esa sala")                            
                    else:
                         break                                
            else:
                print("El cliente no está registrado")                                        
        else:
            print("ERROR! NO SE HA REGISTRADO ALGUNA SALA")
        
    if opcion == 2:
        print("Editar el nombre de un evento reservado\n")
        eventos = list(map(list,eventos))
        folio_evento = int(input("Folio del evento: "))
        
        for clave_evento in eventos:
            if clave_evento[0] == folio_evento:
                nombre_nuevo=input("Ingrese el nuevo nombre del evento: ")
                clave_evento[2]=nombre_nuevo
                print(eventos)
                
    if opcion == 3:
        print("Consultar reservaciones\n")
        fechaExistente=False
        fecha_consulta = input("Ingrese la fecha que desea consultar (dd/mm/aaaa): ")
        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
        dia_consulta = fecha_consulta.day
        mes_consulta = fecha_consulta.month
        año_consulta = fecha_consulta.year            
        tupla_consulta = (dia_consulta, mes_consulta, año_consulta)
        print("--------------------------------------------------------------------")
        print(f"**\t\tREPORTE DE RESERVACIONES PARA EL DIA {fecha_consulta}\t\t**")
        print("--------------------------------------------------------------------")
        print("SALA\t CLIENTE\t\t EVENTO\t\t TURNO")
        
        for num_cliente_buscar, id_buscar, nombre_buscar, sala_buscar, turno_buscar, fecha_buscar in eventos:
            if tupla_consulta == fecha_buscar:
                for numero_sala, sala_nombre, sala_cupo in sala:
                    if numero_sala==sala_buscar:
                        imprimir_sala=numero_sala
                for numero_cliente, cliente_nombre, cliente_apellido in clientes:
                    if numero_cliente == num_cliente_buscar:
                        imprimir_cliente=cliente_nombre
                        imprimir_apellido=cliente_apellido
                for num_cliente, numero_evento, evento_nombre, clave_sala, evento_turno, evento_fecha in eventos:
                    if numero_evento==id_buscar:
                        imprimir_evento=evento_nombre
                        imprimir_turno=evento_turno
                        
                print("--------------------------------------------------------------------")
                print(f"{imprimir_sala}\t{imprimir_cliente} {imprimir_apellido}\t\t{imprimir_evento}\t\t{imprimir_turno}")
        print("----------------------------FIN DEL REPORTE----------------------------")
        fechaExistente = True
        
    if opcion == 4:
        print("Registrar un nuevo cliente\n")        
        nombre_cliente=input("Ingrese el nombre del cliente: ")
        apellidos=input("Ingrese los apellidos del cliente: ")
        clave_cliente += 1
        print("Asistente agrego.")
        
        clientes.append((clave_cliente, nombre_cliente, apellidos))

        print(clientes)
    
    if opcion == 5:
        print("Registrar una sala\n")
        
        nombre_sala = input("Ingrese el nombre de la sala: ")
        cupo_sala = input("Ingrese el cupo de la sala: ")
        clave_sala += 1
        print("Sala agregada.")
        
        sala.append((clave_sala, nombre_sala, cupo_sala))
        
        print(sala)
    
    if opcion == 6:
        print("Usted a salido con éxito\n")
        break

# Sistema de Gestión de Reservas de Hotel

def validar_codigo_reserva(codigo_reserva):
    return codigo_reserva.strip() != ""

def validar_nombre_huesped(nombre_huesped):
    return nombre_huesped.strip().lower() != ""

def validar_noche(noche):
    if noche <= 0:
        return False
    return True
    
def validar_valor_noche(valor_noche):
    if valor_noche <= 0:
        return False
    return True    
    
def total_hospedaje(noche, valor_noche):
    
    total_hosp = noche * valor_noche   
    return total_hosp 
    
def categoria_hospedaje(total):
    
    if total < 200000:
        return "Economica"
        
    elif total >= 200000 and total <= 500000:
        return "Estandar"
    
    elif total > 500000:
        return "Premium"   

def buscar_reserva(reservas, codigo_reserva):
    
    for reserva in reservas:
        
        if reserva["codigo_reserva"] == codigo_reserva:
            return reserva
    
    return None    
  

#REGISTRO DE RESERVA (opcion 1)
def registrar_reserva(reservas):
    print("\n************ Registro de Reservas **********")
    
    codigo_reserva = input("\nIngrese el codigo de la reserva : ").strip()
    
    #validar codigo
    if not validar_codigo_reserva(codigo_reserva):
        print("Error: El código de reserva no puede estar vacio")
        return
    
    #validar código único      
    if buscar_reserva(reservas,codigo_reserva) is not None:
        print("Error: El código ya existe")
        return
    
    
    nombre_huesped = input("\nIngrese Nombre del huésped : ").strip().lower()
    
    #validar nombre
    if not validar_nombre_huesped(nombre_huesped):
        print("Error: El nombre del huesped no puede ir vacio")
        return
    
    try:
        noche = int(input("Ingrese cantidad de noches a alojar : "))
        
        #validar noche
        if not validar_noche(noche):
            print("Error: Las noches no pueden ser menor a 1")
            return
        
        #validar valor noche    
        valor_noche = int(input("Ingrese valor por noche : $"))
        
        if not validar_valor_noche(valor_noche):
            print("El valor por noche no puede ser menor a 1 ")
            return
        
    except ValueError:
        print("Debe ingresar valores numericos ")
        return
    
    #calcular total
    total = total_hospedaje(noche,valor_noche)
    
    #calcular categoria
    categoria = categoria_hospedaje(total)
    
    #Diccionario
    reserva = {
        "codigo_reserva": codigo_reserva,
        "nombre_huesped": nombre_huesped,
        "noche": noche,
        "valor_noche": valor_noche,
        "total": total,
        "categoria": categoria
        }  
    
    #Guardar reserva    
    reservas.append(reserva)
    
    print("\nReserva registrada correctamente")
    print(f"Total hospedaje ${total}")
    print(f"categoria: {categoria}")

#BUSCAR RESERVA (opcion 2)
def mostrar_busqueda(reservas):
    codigo = input("Ingrese código de reserva: ").strip()

    reserva = buscar_reserva(reservas, codigo)

    if reserva is None:
        print("Reserva no encontrada")
        return

    print("\n===== RESERVA ENCONTRADA =====")
    print("==============================")
    print("Código Reserva :", reserva["codigo_reserva"])
    print("Nombre Huésped :", reserva["nombre_huesped"])
    print("Noches         :", reserva["noche"])
    print("Valor Noche    :", reserva["valor_noche"])
    print("Total          :", reserva["total"])
    print("Categoría      :", reserva["categoria"])
    print("==============================")
    
    
#ACTUALIZAR RESERVA (opcion 3)
def actualizar_reserva(reservas):
    print("\n********** ACTUALIZAR RESERVA **********")
    codigo = input("Ingrese codigo de reserva : ").strip()
    
    reserva = buscar_reserva(reservas, codigo)
    
    if reserva is None:
        print("La Reserva no se encuentra ")
        return
    
    print(f'''Datos actuales :
          Huesped : {reserva['nombre_huesped']}
          Noches : {reserva['noche']}
          Valor por noches : ${reserva['valor_noche']}
          ''')
    
    try:
        
        nueva_noche = int(input("Ingrese la cantidad nueva de noches : "))
        if not validar_noche(nueva_noche):
            print("Error las noches ingresadas deben ser mayor a 0 ")
            return
        
        nuevo_valor = int(input("Ingrese un nuevo valor por noche : "))
        
        if not validar_valor_noche(nuevo_valor):
            print("Error : valor por noche incorrecto ")
            return
    
    except ValueError:
        print("Ingrese datos validos ")
        return
    
    #datos actualizados
    reserva["noche"] = nueva_noche
    reserva["valor_noche"]= nuevo_valor
    reserva["total"] = total_hospedaje(nueva_noche, nuevo_valor)
    reserva["categoria"] = categoria_hospedaje(reserva["total"])
    
    print(f'''Datos actualizados :
          Nuevo total : ${reserva['total']}
          Nueva categoria : {reserva['categoria']}
          ''')        

#ELIMINAR RESERVA (opcion 4)
def eliminar_reserva(reservas):
    codigo_reserva = input("Ingrese el código de reserva: ").strip()

    reserva = buscar_reserva(reservas, codigo_reserva)

    if reserva is None:
        print("Reserva no encontrada")
        return

    reservas.remove(reserva)

    print("Reserva eliminada correctamente")
    
#MOSTRAR RESERVA (opcion 5)
def mostrar_reserva(reservas):
    print("\n===== LISTADO DE RESERVAS =====")

    if len(reservas) == 0:
        print("No existen reservas registradas")
        return
    
    for reserva in reservas:
        print("========================")
        print("Código Reserva :", reserva["codigo_reserva"])
        print("Nombre Huésped :", reserva["nombre_huesped"])
        print("Noches         :", reserva["noche"])
        print("Valor Noche    :", reserva["valor_noche"])
        print("Total          :", reserva["total"])
        print("Categoría      :", reserva["categoria"])
        print("========================")

#MOSTRAR ESTADISTICAS ( opcion 6)
def mostrar_estadisticas(reservas):
    print("\n====== ESTADISTICAS ======")
    
    if len(reservas) == 0:
        print("No hay reservas registradas ")
        return
    
    cantidad_reservas = len(reservas)
    ingresos_totales = 0
    
    for reserva in reservas:
        ingresos_totales += reserva["total"]
    
    reserva_mayor = reservas[0]
    
    for reserva in reservas:
        if reserva["total"] > reserva_mayor["total"]:
            reserva_mayor = reserva
    
    promedio = ingresos_totales / cantidad_reservas
    
    print(f"Cantidad total de reservas : {cantidad_reservas}")
    print(f"Ingresos totales           : ${ingresos_totales}")
    print(f"Promedio por reserva       : ${promedio:.2f}")

    print("\n==== RESERVA DE MAYOR VALOR  ====")
    print(f"Código    : {reserva_mayor['codigo_reserva']}")
    print(f"Huésped   : {reserva_mayor['nombre_huesped']}")
    print(f"Total     : ${reserva_mayor['total']}")
    print(f"Categoría : {reserva_mayor['categoria']}")
    print("====================================")
    


#SALIR (opcion 7)
def salir():
    print("Gracias por usar el sistema de reservas ")
    return


#MENU PRINCIPAL
def menu_principal():
    
      print("\n******** MENU RESERVAS DEL HOTEL ***** ")
        
      print("\n1. Registrar reserva")
      print("2. Buscar reserva")
      print("3. Actualizar reserva")
      print("4. Eliminar reserva")
      print("5. Mostrar reservas")
      print("6. Mostrar estadísticas")
      print("7. Salir")
      print("=========================================")


#PROGRAMA PRINCIPAL
def main():
    
    reservas = [] 
    
    while True:
        
        menu_principal()
        
        try:
            
            opcion = int(input("\nIngrese opcion del MENU : "))
            
            if opcion == 1:
                registrar_reserva(reservas)
                
            elif opcion == 2:
                mostrar_busqueda(reservas)
            
            elif opcion == 3:
                actualizar_reserva(reservas)
                
            elif opcion == 4:
                eliminar_reserva(reservas)
                
            elif opcion == 5:
                mostrar_reserva(reservas)
                
            elif opcion == 6:
                mostrar_estadisticas(reservas)
            
            elif opcion == 7:
                salir()
                break                  
            
            else:
                print("Opcion Invalida") 
        
        except ValueError:
            print("Debe ingresar una opcion valida")        

            
main()            
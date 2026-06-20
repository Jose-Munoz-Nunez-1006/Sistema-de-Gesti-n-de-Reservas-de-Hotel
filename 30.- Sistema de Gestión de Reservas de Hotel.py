
# Sistema de Gestión de Reservas de Hotel

def validar_codigo_reserva(codigo_reserva):
    return codigo_reserva.strip() != ""

def validar_nombre_husped(nombre_huesped):
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
        return "Standar"
    
    elif total > 500000:
        return "Premium"       
           
    

def buscar_reserva(reservas, codigo_reserva):
    
    for reserva in reservas:
        
        if reserva["codigo_reserva"] == codigo_reserva:
            return reserva
    
    return None  
  

#REGISTRO DE RESERVA (opcion 1)
def registar_reserva(reservas):
    print("\n************ Registro de Reservas **********")
    
    codigo_reserva = input("\nIngrese el codigo de la reservan ").strip()
    
    #validar codigo
    if not validar_codigo_reserva(codigo_reserva):
        print("Error: El código de reserva no puede estar vacio")
        return
    
    #validar código único      
    if buscar_reserva(reservas,codigo_reserva) is not None:
        print("Error: El código ya existe")
        return
    
    
    nombre_huesped = input("\nIngrese Nombre del huésped ").strip().lower()
    
    #validar nombre
    if not validar_nombre_husped(nombre_huesped):
        print("Error: El nombre del huesped no puede ir vacio")
        return
    
    try:
        noche = int(input("Ingrese cantidad de noches a alojar "))
        
        #validar noche
        if not validar_noche(noche):
            print("Error: Las noches no pueden ser menor a 1")
            return
        
        #validar valor noche    
        valor_noche = int(input("Ingrese valor por noche"))
        
        if not validar_valor_noche(valor_noche):
            print("El valor por noche no puede ser menor a 1")
            return
        
    except ValueError:
        print("\Debe ingresar valores numericos ")
        return
    
    #calcular total
    total = total_hospedaje(noche,validar_noche)
    
    #calcular categoria
    categoria = categoria_hospedaje(total)
    
    #Diccionario
    reserva ={"codigo_reseva": codigo_reserva,
              "noche_huesped": nombre_huesped,
              "noche": noche,
              "valor_noche": valor_noche,
              "total": total,
              "categoria": categoria}  
    
    #Guardar reserva    
    reservas.append(reserva)
    
    print("\nReserva registrada correctamente")
    print(f"Total hospedaje ${total}")
    print(f"categoria: {categoria}")



#BUSCAR RESERVA (opcion 2)

#ACTUALIZAR RESERVA (opcion 3)

#ELIMINAR RESERVA (opcion 4)

#MOSTRAR RESERVA (opcion 5)

#MOSTRAR ESTADISTICAS ( opcion 6)

#SALIR (opcion 7)


#MENU PRINCIPAL
def menu_principal():
    
      print("\n******** MENU Reservas de Hotel ***** ")
        
      print("\n1. Registrar reserva")
      print("2. Buscar reserva")
      print("3. Actualizar reserva")
      print("4. Eliminar reserva")
      print("5. Mostrar reservas")
      print("6. Mostrar estadísticas")
      print("7. Salir")


#PROGRAMA PRINCIPAL
def main():
    
    reservas = [] 
    
    while True:
        
        menu_principal()
        
        try:
            
            opcion = int(input("\nIngrese opcion del MENU"))
            
            if opcion == 1:
                registar_reserva(reservas)
            
            elif opcion == 2:
            
            elif opcion == 3:
                
            elif opcion == 4:
                
            elif opcion == 5:
                
            elif opcion == 6:
            
            elif opcion == 7:
                print("Cerrando el sistema...")
                break                  
            
            else:
                print("Opcion Invalida") 
        
        except ValueError:
            print("Debe ingresar una opcion valida")        

            
main()            
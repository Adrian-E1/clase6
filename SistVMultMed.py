from datetime import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__caninos = {}
        self.__felinos = {}
    
    def verificarExiste(self,historia):
        return historia in self.__caninos or historia in self.__felinose
        
    def verNumeroMascotas(self):
        return len(self.__caninos) + len(self.__felinos) 
    
    def ingresarMascota(self,mascota):
        if mascota.verTipo().lower() == "canino":
            self.__caninos[mascota.verHistoria()] = mascota
        elif mascota.verTipo().lower() == "felino":
            self.__felinos[mascota.verHistoria()] = mascota
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__caninos:
            return self.__caninos[historia].verFecha()
        elif historia in self.__felinos:
             return self.__felinos[historia].verFecha()
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__caninos:
            return self.__caninos[historia].verLista_Medicamentos()
        elif historia in self.__felinos:
             return self.__felinos[historia].verLista_Medicamentos()
        return None
    
    def eliminarMascota(self, historia):
        if historia in self.__caninos:
            del self.__caninos[historia]
            return True
        elif historia in self.__felinos:
            del self.__felinos[historia]
            return True
        return False 
    
    def eliminarMedicamento(self, historia, nombremed):
        mascota = self.__caninos.get(historia) or self.__felinos.get(historia)
        if mascota:
            lista = mascota.verLista_Medicamentos()
            for med in lista:
                if med.verNombre() == nombremed:
                    lista.remove(med)
                    print(f"El medicamento {nombremed} fue eliminado.")
                    return True
            print("El medicamento no fue encontrado")
            return False
        print(f"No se encontro una mascota con esa historia: {historia}")
        return False

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                while True:
                    try:
                        fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                        datetime.strptime(fecha, "%d/%m/%Y")
                        break
                    except ValueError:
                        print("El formato de la fecha debe ser (dia/mes/año).")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]
                nombres_med = set()

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    if nombre_medicamentos in nombres_med:
                        print("No se puede ingresar dos medicamentos con el mismo nombre")
                        continue
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                    nombres_med.add(nombre_medicamentos)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            nombre_medicamento = input("Ingrese el nombre del medicamento: ")
            servicio_hospitalario.eliminarMedicamento(historia, nombre_medicamento)
        
        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                


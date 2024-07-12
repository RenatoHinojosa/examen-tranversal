import random,csv

trabajadores = [
    {"nombre":"Juan Perez"},
    {"nombre":"Maria Garcia"},
    {"nombre":"Carlos Lopez"},
    {"nombre":"Ana Martinez"},
    {"nombre":"Pedro Rodriguez"},
    {"nombre":"Laura Hernandez"}, 
    {"nombre":"Miguel Sanchez"},
    {"nombre":"Isabel Gomez"},
    {"nombre":"Elena Fernandez"},
]

sueldos=[]

#

def ingresar_sueldo(trabajadores):
    for trabajador in trabajadores:
        sueldo=random.randint(300000,2500000)
        trabajador["sueldo"]=sueldo
        sueldos.append(sueldo)
    print("sueldos registrados correctamente")




sueldosbajos=[]
sueldosmedios=[]
sueldosaltos=[]
def clasificar_sueldos():
    for trabajador in trabajadores:
        if trabajador["sueldo"]<800000:
            sueldosbajos.append(trabajador)
        if trabajador["sueldo"]>=800000 and trabajador["sueldo"]<=2000000 :
            sueldosmedios.append(trabajador)
        if trabajador["sueldo"]>2000000:
            sueldosaltos.append(trabajador)
            
    print("="*50)        
    print(f"SUELDOS MENORES A 800.000 TOTAL:{len(sueldosbajos)}")
    print("|  Nombre Empleado |  sueldo  |")
    for trabajador in sueldosbajos:
        print(f"{trabajador["nombre"]}  {trabajador["sueldo"]}")
    print("="*50)
    print(f"SUELDOS ENTRE 800.000 Y 2.000.000 TOTAL:{len(sueldosmedios)}")
    print("|  Nombre Empleado |  sueldo  |")
    for trabajador in sueldosmedios:
        print(f"{trabajador["nombre"]}  {trabajador["sueldo"]}")
        
    print("="*50)
    print(f"SUELDOS MAYORES A 2.000.000 TOTAL:{len(sueldosaltos)}")
    print("|  Nombre Empleado |  sueldo  |")
    for trabajador in sueldosaltos:
        print(f"{trabajador["nombre"]}  {trabajador["sueldo"]}")




def estadisticas():
    sueldomenor=min(sueldos)
    sueldomayor=max(sueldos)
    sueldoprom=sum(sueldos) / len(sueldos)
    
    print(f"Sueldo Menor: {sueldomenor}")
    print(f"Sueldo mayor: {sueldomayor}")
    print(f"promedio de sueldos: {round(sueldoprom)}")



def reporte_sueldos():
    with open ('registro.csv','w', newline="") as archivo:
        writer=csv.writer(archivo)
        writer.writerow(['nombre','SueldoBase', 'DescuentoSalud', 'DescuentoAFP', 'SueldoLiquido'])
        for trabajador in trabajadores:
            salud=trabajador["sueldo"]*0.07
            afp=trabajador["sueldo"]*0.12
            liquido=salud+afp
            sueldoliquido=trabajador["sueldo"]-liquido
            writer.writerow([f"{trabajador["nombre"]} ${trabajador["sueldo"]} ${round(salud)} ${round(afp)} ${round(sueldoliquido)}"])
            
def salir():
    print("finalizando Programa...")
    print("Desarrollado por: Renato Hinojosa")
    print("RUT: 22.061.620-7")

while True:
    print("(1) Asignar Sueldos")
    print("(2) Clasificar Sueldos")
    print("(3) Ver Estadisticas")
    print("(4) Reporte de Sueldos")
    print("(5) salir")
    opc=input("Ingrese una opcion\n>>>")
    match opc:
        case "1":
            ingresar_sueldo(trabajadores)
        case "2":
            try:
                clasificar_sueldos()
            except:
                print("Debes asignar los sueldos antes!!")
        case "3":
            try:
                estadisticas()
            except:
                print("Debes asignar los sueldos antes!!")
        case "4":
            try:
                reporte_sueldos()
            except:
                print("debes ingresar los sueldos antes!!!")
        case "5":
            salir()
            break
        case _:
            print("Ingresa una opcion valida")


        

   
        
        
        
        
    
    

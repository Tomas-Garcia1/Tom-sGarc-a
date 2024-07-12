import random
import statistics

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
    "Abel Gómez", "Francisco Díaz", "Elena Fernández"
]

sueldos = [0] * len(trabajadores)

def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    bajos = [sueldo for sueldo in sueldos if sueldo < 1000000]
    medios = [sueldo for sueldo in sueldos if 1000000 <= sueldo < 2000000]
    altos = [sueldo for sueldo in sueldos if sueldo >= 2000000]

    print("La clasificación de sueldos es: ")
    print(f"Sueldos menores a $800.000 TOTAL: {len(bajos)} empleados.")
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(medios)} empleados.")
    print(f"Sueldos superiores a $2.000.000 TOTAL: {len(altos)} empleados.")

def ver_estadisticas():
    if not any(sueldos):
        print("Primero debe asignar sueldos.")
        return
    
    print("Estadísticas de sueldos:")
    print(f"El sueldo promedio es: ${statistics.mean(sueldos):,.2f} pesos.")
    print(f"El sueldo más balanceado es: ${statistics.median(sueldos):,.2f} pesos.")
    print(f"El sueldo más alto es: ${max(sueldos):,.2f} pesos.")
    print(f"El sueldo más bajo es: ${min(sueldos):,.2f} pesos.")

def reporte_sueldos():
    print("Reporte de sueldos: ")
    print("Trabajador       Sueldo base        Descuento Salud          Descuento AFP")
    for trabajador, sueldo in zip(trabajadores, sueldos):
        print(f"{trabajador}:    ${sueldo:,.2f}         {sueldo*7/100}              {sueldo*12/100}")

def menu():
    while True:
        print("Menú:")
        print("1. Para asignar sueldos aleatoriamente: ")
        print("2. Para clasificar los sueldos: ")
        print("3. Para ver las estadísticas: ")
        print("4. Para ver el reporte de sueldos: ")
        print("5. Salir del programa.")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            asignar_sueldos()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("Finalizando programa…")
            print("Desarrollado por Tomás García")
            print("Rut 21.808.696-9")
            break
        else:
            print("Opción no válida, ingrese una opción")

if __name__ == "__main__":
    menu()
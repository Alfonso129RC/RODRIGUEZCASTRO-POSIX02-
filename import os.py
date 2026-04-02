import os

def menu():
    print("\n--- Gestor de Archivos ---")
    print("1. Ver archivos")
    print("2. Crear carpeta")
    print("3. Eliminar archivo")
    print("4. Mostrar ruta actual")
    print("5. Cambiar de directorio")
    print("6. Crear archivo")
    print("7. Salir")

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\nContenido del directorio:")
        try:
            for f in os.listdir():
                print(f)
        except:
            print("Error al listar archivos.")

    elif opcion == "2":
        nombre = input("Nombre de la carpeta: ")
        try:
            os.mkdir(nombre)
            print("Carpeta creada correctamente.")
        except:
            print("No se pudo crear la carpeta (puede que ya exista).")

    elif opcion == "3":
        nombre = input("Archivo a eliminar: ")
        try:
            os.remove(nombre)
            print("Archivo eliminado correctamente.")
        except:
            print("No se pudo eliminar el archivo.")

    elif opcion == "4":
        print("Ruta actual:", os.getcwd())

    elif opcion == "5":
        ruta = input("Ruta a la que deseas cambiar: ")
        try:
            os.chdir(ruta)
            print("Directorio cambiado correctamente.")
        except:
            print("No se pudo cambiar de directorio.")

    elif opcion == "6":
        nombre = input("Nombre del archivo: ")
        try:
            with open(nombre, "w") as f:
                f.write("Archivo creado desde Python.\n")
            print("Archivo creado correctamente.")
        except:
            print("Error al crear el archivo.")

    elif opcion == "7":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")
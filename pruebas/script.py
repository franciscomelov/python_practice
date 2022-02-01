try:
    mi_archivo = open("contenido/datos_muestra/mi_archivo.txt")
except FileNotFoundError:
    print(f"Lo siento, el archivo no existe")
else:
    contenido = mi_archivo.read()
    print(contenido)
finally:
    mi_archivo.close()

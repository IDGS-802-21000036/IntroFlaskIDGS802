from io import open

archivo_texto=open("anombres.txt", 'r')
#archivo_texto.write('\n datos en el archivo')
#archivo_texto.close()
#print(archivo_texto.read())
#archivo_texto.seek(0)
#print(archivo_texto.readlines())
#archivo_texto.close()
for linea in archivo_texto.readlines():
    print(linea.rstrip())

archivo_texto.close()

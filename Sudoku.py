archivo = open("sudoku_valido.txt","r")
lineas=archivo.readlines()
matriz =[]
for i in range(len(lineas)):
    matriz.append(str(lineas[i]).split())
print(matriz)  

archivo = open("sudoku_invalido.txt","r")
lineas=archivo.readlines()
matriz =[]
for i in range(len(lineas)):
    matriz.append(str(lineas[i]).split())
print(matriz)    
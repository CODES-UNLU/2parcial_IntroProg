#################################
#Invertir una lista de números
#################################
# Escribí un programa que:
# Pida al usuario ingresar números positivos.
# Guarde los valores en una lista hasta que se ingrese "fin".
# Luego, cree una nueva lista con los mismos elementos, pero en orden inverso.
# Muestre la lista original y la invertida.

lista=[]
numero_positivo= input("ingrese un numero positivo(o fin para terminar): ")
while numero_positivo !="fin":
    if numero_positivo.isdigit() and int(numero_positivo)>0:
        lista.append(int(numero_positivo))
    else:
        print("numero invalido.Solo numero positivo")
    numero_positivo= input("ingrese otro numero positivo(o fin): ")

inversa=[]
for i in range(len(lista)-1,-1,-1):
    inversa.append(lista[i])
print("lista original:", lista)
print("lista inversa:", inversa)

#################################
# Registro de Voltaje y Presión
#################################
# Escribí un programa que:
# Pida al usuario ingresar un voltaje.
# Luego, según ese voltaje, solicite el nivel de presión correspondiente.
# Guarde cada valor en su lista respectiva: voltajes y presiones, emparejados por índice.
# Termine cuando el usuario escriba "fin" como voltaje.
# Al final, muestre ambas listas y cuántas mediciones se hicieron.

def voltaje_y_presion():
    voltaje = []
    presion = []
    bandera = True
    while bandera:
        dato_voltaje = input("Ingrese un voltaje: ")
        if dato_voltaje == "fin":
            bandera = False
        if dato_voltaje.isdigit():    
            voltaje.append(dato_voltaje)
            dato_presion = int(input("Ingrese la presion: "))
            presion.append(dato_presion)
    
    for i in range(len(voltaje)):
        print("Posicion", i,"Voltaje:",voltaje[i], "Presion: ", presion[i])
        
voltaje_y_presion()

################################
# Carga de Productos
###############################
# Escribi un programa que:
# Pida al usuario cargar ilimitadamente productos, cantidades y categoria a la que pertenecen los productos.
# Los valores se deben ir almacenando hasta que el usuario ingrese "fin" como nombre.
#
# Validar:
#     *El nombre debe ser alfanumérico (isalnum()),
#     *La cantidad es un número entero (isdigit()),
#     *La categoría contenga solo letras (isalpha()).

def supermercado():
    productos = []
    cantidades = []
    categorias = []
    
    bandera = True
    
    while bandera:
        producto = input("Ingrese nombre producto: ")
        if producto == "fin":
            bandera = False
        else:
            if producto.isalnum():
                productos.append(producto)
                cantidad = input("Ingrese la cantida: ")
                if cantidad.isdigit():
                    cantidades.append(cantidad)
                    categoria = input("Ingrese una categoria: ")
                    if categoria.isalpha():
                        categorias.append(categoria)
        
    for i in range(len(productos)):
        print("Posicion: ", i, "Producto: ", productos[i], "Cantidaad: ", cantidades[i], "Categoria: ", categorias[i])
        
supermercado()
        
     
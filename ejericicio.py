print ("Hola mundo")

# Diseñar una función que haga lo siguiente 

# def areatriangulo(base,altura):
#     area = (base*altura)/2
#     return area

# area1 = areatriangulo(10,5)

# print("El area del triagulo es: ", area1)


# Diseñar una función que realice el calculo de un tanque de agua 
# Determina la cantidad maxima del tanque de agua - su base y altura son de 5 metros 
#

def capacidad(base,altura, profundidad):
    area = (base*altura)*profundidad
    return area

capacidad1 = capacidad(5,5,5)
capacidad2 = capacidad(5,5,10)
capacidad3 = capacidad(5,5,100)

print("la capacidad es de: ", capacidad1)
print("la capacidad es de: ", capacidad2)
print("la capacidad es de: ", capacidad3)


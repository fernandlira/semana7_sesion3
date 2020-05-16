from classes.funciones import Funciones

j = None
while j is not 3:
    j = int(input("Que desea hacer? (1) Listar Productos (2) Agregar Productos (3) Salir : "))
    if j == 1:
        Funciones.listar_productos()
    if j == 2:
        try:
            cantidad = int(input("Cuantos productos desea ingresar? "))
            if cantidad < 0:
                raise Exception("La cantidad debe ser positiva")
            else:
                Funciones.insertar_producto(cantidad)
        except ValueError:
            print(f'Debes ingresar un número en el ID de categoria')
        except Exception as e:
            print(f'{str(e)}')
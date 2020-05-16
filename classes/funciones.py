from classes.productos import Producto
from classes.categorias import Categoria

class Funciones:
    def insertar_producto(cantidad):
        categoria = Categoria()
        categoria.listar()
        i = 1
        while True:
                if i > cantidad:
                    break
                while True:
                    try:
                        id_categoria = int(input(f"Ingrese id de la categoria a la que pertenece el producto  n°{i}: "))
                        if id_categoria in categoria.ids:
                            break
                        else:
                            raise Exception("Debe elegir un ID valido")
                    except ValueError:
                        print(f'Debes ingresar un número en el ID de categoria')
                    except Exception as e:
                        print(f'{str(e)}')
                nombre = input(f"Ingrese nombre del producto n°{i}: ")

                while True:
                    try:
                        stock = int(input(f"Ingrese stock del producto  n°{i}: "))
                        if stock < 0:
                            raise Exception("El stock no puede ser negativo")
                        else: 
                            break
                    except ValueError:
                        print(f'Debes ingresar un número en el ID de categoria')
                    except Exception as e:
                        print(f'{str(e)}')
                while True:
                    try:
                        precio = float(input(f"Ingrese precio del producto  n°{i}: "))
                        if precio < 0:
                            raise Exception("El precio no puede ser negativo")
                        else:
                            break
                    except ValueError:
                        print(f'Debes ingresar un número en el ID de categoria')
                    except Exception as e:
                        print(f'{str(e)}')
                producto = Producto(id_categoria,nombre,stock,precio)
                producto.insertar()
                i+=1
    
    def listar_productos():
        Producto.listar()

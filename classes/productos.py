from connection.conn import conexion

class Producto:
    def __init__(self,id_categoria,producto,stock,precio):
        self.id_categoria = id_categoria
        self.producto = producto
        self.stock = stock
        self.precio = precio
    
    def insertar(self):
        conn = conexion()
        conn.cursor.execute(f"INSERT INTO productos (id_categoria,producto,stock,precio) values (%(id_categoria)s,%(producto)s,%(stock)s,%(precio)s)", {'id_categoria': self.id_categoria, 'producto': self.producto, 'stock': self.stock, 'precio' : self.precio});
        conn.commit()
        conn.cerrar_conexion()
    
    def listar():
        conn = conexion()
        query = "SELECT productos.id,productos.producto,productos.stock,productos.precio,categorias.categoria FROM productos INNER JOIN categorias ON productos.id_categoria = categorias.id WHERE productos.stock > 0"
        conn.ejecutar_sentencia(query)
        filas = conn.cursor.fetchall()
        for registro in filas:
            print(f"""
            ID: {registro[0]},
            Nombre: {registro[1]},
            Stock: {registro[2]},
            Precio: {registro[3]},
            Categoria: {registro[4]}
            """)

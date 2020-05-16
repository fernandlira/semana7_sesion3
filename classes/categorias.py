from connection.conn import conexion

class Categoria:
    def __init__(self):
        self.ids = []
        
    def listar(self):
        self.ids = []
        conn = conexion()
        query = "SELECT * from categorias"
        conn.ejecutar_sentencia(query)
        filas = conn.cursor.fetchall()
        for registro in filas:
            print(f"""
            ID: {registro[0]},
            Nombre: {registro[1]}
            """)
            self.ids.append(registro[0])

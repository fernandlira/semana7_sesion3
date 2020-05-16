import psycopg2

class conexion:
    def __init__(self,host="localhost",user="postgres",password="liraq_07",database="tienda"):
        try:
            self.db = psycopg2.connect(host=host,user=user,password=password,database=database)
            self.cursor = self.db.cursor()
            print("Conexion exitosa")
        except Exception as e:
            print(f"str({e})")
    
    def ejecutar_sentencia(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor
        except Exception as e:
            print(f"str({e})")
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.db.close()
    
    def commit(self):
        self.db.commit()
        return True
    
    def rollback():
        self.db.rollback()
        return True
        
    

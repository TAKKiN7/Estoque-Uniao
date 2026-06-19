import psycopg
from tkinter import messagebox as msg

class TI_Database:
    def __init__(self):
        self.create_table()

    def conn(self ,master = None):
        try:
            conn = psycopg.connect(
                host="192.168.6.175",
                port=5432,
                dbname="projeto_impressora",
                user="eustaquio_tk",
                password="user_admin347",
                connect_timeout=3
            )

            return conn
        except psycopg.OperationalError:
            msg.showerror(
                "Erro de conexão",
                "Não foi possível conectar ao banco de dados.\n\n"
                "Verifique se o servidor está ligado e acessível.", parent=master
            )
            return None
        
    
    def create_table(self):
        conn = self.conn()

        if not conn:
            return  # Não foi possivel conectar ao banco
        
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS equipamentos_ti " \
            "(id SERIAL PRIMARY KEY," \
            "produto VARCHAR(100)," \
            "modelo VARCHAR(30) UNIQUE ," \
            "estoque INTEGER DEFAULT 0)" \
            )


ti_db : TI_Database = TI_Database()
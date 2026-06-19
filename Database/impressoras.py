import psycopg
from tkinter import messagebox as msg

class Impressora_Database:

    def conn(self, master=None):
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
                "Verifique se o servidor está ligado e acessível.",
                parent=master
            )
            return None
        
    

    def create_table(self):
        conn = self.conn()

        if not conn:
            return  # Não foi possivel conectar ao banco
        
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS impressoras " \
            "(id SERIAL PRIMARY KEY," \
            "modelo VARCHAR(100)," \
            "ip VARCHAR(20) UNIQUE NOT NULL," \
            "local VARCHAR(50) NOT NULL," \
            "tonner INTEGER DEFAULT 0)" \
            )


    def listar_registros(self, master=None):
        conn = self.conn(master=master)

        if not conn:
            return None
        
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM impressoras")
            registros = cur.fetchall()

            if not registros:
                return "Nenhum registro encontrado"
            
            return registros
        

    
    def nova_impressora(self, values : tuple, master=None):
        conn = self.conn(master=master)
        if not conn:
            return None
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO impressoras (modelo, ip, local) VALUES (%s, %s, %s)", values)
                conn.commit()
        finally:
            conn.close()

    
    def remover_impressora(self, codigo, master):
        conn = self.conn(master=master)
        if not conn:
            return None
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM impressoras " \
                "WHERE id = %s", (codigo, ))
                conn.commit()
                return "Impressora removida com sucesso"
        except:
            return "Não foi possível remover a impressora"
        finally:
            conn.close()

        
impressora_db : Impressora_Database = Impressora_Database()

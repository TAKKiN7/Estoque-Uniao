import psycopg
from tkinter import messagebox as msg

class Usuario_Database:
    def __init__(self):
        pass

    def conn(self):
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
                "Verifique se o servidor está ligado e acessível."
            )
            return None
        
    

    def create_table(self):
        conn = self.conn()

        if not conn:
            return  # Não foi possivel conectar ao banco
        
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS usuarios " \
            "(id SERIAL PRIMARY KEY," \
            "nome VARCHAR(20) UNIQUE NOT NULL," \
            "senha VARCHAR(50) NOT NULL)")
    

    def criar_usuario(self, values : tuple):
        conn = self.conn()
        if not conn:
            return None
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO usuarios (nome, senha) VALUES (%s, %s)", values)
                conn.commit()
        finally:
            conn.close()

    

    def listar_usuarios(self):
        conn = self.conn()
        if not conn:
            return None
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM materiais_op ORDER BY item ASC")
                usuarios = cur.fetchall()

                return usuarios
        finally:
            conn.close()

    

usuario_db : Usuario_Database = Usuario_Database()
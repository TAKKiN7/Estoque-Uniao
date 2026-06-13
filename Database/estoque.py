import psycopg
from tkinter import messagebox as msg
from customtkinter import CTk

class Database:

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
        

    def inserir_porduto(self, values : tuple):
        conn = self.conn()
        if not conn:
            return
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO materiais_op (item, estoque) VALUES (%s, %s)", values)
                conn.commit()
        finally:
            conn.close()

    
    def listar_produtos(self):
        conn = self.conn()
        if not conn:
            return
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM materiais_op ORDER BY item ASC")
                produtos = cur.fetchall()

                return produtos
        finally:
            conn.close()

    

    def consultar_produto_codigo(self, codigo):
        conn = self.conn()
        if not conn:
            return
        try:
            with self.conn() as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM materiais_op WHERE codigo = %s", (codigo, )) 
                produto = cur.fetchone()
                
                if not produto:
                    return None

                return produto
        finally:
            conn.close()


    def remover_produto(self, codigo) -> str:
        res = self.consultar_produto_codigo(codigo)

        if not res:
            return "Produto não encontrado no banco de dados!"
        
        conn = self.conn()
        if not conn:
            return
        try:
            with self.conn() as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM materiais_op WHERE codigo = %s", (codigo, ))

                conn.commit()
                return "Produto removido com sucesso!"
        finally:
            conn.close()

    
    def atualizar_produto(self, codigo, values):
        res = self.consultar_produto_codigo(codigo)
        
        if not res:
            return "Produto não encontrado no banco de dados!"
        
        conn = self.conn()
        if not conn:
            return
        try:
            with self.conn() as conn:
                cur = conn.cursor()
                cur.execute("UPDATE materiais_op set item = %s, estoque = %s " \
                "WHERE codigo = %s", (values))

                conn.commit()
                return "Produto atualizado com sucesso!"
        finally:
            conn.close()

database : Database = Database()

if __name__ == "__main__":
    registros = database.listar_produtos()

    for registro in registros:
        print(registro)
        break
    print("Operação realizada!")
    
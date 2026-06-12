import psycopg

class Database:

    def conn(self):
        conn = psycopg.connect(
            host="192.168.6.175",
            port=5432,
            dbname="projeto_impressora",
            user="eustaquio_tk",
            password="user_admin347"
        )

        return conn
        

    def inserir_porduto(self, values : tuple):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO materiais_op (item, estoque) VALUES (%s, %s)", values)
            conn.commit()
        

    
    def listar_produtos(self):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM materiais_op ORDER BY item ASC")
            produtos = cur.fetchall()

            return produtos

    

    def consultar_produto_codigo(self, codigo):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM materiais_op WHERE codigo = %s", (codigo, )) 
            produto = cur.fetchone()
            
            if not produto:
                return None

            return produto


    def remover_produto(self, codigo) -> str:
        res = self.consultar_produto_codigo(codigo)

        if not res:
            return "Produto não encontrado no banco de dados!"
        
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM materiais_op WHERE codigo = %s", (codigo, ))

            conn.commit()
            return "Produto removido com sucesso!"

    
    def atualizar_produto(self, codigo, values):
        res = self.consultar_produto_codigo(codigo)
        
        if not res:
            return "Produto não encontrado no banco de dados!"

        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("UPDATE materiais_op set item = %s, estoque = %s " \
            "WHERE codigo = %s", (values))

            conn.commit()
            return "Produto atualizado com sucesso!"


database : Database = Database()

if __name__ == "__main__":
    registros = database.listar_produtos()

    for registro in registros:
        print(registro)
        break
    print("Operação realizada!")
    
import sqlite3
from pathlib import Path


class Database:
    def __init__(self):
        self.criar_tabela()



    def conn(self):
        db_path : Path = Path.cwd() / "Database/db.db"
        conn : sqlite3.Connection = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn


    def criar_tabela(self):
        with self.conn() as conn:
            cur : sqlite3.Cursor = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS estoque (codigo INTEGER PRIMARY KEY AUTOINCREMENT," \
            "produto VARCHAR(70)," \
            "modelo VARCHAR(50)," \
            "quantidade INTEGER)")
            conn.commit()


    def inserir_porduto(self, values : tuple):
        with self.conn() as conn:
            cur : sqlite3.Cursor = conn.cursor()
            cur.execute("INSERT INTO estoque (produto, modelo, quantidade) VALUES (?, ?, ?)", values)
            conn.commit()

    
    def listar_produtos(self):
        with self.conn() as conn:
            cur : sqlite3.Cursor = conn.cursor()
            cur.execute("SELECT * FROM estoque")
            produtos = cur.fetchall()

            itens : list = list()

            for produto in produtos:
                item : dict = dict(produto)
                itens.append(item)

            return itens


database : Database = Database()

if __name__ == "__main__":
    database : Database = Database()
    values : tuple = ("Impressora", "Brother-LD2450", 2)
    #database.inserir_porduto(values)

    produtos = database.listar_produtos()
    print(produtos)
    
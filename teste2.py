import psycopg2

class Connection:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="dbproject",
            user="postgres",
            password="12345678",
            host="localhost"
        )
        self.cur = self.conn.cursor()

    def execute(self, sql, args):
        self.cur.execute(sql, args)

    def commit(self):
        self.conn.commit()

    def query(self, sql, args):
        self.cur.execute(sql, args)
        return self.cur.fetchone()

    def close(self):
        self.cur.close()
        self.conn.close()

class ProdutoApp:
    def __init__(self):
        self.load_data()
    
    def load_data(self):
        try:
            conn = psycopg2.connect(
                dbname="dbproject",
                user="postgres",
                password="12345678",
                host="localhost"
            )
            cur = conn.cursor()
            cur.execute("SELECT * FROM produto")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            
            conn.close()
        except Exception as e:
            print("Erro ao buscar dados:", str(e))
            
            
class ClienteForm:
    def submit(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        sexo = input("Sexo: ")
        email = input("Email: ")
        cidade = input("Cidade: ")
        timefutebol = input("Time de Futebol: ")
        animefavorito = input("Anime Favorito: ")

        insert_cliente(nome, cpf, sexo, email, cidade, timefutebol, animefavorito)

def insert_cliente(nome, cpf, sexo, email, cidade, timefutebol, animefavorito):
    try:
        conn = psycopg2.connect(
            dbname="dbproject",
            user="postgres",
            password="12345678",
            host="localhost"
        )
        cur = conn.cursor()

        sql = "INSERT INTO cliente (nome, cpf, sexo, email, cidade, timefutebol, animefavorito) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cur.execute(sql, (nome, cpf, sexo, email, cidade, timefutebol, animefavorito))

        conn.commit()
        cur.close()
        conn.close()
        print("Cliente inserido com sucesso!")

    except Exception as e:
        print("Erro ao inserir cliente:", str(e))            

class FormaPagamentoForm:
    def submit(self):
        tipo = input("Tipo de pagamento (Cartão, Boleto, Pix, Berries): ")
        status = input("Status: ")

        # Verifique se a forma de pagamento é válida
        if tipo not in ["Cartão", "Boleto", "Pix", "Berries"]:
            print("Forma de pagamento inválida. Por favor, escolha entre Cartão, Boleto, Pix e Berries.")
            return

        insert_forma_pagamento(tipo, status)

def insert_forma_pagamento(tipo, status):
    try:
        conn = psycopg2.connect(
            dbname="dbproject",
            user="postgres",
            password="12345678",
            host="localhost"
        )
        cur = conn.cursor()
        
        sql = "INSERT INTO FormaPagamento (tipo, status) VALUES (%s, %s);"
        cur.execute(sql, (tipo, status))
        
        conn.commit()
        cur.close()
        conn.close()
        print("Forma de pagamento inserida com sucesso!")

    except Exception as e:
        print("Erro ao inserir forma de pagamento:", str(e))

if __name__ == "__main__":
    app = ProdutoApp()
    cliente_form = ClienteForm()
    cliente_form.submit()
    forma_pagamento_form = FormaPagamentoForm()
    forma_pagamento_form.submit()


if __name__ == "__main__":
    app = ProdutoApp()
    form = ClienteForm()
    form.submit()
    forma_pagamento_form = FormaPagamentoForm()
    forma_pagamento_form.submit()
import mysql.connector
def conectar_banco():
    return mysql.connector.connect(
        host = "paparella.com.br",
        user = "paparell_aluno_1",
        password = "@Senai2025",
        database = "paparell_python"
    )

def pegar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor(buffered=True)
    cursor.execute("""SELECT * FROM iot """)
    return cursor.fetchall()

def atualizar_valores(id, nome, ip, led, rele, lcd, servo):
    conexao = conectar_banco()
    cursor = conexao.cursor(buffered=True)
    cursor.execute("""UPDATE iot set nome=%s,ip=%s,estado_led=%s,relay=%s, 
                   lcd=%s,servo=%s WHERE id=%s """,(nome,ip,led, rele, lcd, servo, id))
    conexao.commit()
    cursor.close()

def pegar_dispositivo(id):
    conexao = conectar_banco()
    cursor = conexao.cursor(buffered=True)
    cursor.execute("""SELECT * FROM iot WHERE id=%s """,(id,))
    return cursor.fetchone()

def adicionar_dispositivo(nome,ip):
    conexao = conectar_banco()
    cursor = conexao.cursor(buffered=True)
    cursor.execute("""INSERT INTO iot (nome,ip) VALUES (%s,%s)""",(nome,ip))
    conexao.commit()
    cursor.close()



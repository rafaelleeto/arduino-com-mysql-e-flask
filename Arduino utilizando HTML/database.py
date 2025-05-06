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

def atualizar_valores(nome,led,ip,id):
    conexao = conectar_banco()
    cursor = conexao.cursor(buffered=True)
    cursor.execute("""UPDATE iot set nome=%s,estado_led=%s,ip=%s WHERE id=%s """,(nome,led,ip,id))
    conexao.commit()
    cursor.close()




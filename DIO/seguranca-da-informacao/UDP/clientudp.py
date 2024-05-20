import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!")

host = 'localhost'
porta = 5430

mensagem = "Olá, servidor!"

try:
    print(f"Cliente: {mensagem}")
    s.sendto(mensagem.encode(), (host, porta))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")
except Exception as e:
    print(f"Erro na conexão: {e}")
finally:
    print("Cliente UDP finalizado.")
    s.close()
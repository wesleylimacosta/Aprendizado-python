import random, string

tamanho = 16
valores = string.ascii_letters + string.digits + string.punctuation
rnd = random.SystemRandom()

senha = ''.join(rnd.choice(valores) for i in range(tamanho))
print(senha)

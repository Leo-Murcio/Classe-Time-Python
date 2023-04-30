class Time:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores

    def adiciona_jogador(self, nome, camisa):
        self.jogadores.append([nome, camisa])

    def imprime_jogadores(self):
        print(f"Jogadores do time {self.nome}:")
        for jogador in self.jogadores:
            print(f"{jogador[0]} -- Camisa {jogador[1]}")

time = Time("PSG", [["Messi", 30], ["Neymar", 10], ["Mbappe", 7]])
time.adiciona_jogador("Haaland", 9)
time.imprime_jogadores()
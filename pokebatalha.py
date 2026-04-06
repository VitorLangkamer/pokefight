import requests
import random

class Pokemon:
    def __init__(self, nome):
        self.nome = nome.capitalize()
        self.ataque = 0
        self.defesa = 0
        self.moves = []
        self.carregar_status()

    def carregar_status(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.nome.lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            self.pontos_vida = dados['stats'][0]['base_stat']
            self.ataque = dados['stats'][1]['base_stat']
            self.defesa = dados['stats'][2]['base_stat']
            self.moves = dados['moves'][:4] 
            print(f"Status de {self.nome}: Vida={self.pontos_vida}, Ataque={self.ataque}, Defesa={self.defesa}")
        else:
            raise Exception(f"Este Pokémon '{self.nome}' não foi encontrado.")

    def receber_dano(self, dano):
        self.pontos_vida -= dano
        if self.pontos_vida < 0:
            self.pontos_vida = 0

    def esta_vivo(self):
        return self.pontos_vida > 0

class Batalha:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def atacar(self, atacante, defensor):
        dano_base = atacante.ataque - defensor.defesa // 2
        dano = max(1, dano_base + random.randint(-5, 5))
        defensor.receber_dano(dano)
        print(f"{atacante.nome} ataca {defensor.nome} causando {dano} de dano! (Vida restante: {defensor.pontos_vida})")

    def iniciar(self):
        print(f"\n Batalha entre {self.pokemon1.nome} e {self.pokemon2.nome} começa! ")
        turno = 0
        while self.pokemon1.esta_vivo() and self.pokemon2.esta_vivo():
            print("\n--- Novo Turno ---")
            print(f" {self.pokemon1.nome} HP: {self.pokemon1.pontos_vida} |  {self.pokemon2.nome} HP: {self.pokemon2.pontos_vida}")

            if turno % 2 == 0: 
                atacante, defensor = self.pokemon1, self.pokemon2
            else:  
                atacante, defensor = self.pokemon2, self.pokemon1

            print(f"\nÉ a vez de {atacante.nome}!")
            acao = self.escolher_acao(atacante)
            if acao == "fugir":
                print(f"{atacante.nome} fugiu da batalha!")
                break
            elif acao:
                self.atacar(atacante, defensor)
            
            turno += 1

        print("\n--- Fim da Batalha ---")
        if not self.pokemon1.esta_vivo() and not self.pokemon2.esta_vivo():
             print("Ambos os Pokémon desmaiaram! É um empate!")
        elif self.pokemon1.esta_vivo():
            print(f" {self.pokemon1.nome} venceu a batalha!")
        elif self.pokemon2.esta_vivo():
            print(f" {self.pokemon2.nome} venceu a batalha!")

    def escolher_acao(self, pokemon_atual):
        while True:
            print(f"O que {pokemon_atual.nome} fará?")
            
            for i, move_data in enumerate(pokemon_atual.moves):
                move_name = move_data['move']['name']
                print(f"{i+1}. {move_name.replace('-', ' ').capitalize()}")
            
            num_fugir = len(pokemon_atual.moves) + 1
            print(f"{num_fugir}. Fugir")
            
            escolha = input(f"Escolha sua ação (1-{num_fugir}): ")
            
            if escolha == str(num_fugir):
                return "fugir"
            elif escolha.isdigit() and 1 <= int(escolha) <= len(pokemon_atual.moves):
                return pokemon_atual.moves[int(escolha) - 1]['move']['name']
            else:
                print("Escolha inválida. Tente novamente.")

def escolher_pokemon(jogador):
    while True:
        nome_pokemon = input(f"{jogador}, escolha seu Pokémon: ").strip()
        try:
            pokemon = Pokemon(nome_pokemon)
            return pokemon
        except Exception as e:
            print(e)
            print("Por favor, tente novamente.")

if __name__ == "__main__":
    print("Bem-vindo à Batalha Pokémon!")
    
    pokemon1_jogador = escolher_pokemon("Jogador 1")
    pokemon2_jogador = escolher_pokemon("Jogador 2")

    batalha = Batalha(pokemon1_jogador, pokemon2_jogador)
    batalha.iniciar()
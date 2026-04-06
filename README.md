# PokéBatalha (Python)

Um mini jogo de batalha Pokémon no terminal, onde dois jogadores
escolhem seus Pokémon e lutam em turnos até que um vença ou ambos sejam
derrotados.

------------------------------------------------------------------------

## Funcionalidades

-   Busca dados reais de Pokémon via API (PokeAPI)
-   Sistema de batalha por turnos
-   Cálculo de dano baseado em ataque e defesa
-   Variação aleatória no dano
-   Opção de fugir da batalha
-   Escolha interativa de ações

------------------------------------------------------------------------

## Como funciona

O jogo utiliza a PokeAPI para buscar:

-   Vida (HP)
-   Ataque
-   Defesa
-   Movimentos do Pokémon

Cada turno: 1. Um jogador ataca 2. O dano é calculado 3. O HP do
adversário diminui 4. Repete até alguém vencer ou fugir

------------------------------------------------------------------------

## Requisitos

Antes de rodar, instale a dependência:

pip install requests

------------------------------------------------------------------------

## Como executar

python pokebatalha.py

------------------------------------------------------------------------

## Como jogar

1.  Jogador 1 escolhe um Pokémon (ex: pikachu)
2.  Jogador 2 escolhe outro Pokémon (ex: charizard)
3.  Cada turno você escolhe um ataque ou fugir
4.  A batalha continua até o fim

------------------------------------------------------------------------

## Exemplo

Bem-vindo à Batalha Pokémon!

Jogador 1, escolha seu Pokémon: pikachu\
Jogador 2, escolha seu Pokémon: bulbasaur

Batalha entre Pikachu e Bulbasaur começa!

------------------------------------------------------------------------

## Observações

-   Os nomes dos Pokémon devem existir na API
-   É necessário conexão com internet
-   O jogo roda no terminal (CLI)

------------------------------------------------------------------------

## Melhorias futuras (ideias)

-   Sistema de tipos (água, fogo, etc.)
-   Habilidades especiais
-   Salvar progresso
-   Modo contra IA
-   Interface gráfica

------------------------------------------------------------------------

## Autor

Desenvolvido por Victor

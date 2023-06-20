
import random
# Definindo o tabuleiro
tabuleiro = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro():
    print("  0 1 2")
    for i in range(len(tabuleiro)):
        print(str(i) + " " + " ".join(tabuleiro[i]))

# Função para verificar se alguém ganhou
def verificar_ganhador(jogador):
    for i in range(len(tabuleiro)):
        # Verifica linhas
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
        # Verifica colunas
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    # Verifica diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

jogador_atual = "X"

while True:
    imprimir_tabuleiro()

    if( jogador_atual == "0"):
        linha = (random.randint(0,2))
        coluna = (random.randint(0,2))
        resultado = f'{linha},{coluna}'
        jogada = str(resultado)
    else:
        jogada = input("Digite a jogada de " + jogador_atual + " (linha,coluna): ")
    print(jogada)
    linha, coluna = jogada.split(",")

    if tabuleiro[int(linha)][int(coluna)] != "-":
        print("Jogada inválida. Tente novamente.")
        continue

    tabuleiro[int(linha)][int(coluna)] = jogador_atual

    if verificar_ganhador(jogador_atual):
        print("Jogador " + jogador_atual + " ganhou!")
        break

    if "-" not in tabuleiro[0] and "-" not in tabuleiro[1] and "-" not in tabuleiro[2]:
        print("Empate!")
        break

    jogador_atual = "0" if jogador_atual == "X" else "X"


# Melhorias(possíveis futuramente) :
# 1. Substituição de letras por frequência mais automatizada
#   (sugestões para usos de vogais e regras gramaticais ou possibilidades diretas de tradução)

# Observações :
# 1. Apenas lê e escreve arquivos de texto
# 2. Não tem tratamento para escolha de itens inválidos no menu
# 3. Utiliza o alfabeto tanto quanto simbolos da escrita portuguesa brasileira

import string
import simbolos
import importa_exporta


alfabeto = list(string.ascii_lowercase)
frequencia = {}


def menu():
    zerar_contador_letras()
    mensagem = importa_exporta.pega_mensagem()
    conta_letras(mensagem)
    loop(mensagem)


def loop(mensagem):
    flag = True
    while flag:
        print("\n\n ==> Mensagem atual : '{}' <==".format(mensagem))
        acao = int(input('\n\n O que fazer em seguida?' \
                    +'\n\n1. Subistituir letras'        \
                    +'\n2. Refazer contagem de letras'  \
                    +'\n3. Exportar mensagem'           \
                    +'\n\nDigite o número da opção : ' ))
        if acao == 1:
            char = input('\nDigite o símbolo que vai ser substituído : ')
            novo_char = input('Digite o símbolo que irá substituir : ')
            mensagem = simbolos.substituir_caracter(mensagem, char, str(novo_char))
        elif acao == 2:
            zerar_contador_letras()
            conta_letras(mensagem)
        elif acao == 3:
            importa_exporta.exporta_mensagem(mensagem, 'cifra-sub', 1)
            flag = False


def mostra_contagem():
    print('\n\nLetras contadas e suas frequências na mensagem\n')
    for letra in frequencia:
        contador = ''
        for _ in range(0, frequencia[letra]):
            contador += '%'
        if frequencia[letra] != 0:
            print(" letra '{}': {} {}".format(letra, frequencia[letra], contador))
    print('')


def zerar_contador_letras():
    for letra in alfabeto:
        frequencia[letra] = 0


def conta_letras(mensagem):
    for char in mensagem:
        if not simbolos.verifica_caracter(char):
            frequencia[char] += 1
    mostra_contagem()


if __name__ == "__main__":
    menu()
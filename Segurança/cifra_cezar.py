# Melhorias(possíveis futuramente) :
# 1. Fazer novo programa para cifra para deslocamentos de palavras
#   (cada letra é deslocada por um valor de uma outra letra)
# 2. Corrigir escolhas incorretas para o menu
# 3. Refatorar o código para ser mais "pitônico"
# 4. Comentar os códigos corretamente para subir para o github
# 5. Criar funcionalidade de importação de alfabetos e simbolos da língua

# Observações :
# 1. Apenas lê e escreve arquivos de texto
# 2. Não tem tratamento para escolha de itens inválidos no menu
# 3. Utiliza o alfabeto tanto quanto simbolos da escrita portuguesa brasileira

import string
import simbolos
import importa_exporta


alfabeto = list(string.ascii_lowercase)


def menu():
    textomenu = '\n\n\n -- MENU --' \
        + '\n\n1. Cifrar mensagem' \
        + '\n2. Decifrar mensagem' \
        + '\n3. Encerrar' \
        + '\n\nDigite o número da opção : '
    loop(True, textomenu)


def loop(opcao, textomenu):
    while opcao == True or opcao != 3:
        resultado = ''
        opcao = int(input(textomenu))
        if opcao != 3:
            dados = pega_dados()
        if opcao == 1:
            resultado = faz_cifra(dados)
        elif opcao == 2:
            resultado = decifra(dados)
        importa_exporta.exporta_mensagem(resultado, 'cifra-czr', 0)


def pega_dados():
    mensagem = importa_exporta.pega_mensagem()
    deslocamento = int(input('Digite o valor do deslocamento : '))
    return {'mensagem': mensagem.lower(), 'deslocamento': deslocamento}


def decifra(dados):
    cifra = dados['mensagem']
    deslocamento = dados['deslocamento']
    mensagem = ''
    for char in cifra:
        if simbolos.verifica_caracter(char):
            mensagem += char
        else:
            indice = alfabeto.index(char)
            if indice - deslocamento < 0:
                indice = len(alfabeto) + (indice - deslocamento) # Soma pois o resultado de indice - deslocamento é negativo
            else:
                indice -= deslocamento
            mensagem += alfabeto[indice]
    return mensagem


def faz_cifra(dados):
    mensagem = dados['mensagem']
    deslocamento = dados['deslocamento']
    cifra = ''
    for char in mensagem:
        if simbolos.verifica_caracter(char):
            cifra += char
        else:
            indice = alfabeto.index(char)
            if indice + deslocamento > len(alfabeto)-1:
                indice = (indice + deslocamento) - len(alfabeto)
            else:
                indice += deslocamento
            cifra += alfabeto[indice]
    return cifra


if __name__ ==  "__main__":
    menu()
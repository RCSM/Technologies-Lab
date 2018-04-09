def verifica_caracter(char):
    sinais = [' ', '.', '!', '?', ',', '-']
    for sinal in sinais:
        if sinal == char:
            return True
    return False

def substituir_caracter(mensagem, char, novo_char):
    letras = list(mensagem)
    for indice in range(len(letras)):
        if letras[indice] == char:
            letras[indice] = novo_char
    nova_mensagem = ''.join(letras)
    return nova_mensagem
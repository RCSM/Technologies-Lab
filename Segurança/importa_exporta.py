from json import dump

def importa_chave():
    nomearquivo = input('Digite o nome do arquivo(sem extensão) : ')
    nomearquivo += '.txt'
    with open(nomearquivo, 'r') as arquivo:
        chave = arquivo.read()
    return chave


def pega_mensagem():
    importar = input('Importar mensagem(y/n)? ')
    if importar == 'y':
        nomearquivo = input('Digite o nome do arquivo(sem extensão) : ')
        nomearquivo += '.txt'
        with open(nomearquivo, 'r') as arquivo:
            mensagem = arquivo.read()
    else:
        mensagem = input('Digite a mensagem : ')
    return mensagem


def exporta_mensagem(mensagem, nome_arquivo, tipo):
    exportar = input('Exportar mensagem(y/n)? ')
    if exportar == 'y':
        nome_arquivo = nome_arquivo + '.txt'
        with open(nome_arquivo, 'w') as arquivo:
            if tipo == 0:
                arquivo.write(mensagem)
            else:
                dump(mensagem, arquivo)
        print('Mensagem escrita no arquivo com sucesso')

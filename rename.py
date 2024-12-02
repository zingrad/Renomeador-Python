import os
import unicodedata

## essa linha vai remover os acentos era pra remover os caracteres indesejados também
## preferi manter um array para caso tenha algum caracter que esse código não esteja filtrando
def remover_caracteres_especiais(txt):
    return ''.join(c for c in unicodedata.normalize('NFD', txt)
                   if unicodedata.category(c) != 'Mn')

def renomear_arquivos():
    pasta_atual = os.getcwd()
    arquivos = os.listdir(pasta_atual)

    caracteres_indesejados = ['@', '=', '%', '#', '&', '*', '$', '!', '-','1950x900','[0,1,2,3,4,5,6,7,8,9]' , '?', '^', '{', '}', '[', ']']

    for arquivo in arquivos:
        if os.path.isfile(arquivo):
            nome_atual, extensao = os.path.splitext(arquivo)

            # Remove caracteres especiais e converte para minúsculas
            novo_nome = remover_caracteres_especiais(nome_atual).lower()

            novo_nome = novo_nome.replace(' ', '-')

            # Remove cada caractere indesejado do array caracteres_indesejados
            for c in caracteres_indesejados:
                novo_nome = novo_nome.replace(c, '')

            # Normaliza a extensão para minúsculas para manter a extensão do arquivo
            extensao = extensao.lower()

            # Monta o novo caminho do arquivo, aqui você pode deixar a pasta atual já que é renomeação
            novo_caminho = os.path.join(pasta_atual, novo_nome + extensao)

            # Renomeia o arquivo apenas se o novo nome for diferente do atual, isso melhora a performace para muitos arquivos
            if arquivo != novo_nome + extensao:
                os.rename(os.path.join(pasta_atual, arquivo), novo_caminho)
                print(f"Renomeado {arquivo} para {novo_nome + extensao}")

    print("Renomeação concluída.")

if __name__ == "__main__":
    renomear_arquivos()
    input("Pressione Enter para sair...")


    ## ainda não coloquei nenhuma tratativa de erros, caso encontre algum pode me sinalizar ou tentar resolver :)

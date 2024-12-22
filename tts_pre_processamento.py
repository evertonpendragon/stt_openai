import os

def clean_dir(diretorio):
    try:
        # Listar todos os arquivos no diretório
        for arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            # Verificar se é um arquivo e apagar
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
        print(f"Todos os arquivos em '{diretorio}' foram apagados com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


input = open(r"translator_output\output.txt",'r',encoding='utf-8')
input = [x for x in input.readlines() if x.strip().replace("\n","")]

input = [x.replace("’", "'").replace("‘", "'") for x in input]
input = [x.replace("“", "\"").replace("”", "\"") for x in input]

#print(input)
partes = [""]
chars = 0
index = 0
for l in input:
    if len(l) + chars < 4000:
        partes[index]+=" "+ l
        chars += len(l)
    else:
        index += 1
        partes.append(l)
        chars = len(l)




#limpa diretorio
voice_input_dir = "voice_input"
voice_input_file = os.path.join(voice_input_dir, "voice_input.txt")
clean_dir(voice_input_dir)


with open(voice_input_file,"w",encoding='utf-8') as f:
    lines = "\n§\n".join(partes)
    f.write(lines)


#aqui eu tentei quebrar o arquivo de entrada em varios arquivos de ate 4000 bytes, mas me lembrei que poderia enviar um arquivo  de ate 125 mil bytes para a api. estou reservendo esse codigo por enquanto





input = open(r"translator_input\input.txt",'r',encoding='utf-8')
input = [x for x in input.readlines() if x.strip().replace("\n","")]

input = [x.replace("’", "'").replace("‘", "'") for x in input]

input = [x.replace("’", "'").replace("‘", "'") for x in input]

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


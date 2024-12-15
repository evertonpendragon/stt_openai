import  openai 
import os
from dotenv import load_dotenv
#from pydub import AudioSegment
#import requests
from datetime import datetime

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

hoje=datetime.today().strftime("%y%m%d%H%M%S")


def formata_texto(texto):
    return texto.replace("\n\n", '\n')

def traduzir_texto(conteudo):
    prompt = (
        "Traduza na íntegra os textos enviados aqui para o português. Qualquer número ordinal ou cardinal deve ser transcrito por extenso. "
        "Qualquer número referente a milênios deve ser transcrito por extenso. Notação de datas imperiais como '999.M41' deve ser transcritas por extenso, "
        "como 'novecentos e noventa e nove do quadragésimo primeiro milênio. Os nomes das legiões também devem ser transcritos por extenso, por exemplo, "
        "'VIª Legião' ficará 'Sexta Legião'. Não traduza os títulos dos personagens, como por exemplo 'Wolf King' e 'Great Wolf'."
    )

    try:
        response = openai.chat.completions.create(
            model= "gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um escritor especializado."},
                {"role": "user", "content": f"{prompt}\n\nTexto:\n{conteudo}"}
            ],
            temperature=0
        )
        response_dict = response.model_dump()
        return response_dict["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Erro ao acessar a API da OpenAI:", e)
        return None

# Ler o arquivo de entrada
input_file = "translator_input/input.txt"
output_file = "translator_output/output.txt"

try:
    with open(input_file, "r", encoding="utf-8") as f:
        conteudo = f.read()

    conteudo = formata_texto(conteudo)
    # Traduzir o conteúdo
    traducao = traduzir_texto(conteudo)

    if traducao:
        # Gravar o resultado no arquivo de saída
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(traducao)
        print("Tradução concluída e salva em", output_file)
    else:
        print("Falha na tradução.")

except FileNotFoundError:
    print(f"O arquivo {input_file} não foi encontrado.")
except Exception as e:
    print("Erro:", e)
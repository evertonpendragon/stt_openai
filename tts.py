from openai import OpenAI
import os
from dotenv import load_dotenv
from pydub import AudioSegment
import requests
from datetime import datetime

client = OpenAI()
hoje=datetime.today().strftime("%y%m%d%H%M%S")

# Carregar a API key de forma segura
load_dotenv()
client.api_key = os.getenv("OPENAI_API_KEY")

def text_to_speech(text, output_file="output.mp3", language="pt"):
    try:
        # Parâmetros da requisição para síntese de fala
        response = client.audio.speech.create(
            model="tts-1",
            voice='onyx',
            input=text
        )

        # URL do áudio gerado
        # audio_url = response.get("audio_url")
        # if not audio_url:
        #     raise Exception("Falha ao gerar a síntese de fala.")

        # Download do áudio gerado
        # audio_data = requests.get(audio_url)
        # if audio_data.status_code == 200:
        #     # Salvar o arquivo MP3
        #     with open(output_file, "wb") as audio_file:
        #         audio_file.write(audio_data.content)
        #     print(f"Áudio salvo com sucesso em {output_file}")
        # else:
        #     raise Exception(f"Erro ao baixar o áudio: {audio_data.status_code}")

        response.stream_to_file(output_file)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    input_text = r"voice_input\voice_input.txt"



    if os.path.exists(input_text):
        with open(input_text,'r',encoding='utf-8') as f:
            txt = f.read()


    textos= txt.split("§")
    for texto in textos:
        print("texto1", len(texto))
        if len(texto) > 4096:
            raise Exception("ERRO, texto muito grande. Máx caracteres = 4096")
            exit(-1)
    # Texto para conversão
    #texto = "Olá! Este é um exemplo de conversão de texto em fala usando a API OpenAI."
    
    # Nome do arquivo MP3 de saída
    i=1
    for texto in textos:
        arquivo_saida = rf"voice_output\fala_pt_{hoje}_{i}.mp3"
        print (arquivo_saida)
        i+=1
        # Chamar a função de conversão
        text_to_speech(texto, arquivo_saida)

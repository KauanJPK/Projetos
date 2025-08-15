from django.shortcuts import render
from django.http import HttpResponse
import requests
from google import genai
import dotenv
import os

dotenv.load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))


def entrada(request):

    #Requisição das frases 
    url = "https://random-quotes-freeapi.vercel.app/api/random"
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        quote = data.get("quote", "Sem citação disponível")
        author = data.get("author", "Desconhecido")
        response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f'Traduza para portugues brasil em apenas uma frase e sem aspas ou demais {quote}'
)
    else:
        quote = f"Erro ao buscar frase (Status {r.status_code})"
        author = "Sistema"

        #Retorno do template do website

    return render(request,'entrada.html', {
        'quote': response.text,
        'author': author
    })

import openai
from PIL import Image
import requests
from io import BytesIO

# Suas chaves de API
openai.api_key = 'SUA_CHAVE_API'

def gerar_texto(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )
    return response.choices[0].text.strip()

def gerar_imagem(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

# Função principal
def main():
    prompt_texto = """
    Descreva a importância da Inteligência Artificial em diferentes tipos de negócios e como ela pode auxiliar os humanos nos setores financeiro, saúde, varejo, manufatura, transporte e logística, e recursos humanos.
    """
    prompt_imagem = """
    Uma imagem composta com diferentes seções representando vários setores de negócios impactados pela IA. No centro, uma figura de um cérebro digital, simbolizando a IA, com ramificações que conectam cada setor:
    1. Financeiro: Uma representação de gráficos financeiros, computadores analisando dados e ícones de segurança.
    2. Saúde: Médicos e enfermeiros interagindo com telas holográficas que mostram resultados de exames e diagnósticos.
    3. Varejo: Um cliente interagindo com um chatbot em uma loja online e prateleiras de uma loja física sendo geridas por robôs.
    4. Manufatura: Robôs trabalhando ao lado de humanos em uma linha de montagem, com sensores monitorando máquinas.
    5. Transporte e Logística: Caminhões autônomos e drones fazendo entregas, mapas de rotas otimizadas sendo exibidos em telas.
    6. Recursos Humanos: Entrevistas sendo conduzidas via videoconferência, gráficos de desempenho de funcionários e análises de clima organizacional.
    Cada seção conectada ao cérebro digital no centro.
    """

    # Gerar texto
    texto_gerado = gerar_texto(prompt_texto)
    print("Texto Gerado:\n", texto_gerado)

    # Gerar imagem
    imagem_url = gerar_imagem(prompt_imagem)
    response = requests.get(imagem_url)
    img = Image.open(BytesIO(response.content))
    img.show()

if __name__ == "__main__":
    main()
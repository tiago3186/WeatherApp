import tkinter as tk
import requests

def buscar():
    cidade = entrada.get()

    # Substitua "{sua_chave_de_API}" pela sua chave de API da OpenWeatherMap.
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cidade, "af76a06d440fda0208b27f511582cab6")


    # Faz uma solicitação GET à API e armazena a resposta.
    response = requests.get(url)

    # Verifica se a resposta foi bem sucedida (código de status HTTP 200).
    if response.status_code == 200:
        # Converte a resposta em um dicionário Python.
        data = response.json()

        temperatura_celsius = round((data['main']['temp'] - 273.15))

        # Atualiza o rótulo com as informações relevantes de previsão do tempo.
        condicao_atual.config(text=f"Condição atual: {data['weather'][0]['description']}")
        temp_atual.config(text=f"Temperatura atual: {temperatura_celsius}°C")
        umidade_atual.config(text=f"Umidade atual: {data['main']['humidity']}%")
        resultado.config(text=f"")
    else:
        # Caso contrário, exibe uma mensagem de erro.
        condicao_atual.config(text=f"")
        temp_atual.config(text=f"")
        umidade_atual.config(text=f"")
        resultado.config(text=f"Erro ao obter a previsão do tempo: código de status {response.status_code}")

# Cria a janela principal da aplicação.
janela = tk.Tk()

# Define o título da janela.
janela.title("Previsão do Tempo")

# Define o tamanho mínimo da janela.
janela.minsize(300, 200)

# Define o tamanho máximo da janela igual ao tamanho mínimo (impedindo a maximização).
janela.maxsize(*janela.minsize())

# Impede a maximização da janela.
janela.resizable(False, False)

# Define o ícone da janela
janela.iconbitmap("rain.ico")

# Cria a caixa de entrada de texto e o botão de pesquisa.
entrada = tk.Entry(janela)
botao_pesquisa = tk.Button(janela, text="Pesquisar", command=buscar)

# Cria os rótulos para exibir as informações de previsão do tempo.
condicao_atual = tk.Label(janela, text="")
temp_atual = tk.Label(janela, text="")
umidade_atual = tk.Label(janela, text="")

# Cria o rótulo para exibir mensagens de erro.
resultado = tk.Label(janela, text="")

# Define a posição dos widgets na janela.
entrada.pack(padx=10, pady=10)
botao_pesquisa.pack(padx=10, pady=5)
condicao_atual.pack(padx=10, pady=5)
temp_atual.pack(padx=10, pady=5)
umidade_atual.pack(padx=10, pady=5)
resultado.pack(padx=10, pady=5)

# Inicia o loop principal da aplicação.
janela.mainloop()
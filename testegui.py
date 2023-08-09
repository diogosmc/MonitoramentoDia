import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def salvar_monitoramento():
    data_atual = datetime.now().strftime("%d-%m")
    titulo_arquivo = f"Dia_{data_atual}.txt"

    hora_acordou = entry_hora_acordou.get("1.0", tk.END)
    refeicoes = entry_refeicoes.get("1.0", tk.END)
    litros_agua = entry_litros_agua.get("1.0", tk.END)
    exercicio = entry_exercicio.get("1.0", tk.END)
    contato_sol_natureza = entry_contato_sol_natureza.get("1.0", tk.END)
    tempo_estudo = entry_tempo_estudo.get("1.0", tk.END)
    menos_1_hora_internet = entry_menos_1_hora_internet.get("1.0", tk.END)
    hora_deitar = entry_hora_deitar.get("1.0", tk.END)
    resumo_aprendizado = text_resumo_aprendizado.get("1.0", tk.END)

    conteudo = f"""
Monitoramento do Dia {data_atual}:

Hora que acordou: {hora_acordou.strip()}
Quantas refeições fez: {refeicoes.strip()}
Bebeu quantos Litros de água: {litros_agua.strip()}
Fez algum exercício: {exercicio.strip()}
Teve contato com o Sol / Natureza: {contato_sol_natureza.strip()}
Estudou por quanto tempo: {tempo_estudo.strip()}
Ficou menos de 1 hora na Internet? (Lazer): {menos_1_hora_internet.strip()}
Hora que está indo deitar: {hora_deitar.strip()}

Resuma o que aprendeu de novo hoje:

{resumo_aprendizado.strip()}
"""

    pasta_monitoramento = "Monitoramento_Dia_a_Dia"
    if not os.path.exists(pasta_monitoramento):
        os.makedirs(pasta_monitoramento)

    caminho_arquivo = os.path.join(pasta_monitoramento, titulo_arquivo)

    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write(conteudo)

    messagebox.showinfo("Sucesso", f"Arquivo {titulo_arquivo} salvo na pasta {pasta_monitoramento}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Monitoramento Diário")
largura_janela = 500
altura_janela = 600
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = 50
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
janela.configure(bg="black")  # Cor de fundo preto

# Função para criar uma pergunta com espaço em branco ao lado
def criar_pergunta(pergunta):
    frame = tk.Frame(janela, bg="black")
    frame.pack(fill=tk.X, pady=5)
    
    lbl_pergunta = tk.Label(frame, text=pergunta, fg='white', bg='black')
    lbl_pergunta.pack(side=tk.LEFT)

    entry_resposta = tk.Text(frame, wrap="word", height=1, width=20, fg='white', bg='black',font=('Arial', 10))
    entry_resposta.pack(side=tk.LEFT, fill=tk.X, expand=True)
    return entry_resposta

# Perguntas e campos de entrada
entry_hora_acordou = criar_pergunta("Hora que acordou:")
entry_refeicoes = criar_pergunta("Quantas refeições fez:")
entry_litros_agua = criar_pergunta("Bebeu quantos Litros de água:")
entry_exercicio = criar_pergunta("Fez algum exercício:")
entry_contato_sol_natureza = criar_pergunta("Teve contato com o Sol / Natureza:")
entry_tempo_estudo = criar_pergunta("Estudou por quanto tempo:")
entry_menos_1_hora_internet = criar_pergunta("Ficou menos de 1 hora na Internet? (Lazer):")
entry_hora_deitar = criar_pergunta("Hora que está indo deitar:")

# Frame para as perguntas
frame_perguntas = tk.Frame(janela, bg="black")
frame_perguntas.pack(fill=tk.BOTH, pady=5)

# Título "Resuma o que aprendeu de novo hoje:"
lbl_resumo_titulo = tk.Label(frame_perguntas, text="Resuma o que aprendeu de novo hoje:", fg='white', bg='black')
lbl_resumo_titulo.pack()

# Campo de texto para o resumo
frame_resumo = tk.Frame(janela, bg="black")
frame_resumo.pack(fill=tk.BOTH, pady=5, expand=True)

text_resumo_aprendizado = tk.Text(frame_resumo, wrap="word", width=40, height=10, fg='white', bg='black')
text_resumo_aprendizado.pack(fill=tk.BOTH, expand=True)
text_resumo_aprendizado.configure(insertbackground='white') 

# Botão para salvar o monitoramento
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_monitoramento, fg='white', bg='black')
botao_salvar.pack(pady=20)

janela.mainloop()

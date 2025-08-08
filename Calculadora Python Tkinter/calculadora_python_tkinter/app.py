from tkinter import *
import math
import re


class CalculadoraTk:
    def __init__(self, master=None):

        self.widget1 = Frame(master, bg="#EF8FFA")
        self.widget1.pack()

        self.ecra = Label(master, width= 12, height= 2, bg='#B509C8', textvariable="", fg="white", anchor="e")
        self.ecra['text'] = ''
        self.ecra["font"] = ("Arial", 20, "bold")
        self.ecra.pack(side="top")

        self.numeros_Frame = Frame(master, width= 25, height= 2)
        self.numeros_Frame["bg"] = 'White'
        self.numeros_Frame.pack()

        botoes = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "0", "/","X",
            "+", "-","(",")","%",
            "√", "=", "C",
        ]
        for i, valor in enumerate(botoes):
            row = i // 4
            col = i % 4
            if valor == "=":
                btn = Button(self.numeros_Frame, text=valor, width=5, height=2, bg="green", fg="white")
                btn.bind('<Button-1>', self.calcular)
            elif valor == "C":
                btn = Button(self.numeros_Frame, text=valor, width=5, height=2, fg="white", bg="red")
                btn.bind('<Button-1>', self.apagar)
            else:
                btn = Button(self.numeros_Frame, text=valor, width=5, height=2, bg="#E027F5", fg="white")
                btn.bind('<Button-1>', self.adicionar)
            if valor == "C":
                btn.grid(row=row, column=col, padx=5, pady=5, columnspan=5)
            if valor == "=":
                btn.grid(row=row, column=col, padx=5, pady=5, columnspan=3)
            else:
                btn.grid(row=row, column=col, padx=5, pady=5)

    def criarBotao(self, valor):
        botao = Button(self.numeros_Frame, text=valor, width=5, height=2)
        botao.bind('<Button-1>', self.adicionar)
        botao.pack(side="left")
            
    def adicionar(self, event):
        texto_atual = self.ecra['text']
        novo_texto = str(texto_atual) + event.widget['text']
        self.ecra['text'] = novo_texto

    def apagar(self, event):
        self.texto = ""
        self.ecra['text'] = self.texto

    def calcular(self, event):
        for char in self.ecra['text']:
            if char == "X":
                self.ecra['text'] = self.ecra['text'].replace("X", "*")
            elif char == "%":
                porcentagem = self.ecra['text'].replace("%", "*/100*")
                self.ecra['text'] = str(eval(porcentagem))

        try:
            resultado = eval(self.ecra['text'], {"__builtins__": None}, {"math": math})
            self.ecra['text'] = str(resultado)
        except Exception as e:
            self.ecra['text'] = "Erro"
            print(f"Erro ao calcular: {e}")

    padrao = re.compile(r'((?:\d+\.?\d*|\([^()]*\))?)√(\([^()]*\)|\d+\.?\d*)')

    def substituir_raiz(self, match):
        multiplicador = match.group(1)
        radicando = match.group(2)
        if not multiplicador:
            multiplicador = '1'
        return f'({multiplicador}*({radicando}**0.5))'

    def calcular(self, event):
        texto = self.ecra['text']
        texto = texto.replace("X", "*")
        texto = texto.replace("%", "*/100*")
        texto = self.padrao.sub(self.substituir_raiz, texto)
        try:
            resultado = eval(texto, {"__builtins__": None}, {"math": math})
            self.ecra['text'] = str(resultado)
        except Exception as e:
            self.ecra['text'] = "Erro"
            print(f"Erro ao calcular: {e}")


Calculadora = Tk()
Calculadora.title("Calculadora")
CalculadoraTk(Calculadora)
Calculadora.mainloop()













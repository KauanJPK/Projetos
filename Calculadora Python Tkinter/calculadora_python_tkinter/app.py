from tkinter import *
import math


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
            "+", "-","%",
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
                self.ecra['text'] = self.ecra['text'].replace("%", "/100")
            elif char == "√":
                i = self.ecra['text'].index("√")
                j = i + 1
                while j < len(self.ecra['text']) and (self.ecra['text'][j].isdigit() or self.ecra['text'][j] == '.'):
                    j += 1
                numero = self.ecra['text'][i+1:j]
                self.ecra['text'] = self.ecra['text'][:i] + f"math.sqrt({numero})" + self.ecra['text'][j:]
        try:
            resultado = eval(self.ecra['text'], {"__builtins__": None}, {"math": math})
            self.ecra['text'] = str(resultado)
        except Exception as e:
            self.ecra['text'] = "Erro"
            print(f"Erro ao calcular: {e}")


Calculadora = Tk()
Calculadora.title("Calculadora")
CalculadoraTk(Calculadora)
Calculadora.mainloop()













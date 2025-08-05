from tkinter import *


class App:
    def __init__(self, master=None):

        self.widget1 = Frame(master, bg="#EF8FFA")
        self.widget1.pack()

        self.ecra = Label(master, width= 30, height= 2, bg='#B509C8')
        self.ecra['text'] = ''
        self.ecra.pack(side="top")

        self.numeros_Frame = Frame(master, width= 25, height= 2)
        self.numeros_Frame["bg"] = 'White'
        self.numeros_Frame.pack()

        botoes = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "0", "/",
            "*", "+", "-",
             "=", "C"
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
        calculo = self.ecra['text']
        if any(op in calculo for op in ['/', '*', '+', '-']):
            calculado = eval(calculo)
            self.ecra['text'] = str(calculado)

root = Tk()
App(root)
root.mainloop()













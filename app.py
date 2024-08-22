from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class Application:
    def __init__(self, root):
        self.root = root
        
        # Título e cor de fundo
        self.root.title("Aplicativo Banco")
        self.root.configure(background="#1d1e1e")        
        
        # Tamanho da interface
        self.root.geometry('1060x600')
        self.root.resizable(False, False)  # Responsividade

        # Iniciando frame dentro da janela do app
        self.frame = Frame(self.root, bd=4, highlightbackground="#444949", highlightthickness=2, background='#2f3031')
        self.frame.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.75)

        self.saldo = 1000.00
        self.limite = 500

        self.defineNome()

        #Bind da tecla Enter na primeira tela (definir nome)
        self.root.bind('<Return>', self.enterNome)

    def defineNome(self):
        perguntaNome = Label(self.frame, text="Digite seu nome", font=('Arial', 14))
        perguntaNome.place(relx=0.425, rely=0.0)

        self.entry = Entry(self.frame, font=('Arial', 14))
        self.entry.place(relx=0.4, rely=0.1, relwidth=0.2)

        self.botao = Button(self.frame, text="Confirmar", font=('Arial', 14), command=self.inicializador)
        self.botao.place(relx=0.4, rely=0.2, relwidth=0.2)

    # Iniciando tela no root
    def inicializador(self):
        entry_text = self.entry.get()

        for widget in self.frame.winfo_children():
            widget.destroy()

        labelNome = Label(self.root, text=f"Bem vindo, {entry_text}", bg="#1d1e1e", fg="white", font=('Arial', 14))
        labelNome.place(relx=0.00, rely=0.03, relwidth=0.2)

        self.labelSaldo = Label(self.root, text=f"Saldo: R$ {self.saldo:.2f}", bg="#1d1e1e", fg="white", font=('Arial', 14))
        self.labelSaldo.place(relx=0.8, rely=0.03, relwidth=0.2)

        self.saque()
        self.deposito()
        self.botaoConfirmar()
        self.criarExtrato()

        # Atualiza o bind do Enter para o próximo botão "Confirmar"
        self.root.bind('<Return>', self.enterConfirma)

    #------------------------ Definindo Botão, Labels e Entrys -----------------------------------------------------------------------
    def saque(self):
        labelSaque = Label(self.root, text="Saque: ", bg="#1d1e1e", fg="white", font=('Arial', 14))
        labelSaque.place(relx=0.00, rely=0.15, relwidth=0.2)

        self.entrySaque = Entry(self.root, font=('Arial', 14))
        self.entrySaque.place(relx=0.13, rely=0.15, relwidth=0.2)

    def deposito(self):
        labelDeposito = Label(self.root, text="Depósito: ", bg="#1d1e1e", fg="white", font=('Arial', 14))
        labelDeposito.place(relx=0.49, rely=0.15, relwidth=0.2)

        self.entryDeposito = Entry(self.root, font=('Arial', 14))
        self.entryDeposito.place(relx=0.63, rely=0.15, relwidth=0.2)

    def botaoConfirmar(self):
        botaoConfirma = Button(self.root, text="Confirmar", font=('Arial', 14), command=self.pegaInfo, bg="#101527", fg="#11EC41")
        botaoConfirma.place(relx=0.85, rely=0.13)

    
#---------------------------------- Criando tabela com TTK -------------------------------------------------------------------------   
    def criarExtrato(self):
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(self.frame, columns=('Saque', 'Depósito', 'Saldo', 'Data/Hora'), show='headings', yscrollcommand=self.scrollbar.set)
        self.tree.pack(expand=True, fill=BOTH)

        self.tree.heading('Saque', text='Saque')
        self.tree.heading('Depósito', text='Depósito')
        self.tree.heading('Saldo', text='Saldo')
        self.tree.heading('Data/Hora', text='Data/Hora')

        self.scrollbar.config(command=self.tree.yview)
        
    # Função que faz a lógica de saque e Depósito
    def pegaInfo(self):
        saqueEntry = self.entrySaque.get()
        depositoEntry = self.entryDeposito.get()

        if saqueEntry == '' and depositoEntry == '':
            return  
        try:
            if saqueEntry:
                saque = float(saqueEntry)
                if saque <= self.limite:
                    if saque > 0:
                        if saque <= self.saldo:
                            self.saldo -= saque
                            self.entrySaque.delete(0, END)
                        else:
                            return messagebox.showinfo("Erro", "Saldo insuficiente para saque!")
                    else:
                        self.entrySaque.delete(0, END)
                        return messagebox.showinfo("Erro", "Digite um número válido!")
                else:
                    return messagebox.showinfo("Negado", "O saque excedeu o limite de 500 reais!")
            if depositoEntry:
                deposito = float(depositoEntry)
                if deposito > 0:
                    self.saldo += deposito
                    self.entryDeposito.delete(0, END)
                else:
                    self.entryDeposito.delete(0, END)
                    return messagebox.showinfo("Erro", "Digite um número válido!")
            
            if saqueEntry == '':
                saque = 0

            if depositoEntry == '':
                deposito = 0
            
            self.labelSaldo.config(text=f"Saldo: R$ {self.saldo:.2f}")

            data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            
            #Inserindo dados na tabela ttk
            self.tree.insert('', 'end', values=(f"R$ {saque:.2f}", f"R$ {deposito:.2f}", f"R$ {self.saldo:.2f}",data_hora))

        except ValueError:
            messagebox.showinfo("Erro", "Digite valores numéricos!")

    
    # Vinculando tecla Enter
    def enterNome(self, event):
        self.inicializador()

    def enterConfirma(self, event):
        self.pegaInfo()

# Inicialização da interface Tkinter
if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()

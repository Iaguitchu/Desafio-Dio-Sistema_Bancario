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
        self.root.resizable(False, False)

        # Iniciando frame dentro da janela do app
        self.frame = Frame(self.root, bd=4, highlightbackground="#444949", highlightthickness=2, background='#2f3031')
        self.frame.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.75)

        self.frame2 = Frame(self.root, bd=4, background='#1d1e1e')
        self.frame2.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.18)

        # self.saldo = 1000.00
        self.limite = 500
        self.lista_usuarios = []
        self.mostraUsuarios()

    def criaUsuario(self):
        self.limpa_tela()

        Label(self.frame, text="Cadastro de Usuário", bg="#2f3031", fg = "white", font=('Arial', 25)).pack()
        Label(self.frame, text="CPF", bg="#2f3031", fg = "white", font=('Arial', 14)).place(relx=0.150, rely=0.2)
        self.Cpf = Entry(self.frame)
        self.Cpf.place(relx=0.150, rely=0.30)

        Label(self.frame, text="Primeiro Nome",bg="#2f3031", fg = "white", font=('Arial', 14)).place(relx=0.150, rely=0.45)
        self.Nome = Entry(self.frame)
        self.Nome.place(relx=0.150, rely=0.55)

        Label(self.frame, text="Data de nascimento", bg="#2f3031", fg = "white", font=('Arial', 14)).place(relx=0.425, rely=0.2)
        self.DataNasc = Entry(self.frame)
        self.DataNasc.place(relx=0.425, rely=0.30)

        Label(self.frame, text="Endereço",bg="#2f3031", fg = "white", font=('Arial', 14)).place(relx=0.425, rely=0.45)
        self.Endereco = Entry(self.frame)
        self.Endereco.place(relx=0.425, rely=0.55)

        Button(self.frame, text="Salvar", bg='#2ac70e',font=('Arial',10,'bold'),command=self.salvarUsuario).place(relx=0.8, rely=0.85)
        Button(self.frame, text="Voltar", bg='red',fg="white",font=('Arial',10,'bold'),command=self.mostraUsuarios).place(relx=0.9, rely=0.85)

        self.root.bind('<Return>', lambda event: self.salvarUsuario())


    # Função para limpar a tela
    def limpa_tela(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        for widget in self.frame2.winfo_children():
            widget.destroy()

    def salvarUsuario(self):
        novo_cpf = self.Cpf.get()
        nome = self.Nome.get()

        if len(nome) > 15:
            return messagebox.showinfo("Aviso", "O nome tem que ter menos de 16 caracteres")

    
        # Verifica se o CPF já existe na lista de usuários
        for usuario in self.lista_usuarios:
            if usuario["cpf"] == novo_cpf:
                return messagebox.showinfo("Erro", "CPF já cadastrado!")

        usuario = {
            "cpf": self.Cpf.get(),
            "nome": self.Nome.get(),
            "data_nascimento": self.DataNasc.get(),
            "endereco": self.Endereco.get(),
            "contas": []
        }

        for k,i in usuario.items():
            if k != "contas":
                if len(i) == 0:
                    return messagebox.showinfo("Erro", "Nenhum campo pode ser vazio!")


        self.lista_usuarios.append(usuario)
        return self.mostraUsuarios()
    
    def mostraUsuarios(self):
        self.limpa_tela()
        
        x = 0.100
        y = 0.10

        Label(self.frame, text="Usuários Cadastrados", bg = '#2f3031', fg = 'white',font=('Arial', 16, 'bold')).pack()

        btnCriarUsuario = Button(self.frame, text="Criar Usuário", bg='#2ac70e', font=('Arial', 10,'bold'), command=self.criaUsuario)
        btnCriarUsuario.place(relx=0.45, rely=0.10)
        
        for index, usuario in enumerate(self.lista_usuarios):
            # Passa o índice do usuário para a função
            usuarioCadastrados = Button(self.frame, text=f"{usuario['nome']}", font=('Arial', 14,'bold'), width= 15,
                                        bg='#2f3031',fg="white", command=lambda idx=index: self.mostraConta(idx))
            y += 0.10 
            if y > 0.75:
                y = 0.20
                x += 0.200
            usuarioCadastrados.place(relx= x, rely= y)
       

    def mostraConta(self, usuario_index):
        self.limpa_tela()

        x = 0.100
        y = 0.10
        
        usuario = self.lista_usuarios[usuario_index]
        
        Label(self.frame2, text=f"Bem vindo, {usuario['nome']}",
               bg = '#2f3031', fg = 'white', font=('Arial', 12)).place(relx=0.0, rely=0.10)
        
        Label(self.frame2, text=f"CPF {usuario['cpf']}",
               bg = '#2f3031', fg = 'white', font=('Arial', 12)).place(relx=0.25, rely=0.10)
        
        Label(self.frame2, text=f"Data Nasc {usuario['data_nascimento']}",
               bg = '#2f3031', fg = 'white', font=('Arial', 12)).place(relx=0.45, rely=0.10)
        
        Label(self.frame2, text=f"Endereço {usuario['endereco']}",
               bg = '#2f3031', fg = 'white', font=('Arial', 12)).place(relx=0.65, rely=0.10)
        
        for count, conta in enumerate(usuario["contas"]):
            self.contaBanco = Button(self.frame, text=f"Agência: {conta['agencia']} - C/C: {conta['conta_corrente']}", font=('Arial', 14,'bold'),
                                      width= 25, bg='#2f3031',fg="white",command=lambda c=count: self.inicializador(usuario_index, c))
            y += 0.10 
            if y > 0.75:
                y = 0.20
                x += 0.400
            self.contaBanco.place(relx= x, rely= y)
        
        btnAdicionarConta = Button(self.frame, text="Adicionar Conta", bg='#2ac70e', font=('Arial',10,'bold'),command=lambda: self.adicionarConta(usuario_index))
        btnAdicionarConta.pack()

        btnVoltar = Button(self.frame, text="Voltar", bg="red", fg="white",font=('Arial',10,'bold'),command=self.mostraUsuarios)
        btnVoltar.place(relx=0.90, rely=0.85)


    def adicionarConta(self, usuario_index):
        self.limpa_tela()
        
        usuario = self.lista_usuarios[usuario_index]
        
        Label(self.frame, text=f"Adicionar Conta para {usuario['nome']}", bg="#2f3031", fg = "white", font=('Arial', 25)).pack()

        Label(self.frame, text="Agência:", bg="#2f3031", fg = "white",font=('Arial', 14)).place(relx=0.150, rely=0.2)
        agencia_entry = Entry(self.frame)
        agencia_entry.place(relx=0.150, rely=0.3)

        Label(self.frame, text="C/C:", bg="#2f3031", fg = "white",font=('Arial', 14)).place(relx=0.425, rely=0.2)
        conta_corrente_entry = Entry(self.frame)
        conta_corrente_entry.place(relx = 0.425, rely=0.3)

        btnSalvarConta = Button(self.frame, text="Salvar", bg="#2ac70e", font=('Arial',10,'bold'), command=lambda: self.salvarConta(usuario['nome'],usuario_index, agencia_entry.get(), conta_corrente_entry.get()))
        btnSalvarConta.pack()

        btnVoltar = Button(self.frame, text="Voltar", bg="red", fg="white",font=('Arial',10,'bold'), command=lambda: self.mostraConta(usuario_index))
        btnVoltar.place(relx=0.90, rely=0.85)

    def salvarConta(self, nome ,usuario_index, agencia, conta_corrente):
        if len(agencia) > 5 or len(conta_corrente) > 5:
            return messagebox.showinfo("Aviso!", "Agencia e Conta corrente só podem ter no máximo 5 caracteres!")
        if len(agencia) == 0 or len(conta_corrente) == 0:
            return messagebox.showinfo("Aviso!", "Todos os campos são obrigatórios!")

        self.lista_usuarios[usuario_index]["contas"].append({
            "usuario":nome,
            "agencia": agencia,
            "conta_corrente": conta_corrente,
            "saldo":1000,
            "extrato":[]
        })
        self.mostraConta(usuario_index)

    

    # Iniciando tela no root
    def inicializador(self, usuario_index, conta_index):
        self.limpa_tela()

        usuario = self.lista_usuarios[usuario_index]
        conta = usuario['contas'][conta_index]

        labelNome = Label(self.frame2, text=f"Bem vindo, {usuario['nome']}", bg="#1d1e1e", fg="white", font=('Arial', 14))
        labelNome.place(relx=0.00, rely=0.03, relwidth=0.2)

        self.labelSaldo = Label(self.frame2, text=f"Saldo: R$ {conta['saldo']:.2f}", bg="#1d1e1e", fg="white", font=('Arial', 14))
        self.labelSaldo.place(relx=0.8, rely=0.03, relwidth=0.2)

        self.saque()
        self.deposito()
        self.botaoConfirmar(usuario_index, conta_index)
        self.criarExtrato(usuario_index, conta_index)
        self.botaoSair(usuario_index)
        

        # Atualiza o bind do Enter para o próximo botão "Confirmar"
        self.root.bind('<Return>', lambda event: self.pegaInfo(usuario_index, conta_index))


    #------------------------ Definindo Botão, Labels e Entrys -----------------------------------------------------------------------
    def saque(self):
        labelSaque = Label(self.frame2, text="Saque: ", bg="#1d1e1e", fg="white", font=('Arial', 14))
        labelSaque.place(relx=0.00, rely=0.60, relwidth=0.2)

        self.entrySaque = Entry(self.frame2, font=('Arial', 14))
        self.entrySaque.place(relx=0.13, rely=0.60, relwidth=0.2)

    def deposito(self):
        labelDeposito = Label(self.frame2, text="Depósito: ", bg="#1d1e1e", fg="white", font=('Arial', 14))
        labelDeposito.place(relx=0.49, rely=0.60, relwidth=0.2)

        self.entryDeposito = Entry(self.frame2, font=('Arial', 14))
        self.entryDeposito.place(relx=0.63, rely=0.60, relwidth=0.2)

    def botaoConfirmar(self, usuario_index, conta_index):
        botaoConfirma = Button(self.frame2, text="Confirmar", font=('Arial', 14), command=lambda: self.pegaInfo(usuario_index, conta_index), bg="#101527", fg="#11EC41")
        botaoConfirma.place(relx=0.85, rely=0.60)

    def botaoSair(self, usuario_index):
        botaoSair = Button(self.frame2, text="Sair", font=('Arial', 14), command=lambda: self.mostraConta(usuario_index), bg="#101527", fg="#11EC41")
        botaoSair.place(relx=0.95, rely=0.60)


    
#---------------------------------- Criando tabela com TTK -------------------------------------------------------------------------   
    def criarExtrato(self, usuario_index, conta_index):
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(self.frame, columns=('Saque', 'Depósito', 'Saldo', 'Data/Hora'), show='headings', yscrollcommand=self.scrollbar.set)
        self.tree.pack(expand=True, fill=BOTH)

        self.tree.heading('Saque', text='Saque')
        self.tree.heading('Depósito', text='Depósito')
        self.tree.heading('Saldo', text='Saldo')
        self.tree.heading('Data/Hora', text='Data/Hora')

        self.scrollbar.config(command=self.tree.yview)

        # Preencher o Treeview com o histórico de transações
        conta = self.lista_usuarios[usuario_index]["contas"][conta_index]
        for transacao in conta['extrato']:
            saque = transacao['saque']
            deposito = transacao['deposito']
            saldo = conta['saldo']  
            data_hora = transacao['data_hora']
            self.tree.insert('', 'end', values=(f"R$ {saque:.2f}" if saque else '', f"R$ {deposito:.2f}" if deposito else '', f"R$ {saldo:.2f}", data_hora))

        
    # Função que faz a lógica de saque e Depósito
    def pegaInfo(self, usuario_index, conta_index):
        saqueEntry = self.entrySaque.get()
        depositoEntry = self.entryDeposito.get()

        if saqueEntry == '' and depositoEntry == '':
            return

        conta = self.lista_usuarios[usuario_index]["contas"][conta_index]
        saldo = conta['saldo']

        try:
            if saqueEntry:
                saque = float(saqueEntry)
                if saque <= self.limite:
                    if saque > 0:
                        if saque <= saldo:
                            saldo -= saque
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
                    saldo += deposito
                    self.entryDeposito.delete(0, END)
                else:
                    self.entryDeposito.delete(0, END)
                    return messagebox.showinfo("Erro", "Digite um número válido!")

            if saqueEntry == '':
                saque = 0

            if depositoEntry == '':
                deposito = 0
            
            # Atualiza o saldo na conta
            conta['saldo'] = saldo
            self.labelSaldo.config(text=f"Saldo: R$ {saldo:.2f}")

            # Adiciona a transação ao extrato
            data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            conta['extrato'].append({'saque': saque, 'deposito': deposito, 'saldo': saldo,'data_hora': data_hora})

            # Inserindo dados na tabela ttk
            self.tree.insert('', 'end', values=(f"R$ {saque:.2f}", f"R$ {deposito:.2f}", f"R$ {saldo:.2f}", data_hora))

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

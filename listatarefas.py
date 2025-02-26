import tkinter as tk 
from tkinter import messagebox


class tela():
    def adicionar_tarefa(self, tabela):
        self.tabela = tabela
        self.tabela.title(" Gestão de Tarefas ")

        #criação de widgets
        self.createwidgets()
     
    def createwidgets(self):
        tk.Label(self.tabela, text= 'Nome da tarefa:').grid(row=1, column=0)
        tk.Label(self.tabela, text= 'Descrição:').grid(row=2, column=0)
        tk.Label(self.tabela, text= 'Data:').grid(row=3, column=0)
        tk.Label(self.tabela, text= 'Hora:').grid(row=4, column=0)


        #Criação de caixas de textos
        self.nome_entry = tk.Entry(self.tabela)
        self.descricao_entry = tk.Entry(self.tabela)
        self.data_entry = tk.Entry(self.tabela)
        self.hora_entry = tk.Entry(self.tabela)





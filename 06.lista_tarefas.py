import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
from ttkbootstrap.constants import *

class ToDoListApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Lista de tarefas")
        self.janela.geometry("300x400")
        self.fonte = ("Verdana", "12")

        self.container1 = ttk.Frame(janela)
        self.container1.pack()
        self.container2 = ttk.Frame(janela)
        self.container2.pack()
        self.container3 = ttk.Frame(janela)
        self.container3.pack()
        self.container4 = ttk.Frame(janela)
        self.container4.pack()

        self.titulo = ttk.Label(self.container1, bootstyle="light", text="Insira uma tarefa no campo abaixo")
        self.titulo.pack(pady=5)
        self.entrada = ttk.Entry(self.container1, bootstyle="info")
        self.entrada.pack(side=LEFT, padx=30, pady=5)
        self.titulo = ttk.Label(self.container2, bootstyle="light", text="Lista de Tarefas", font=15)
        self.titulo.pack(pady=10)
        self.lista = Listbox(self.container3)
        self.lista.pack(pady=10)
        self.b1 = ttk.Button(self.container4, text="Criar", bootstyle=SUCCESS, command=self.adicionar_tarefa)
        self.b1.grid(row=0, column=0)
        self.b2 = ttk.Button(self.container4, text="Apagar", bootstyle=DANGER, command=self.remover_tarefa)
        self.b2.grid(row=0, column=1)
        
    def adicionar_tarefa(self):
        lista_tarefas = []
        tarefa = self.entrada.get()
        lista_tarefas.append(tarefa)
        for i in lista_tarefas:
            self.lista.insert(len(i)+1, i)
        self.entrada.delete(0, tk.END)
    
    def remover_tarefa(self):
        tarefa_selecionada = self.lista.curselection()
        if tarefa_selecionada:
            tarefa_removida = self.lista.get(tarefa_selecionada[0])
            self.lista.delete(tarefa_selecionada[0])
            self.lista_tarefas.remove(tarefa_removida)
        else:
            tk.messagebox.showwarning("Seleção Vazia", "Por favor, selecione uma tarefa para remover.")

    

    






def main():
    janela = ttk.Window(themename="darkly")
    lista = ToDoListApp(janela)
    janela.mainloop()

if __name__ == "__main__":
    main()
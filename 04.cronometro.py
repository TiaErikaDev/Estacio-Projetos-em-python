from tkinter import *

class Cronometro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cronômetro")
        
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.ativo = False

        self.visor = Label(janela, text=f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}", font=("Helvetica", 24))
        self.visor.pack(pady=20)

        self.parar = Button(text="Parar", command=self.parar)
        self.parar.pack(side=LEFT, padx=10)
        
        self.zerar = Button(text="Zerar", command=self.zerar)
        self.zerar.pack(side=LEFT, padx=10)

        self.iniciar = Button(text="Iniciar", command=self.iniciar)
        self.iniciar.pack(side=LEFT, padx=10)

    
    def atualizarTempo(self):
        if self.ativo:
            self.segundos += 1
            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1
                if self.minutos == 60:
                    self.minutos = 0
                    self.horas += 1
        
        self.visor.config(text=f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}")
        self.janela.after(1000, self.atualizarTempo)
    
    def iniciar(self):
        if not self.ativo:
            self.ativo = True
            self.atualizarTempo()

    def parar(self):
        self.ativo = False

    def zerar(self):
        self.ativo = False
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.visor.config(text=f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}")

def main():
    janela = Tk()
    stopwatch = Cronometro(janela)
    janela.mainloop()
                
if __name__ == "__main__":
    main()







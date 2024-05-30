from tkinter import *
from tkinter import messagebox

class CalculadoraIMC:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora IMC")

        self.titulo = Label(janela, text="Calculadora IMC", font=("Times New Roman", 20))
        self.titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        self.altura_label = Label(janela, text="ALTURA (m)", font=("Times New Roman", 15))
        self.altura_label.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")

        self.altura_entry = Entry(janela)
        self.altura_entry.grid(column=0, row=2, padx=10, pady=10, sticky="nsew")

        self.peso_label = Label(janela, text="PESO (kg)", font=("Times New Roman", 15))
        self.peso_label.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")

        self.peso_entry = Entry(janela)
        self.peso_entry.grid(column=1, row=2, padx=10, pady=10, sticky="nsew")

        self.botao_resultado = Button(janela, text="Calcular IMC", command=self.calculo_imc)
        self.botao_resultado.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        self.resultado = StringVar()
        self.resultado_label = Label(janela, textvariable=self.resultado,  font=("Times New Roman", 20))
        self.resultado_label.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

    def calculo_imc(self):
        try:
            peso = float(self.peso_entry.get())
            altura = float(self.altura_entry.get())
            imc = peso / (altura ** 2)
            self.resultado.set(f"Seu IMC é: {imc:.2f}")
            
            if imc < 18.5:
                categoria = "Abaixo do peso"
            elif 18.5 <= imc < 24.9:
                categoria = "Peso normal"
            elif 25 <= imc < 29.9:
                categoria = "Sobrepeso"
            else:
                categoria = "Obesidade"
            
            messagebox.showinfo("Resultado", f"Seu IMC é: {imc:.2f}\nCategoria: {categoria}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

def main():
    janela = Tk()
    calculadora = CalculadoraIMC(janela)
    janela.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk

# Função para calcular a área do triângulo
def calcular_area(base, altura):
    area = (base * altura) / 2
    return area

# Função para calcular e mostrar o resultado
def calcular_e_mostrar():
    base = float(base_entry.get())
    altura = float(altura_entry.get())
    area = calcular_area(base, altura)
    resultado_label.config(text=f"Área do triângulo: {area:.2f}")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de Área de Triângulo")

# Cria os widgets
base_label = tk.Label(root, text="Base do triângulo:")
base_label.grid(row=0, column=0)

base_entry = tk.Entry(root)
base_entry.grid(row=0, column=1)

altura_label = tk.Label(root, text="Altura do triângulo:")
altura_label.grid(row=1, column=0)

altura_entry = tk.Entry(root)
altura_entry.grid(row=1, column=1)

calcular_button = tk.Button(root, text="Calcular", command=calcular_e_mostrar)
calcular_button.grid(row=2, column=0, columnspan=2)

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=3, column=0, columnspan=2)

# Inicia a janela
root.mainloop()
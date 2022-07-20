import tkinter as tk
from tkinter import font
from turtle import color
import cpfutil


root = tk.Tk()

def validate_cpf(stringvar: tk.StringVar, button: tk.Button):
    cpf = stringvar.get()
    
    if cpfutil.is_valid(cpf):
        button.config(
            text='CPF VÁLIDO!', activeforeground='green', foreground='green',
        )
    else:
        button.config(
            text='CPF INVÁLIDO!', activeforeground='red', foreground='red',
        )
        
def generate_cpf(stringvar: tk.StringVar, button: tk.Button):
    cpf = cpfutil.generate()
    cpf_formatado = cpfutil.formater(cpf)
    stringvar.set(cpf_formatado)

main_title = tk.Label(
    root, 
    text="Gerador/Validador de CPF",   #Cria um label com o texto "CPF Generator"
    bg='#28282b',
    font=('Helvetica', 14, 'bold'),
    fg='#ffffff'
)
main_title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

validate_label = tk.Label(root, text="Validar", bg='#28282b', font=('Helvetica', 11, 'bold'), fg='#ffffff')
validate_label.grid(row=1, column=0, pady=10)

validate_stringvar = tk.StringVar()
validate_entry = tk.Entry(root, bd=5, relief='flat', width=20, font=('Helvetica', 11), textvariable=validate_stringvar, highlightthickness=1)
validate_entry.grid(row=1, column=1, pady=10)

validate_button = tk.Button(root, text="Validar", bg='#28282b', font=('Helvetica', 11, 'bold'), fg='#ffffff')
validate_button.grid(row=1, column=2, sticky='we')
validate_button.config(command=lambda: validate_cpf(
     validate_stringvar, validate_button
))


generate_label = tk.Label(root, text="Gerar:", bg='#28282b', font=('Helvetica', 11, 'bold'), fg='#ffffff')
generate_label.grid(row=2, column=0, pady=10)

generate_stringvar = tk.StringVar()
generate_entry = tk.Entry(root, bd=5, relief='flat', width=20, font=('Helvetica', 11), textvariable=generate_stringvar, highlightthickness=1)
generate_entry.grid(row=2, column=1, pady=10)

generate_button = tk.Button(root, text="Gerar", bg='#28282b', font=('Helvetica', 11, 'bold'), fg='#ffffff')
generate_button.grid(row=2, column=2, sticky='we')
generate_button.config(command=lambda: generate_cpf(
     generate_stringvar, validate_button
))

root.title('Gerador/Validador de CPF by @diwalker')
root.config(background='#28282b', padx=20, pady=20)
root.mainloop()
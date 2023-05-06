import random
import string
import tkinter as tk

#Define la clase PasswordGenerator y su método constructor:
class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        root.iconbitmap('logo.ico')
        self.root.title("Generador de contraseñas JM")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        #Dentro del método constructor, crea los elementos de la GUI necesarios: 
        #   etiquetas, campos de entrada y botones
        self.length_var = tk.StringVar()
        self.length_var.set("5")
        self.password_var = tk.StringVar()
        
        length_label = tk.Label(self.root, text="Numero de Caracteres:", fg="black")
        length_label.grid(row=0, column=0, padx=10, pady=10)
        
        length_entry = tk.Entry(self.root, textvariable=self.length_var)
        length_entry.grid(row=0, column=1, padx=10, pady=10)
        
        generate_button = tk.Button(self.root, text="Generar Contraseña", command=self.generate_password, bg="#9DCDF5", fg="black")
        generate_button.grid(row=1, column=0, padx=10, pady=10)
        
        password_label = tk.Label(self.root, text="Contraseña:" , fg="black")
        password_label.grid(row=2, column=0, padx=10, pady=10)
        
        password_entry = tk.Entry(self.root, textvariable=self.password_var, state="readonly")
        password_entry.grid(row=2, column=1, padx=10, pady=10,)
# generará la contraseña en base a la longitud ingresada
    def generate_password(self):
        length = int(self.length_var.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.password_var.set(password)
#ejecuta el programa con la siguiente línea:

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
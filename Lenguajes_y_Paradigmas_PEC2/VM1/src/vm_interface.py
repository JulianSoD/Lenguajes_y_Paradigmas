import tkinter as tk
from tkinter import filedialog, messagebox
from src.virtual_machine import VirtualMachine

class VMInterface:
    def __init__(self, master):
        self.master = master
        master.title("Máquina Virtual")
        master.geometry("400x400") 
        master.configure(bg="#f0f0f0")

        self.vm = VirtualMachine()

        self.label = tk.Label(master, text="Introduce la operación:", bg="#f0f0f0")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=30)
        self.entry.pack(pady=10)

        self.run_button = tk.Button(master, text="Ejecutar", command=self.run, bg="#4CAF50", fg="white")
        self.run_button.pack(pady=5)

        self.attach_button = tk.Button(master, text="Adjuntar archivo", command=self.attach_file, bg="#2196F3", fg="white")
        self.attach_button.pack(pady=5)

        self.download_button = tk.Button(master, text="Descargar archivo", command=self.download_audio, bg="#FF5722", fg="white")
        self.download_button.pack(pady=5)

        self.output_label = tk.Label(master, text="", bg="#f0f0f0")
        self.output_label.pack(pady=10)

        self.stack_label = tk.Label(master, text="Estado de la pila: []", bg="#f0f0f0")
        self.stack_label.pack(pady=10)

    def run(self):
        operation = self.entry.get()
        try:
            result = self.vm.execute(operation)
            self.output_label.config(text=f"Resultado de la operación y número de compases: {result}")
            self.stack_label.config(text=f"Estado de la pila: {self.vm.stack}")

        except Exception as e:
            self.output_label.config(text=f"Error: {e}")

    def attach_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                result = self.vm.execute_from_file(file_path)
                self.output_label.config(text=f"Resultado final: {result}")
                self.stack_label.config(text=f"Estado de la pila: {self.vm.stack}")
            except Exception as e:
                self.output_label.config(text=f"Error al leer el archivo: {e}")

    def download_audio(self):
        if self.vm.stack:
            result = self.vm.stack[-1] 
            if 0 <= result <= 29:
                file_path = filedialog.asksaveasfilename(defaultextension=".wav",
                                                           filetypes=[("WAV files", "*.wav")],
                                                           initialfile="")
                if file_path: 
                    self.vm.create_audio(result, file_path) 
                    messagebox.showinfo("Éxito", f"Archivo WAV generado en: {file_path}")
                else:
                    messagebox.showwarning("Advertencia", "No se ha seleccionado un nombre de archivo.")
            else:
                messagebox.showwarning("Advertencia", "El resultado no está en el rango de 0 a 29.")
        else:
            messagebox.showwarning("Advertencia", "La pila está vacía.")

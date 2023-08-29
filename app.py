import tkinter as tk
import socket
import os

class InfoWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("SkalaInfo Display")
        self.root.geometry("300x150")
        self.root.overrideredirect(True)  # Remover a barra de título
        self.root.attributes("-topmost", True)  # Mantém a janela no topo

        # Tornar a janela um pouco transparente
        self.root.attributes("-alpha", 0.8)

        # Posiciona a janela no canto inferior direito
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"+{screen_width - 300}+{screen_height - 150}")

        # Logo da empresa
        self.logo_path = "caminho_para_o_logo.png"
        self.logo = tk.PhotoImage(file=self.logo_path)
        self.logo_label = tk.Label(root, image=self.logo)
        self.logo_label.pack()

        # Informações
        self.hostname_label = tk.Label(root, text=f"Nome do Computador: {socket.gethostname()}")
        self.hostname_label.pack()
        
        self.ip_label = tk.Label(root, text=f"Endereço IP: {socket.gethostbyname(socket.gethostname())}")
        self.ip_label.pack()

        self.user_label = tk.Label(root, text=f"Usuário Conectado: {os.getlogin()}")
        self.user_label.pack()

        self.network_label = tk.Label(root, text="Rede Conectada: Verifique no sistema")
        self.network_label.pack()

        # Botão de fechar
        self.close_button = tk.Button(root, text="Fechar", command=root.destroy)
        self.close_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = InfoWindow(root)
    root.mainloop()

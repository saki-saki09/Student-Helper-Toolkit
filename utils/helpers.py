from colorama import init, Fore, Style
import os

init(autoreset=True)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input(Fore.YELLOW + "\nPress Enter to continue...")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + f"\n{text}")
    print(Fore.CYAN + "=" * len(text))


def success(msg):
    print(Fore.GREEN + f"✅ {msg}")


def error(msg):
    print(Fore.RED + f"❌ {msg}")


def info(msg):
    print(Fore.BLUE + f"ℹ️ {msg}")
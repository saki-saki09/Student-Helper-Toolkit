from modules import calculator, file_renamer, organizer, graph_generator
from utils.helpers import clear, pause, title, error


def show_logo():
    try:
        with open("assets/logo.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except:
        print("Student Helper Toolkit")

def show_menu():
    clear()
    show_logo()
    title("Student Helper Toolkit v1.0")

    print("1. 🧮 Calculator")
    print("2. 📁 File Renamer")
    print("3. 📂 File Organizer")
    print("4. 📊 Graph Generator")
    print("5. ❌ Exit")
    print("=" * 35)


def run():
    while True:
        show_menu()
        choice = input("👉 Choose option: ").strip()

        if choice == '1':
            calculator.run()
        elif choice == '2':
            file_renamer.run()
        elif choice == '3':
            organizer.run()
        elif choice == '4':
            graph_generator.run()
        elif choice == '5':
            print("\n👋 Goodbye!")
            break
        else:
            error("Invalid choice!")

        pause()


if __name__ == "__main__":
    run()
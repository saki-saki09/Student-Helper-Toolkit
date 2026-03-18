import matplotlib.pyplot as plt
from utils.helpers import title, error, success, info


def run():
    title("📊 Graph Generator")

    info("Enter values separated by space (example: 1 2 3 4)")

    try:
        x = list(map(float, input("Enter X values: ").split()))
        y = list(map(float, input("Enter Y values: ").split()))

        if len(x) != len(y):
            error("X and Y must have same length!")
            return

        info("Generating graph...")

        plt.plot(x, y, marker='o')
        plt.title("Generated Graph")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid()

        plt.show()

        success("Graph displayed successfully!")

    except:
        error("Invalid input!")
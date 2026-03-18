from utils.helpers import title, error, success, info


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            error("Please enter a valid number!")


def basic_mode():
    title("🧮 Basic Calculator")

    a = get_number("Enter first number: ")
    op = input("Operator (+, -, *, /, %, **): ").strip()
    b = get_number("Enter second number: ")

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            error("Cannot divide by zero!")
            return
        result = a / b
    elif op == '%':
        result = a % b
    elif op == '**':
        result = a ** b
    else:
        error("Invalid operator!")
        return

    success(f"Result: {result}")


def expression_mode():
    title("⚡ Expression Calculator")
    info("Example: 2 + 3 * 5")

    expr = input("Enter expression: ")

    try:
        allowed_chars = "0123456789+-*/(). %"
        for char in expr:
            if char not in allowed_chars:
                error("Invalid character detected!")
                return

        result = eval(expr)
        success(f"Result: {result}")

    except:
        error("Invalid expression!")


def run():
    print("\n1. Basic Mode")
    print("2. Expression Mode")

    choice = input("Choose mode: ")

    if choice == '1':
        basic_mode()
    elif choice == '2':
        expression_mode()
    else:
        error("Invalid choice!")
a, operation, b = input("Enter initial operation (e.g., '10 + 5'): ").split()
a, b = int(a), int(b)

valid_operations = {"+", "-", "*", "/", "%"}

if operation not in valid_operations:
    print("Only +, -, *, /, % are supported.")
else:
    match operation:
        case '+': a += b
        case '-': a -= b
        case '*': a *= b
        case '/': a //= b  # Integer division
        case '%': a %= b
        case _: pass
    print(f"Result: {a}")

while True:
    user_input = input("Enter operation and number (or 'q' to quit): ").split()
    
    if user_input[0] == 'q':  # Exit condition
        print("Exiting...")
        break

    if len(user_input) != 2:
        print("Invalid input. Use format: '+ 5' or 'q' to quit.")
        continue

    operation, b = user_input
    b = int(b)

    if operation not in valid_operations:
        print("Only +, -, *, /, % are supported.")
        continue

    match operation:
        case '+': a += b
        case '-': a -= b
        case '*': a *= b
        case '/': a //= b
        case '%': a %= b
        case _: continue

    print(f"Result: {a}")

# __main__.py
import argparse
from calculator import Calculator

calc = Calculator()


def main():
    parser = argparse.ArgumentParser(description="Simple Calculator")
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide", "root", "reset"],
        help="The operation to perform",
    )
    parser.add_argument(
        "value", type=float, nargs="?", default=0, help="The value to operate on"
    )

    args = parser.parse_args()

    # this variable is used to process the command line input once
    init_call = True
    while True:
        if init_call:
            process_operation(args.operation, args.value)
            init_call = False
        exit_input = input(
            "Type 'exit' to quit the calculator or enter the new operation: "
        )
        if exit_input.lower() == "exit":
            break
        if len(exit_input.split(" ")) > 1:
            args.operation = exit_input.split(" ")[0]
            try:
                args.value = float(exit_input.split(" ")[1])
            except ValueError as e:
                print(e)
                continue
            process_operation(args.operation, args.value)
        else:
            args.operation = exit_input.split(" ")[0]
            process_operation(args.operation, args.value)


def process_operation(operation: str, value: float) -> None:
    try:
        if operation == "add":
            print(f"Result: {calc.add(value)}")
        elif operation == "subtract":
            print(f"Result: {calc.subtract(value)}")
        elif operation == "multiply":
            print(f"Result: {calc.multiply(value)}")
        elif operation == "divide":
            print(f"Result: {calc.divide(value)}")
        elif operation == "root":
            print(f"Result: {calc.root(value)}")
        elif operation == "reset":
            print(f"Result: {calc.reset()}")
        else:
            print("Not supported operation.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: Division by Zero"

def main():
    # Berekeningen
    results = []
    results.append(f"Addition: {add(100, 10)}")
    results.append(f"Subtraction: {subtract(100, 10)}")
    results.append(f"Multiplication: {multiply(100, 10)}")
    results.append(f"Division: {divide(100, 10)}")

    # Schrijf de resultaten naar een tekstbestand
    with open("output.txt", "w") as file:
        for result in results:
            file.write(result + "\n")
    
    print("Results have been written to output.txt")

if __name__ == "__main__":
    main()

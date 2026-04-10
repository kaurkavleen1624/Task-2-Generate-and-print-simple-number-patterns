# Task-2-Generate-and-print-simple-number-patterns
Level 1-Task2 - Optimized Python number pyramid pattern using nested loops for structure control
# 🔺 Number Pyramid Pattern (Python)

This project prints a **right-aligned number pyramid pattern** using Python and nested loops.

## 📌 Description
The program generates a pyramid where:
- Each row contains the same number repeated
- The number corresponds to the row number
- The pyramid is right-aligned using spaces

## 🧠 Concept Used
- Nested loops
- String multiplication
- Basic pattern printing logic in Python

## 💻 Code

```python
def print_number_pyramid(rows):
    """Generate right-aligned number pyramid pattern using nested loops."""
    for i in range(1, rows + 1):
        # Print leading spaces for alignment
        print(" " * (rows - i), end="")
        # Print row number i times
        for j in range(i):
            print(i, end=" ")
        print()  # New line

# Main execution - configurable height
HEIGHT = 5
print(f"TII Task 2: Number Pyramid Pattern (Height: {HEIGHT})")
print("-" * 35)
print_number_pyramid(HEIGHT)

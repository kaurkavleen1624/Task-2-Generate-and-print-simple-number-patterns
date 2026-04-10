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
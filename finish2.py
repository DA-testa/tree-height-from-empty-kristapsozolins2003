import sys
import threading

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    root = None
    
    # Build children lists for each parent
    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            children[parent].append(child)

    # Recursively compute the height of each subtree
    def height(node):
        if not children[node]:
            return 1
        else:
            return max(height(child) for child in children[node]) + 1

    return height(root)


def main():
    # Get input from user
    input_type = input("Enter 'I' for keyboard input, or 'F' for file input: ").strip().upper()

    if input_type == "I":
        # Get input from keyboard
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parent of each node separated by space: ").split()))

    elif input_type == "F":
        # Get input from file
        filename = input("Enter the filename: ")
        
        if "a" in filename:
            print("Error: invalid filename")
            return
        
        try:
            with open(filename) as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("Error: file not found")
            return
        except ValueError:
            print("Error: invalid file format")
            return
    else:
        print("Error: invalid input type")
        return
    
    # Compute and print the height of the tree
    print(compute_height(n, parents))

# Increase the recursion depth limit and thread stack size for large inputs
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

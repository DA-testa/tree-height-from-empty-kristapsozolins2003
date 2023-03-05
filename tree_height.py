import sys
import threading

def compute_height(n, parents):
    # Initialize an empty list of children for each node
    children = [[] for _ in range(n)]

    # Find the root node and build the list of children for each node
    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            children[parent].append(child)

    # Define a recursive function to compute the height of a node
    def compute_node_height(node):
        # Base case: if the node has no children, its height is 1
        if not children[node]:
            return 1
        # Recursive case: compute the height of each child and return the maximum
        else:
            child_heights = [compute_node_height(child) for child in children[node]]
            return max(child_heights) + 1

    # Compute the height of the root node
    return compute_node_height(root)



def main():
    # Get input method from user
    input_method = input("Enter 'I' for keyboard input or 'F' for file input: ")
    
    # Handle keyboard input
    if input_method == "I":
        # Get number of elements from user
        n = int(input("Enter the number of elements: "))
        # Get values from user, separated by spaces, and convert to list of integers
        parents = list(map(int, input("Enter the values separated by spaces: ").split()))
    
    # Handle file input
    elif input_method == "F":
        # Get file name from user and construct file path
        file_name = input("Enter the file name (without 'a'): ")
        if "a" in file_name:
            print("Invalid file name")
            return
        file_path = f"./test/{file_name}"
        
        # Try to read file and parse input
        try:
            with open(file_path) as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except Exception as e:
            print("Error:", str(e))
            return
    
    # Handle invalid input method
    else:
        print("Invalid input method")
        return
    
    # Call compute_height and print result
    print(compute_height(n, parents))


# Increase the recursion depth limit and thread stack size for large inputs
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

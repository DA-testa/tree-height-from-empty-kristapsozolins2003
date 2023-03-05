import sys
import threading


def find_tree_height(num_nodes, parent_nodes):
    child_nodes = [[] for _ in range(num_nodes)]
    root_node = None
    
    for i, parent in enumerate(parent_nodes):
        if parent == -1:
            root_node = i
        else:
            child_nodes[parent].append(i)
    
    # Define a recursive function to calculate the height of the tree
    def calc_height(node):
        height = 1
        
        if not child_nodes[node]:
            return height
        else:
            for child in child_nodes[node]:
                height = max(height, calc_height(child))
            
            return height + 1
    
    # Call the recursive function to calculate the height of the tree
    return calc_height(root_node)


def main():
    input_type = input("Enter 'I' for keyboard input or 'F' for file input: ")
    
    if input_type == "I":
        # Get number of nodes and parent node values from user input
        num_nodes = int(input("Enter the number of nodes: "))
        parent_nodes = list(map(int, input("Enter parent node values separated by spaces: ").split()))
    
    elif input_type == "F":
        # Get file name from user input
        file_name = input("Enter the file name: ")
        
        if "a" in file_name:
            print("Error: File name cannot contain the letter 'a'.")
            return
        
        try:
            # Read number of nodes and parent node values from file
            with open(f"./test/{file_name}", "r") as file:
                num_nodes = int(file.readline().strip())
                parent_nodes = list(map(int, file.readline().strip().split()))
        except Exception as e:
            print(f"Error: {e}")
            return
    else:
        print("Error: Invalid input type. Please enter 'I' or 'F'.")
        return
    
    # Calculate and output the height of the tree
    print(find_tree_height(num_nodes, parent_nodes))


sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()

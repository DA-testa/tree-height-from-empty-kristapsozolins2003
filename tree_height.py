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
    # Check for file input
    try:
        with open('input.txt') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    except FileNotFoundError:
        # Read input from standard input
        n = int(input())
        parents = list(map(int, input().split()))

    # Compute and print the height of the tree
    print(compute_height(n, parents))

# Increase the recursion depth limit and thread stack size for large inputs
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

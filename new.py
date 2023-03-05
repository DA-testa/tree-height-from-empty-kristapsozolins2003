import sys
import numpy as np
import threading

sys.setrecursionlimit(10 ** 7)

def compute_height(n, parents):
    heights = [-1] * n
    
    def get_height(node):
        if heights[node] != -1:
            return heights[node]
        if parents[node] == -1:
            heights[node] = 1
        else:
            heights[node] = 1 + get_height(parents[node])
        return heights[node]
    
    max_height = 0
    for node in range(n):
        if heights[node] == -1:
            max_height = max(max_height, get_height(node))
    
    return max_height

def main():
    input_type = input().strip()[0]
    if input_type == "F":
        filename = input().strip()
        try:
            with open(filename) as f:
                n = int(f.readline().strip())
                parents = np.array(f.readline().strip().split(), dtype=int)
        except FileNotFoundError:
            print("Error: File or path has been inputted incorectly")
            return
    elif input_type == "I":
        n = int(input().strip())
        parents = np.array(input().strip().split(), dtype=int)
    else:
        print("Error")
        return
    
    print(compute_height(n, parents))

if __name__ == "__main__":
    thread = threading.Thread(target=main)
    thread.start()

import sys
import threading


def compute_height(n, parents):
    # Write this function
    kur = [[] for _ in range(n)]
    root = None
    #max_height = 0
    # Your code here
    for g, parent in enumerate(parents):
        if parent == -1:
            root = g
           
        else:
            kur[parent].append(g)

    def max_height(vuzol):
        height = 1
        
        if not kur[vuzol]:
            return height
        else:
            for child in kur[vuzol]:
                height = max(height, max_height(child))

            return height + 1
    return max_height(root)

def main():
    # implement input form keyboard and from files
    text = input()
    if "I" in text:
        # input number of elements
        n = int(input())
        # input values in one variable, separate with space, split these values in an array
        parents = list(map(int, input().split()))
    elif "F" in text:

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision 
        path = './test/'
        file = input()
        folder = path + file
        if "a" not in file:
            try:
                with open(folder) as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
            except Exception as e:
                print("Kluda:(", str(e))
                return
            
        else:
            print("Kluda")
            return
        
    else:
        print("Enter 'I' or 'F':")
        return
            
    # call the function and output it's result
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Importing lib for regex - E1
import re

# Defining Tree class in order to generate binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# defining a global varible called recursionLen - This updates the realtime length of the tree, eventually used to determine if there are multiple Roots - E4
reclen = 0

# A cheat way to get around the issue of the print tree method executing when an E3 error occurs within the recursive tree building loop
E3 = False

# Possible improvments - Have an indepent fuction for errors - Could elimiate some of the odditys with the order in which certain cases get called
def main():
    # Reading input
    inputStr = input()
    
    # Defining the regex string used for testing inputs - E1
    # The tolerances could probably be tighter but it works well
    # Should I expand on this?
    regex = "( ?\(([A-Z]),([A-Z])\))"
    # If the regex doesn't match, print the E1 error and return
    if not re.match(regex, inputStr):
        print("E1")
        return
    
    # Spliting the input string into an array
    arr = inputStr.split()
    
    # Defining a dictionary in order to keep track of E5 errors
    seen = {}
    
    # Looping through array to check for a variety of errors - E5, E2, as well as to transform the data into a form that is easier to manipulate
    for k,v in enumerate(arr):
        
        # Calling setDefault in order to allow for appending to an array for the value
        seen.setdefault(arr[k][1], [])
        
        # Checking if there is a key value pair already equal to the one currently being added to the array, IE checking for duplicate pairs - E2
        if arr[k][3] in seen[arr[k][1]]:
            print("E2")
            return
        
        # If the "value"(arr[k][3]) is in seen(as a key), that is an indication that the input contains a cycle - E5
        if arr[k][3] in seen:
            print("E5")
            return

        # Apending a K/V pair to the dictionary, and reformating the index in the array to be easier to work with
        seen[arr[k][1]].append(arr[k][3])
        arr[k] = [arr[k][1], arr[k][3]]
    
    # Begining the tree witha root, and the leftmost value - which will always be added, and to the left of the root
    root = TreeNode(arr[0][0], TreeNode(arr[0][1]))
    
    # Calling the createTree Recursive method, starting at the root, and with the array "missing" the first k/v pair as it has already been added
    createTree(root, arr[1:], root)
    
    # This is after the recursive function has finish - if there were no double roots(which would be unassinged using my method), the reclen would be one less than
    # the len of the array - E4
    if reclen + 1 != len(arr):
        print("E4")
        return
    
    # A cheats way to ensure that if a parent has more than two children, the tree does not get printed - set in create three if E3 is come across - E3
    if not E3:
        print(printTree(root))
    
# Method to create the tree structure which will later be printed
def create_Tree(head, arr, root):
    # Defining global varibles
    global reclen
    global E3
    
    # Ensuring that the head is still valid, and the the array still has contents
    if head and len(arr) != 0:
        
        # if the "head" value of the key value pair is equal to the head value of the tree, it means that we can build out the tree with another value
        if head.val == arr[0][0]:
            
            # If head.left does not exist, assign it to a new node, with the value of the "child" value in the current keypair
            if not head.left:
                head.left = TreeNode(arr[0][1])
                # Incrementing reclen to keep track of real length - E4
                reclen += 1
                
                # If head.left does not exist, assign it to a new node, with the value of the "child" value in the current keypair
            elif not head.right:
                head.right = TreeNode(arr[0][1])
                # Incrementing reclen to keep track of real length - E4
                reclen += 1
                
            # This else will only get triggered if there is already a head.left and head.right - indicating there is more than two children - E3
            else:
                print("E3")
                
                # Setting global var in order to get around issue of returning out E3 error code
                E3 = True
                
                # Adding the length of the rest of the array to reclen to prevent error E4 from triggering - E3 has already triggered
                reclen += len(arr)
                return
            
            # After a value has been assigned, restart the process of the root of the tree, with the assigned value removed from the array
            createTree(root, arr[1:], root)
        
        # This else is triggered if head.val != arr[0][0] - moving exploring the entire left side of each branch before exploring the next right side.
        else:
            createTree(head.left, arr, root)
            createTree(head.right, arr, root)
            
    # If head is not valid or the length of array is 0, this else is triggered - indicates the end of the recursive function
    else:
        return
    
# The print tree recursive function - used to print the entirity of the tree in the described format
def printTree(head):
    # If the head does not exist, there is nothing to return - return empty quotes
    if not head:
        return ""
    # Returning an output in the correct format
    else:
        return "(" + head.val + printTree(head.left) + printTree(head.right) + ")"

# My test case
#(A,B) (A,C) (B,D) (D,E) (C,F) (E,G) (F,H) (D,P) (P,X) (F,Y) (P,Z) (Z,K) (Y,C) (A,B)
main()
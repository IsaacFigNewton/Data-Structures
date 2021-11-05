class BinarySearchTree:
    #Create the TreeNode class
    class TreeNode:
        def __init__(self, key, data = None):
            self.parent = None
            self.left = None
            self.right = None
            self.key = key
            self.data = data

        def isLeftChild(self):
            return self.parent != None and self.parent.left == self

        def isRightChild(self):
            return self.parent != None and self.parent.right == self

        def isRoot(self):
            return self.parent is None

        def isLeaf(self):
            return self.right is None and self.left is None

        def hasAnyChildren(self):
            return self.right != None or self.left != None

        def hasBothChildren(self):
            return self.right != None and self.left != None

        def print(self):
            print("Information for node with key " + str(self.key) + ":")
            print("Key: " + str(self.key))
            print("Data: " + str(self.data))

            #parent info
            if (self.parent != None):
                print("Parent's key: " + str(self.parent.key))
            else:
                print("This node is either root or an orphan.")

            #right child info
            if (self.left != None):
                print("Left child's key: " + str(self.left.key))
            else:
                print("This node has no left child.")

            #right child info
            if (self.right != None):
                print("Right child's key: " + str(self.right.key))
            else:
                print("This node has no right child.")

            print()

    #constructor here
    def __init__(self):
        #enter stuff here
        self.root = None
        self.keys = []
        self.num_items = 0

    #methods
    def findWithKey(self, key):
        #returns True if key is in a node of the tree, else False
        return self.keys.count(key)>0

    def find_min(self, currentNode):
        #returns min value in the tree
        while (currentNode.left != None):
            currentNode = currentNode.left

        return currentNode

    def find_max(self, currentNode):
        #returns max value in the tree
        while (currentNode.right != None):
            currentNode = currentNode.right

        return currentNode

    def getNodeWithKey(self, key):
        currentNode = self.root

        if (currentNode is None or key is None):
            print("Please only pass trees and keys with values to this method.")
            return None

        while (currentNode.key != key):
            if (currentNode.key < key):
                currentNode = currentNode.right
            elif (currentNode.key > key):
                currentNode = currentNode.left
            if (currentNode is None):
                print("No node with key \'" + str(key) + "\' was found in the tree.")
                return None
        return currentNode

    def insert(self, newKey):
        #inserts a node with key and data into the correct position if not a duplicate.
        newNode = BinarySearchTree.TreeNode(newKey, newKey)

        #1 find the spot to insert the node
        currentNode = self.root
        parentNode = None

        #if there's nothing in the tree, give it a root node
        if (currentNode == None):
            self.root = newNode
            #increment num_items and add the key to the list of keys
            self.num_items += 1
            self.keys.insert(0, newKey)
            return None

        #While there's still more tree to traverse/while we haven't reached the bottom of the tree
        while (currentNode != None):
            #if the current node has data in it
            if (currentNode.key != None):
                if (currentNode.key > newKey):
                    #slide to the left
                    parentNode = currentNode
                    currentNode = currentNode.left
                elif (currentNode.key < newKey):
                    #slide to the right
                    parentNode = currentNode
                    currentNode = currentNode.right
                #if the data for the node bing inserted is a duplicate
                else:
                    #cha-cha real smooth
                    print("The data you tried to insert was a duplicate, so no action was taken.")
                    return None

        #2 once you've reached the bottom of the tree, modify the surrounding nodes' pointers
        if (parentNode.key > newKey):
            # set the parent's left pointer
            parentNode.left = newNode
        elif (parentNode.key < newKey):
            # set the parent's right pointer
            parentNode.right = newNode

        #3 modify newNode's parent pointer respectively
        newNode.parent = parentNode

        #4 increment num_items and add the key to the list of keys
        self.num_items += 1
        self.keys.insert(0, newKey)

    def findSuccessor(self, node):
        #the successor should be the largest value in the left child subtree
        #or smallest value in the right child subtree
        succ = None

        #if the node is the left child
        if (node.left != None):
            #the successor is the maximum value of the left child subtree
            succ = self.find_max(node.left)
        #otherwise, if it's the right child
        elif (node.right != None):
            #the successor is the minimum value of the right child subtree
            succ = self.find_min(node.right)
        else:
            print("Error: The successor node was a leaf")

        return succ

    def setInternalCurrentNodePointers(self, currentNode, successor):
        #if the currentNode is root or an orphan somehow
        if (currentNode.parent is None):
            #change the values of the node the children nodes are pointing to, not the whole subtree
            if (currentNode.left != None):
                currentNode.left.parent.key = successor.key
                currentNode.left.parent.data = successor.data
            if (currentNode.right != None):
                currentNode.right.parent.key = successor.key
                currentNode.right.parent.data = successor.data
        #if the currentNode is a left child
        elif (currentNode.isLeftChild()):
            # change the values of the node the parent is pointing to, not the whole subtree
            currentNode.parent.left.key = successor.key
            currentNode.parent.left.data = successor.data

            # change the values of the node the children nodes are pointing to, not the whole subtree
            if (currentNode.left != None):
                currentNode.left.parent.key = successor.key
                currentNode.left.parent.data = successor.data
            if (currentNode.right != None):
                currentNode.right.parent.key = successor.key
                currentNode.right.parent.data = successor.data
        #if the currentNode is a right child
        else:
            # change the values of the node the parent is pointing to, not the whole subtree
            currentNode.parent.right.key = successor.key
            currentNode.parent.right.data = successor.data

            # change the values of the node the children nodes are pointing to, not the whole subtree
            if (currentNode.left != None):
                currentNode.left.parent.key = successor.key
                currentNode.left.parent.data = successor.data
            if (currentNode.right != None):
                currentNode.right.parent.key = successor.key
                currentNode.right.parent.data = successor.data

    def remove(self, currentNode):
        #if the node is a leaf, sever the parent's ties with it
        if (currentNode.isLeaf()):  # leaf
            #currentNode.print()
                #for debugging
                #print("(remove method called) Parent's key: " + str(currentNode.parent.key))
            if (currentNode == currentNode.parent.left):
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        #otherwise, if it has a child (aka is an interior node), get the successor (max of left child subtree or min of right child subtree)
        else:
            #recursively shift the successors

            #get the first successor node
            successor = self.findSuccessor(currentNode)

            #while the successor node isn't a leaf
            while(successor.hasAnyChildren() == True):
                #set its parent and childrens' pointers to it as having the key
                #and data of its successor
                self.setInternalCurrentNodePointers(currentNode, successor)

                #update the currentNode and successor's values
                currentNode = successor
                successor = self.findSuccessor(currentNode)

            #when successor is found to be a leaf
            #set the currentNode values one last time
            self.setInternalCurrentNodePointers(currentNode, successor)
            #remove the leaf
            if (successor.isLeftChild()):
                successor.parent.left = None
            else:
                successor.parent.right = None

    def delete(self, key):
        if (self.num_items > 1):
            nodeToRemove = self.getNodeWithKey(key)
            if (nodeToRemove != None):
                #for debugging
                #print("(delete method called) Parent's key: " + str(nodeToRemove.parent))
                self.remove(nodeToRemove)

                self.keys.pop(self.keys.index(key))
                self.num_items -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif (self.num_items == 1 and self.root.key == key):
            self.root = None

            self.keys.pop(self.keys.index(key))
            self.num_items -= 1
        else:
            raise KeyError("Error, key not in tree")

    def print_tree(self):
        #print inorder the entire tree
        return self.inorder_print_tree()

    def is_empty(self):
        #returns True if tree is empty, else False
        if (len(self.keys) == 0):
            return True
        else:
            return False

    #unfinished
    def inorder_print_tree(self, node):
        #create the queue
        if node != None:
            self.inorder_print_tree(node.left)
            print(node.key)
            self.inorder_print_tree(node.right)

    #get the height of the tree: the length of the path from the root to the farthest leaf node
    def height(self, node):
        #if the bottom of the tree has been reached, return 0
        if (node == None):
            return 0
        else:
            #find the height of each subtree recursively
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            #if the left is longer than the right, use that
            if (lheight > rheight):
                return lheight + 1
            else:
                return rheight + 1

    #print nodes at the current level
    def print_current_level(self, node, relLevel, level):
        if (node == None):
            return None
        #if the relative level is 0
        if (relLevel == 0):
            #print the level and nodes on it
            """
            ex:
            0 value
            1 value
            1 value
            2 value
            2 value
            2 value
            2 value
            ...
            """
            print(str(level) + " " + str(node.key))
        elif (relLevel > 0):
            #if the level is further down, go to the children and decrement the level
            self.print_current_level(node.left, relLevel-1, level)
            self.print_current_level(node.right, relLevel-1, level)

    def print_levels(self):
        #inorder traversal prints list of pairs, [key, level of the node] where root is level 0
        #for every node at every level down to the bottom...
        for i in range(0, self.height(self.root)):
            #go down to that level and print the values of the nodes on it
            self.print_current_level(self.root, i, i)

    """
    The following methods use code adapted from this site:
    https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html#lst-bst8
    
    isLeftChild(self)
    isRightChild(self)
    isRoot(self)
    isLeaf(self)
    hasAnyChildren(self)
    hasBothChildren(self)
    spliceOut(self)
    findSuccessor(self, node)
    remove(self, currentNode)
    delete(self, key)
    inorder_print_tree(self, node)
    """
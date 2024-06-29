class Node:
    def __init__(self,data,parent=None,left=None,right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

class SplayTree:
    def __init__(self,data):
        self.root = Node(data)

    def insert(self,data,pos=None):
        newNode = Node(data)
        if pos is None:
            pos = self.root

        if data < pos.data:
            if pos.left is None:
                pos.left = newNode
                newNode.parent = pos
            else:
                self.insert(data, pos.left)

        elif data > pos.data:
            if pos.right is None:
                pos.right = newNode
                newNode.parent = pos
            else:
                self.insert(data, pos.right)

        self.splay(newNode)

    def zig(self,x):
        y = x.left
        x.left = y.right
        if(y.right!=None):
            y.right.parent = x

        y.parent = x.parent

        if(x.parent == None):
            self.root = y

        elif(x == x.parent.left):
            x.parent.left = y

        elif(x == x.parent.right):
            x.parent.right = y

        y.right = x
        x.parent = y

        return y

    def zag(self,x):
        y = x.right
        x.right = y.left

        if(y.left !=None):
            y.left.parent = x

        y.parent = x.parent

        if(x.parent==None):
            self.root = y

        elif(x == x.parent.right):
            x.parent.right = y
        else:
            x.parent.left = y

        y.left = x
        x.parent = y
        return y

    def splay(self,node):
        while(node.parent!=None):
            if(node.parent == self.root):
                if(node == node.parent.left):
                    self.root = self.zig(node.parent)
                else:
                    self.root = self.zag(node.parent)
            else:
                parent = node.parent
                grandParent = parent.parent
                if(node == parent.left and parent == grandParent.left):
                    self.zig(grandParent)
                    self.zig(parent)

                elif(node == parent.right and parent == grandParent.right):
                    self.zag(grandParent)
                    self.zag(parent)

                elif(node == parent.left and parent == grandParent.right):
                    self.zig(parent)
                    self.zag(grandParent)

                elif (node == parent.right and parent == grandParent.left):
                    self.zag(parent)
                    self.zig(grandParent)

    def find(self,ele,pos=None):
        if pos is None:
            pos = self.root
        if pos.data == ele:
            return pos
        elif ele < pos.data:
            if pos.left is not None:
                return self.find(ele,pos.left)
        else:
            if pos.right is not None:
                return self.find(ele,pos.right)

    def findMin(self,pos=None):
        if pos == None:
            pos = self.root
        if pos.left is None:
            return pos
        else:
            self.findMin(pos.left)

    def findMax(self,pos=None):
        if pos == None:
            pos = self.root
        if pos.right is None:
            return pos
        else:
            self.findMax(pos.right)

    def delete(self,ele,pos=None):
        if pos is None:
            pos = self.root

        node = self.find(ele)
        if node is None:
            return
        parent = node.parent

        if node.left is None and node.right is None:
            if(node == parent.left):
                parent.left = None
            else:
                parent.right = None
        elif node.left is None or node.right is None:
            if node.left == None:
                if(node == parent.left):
                    parent.left = node.right
                    node.right.parent = parent
                else:
                    parent.right = node.right
                    node.right.parent = parent
            else:
                if (node == parent.left):
                    parent.left = node.left
                    node.left.parent = parent
                else:
                    parent.right = node.left
                    node.left.parent = parent

        elif node.left is not None and node.right is not None:
            lowEle = self.findMin(node.right)
            node.data = lowEle.data
            lowEle.data = 99999999
            self.delete(lowEle.data,node.right)

        if parent is not None:
            self.splay(parent)

    def inorder(self,pos=None):
        if pos ==  None:
            pos = self.root
            print('root is ',self.root.data)

        if pos.left is not None:
            self.inorder(pos.left)

        if pos.right is not None:
            self.inorder(pos.right)

        print('from post order',pos.data)


if __name__ == '__main__':
    root = SplayTree(29)
    root.insert(1)
    root.insert(4)
    root.insert(55)
    root.insert(994)
    root.delete(4)
    root.delete(29)
    root.inorder()
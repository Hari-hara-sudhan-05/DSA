
import  heapq
class Node:
    def __init__(self,char,freq,left=None,right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.code = ''

    def __lt__(self, other):
        return self.freq < other.freq

def generateCode(nodes,d={},val=''):
    new_val = val + str(nodes.code)
    if nodes.char:
        d[nodes.char] = new_val
    if nodes.left:
        generateCode(nodes.left,d,new_val)
    if nodes.right:
        generateCode(nodes.right,d,new_val)

    return d

if __name__  == "__main__":
    string = input("Enter the string: ")
    count={}
    for char in string:
        if char in count:
            count[char] +=1
        else:
            count[char]=1

    nodes = []
    for char,freq in count.items():
        heapq.heappush(nodes,Node(char,freq))

    while len(nodes)>1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.code = 0
        right.code = 1
        newNode = Node(None,left.freq+right.freq,left,right)
        heapq.heappush(nodes,newNode)

    generated_code = generateCode(nodes[0])

    result = ''

    for char in string:
        if char in generated_code:
            result+=generated_code[char]

    print(generated_code)
    print(result)
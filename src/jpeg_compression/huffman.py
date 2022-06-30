# A Huffman Tree Node from GFG
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree


def printNodes(node, x_huff, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left,x_huff, newVal)
    if(node.right):
        printNodes(node.right,x_huff, newVal)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
        x_huff[node.symbol] = newVal





def huff(chars,freq,x_huff):
    # list containing unused nodes
    nodes = []

    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        nodes.append(node(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on theri frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    # Huffman Tree is ready!
    printNodes(nodes[0],x_huff)



if __name__ == '__main__':
    # characters for huffman tree
    chars = ['8', '34', '5', '10', '6', '43','127']

    # frequency of characters
    freq = [ 3, 3, 1, 5, 1, 1, 1]   

    huff(chars,freq,{})
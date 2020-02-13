class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_left_node(self, left):
        self.left = left

    def set_right_node(self, right):
        self.right = right

    def get_left_node(self):
        return self.left

    def get_right_node(self):
        return self.right

    @staticmethod
    def generate_binary_tree():
        print("tarun")
        nodes = []
        for i in range(10):
            nodes.append(BinaryTreeNode(i))
        nodes[0].left = nodes[1]
        nodes[0].right = nodes[2]
        nodes[1].left = nodes[3]
        nodes[1].right = nodes[4]
        nodes[2].left = nodes[5]
        nodes[2].right = nodes[6]
        nodes[3].left = nodes[7]
        nodes[3].right = nodes[8]
        nodes[4].left = nodes[9]
        return nodes[0]

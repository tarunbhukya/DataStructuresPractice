
from datastructures import BinaryTreeNode

binary_tree = BinaryTreeNode.generate_binary_tree()

def preorder_recursive(binary_tree_node, result = []):
    if binary_tree_node is None:
        return

    result.append(binary_tree_node.data)
    preorder_recursive(binary_tree_node.left, result)
    preorder_recursive(binary_tree_node.right, result)

def preorder_itertive(binary_tree_node, result):
    if binary_tree_node is None:
        return
    stack = []
    stack.append(binary_tree_node)
    while stack:
        node = stack.pop()
        if node is None:
            continue
        result.append(node.data)
        stack.append(node.right)
        stack.append(node.left)


def inorder_recursive(binary_tree_node, result):
    if binary_tree_node is None:
        return
    inorder_recursive(binary_tree_node.left, result)
    result.append(binary_tree_node.data)
    inorder_recursive(binary_tree_node.right, result)


def inorder_iterative(binary_tree_node, result):
    if binary_tree_node is None:
        return
    stack = []
    node = binary_tree_node
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right


def postorder_recursive(binary_tree_node, result):
    if binary_tree_node is None:
        return

    postorder_recursive(binary_tree_node.left, result)
    postorder_recursive(binary_tree_node.right, result)
    result.append(binary_tree_node.data)


def postorder_iterative(binary_tree_node, result):
    if binary_tree_node is None:
        return

    stack = []
    visited = set()
    node = binary_tree_node

    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and node.right not in visited:
                node = node.right
            else:
                result.append(node.data)
                visited.add(node)
                node = None


def max_num(binary_tree_node):
    global max_number

    if binary_tree_node is None:
        return

    if max_number < binary_tree_node.data:
        max_number = binary_tree_node.data

    if binary_tree_node.left:
        max_number = max_num(binary_tree_node.left)

    if binary_tree_node.right:
        max_number = max_num(binary_tree_node.right)

    return max_number


def binary_size(binary_node):
    if binary_node is None:
        return 0;
    return binary_size(binary_node.left) + 1 + binary_size(binary_node.right)


def binary_size_iterative(binary_node):
    count = 0
    q = []
    q.append(binary_node)

    while q:
        node = q.pop(0)
        count += 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return count


def reverse_level_traversal(binary_node, result):
    if binary_node is None:
        return
    queue = []
    queue.append(binary_node)
    data = []

    while queue:
        node = queue.pop(0)
        result.append(node.data)

        if node.right:
            queue.append(node.right)

        if node.left:
            queue.append(node.left)

    for i in range(len(result)):
        data.append(result.pop())

    return data


def find_level_with_max_sum(binary_node):
    if binary_node is None:
        return False
    node = binary_node
    queue = []
    max_level = current_level = max_sum = current_sum = 0
    queue.append(node)
    queue.append("#")
    while queue:
        node = queue.pop(0)
        if node == "#":
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = current_level

            current_level += 1
            current_sum = 0
            if queue and queue.__getitem__(0) != "#":
                queue.append("#")
            continue

        current_sum = current_sum + node.data
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return max_level, max_sum


def find_all_paths(binary_node):
    paths = []
    path_finder(binary_node, [], paths)
    return paths

def path_finder(node, path, paths):
    if not node:
        return 0

    path.append(node.data)
    paths.append(path)
    if node.left:
        path_finder(node.left, path + [], paths)
    if node.right:
        path_finder(node.right, path + [], paths)



data = []
max_number = float("-infinity")
print(find_all_paths(binary_tree))

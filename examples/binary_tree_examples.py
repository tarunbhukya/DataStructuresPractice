from datastructures import BinaryTreeNode
binary_node = BinaryTreeNode.generate_binary_tree()
import functools


def find_all_paths(node):
    result = []
    find_node_path(node, [], result)
    return result


def find_node_path(node, path, result):
    if node is None:
        return
    path.append(node.data)
    result.append(path)

    if node.left:
        find_node_path(node.left, path + [], result)
    if node.right:
        find_node_path(node.right, path + [], result)

def find_sum_of_lists(list_array):
    sum = 0
    for i in list_array:
        if type(i) == list:
            sum = sum + functools.reduce(lambda a,b: a+b, i)
    return sum


list_array = find_all_paths(binary_node)
print(list_array)
print(find_sum_of_lists(list_array))
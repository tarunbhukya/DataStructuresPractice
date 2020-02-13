""""
    there are 1000 bottle of which one is poisoned and there are 10 rats for testing
    find which bottle is poisoned
"""""


def find_poisoned_bottle(r):
    # Your code here
    a = 10 * ['0']
    for i in r:
        a[i] = '1'
    a.reverse()
    b = "".join(a)
    return int(b, 2)


print(find_poisoned_bottle([0,3,5,4,9,8]))
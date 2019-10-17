def minMax(operations, x):
    elements = []
    ans = []
    for k, i in enumerate(operations):
        if i == 'push':
            elements.append(x[k])
        else:
            elements.remove(x[k])
        elements.sort()
        ans.append(elements[0] * elements[-1])
    return ans



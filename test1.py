


def efficientJanitor(weight):
    # Write your code here
    weight = sorted(weight)
    n = 0
    left = 0
    right = len(weight)-1
    while len(weight)>1:
        # if
        if weight[-1] + weight[0] > 3.0:
            n += 1
            weight = weight[:-1]
        else:
            weight[-1] = weight[-1] + weight[0]
            weight = weight[1:]
    n += 1
    return n



if __name__ == '__main__':
    weight = [1.01, 1.01, 1.5, 1.99, 2.5]
    res = efficientJanitor(weight)
    print(res)

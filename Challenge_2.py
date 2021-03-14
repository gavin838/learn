class Node:
    def __init__(self, ID, cost):
        self.cost = cost
        self.pre = []
        self.next = []
        self.ID = ID
        self.depth = 0

def dfs(dag, totle_list):
    for next in dag.next:
        if next is not None:
            next.depth = dag.depth+1
            totle_list[next.depth].append(next)
            dfs(next, totle_list)
    return

if __name__ == '__main__':

    A = Node(1, 1)
    B = Node(2, 3)
    C = Node(3, 4)
    D = Node(4, 2)
    A.next.append(B)
    A.next.append(C)
    A.pre = [None]

    B.next.append(D)
    B.pre.append(A)

    C.next.append(D)
    C.pre.append(A)

    D.next = [None]
    D.pre.append(C)
    D.pre.append(B)
    '''
        A 
       / |
      B  C
       |/
       D
    time = A + max(B, C) + D = 7
    '''
    N = 4
    totle_list = [ [] for i in range(N+1)]
    totle_list[0].append(A)
    dfs(A, totle_list)
    cost = 0
    for i in range(4):
        max_t = 0
        for node in totle_list[i]:
            max_t = max(max_t, node.cost)
            # print(node.cost)
        cost += max_t
    print(cost)
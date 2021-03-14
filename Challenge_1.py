class Node:
    def __init__(self, value, type):
        self.value = value
        self.type = type    # supported:1, unsupported:2
        self.next = None


def partion_graph(dag):
    '''
    partition the graph into a list of subgraphs that contain only entirely supported or entirely unsupported nodes.
    '''
    supported_list = list()
    unsupported_list = list()
    cur_type = dag.type
    tmp_list = []
    while dag is not None:
        if dag.type == cur_type:
            tmp_list.append(dag)
            dag = dag.next
        else:
            if cur_type == 1:
                supported_list.append(tmp_list)
            else:
                unsupported_list.append(tmp_list)
            tmp_list=[]
            cur_type = dag.type
            tmp_list.append(dag)
            dag = dag.next
    if cur_type == 1:
        supported_list.append(tmp_list)
    else:
        unsupported_list.append(tmp_list)
    return supported_list, unsupported_list

def assembling_graph(supported_list, unsupported_list):
    '''
    assembling a list of subgraphs that have been partitioned into a single graph
    '''
    if len(supported_list) > 0:
        tail = supported_list[0][-1]
    if len(unsupported_list) > 0 and tail.next != unsupported_list[0][0]:
        dag = unsupported_list[0][0]
        tail = unsupported_list[0][-1]
    else:
        dag = supported_list[0][0]
        tail = supported_list[0][-1].next

    while tail is not None:
        for supp in supported_list:
            if tail == supp[0]:
                tail = supp[-1].next
                break
        for un_supp in unsupported_list:
            if tail == un_supp[0]:
                tail = un_supp[-1].next
                break
    return dag

if __name__ == '__main__':
    dag = Node(1, 1)
    tmp1 = Node(2, 1)
    tmp2 = Node(3, 2)
    tmp3 = Node(4, 2)
    tmp4 = Node(5, 1)
    # node(1)->node(1)->node(2)->node(2)->node(1)->None
    dag.next = tmp1
    tmp1.next = tmp2
    tmp2.next = tmp3
    tmp3.next = tmp4
    tmp4.next = None
    supported_list, unsupported_list = partion_graph(dag)
    print("Support:")
    for su in supported_list:
        for i in su:
            print(i.value)
    for unsu in unsupported_list:
        for i in unsu:
            print(i.value)
    dag = assembling_graph(supported_list, unsupported_list)
    while(dag is not None):
        print(dag.value, dag.type)
        dag = dag.next

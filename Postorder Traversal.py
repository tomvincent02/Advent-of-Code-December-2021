#Inorder traversal

class Graph_search_methods:

    def __init__(self, graph, name_type):
        self._graph = graph
        self._name_type = name_type

    def pre_order(self, graph, name_type, start_node, desired_node):
        while desired_node != start_node:
            if desired_node < start_node:
                #go to the left of the start_node
                pre_order(graph, name_type, left_node, desired_node)
            else: #desired_node < start_node
                #go to the right of the start_node
                pre_order(graph, name_type, right_node, desired_node)

        return 'Found' , desired_node

    def post_order(self, graph, name_type):




    def in_order(self, graph, name_type):


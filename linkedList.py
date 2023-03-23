from node import Node

class LinkedList:
    def __init__(self, head_node=None):
        self.head_node=head_node

    def insert(self, new_node):
        current_node=self.head_node

        if not current_node:
            self.head_node=new_node

        while(current_node):
            next_node=current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node=next_node

    def __iter__(self):
        current_node=self.head_node
        while(current_node):
            yield current_node.get_value()
            current_node=current_node.get_next_node()
class TreeNode:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def is_unique(self):
        current_node = self.parent
        while current_node is not None:
            if self.board.is_equal(current_node.board):
                return False
            current_node = current_node.parent
        return True

def create_tree(node):
    possible_moves = node.board.av_status()
    if possible_moves == []:
        return
    status = False
    for move in possible_moves:
        child_node = TreeNode(move, node)
        if child_node.is_unique():
            status = True
            node.add_child(child_node)
        else:
            del child_node
    if status is False:
        return
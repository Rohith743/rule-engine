# rule_engine.py
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left            # Left child Node
        self.right = right          # Right child Node
        self.value = value          # Value for operand nodes
    def create_rule(rule_string):
    # Implement parsing logic (placeholder example)
    return Node("operand", value=("age", ">", 30))

def combine_rules(rules):
    combined_node = Node("operator", value="OR")
    for rule in rules:
        ast = create_rule(rule)
        combined_node.left = ast  # Implement proper linking
    return combined_node

def evaluate_rule(ast_root, data):
    if ast_root.node_type == "operand":
        return eval(f"{data[ast_root.value[0]]} {ast_root.value[1]} {ast_root.value[2]}")
    elif ast_root.node_type == "operator":
        left_value = evaluate_rule(ast_root.left, data)
        right_value = evaluate_rule(ast_root.right, data)
        return left_value or right_value if ast_root.value == "OR" else left_value and right_value
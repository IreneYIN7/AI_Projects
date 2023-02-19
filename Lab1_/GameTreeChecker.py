class GameNode:
    def __init__(self, label, children=None, score=None):
        self.label = label
        self.children = children or []
        self.score = score

def build_game_tree(graph_str):
    nodes = {}
    for line in graph_str.splitlines():
        parts = line.split("=")
        label = parts[0].strip()
        score = int(parts[1].strip()) if len(parts) > 1 else None
        if label not in nodes:
            nodes[label] = GameNode(label, score=score)
        else:
            nodes[label].score = score
        if len(parts) == 1:
            children_str = parts[0].split(":")[1].strip()[1:-1]
            children = [c.strip() for c in children_str.split(",")]
            for child_label in children:
                if child_label not in nodes:
                    nodes[child_label] = GameNode(child_label)
                nodes[label].children.append(nodes[child_label])
    return nodes[label]

def graphChecker(graph_str):
    nodes = {}
    in_degrees = {}
    out_edges = {}
    root_nodes = set()

    # Create graph nodes
    for line in graph_str.split('\n'):
        print(line)
        line = line.strip()
        if not line:
            continue
        if '=' in line:
            # Leaf node
            label, value_str = line.split('=')
            print(label)
            try:
                value = int(value_str)
            except ValueError:
                print(f"Leaf node {label} has invalid value {value_str}")
                exit(0)
            
            nodes[label] = value
            print(nodes)
        elif ':' in line:
            # Internal node
            label, children_str = line.split(': ')
            print(label)
            print(children_str)
            children = [c.strip() for c in children_str.strip('[]').split(',')]
            nodes[label] = children
            in_degrees[label] = 0
            for child in children:
                out_edges.setdefault(label, set()).add(child)
                in_degrees[child] = in_degrees.get(child, 0) + 1
        else:
            raise ValueError(f"Invalid input: {line}")
    print("node: ", nodes)
    print("in_degrees: ", in_degrees)
    print("out_edges : ", out_edges)
    print("root_nodes: ",root_nodes)
    # Check for missing leaf values
    for node in nodes:
        print(nodes[node])
        print(out_edges.get(node))
        if isinstance(nodes[node], list) and not out_edges.get(node):
            raise ValueError(f"Leaf node {node} has no value")

    # Check for DAG and find root nodes
    for node in nodes:
        if isinstance(nodes[node], list):
            if in_degrees.get(node, 0) == 0:
                root_nodes.add(node)
            if node in out_edges:
                for child in out_edges[node]:
                    in_degrees[child] -= 1
                    if in_degrees[child] < 0:
                        print("Graph is not a DAG")
                        exit(0)
        else:
            if node in out_edges:
                print(f"Leaf node {node} cannot have children")
                exit(0)

    if len(root_nodes) != 1:
        print("Graph must have exactly one root node")
        exit(0)

    return nodes, root_nodes.pop()

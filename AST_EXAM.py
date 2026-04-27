import ast

samples = {
    "For Loop": "for i in range(3): print(i)",
    "Generator Function": "def gen(): yield 1",
    "Conditional Statement": "if x > 5 and x < 20: print(x)",
    "Arithmetic Operation": "x = 5 + 3 * 2"
}


def analyze_node(node, level=0):
    indent = "  " * level

    if isinstance(node, ast.Module):
        print(indent + "Module → Top-level container of the program")

    elif isinstance(node, ast.For):
        print(indent + "For → Loop structure (iteration construct)")

    elif isinstance(node, ast.FunctionDef):
        print(indent + "FunctionDef → Function definition (includes generator if yield exists)")

    elif isinstance(node, ast.Yield):
        print(indent + "Yield → Generator output step (lazy value generation)")

    elif isinstance(node, ast.If):
        print(indent + "If → Conditional branching structure")

    elif isinstance(node, ast.BoolOp):
        print(indent + "BoolOp → Logical operation (AND / OR conditions)")

    elif isinstance(node, ast.Assign):
        print(indent + "Assign → Assignment operator (=) storing values")

    elif isinstance(node, ast.BinOp):
        print(indent + "BinOp → Binary arithmetic operation (+, *, -, /)")

    elif isinstance(node, ast.Call):
        print(indent + "Call → Function call (e.g., range(), print())")

    elif isinstance(node, ast.Name):
        print(indent + "Name → Variable identifier")

    elif isinstance(node, ast.Constant):
        print(indent + "Constant → Literal value (numbers, strings)")

    for child in ast.iter_child_nodes(node):
        analyze_node(child, level + 1)


for name, code in samples.items():
    print("\n==============================")
    print(name)
    print("==============================")

    tree = ast.parse(code)

    print("\nAST STRUCTURE:")
    print(ast.dump(tree, indent=4))

    print("\nEVALUATION (TRANSPILATION FLOW):")
    analyze_node(tree)
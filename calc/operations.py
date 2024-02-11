"""Basic math operations."""

def add(a, b):
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)
 
    return a + b

def sub(a, b):
    """Substract b from a."""

    return a - b
a = int(request.args.get("a"))
b = int(request.args.get("b"))
result = sub(a, b)

    return str(result)

    def mult(a, b):
    """Multiply a and b."""
  a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)

    return a * b

def div(a, b):
    """Divide a by b."""
     a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)


    return a / b
operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)


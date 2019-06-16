def untyped(arg):
    var = arg + 2
    var2 = var * 10

    return var2 / 2


def typed(arg: int) -> float:
    var = arg + 2
    var2 = var * 10

    return var2 / 2

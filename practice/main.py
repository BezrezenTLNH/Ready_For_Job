import typing


def uppercase_action(text: str) -> str:
    return text.upper()

def func(text: str, space: str, action: typing.Callable) -> None:
    if not text:
        return

    print(space + action(text))
    func(text[1:], space + ' ', action)
    print(space + action(text))

print(func('test message idk', ' ', uppercase_action))
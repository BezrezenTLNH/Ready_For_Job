'''
Basix syntax
'''
import typing

#  base type and structures
types =[
    ...,
    None,
    True, False, bool,
    1, int,
    1.1, float,
    ' ', " ", """ """, f'', r'', str,
    b'', bytes,
    [], list,
    (), tuple,
    {1, }, set,
    {}, dict
]

#  basic operators
_ = 1 + 2  #  3
_ = 1 - 2  # -1
_ = 1 * 2  #  2
_ = 1 ** 2  #  1
_ = 1 / 2  #  0.5
_ = 1 // 2  #  0
_ = 1 % 2  #  1
_ = 1 and 2  #  2
_ = 1 or 2  #  1
_ = 1 > 2 | 1 >= 2 | 1 < 2 | 1 <= 2


#  cycle for
for _ in types:
    pass

for _ in types:
    break
else:
    pass


#  comprehensions
a = [i for i in types]  #  [Ellipsis, None, True, False, <class 'bool'>, ..., {}, <class 'dict'>]
b = (i for i in types)  #  <generator object <genexpr> at 0x000001CC69BEFED0>
c = {i for i in types if isinstance(i, typing.Hashable)}  #  {False, True, 1.1, <class 'int'>, ..., , <class 'dict'>}


#  unpacking, slices
e, *f, g = types
h = [*f]
_ = [1, 2, 3][:]  #  some_list[START:STOP:STEP]
_ = {**{}}


#  assert
assert h, 'test'


#  while
while a:
    a.pop()

while a:
    break
else:
    pass


# functions

def func(text: str, space: str, action: typing.Callable) -> None:
    if not text:
        return

    print(space + action(text))
    func(text[1:], space + ' ', action)
    print(space + action(text))


#  lambda functions
func('*' * 11, '', lambda text: ' '.join(i for i in text))


#  decorators
def decorator(multiplier: int):

    def dec(func: typing.Callable):
        #  visible of functions
        global a, b, c, d
        nonlocal multiplier

        if multiplier % 2 == 0:
            multiplier += 1

        def wrap(*args, **kwargs):
            for _ in range(multiplier):

                #  generators
                yield func(*args, **kwargs)

        return wrap
    return dec

@decorator(10)
def f(num: int) -> int:
    return num

qwe = [*f(1)]


#  conditions
if i := d.get(''):
    pass
elif not (q := d.get(1)):
    pass
else:
    ...

match qwe:
    case '1':
        pass
    case _:
        pass


#  exceptions

try:
    1 / 0
except ZeroDivisionError as exc:
    pass
else:
    pass
finally:
    ...

#  classes
class A:

    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test_arg = None

    def main(self):
        ...

    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg

    @test_arg.setter
    def test_atg(self, value: typing.Any):
        self.__test_arg = value

class B(A):

    def main(self) -> None:
        super().main()
        print(self.__test_arg)

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)


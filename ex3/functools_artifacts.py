#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any
from operator import add, mul
from functools import reduce, partial, lru_cache, singledispatch

Operation = Callable[[int, int], int]


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, Operation] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    if not spells:
        return 0
    if operation not in operations:
        return 0

    return reduce(lambda x, y: operations[operation](x, y), spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "0": partial(base_enchantment, 50, "fire"),
        "1": partial(base_enchantment, 50, "water"),
        "2": partial(base_enchantment, 50, "air"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base(_: Any) -> str:
        return "Unknown spell type"

    @base.register
    def _(int_: int) -> str:
        return f"Damage spell: {int_} damage"

    @base.register
    def _(str_: str) -> str:
        return f"Enchantment: {str_}"

    @base.register(list)
    def _(list_: list[Any]) -> str:
        return f"Multi-cast: {len(list_)} spells"

    return base


def main() -> None:
    spell_powers = [40, 30, 10, 10, 5, 4, 1]
    fibonacci_tests = [0, 1, 10, 15]

    print()
    print("Testing spell reducer...")
    print("Sum:", spell_reducer(spell_powers, "add"))
    print("Product:", spell_reducer(spell_powers, "multiply"))
    print("Max:", spell_reducer(spell_powers, "max"))
    # print("Min:", spell_reducer(spell_powers, "min"))
    # print("No spells:", spell_reducer(None, "add"))
    # print("Unknown:", spell_reducer(spell_powers, "Unknown"))

    print()
    print("Testing partial enchanter...")
    partials = partial_enchanter(
        lambda power, element, target: (
            f"Power: {power}, Element: {element}, Target: {target} "
        )
    )
    for i, (name, enchanter) in enumerate(partials.items()):
        print(f"{name} -", enchanter((i - 1) % len(partials)))

    print()
    print("Testing memoized fibonacci...")
    for n in fibonacci_tests:
        print(f"Fib({n}):", memoized_fibonacci(n))
        # print(memoized_fibonacci.cache_info())

    print()
    print("Testing spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell([1, 2, 3]))
    print(spell({1, 2, 3}))


if __name__ == "__main__":
    main()

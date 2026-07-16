#!/usr/bin/env python3
from collections.abc import Callable
from itertools import count


def mage_counter() -> Callable:
    c = count(1)
    return lambda: next(c)


def spell_accumulator(initial_power: int) -> Callable:
    acc = initial_power

    def accumulator(increment: int) -> int:
        nonlocal acc
        acc += increment
        return acc

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, Callable]:
    storage = {}
    return {
        "store": lambda key, value: storage.update({key: value}),
        "recall": lambda key: storage.get(key, "Memory not found"),
    }


def main() -> None:
    print()
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print()
    print("Testing spell accumulator...")
    accumulator_a = spell_accumulator(100)
    accumulator_b = spell_accumulator(100)
    print("Base 100 add 20:", accumulator_a(20))
    print("Base 100 add 30:", accumulator_b(30))

    print()
    print("Testing enchantment factory...")
    factory = enchantment_factory("Flaming")
    print(factory("Sword"))
    # print(factory("Shield"))
    factory = enchantment_factory("Frozen")
    print(factory("Shield"))

    print()
    print("Testing memory vault...")
    store, recall = memory_vault().values()
    print("Store 'secret' = 42")
    store("secret", 42)
    print("Recall 'secret':", recall("secret"))
    print("Recall 'unknown':", recall("unknown"))


if __name__ == "__main__":
    main()

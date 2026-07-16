#!/usr/bin/env python3
from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def poison(target: str, power: int) -> str:
    return f"Poison drains {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (
        spell(target, power) if condition(target, power) else "Spell Fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [spell(target, power) for spell in spells]


def main() -> None:
    print()
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    spell1, spell2 = combined("Dragon", 21)
    print("Combined spell result:", f"{spell1}, {spell2}")

    print()
    print("Testing power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print("Original:", fireball("Goblin", 17))
    print("Amplified:", amplified("Goblin", 17))

    print()
    print("Testing conditional caster...")
    condition = lambda _, power: power > 15
    conditioned = conditional_caster(condition, poison)
    print(f"{conditioned("Knight", 17)}")
    conditioned = conditional_caster(condition, poison)
    print(f"{conditioned("Knight", 13)}")

    print()
    print("Testing spell sequence...")
    sequence = spell_sequence([poison, heal, fireball])
    print(*sequence("Wizard", 42), sep="\n")


if __name__ == "__main__":
    main()

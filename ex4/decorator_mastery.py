#!/usr/bin/env python3
from collections.abc import Callable
from functools import wraps
from time import time, sleep, time_ns
from itertools import product


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def timer() -> Callable:
        print(f"Casting {func.__name__}...")

        start = time()
        result = func()
        end = time()

        print(f"Spell completed in {round(end - start, 3)} seconds")
        return result

    return timer


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def validator(self, spell_name: str, power: int) -> Callable | str:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power)

        return validator

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def retry() -> Callable | str:
            attempt = 0
            while True:
                try:
                    return func()
                except Exception:
                    attempt += 1
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying...",
                            f"({attempt}/{max_attempts})",
                        )
                    else:
                        return (
                            "Spell casting failed "
                            f"after {max_attempts} attempts"
                        )

        return retry

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name.strip()) >= 3 and all(
            c.isalpha() or c.isspace() for c in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (
            f"Successfully cast {spell_name.capitalize()} with {power} power"
        )


def main() -> None:
    test_powers = [15, 8, 6, 10]
    spell_names = ["lightning", "tornado", "meteor", "blizzard"]
    mage_names = ["Rowan", "Sage", "Nova", "Riley", "Casey", "Kai"]
    invalid_names = ["Jo", "A", "Alex123", "Test@Name"]

    print()
    print("Testing spell timer...")

    def fireball() -> str:
        sleep(0.1)
        return "Fireball cast!"

    print("Result:", spell_timer(fireball)())

    print()
    print("Testing retry spell...")

    @retry_spell(3)
    def coin_flip_spell() -> str:
        if (time_ns() // 100) % 2 == 0:
            raise Exception("EPIC FAIL")
        return "Waaaaaaagh spelled !"

    print(coin_flip_spell())

    print()
    print("Testing MageGuild...")

    test = list(product(spell_names, test_powers))
    mage = MageGuild()

    print(mage.validate_mage_name(mage_names[0]))
    print(mage.validate_mage_name(invalid_names[0]))
    for spell, power in test:
        print(mage.cast_spell(spell, power))


if __name__ == "__main__":
    main()

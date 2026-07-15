#!/usr/bin/env python3
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, reverse=True, key=lambda arti: arti.get("power"))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage.get("power") >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage.get("power")).get(
            "power"
        ),
        "min_power": min(mages, key=lambda mage: mage.get("power")).get(
            "power"
        ),
        "avg_power": round(
            sum(mage.get("power") for mage in mages) / len(mages), 2
        ),
    }


def main() -> None:
    print()
    print("Testing artifact sorter...")
    sorted = artifact_sorter(
        [
            {"name": "Orb", "power": 85, "type": "Crystal"},
            {"name": "Dart", "power": 42, "type": "Poison"},
            {"name": "Scroll", "power": 66, "type": "Dark"},
            {"name": "Staff", "power": 92, "type": "Fire"},
        ]
    )
    first = sorted.pop(0)
    second = sorted.pop(0)
    print(
        first.get("type"),
        first.get("name"),
        f"({first.get("power")} power)",
        "comes before",
        second.get("type"),
        second.get("name"),
        f"({second.get("power")} power)",
    )

    print()
    print("Testing spell transformer...")
    print(*spell_transformer(["fireball", "heal", "shield"]))

    mages = [
        {"name": "Gandalf", "power": 94, "element": "Light"},
        {"name": "Dumbledore", "power": 85, "element": "Arcane"},
        {"name": "Doctor Strange", "power": 100, "element": "Time"},
        {"name": "Merlin", "power": 89, "element": "Illusion"},
    ]

    print()
    print("Testing mage_stats...")
    max_power, min_power, avg_power = mage_stats(mages).values()
    print(f"Average: {avg_power:2g} (Range: {min_power}-{max_power})")

    print()
    print("Testing power_filter...")
    filtered = power_filter(mages, avg_power)
    print(
        f"Only {len(filtered)} above average:",
        *[
            f"- {mage.get("name")} with {mage.get("element")} magic"
            for mage in filtered
        ],
        sep="\n",
    )


if __name__ == "__main__":
    main()

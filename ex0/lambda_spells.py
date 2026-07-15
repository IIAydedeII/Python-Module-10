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
    artifacts = [
        {"name": "Shadow Blade", "power": 93, "type": "accessory"},
        {"name": "Fire Staff", "power": 65, "type": "armor"},
        {"name": "Light Prism", "power": 111, "type": "focus"},
        {"name": "Water Chalice", "power": 67, "type": "armor"},
    ]
    mages = [
        {"name": "Phoenix", "power": 50, "element": "earth"},
        {"name": "Luna", "power": 58, "element": "light"},
        {"name": "Storm", "power": 91, "element": "ice"},
        {"name": "Morgan", "power": 64, "element": "shadow"},
        {"name": "Nova", "power": 80, "element": "light"},
    ]
    spells = ["earthquake", "tsunami", "fireball", "lightning"]

    print()
    print("Testing artifact sorter...")
    artifacts_sorted = artifact_sorter(artifacts)
    first = artifacts_sorted.pop(0)
    second = artifacts_sorted.pop(0)
    print(
        first.get("name"),
        f"({first.get("power")} power)",
        "comes before",
        second.get("name"),
        f"({second.get("power")} power)",
    )

    print()
    print("Testing spell transformer...")
    print(*spell_transformer(spells))

    print()
    print("Testing mage_stats...")
    max_power, min_power, avg_power = mage_stats(mages).values()
    print(f"Average: {avg_power:2g} (Range: {min_power}-{max_power})")

    print()
    print("Testing power_filter...")
    mages_filtered = power_filter(mages, avg_power)
    print(
        f"Only {len(mages_filtered)} above average:",
        *[
            f"- {mage.get("name")} with {mage.get("element")} magic"
            for mage in mages_filtered
        ],
        sep="\n",
    )


if __name__ == "__main__":
    main()

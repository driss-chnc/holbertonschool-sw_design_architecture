#!/usr/bin/env python3
"""Factory pattern example."""


class Bus:
    """Represent a bus."""

    def __str__(self):
        """Return the bus lane."""
        return "road"


class Train:
    """Represent a train."""

    def __str__(self):
        """Return the train lane."""
        return "rails"


class Bike:
    """Represent a bike."""

    def __str__(self):
        """Return the bike lane."""
        return "lane"


class Scooter:
    """Represent a scooter."""

    def __str__(self):
        """Return the scooter lane."""
        return "scooter_lane"


class VehicleFactory:
    """Create vehicles using a registry."""

    def __init__(self):
        """Initialize the vehicle registry."""
        self.registry = {
            "bus": Bus,
            "train": Train,
            "bike": Bike,
        }

    def register_kind(self, kind: str, cls):
        """Register a vehicle class under a name."""
        self.registry[kind] = cls

    def create(self, kind: str):
        """Create a vehicle from the registry."""
        cls = self.registry[kind]
        return cls()


def main():
    """Run the factory example."""
    factory = VehicleFactory()

    factory.register_kind("scooter", Scooter)

    print(factory.create("bus"))
    print(factory.create("train"))
    print(factory.create("bike"))
    print(factory.create("scooter"))


if __name__ == "__main__":
    main()

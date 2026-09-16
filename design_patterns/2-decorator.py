#!/usr/bin/env python3
from __future__ import annotations
from abc import ABC, abstractmethod


class Beverage(ABC):
    """Define the interface for beverages."""

    @abstractmethod
    def cost(self) -> int:
        """Return the beverage cost."""
        ...

    @abstractmethod
    def description(self) -> str:
        """Return the beverage description."""
        ...


class Coffee(Beverage):
    """Represent a coffee."""

    def cost(self) -> int:
        """Return the coffee cost."""
        return 50

    def description(self) -> str:
        """Return the coffee description."""
        return "Coffee"


class MilkDecorator(Beverage):
    """Add milk to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initialize the decorator."""
        self._inner = inner

    def cost(self) -> int:
        """Return the wrapped cost plus milk."""
        return self._inner.cost() + 10

    def description(self) -> str:
        """Return the wrapped description plus milk."""
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Add sugar to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initialize the decorator."""
        self._inner = inner

    def cost(self) -> int:
        """Return the wrapped cost plus sugar."""
        return self._inner.cost() + 5

    def description(self) -> str:
        """Return the wrapped description plus sugar."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Add caramel to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initialize the decorator."""
        self._inner = inner

    def cost(self) -> int:
        """Return the wrapped cost plus caramel."""
        return self._inner.cost() + 15

    def description(self) -> str:
        """Return the wrapped description plus caramel."""
        return self._inner.description() + " + caramel"


def main() -> None:
    """Run the decorator example."""
    cup1 = MilkDecorator(Coffee())
    print(cup1.description(), cup1.cost())

    cup2 = MilkDecorator(SugarDecorator(Coffee()))
    print(cup2.description(), cup2.cost())

    cup3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(cup3.description(), cup3.cost())


if __name__ == "__main__":
    main()

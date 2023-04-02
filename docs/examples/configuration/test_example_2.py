from dataclasses import dataclass
from random import Random

from polyfactory import Use
from polyfactory.factories import DataclassFactory


@dataclass
class Person:
    name: str
    age: float
    height: float
    weight: float


class PersonFactory(DataclassFactory[Person]):
    __model__ = Person
    __random__ = Random(10)

    name = Use(DataclassFactory.__random__.choice, ["John", "Alice", "George"])


def test_setting_random() -> None:
    # the outcome of 'factory.__random__.choice' is deterministic, because Random is configured with a set value.
    assert PersonFactory.build().name == "Alice"
    assert PersonFactory.build().name == "John"
    assert PersonFactory.build().name == "Alice"

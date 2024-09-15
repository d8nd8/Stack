from task1 import Stack
import pytest


@pytest.mark.parametrize(
    'brackets,expected',
    (
            ("(((([{}]))))", "Сбалансированно"),
            ("[([])((([[[]]])))]{()}", "Сбалансированно"),
            ("(((([{}]))))", "Сбалансированно"),
            ("}{}", "Несбалансированно"),
            ("{{[(])]}}", "Сбалансированно"),
            ("[[{())}]", "Несбалансированно")

    )
)
def test_brackets(brackets, expected):
    test_bracket_set = Stack()
    assert test_bracket_set.is_balanced(brackets) == expected

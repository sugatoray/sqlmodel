from unittest.mock import patch

from sqlmodel import create_engine

from ...conftest import get_testing_print_function


def test_tutorial(clear_sqlmodel):
    from docs_src.tutorial.where import tutorial003 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        mod.main()

    assert calls == [
        [{"id": 6, "name": "Dr. Weird", "secret_name": "Steve Weird", "age": 36}],
        [{"id": 3, "name": "Rusty-Man", "secret_name": "Tommy Sharp", "age": 48}],
        [
            {
                "id": 7,
                "name": "Captain North America",
                "secret_name": "Esteban Rogelios",
                "age": 93,
            }
        ],
    ]

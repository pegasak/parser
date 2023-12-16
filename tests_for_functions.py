import pytest
from parser_function import get_crypto_info


def test_get_crypto_info():
    result = get_crypto_info()

    assert isinstance(result, str)


if __name__ == "__main__":
    pytest.main()

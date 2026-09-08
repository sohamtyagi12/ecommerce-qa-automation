import pytest


@pytest.mark.parametrize(
    "search_term",
    ["Tshirt", "Top", "Jeans", "Dress"]
)
def test_product_search_data(search_term):

    assert search_term != ""
    assert isinstance(search_term, str)
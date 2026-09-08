import requests
from test_data.account_data import TEST_EMAIL, TEST_PASSWORD


BASE_URL = "https://automationexercise.com/api"


def test_get_all_products():

    response = requests.get(
        f"{BASE_URL}/productsList"
    )

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert len(data["products"]) > 0


def test_search_product():

    response = requests.post(
        f"{BASE_URL}/searchProduct",
        data={"search_product": "top"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert len(data["products"]) > 0


def test_search_invalid_product():

    response = requests.post(
        f"{BASE_URL}/searchProduct",
        data={"search_product": "xyznonexistent123"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert len(data["products"]) == 0

def test_valid_login_api():
    response = requests.post(
        f"{BASE_URL}/verifyLogin",
        data={
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "User exists!"
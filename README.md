# E-Commerce QA Automation Framework

An end-to-end Quality Assurance automation framework built with Python, Selenium, PyTest, REST API testing, SQL database testing, and GitHub Actions CI/CD.

The project automates critical e-commerce workflows including product search, authentication, cart operations, checkout, API validation, and database verification.

---

## 🚀 Features

- End-to-End UI automation using Selenium
- PyTest-based test framework
- Page Object Model (POM)
- Explicit waits for reliable element interaction
- Positive and negative test scenarios
- Parameterized testing
- REST API testing using Python Requests
- SQL database testing
- HTML test reporting
- Automated screenshots/report support
- GitHub Actions CI/CD
- Secure test credential handling using `.gitignore`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Test automation |
| Selenium | Web UI automation |
| PyTest | Test execution and assertions |
| Requests | REST API testing |
| SQL | Database validation |
| MySQL | Database testing |
| Git | Version control |
| GitHub Actions | CI/CD |
| PyTest HTML | Test reporting |

---

## 📁 Project Structure

```text
ecommerce-qa-automation/
│
├── .github/
│   └── workflows/
│       └── qa-tests.yml
│
├── api_tests/
│   └── test_products_api.py
│
├── database/
│   └── db_connection.py
│
├── pages/
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── products_page.py
│
├── test_data/
│   ├── account_data.example.py
│   └── login_data.py
│
├── tests/
│   ├── test_add_to_cart.py
│   ├── test_cart_validation.py
│   ├── test_checkout.py
│   ├── test_database.py
│   ├── test_home_page.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_parameterized.py
│   ├── test_product_search.py
│   ├── test_products.py
│   └── test_remove_product.py
│
├── reports/
├── screenshots/
│
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

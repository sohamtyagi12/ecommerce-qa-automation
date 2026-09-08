from database.db_connection import get_connection


def test_database_insert_and_query():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        INSERT INTO products (name, price, quantity)
        VALUES ('Blue Top', 500, 1)
    """)

    connection.commit()

    cursor.execute("""
        SELECT name, price, quantity
        FROM products
        WHERE name = 'Blue Top'
    """)

    product = cursor.fetchone()

    assert product is not None
    assert product[0] == "Blue Top"
    assert product[1] == 500
    assert product[2] == 1

    connection.close()


def test_database_update():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        INSERT INTO products (name, price)
        VALUES ('Men Tshirt', 400)
    """)

    cursor.execute("""
        UPDATE products
        SET price = 450
        WHERE name = 'Men Tshirt'
    """)

    connection.commit()

    cursor.execute("""
        SELECT price
        FROM products
        WHERE name = 'Men Tshirt'
    """)

    price = cursor.fetchone()[0]

    assert price == 450

    connection.close()
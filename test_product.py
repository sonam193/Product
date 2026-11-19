from product import product_details

def test_product_details():
    result = product_details(101, "Laptop", 2, 50000)

    expected = (
        "Product ID: 101\n"
        "Name: Laptop\n"
        "Quantity: 2\n"
        "Price: 50000"
    )

    assert result == expected
import requests

base_url = 'http://127.0.0.1:5000'  # Адрес вашего локального сервера


# Тестирование POST /books
def test_add_book():
    new_book = {
        'title': 'Sample Book',
        'author': 'John Doe',
        'year': 2023
    }
    response = requests.post(f'{base_url}/books', json=new_book)
    assert response.status_code == 201


# Тестирование GET /books
def test_get_books():
    response = requests.get(f'{base_url}/books')
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


# Тестирование GET /books/<int:id>
def test_get_book():
    response = requests.get(f'{base_url}/books/1')
    assert response.status_code == 200


# Тестирование PUT /books/<int:id>
def test_update_book():
    updated_book = {
        'title': 'Updated Book Title',
        'author': 'Jane Smith',
        'year': 2022
    }
    response = requests.put(f'{base_url}/books/1', json=updated_book)
    assert response.status_code == 200


# Тестирование DELETE /books/<int:id>
def test_delete_book():
    response = requests.delete(f'{base_url}/books/1')
    assert response.status_code == 200


if __name__ == '__main__':
    test_add_book()
    test_get_books()
    test_get_book()
    test_update_book()
    test_delete_book()
    print("All tests passed!")

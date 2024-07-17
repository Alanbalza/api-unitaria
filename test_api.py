import unittest
import requests

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:5000/register'
        self.headers = {'Content-Type': 'application/json'}

    def test_register_user_success(self):
        data = {
            "username": "testuser",
            "password": "testpass",
            "email": "testuser@example.com"
        }
        response = requests.post(self.url, json=data, headers=self.headers)
        print(response.content)  # Añadido para imprimir la respuesta del servidor
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()

import unittest
import json
from app import app

class TasksApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Bem-vindo à API de Tarefas!")

    def test_get_tasks_route(self):
        response = self.app.get('/tasks')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIn('tasks', data)
        self.assertIsInstance(data['tasks'], list)

if __name__ == '__main__':
    unittest.main()
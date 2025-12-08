import requests
from config import Config

class ProjectsPage:
    def __init__(self):
        self.base_url = f"{Config.API_URL}/projects"
        self.headers = Config.HEADERS

    def create_project(self, project_data):# POST /api-v2/projects - Создание проекта
        response = requests.post(self.base_url, json=project_data, headers=self.headers)
        return response

    def get_project(self, project_id):#GET /api-v2/projects/{id} - Получение проекта по ID
        response = requests.get( f"{self.base_url}/{project_id}", headers=self.headers)
        return response

    def update_project(self, project_id, update_data):# PUT /api-v2/projects/{id} - изменение проекта
        response = requests.put(f"{self.base_url}/{project_id}", json=update_data, headers=self.headers)
        return response
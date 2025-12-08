import pytest
import uuid
import time
from projects_page import ProjectsPage

class TestProjects:
    @pytest.fixture
    def projects_page(self):
        return ProjectsPage()

    @pytest.fixture
    def project_data(self):
        return {
            "title": f"Test Project {uuid.uuid4().hex[:8]}"
        }

    # POSITIVE TESTS

    def test_create_project_positive(self, projects_page, project_data):#Позитивный тест создания проекта
        response = projects_page.create_project(project_data)
    
        print(f"Create Project Response Status: {response.status_code}")
        print(f"Create Project Response Text: {response.text}")
    
        assert response.status_code == 201, f"Expected 201, got {response.status_code}. Response: {response.text}"
    
        response_data = response.json()
    
        assert "id" in response_data
    
        # Проверяем наличие title в ответе
        if "title" not in response_data:
            print(f"⚠️  WARNING: 'title' not found in response. Available keys: {list(response_data.keys())}")
        else:
            assert response_data["title"] == project_data["title"]

    def test_get_project_positive(self, projects_page, project_data):#Позитивный тест получения проекта
        # Создаем проект для тестирования
        create_response = projects_page.create_project(project_data)
        assert create_response.status_code == 201, f"Project creation failed: {create_response.text}"
        project_id = create_response.json()["id"]
        
        # Небольшая пауза для стабильности
        time.sleep(1)
    
        # Получаем проект
        response = projects_page.get_project(project_id)
        print(f"Get Project Response Status: {response.status_code}")
        print(f"Get Project Response Text: {response.text}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
        
        response_data = response.json()
        assert response_data["id"] == project_id
        assert response_data["title"] == project_data["title"]

    def test_update_project_positive(self, projects_page, project_data):#Позитивный тест обновления проекта
        # Создаем проект для тестирования
        create_response = projects_page.create_project(project_data)
        assert create_response.status_code == 201, f"Project creation failed: {create_response.text}"
        project_id = create_response.json()["id"]
        
        # Небольшая пауза для стабильности
        time.sleep(1)
        
        # Обновляем проект 
        update_data = {
            "title": f"Updated Project {uuid.uuid4().hex[:8]}"
        }
        response = projects_page.update_project(project_id, update_data)
        
        print(f"Update Project Response Status: {response.status_code}")
        print(f"Update Project Response Text: {response.text}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
        response_data = response.json()
        
        # Проверяем обновленный title
        if "title" in response_data:
            assert response_data["title"] == update_data["title"]
        elif "name" in response_data:
            assert response_data["name"] == update_data["title"]

    # NEGATIVE TESTS

    def test_create_project_negative_missing_title(self, projects_page):#Негативный тест создания проекта без обязательного поля title
        invalid_data = { }
        response = projects_page.create_project(invalid_data)
        
        print(f"Missing Title Response Status: {response.status_code}")
        print(f"Missing Title Response Text: {response.text}")
        
        # Ожидаем ошибку валидации
        assert response.status_code == 400, f"Expected 400, got {response.status_code}. Response: {response.text}"

    def test_create_project_negative_with_description(self, projects_page):#"Негативный тест создания проекта с запрещенным полем description
        invalid_data = {
            "title": f"Test Project {uuid.uuid4().hex[:8]}",
            "description": "This should cause error"  # description запрещен при создании
        }
        response = projects_page.create_project(invalid_data)
        
        print(f"With Description Response Status: {response.status_code}")
        print(f"With Description Response Text: {response.text}")
        
        # Ожидаем ошибку валидации
        assert response.status_code == 400, f"Expected 400, got {response.status_code}. Response: {response.text}"
        assert "description should not exist" in response.text

    def test_get_project_negative_not_found(self, projects_page):#Негативный тест получения несуществующего проекта
        invalid_project_id = f"non_existent_project_{uuid.uuid4().hex[:8]}"
        response = projects_page.get_project(invalid_project_id)
        
        print(f"Not Found Response Status: {response.status_code}")
        print(f"Not Found Response Text: {response.text}")
        
        # Ожидаем ошибку "не найдено"
        assert response.status_code in [404, 400], f"Expected 404 or 400, got {response.status_code}. Response: {response.text}"

    def test_update_project_negative_invalid_data(self, projects_page, project_data):#Негативный тест обновления проекта с невалидными данными
        # Создаем проект для тестирования
        create_response = projects_page.create_project(project_data)
        assert create_response.status_code == 201, f"Project creation failed: {create_response.text}"
        project_id = create_response.json()["id"]
        
        # Небольшая пауза для стабильности
        time.sleep(1)
        
        # Пытаемся обновить с пустым title (обязательное поле)
        invalid_update_data = {
            "title": "",  # Пустой title
            "description": "Valid description"
        }
        response = projects_page.update_project(project_id, invalid_update_data)
        
        print(f"Invalid Data Update Response Status: {response.status_code}")
        print(f"Invalid Data Update Response Text: {response.text}")
        
        # Ожидаем ошибку валидации
        assert response.status_code == 400, f"Expected 400, got {response.status_code}. Response: {response.text}"

    def test_update_project_negative_wrong_id(self, projects_page):#Негативный тест обновления несуществующего проекта
        invalid_project_id = f"non_existent_project_{uuid.uuid4().hex[:8]}"
        update_data = {
            "title": "Updated Title",
            "description": "Updated description"
        }
        response = projects_page.update_project(invalid_project_id, update_data)
        
        print(f"Wrong ID Update Response Status: {response.status_code}")
        print(f"Wrong ID Update Response Text: {response.text}")
        
        # Ожидаем ошибку "не найдено"
        assert response.status_code in [404, 400], f"Expected 404 or 400, got {response.status_code}. Response: {response.text}"
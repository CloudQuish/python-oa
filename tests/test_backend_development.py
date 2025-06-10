"""
Test cases for Backend Development Questions (16-20)
Each test is worth the points specified in the question docstring.
"""

import pytest
import json
import tempfile
import os
from unittest.mock import patch, MagicMock
from questions.backend_development import (
    question_16_create_rest_api,
    Question17DatabaseManager,
    Question18AuthenticationSystem,
    Question19APITestSuite,
    question_20_deployment_config
)


class TestQuestion16RestAPI:
    """Test Question 16: Basic REST API (5 points)"""
    
    @pytest.fixture
    def app(self):
        """Create test app instance"""
        app = question_16_create_rest_api()
        app.config['TESTING'] = True
        return app
    
    @pytest.fixture
    def client(self, app):
        """Create test client"""
        return app.test_client()
    
    def test_get_users_empty(self, client):
        """Test GET /users with empty database"""
        response = client.get('/users')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0
    
    def test_create_user(self, client):
        """Test POST /users to create new user"""
        user_data = {
            "name": "John Doe",
            "email": "john@example.com"
        }
        response = client.post('/users', 
                            data=json.dumps(user_data),
                            content_type='application/json')
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['name'] == "John Doe"
        assert data['email'] == "john@example.com"
        assert 'id' in data
        assert 'created_at' in data
    
    def test_get_user_by_id(self, client):
        """Test GET /users/<id> to get specific user"""
        # First create a user
        user_data = {
            "name": "Jane Doe",
            "email": "jane@example.com"
        }
        create_response = client.post('/users',
                                   data=json.dumps(user_data),
                                   content_type='application/json')
        created_user = json.loads(create_response.data)
        
        # Then get the user by ID
        response = client.get(f'/users/{created_user["id"]}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['name'] == "Jane Doe"
        assert data['email'] == "jane@example.com"
    
    def test_update_user(self, client):
        """Test PUT /users/<id> to update user"""
        # First create a user
        user_data = {"name": "Bob Smith", "email": "bob@example.com"}
        create_response = client.post('/users',
                                   data=json.dumps(user_data),
                                   content_type='application/json')
        created_user = json.loads(create_response.data)
        
        # Update the user
        update_data = {"name": "Bob Johnson", "email": "bob.johnson@example.com"}
        response = client.put(f'/users/{created_user["id"]}',
                            data=json.dumps(update_data),
                            content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['name'] == "Bob Johnson"
        assert data['email'] == "bob.johnson@example.com"
    
    def test_delete_user(self, client):
        """Test DELETE /users/<id> to delete user"""
        # First create a user
        user_data = {"name": "Alice Brown", "email": "alice@example.com"}
        create_response = client.post('/users',
                                   data=json.dumps(user_data),
                                   content_type='application/json')
        created_user = json.loads(create_response.data)
        
        # Delete the user
        response = client.delete(f'/users/{created_user["id"]}')
        assert response.status_code == 204
        
        # Verify user is deleted
        get_response = client.get(f'/users/{created_user["id"]}')
        assert get_response.status_code == 404


class TestQuestion17DatabaseManager:
    """Test Question 17: Database Operations (5 points)"""
    
    @pytest.fixture
    def db_manager(self):
        """Create database manager with temporary database"""
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
            db_path = f.name
        
        manager = Question17DatabaseManager(db_path)
        yield manager
        
        # Cleanup
        if os.path.exists(db_path):
            os.unlink(db_path)
    
    def test_create_user(self, db_manager):
        """Test creating a user"""
        user_id = db_manager.create_user("John Doe", "john@example.com")
        assert user_id is not None
        assert isinstance(user_id, int)
    
    def test_get_user(self, db_manager):
        """Test getting a user by ID"""
        user_id = db_manager.create_user("Jane Doe", "jane@example.com")
        user = db_manager.get_user(user_id)
        
        assert user is not None
        assert user['name'] == "Jane Doe"
        assert user['email'] == "jane@example.com"
        assert user['id'] == user_id
    
    def test_get_all_users(self, db_manager):
        """Test getting all users"""
        db_manager.create_user("User 1", "user1@example.com")
        db_manager.create_user("User 2", "user2@example.com")
        
        users = db_manager.get_all_users()
        assert len(users) == 2
        assert users[0]['name'] == "User 1"
        assert users[1]['name'] == "User 2"
    
    def test_update_user(self, db_manager):
        """Test updating a user"""
        user_id = db_manager.create_user("Bob Smith", "bob@example.com")
        success = db_manager.update_user(user_id, name="Bob Johnson")
        
        assert success is True
        user = db_manager.get_user(user_id)
        assert user['name'] == "Bob Johnson"
        assert user['email'] == "bob@example.com"  # Should remain unchanged
    
    def test_delete_user(self, db_manager):
        """Test deleting a user"""
        user_id = db_manager.create_user("Alice Brown", "alice@example.com")
        success = db_manager.delete_user(user_id)
        
        assert success is True
        user = db_manager.get_user(user_id)
        assert user is None


class TestQuestion18AuthenticationSystem:
    """Test Question 18: Authentication System (5 points)"""
    
    @pytest.fixture
    def auth_system(self):
        """Create authentication system instance"""
        return Question18AuthenticationSystem()
    
    def test_password_hashing(self, auth_system):
        """Test password hashing and verification"""
        password = "testpassword123"
        hashed = auth_system.hash_password(password)
        
        assert hashed != password
        assert auth_system.verify_password(password, hashed) is True
        assert auth_system.verify_password("wrongpassword", hashed) is False
    
    def test_user_registration(self, auth_system):
        """Test user registration"""
        success = auth_system.register_user("test@example.com", "password123", "Test User")
        assert success is True
        
        # Should not allow duplicate registration
        duplicate = auth_system.register_user("test@example.com", "password456", "Another User")
        assert duplicate is False
    
    def test_user_login(self, auth_system):
        """Test user login"""
        # Register user first
        auth_system.register_user("login@example.com", "password123", "Login User")
        
        # Valid login
        token = auth_system.login_user("login@example.com", "password123")
        assert token is not None
        assert isinstance(token, str)
        
        # Invalid login
        invalid_token = auth_system.login_user("login@example.com", "wrongpassword")
        assert invalid_token is None
    
    def test_token_verification(self, auth_system):
        """Test JWT token verification"""
        # Register and login user
        auth_system.register_user("token@example.com", "password123", "Token User")
        token = auth_system.login_user("token@example.com", "password123")
        
        # Verify valid token
        user_data = auth_system.verify_token(token)
        assert user_data is not None
        assert user_data['email'] == "token@example.com"
        
        # Verify invalid token
        invalid_data = auth_system.verify_token("invalid.token.here")
        assert invalid_data is None


class TestQuestion19APITestSuite:
    """Test Question 19: API Testing (5 points)"""
    
    @pytest.fixture
    def test_suite(self):
        """Create API test suite instance"""
        return Question19APITestSuite("http://localhost:5000")
    
    @patch('requests.get')
    def test_get_endpoint(self, mock_get, test_suite):
        """Test GET endpoint testing"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "success"}
        mock_get.return_value = mock_response
        
        result = test_suite.test_get_endpoint("/test")
        assert result['status_code'] == 200
        assert result['data'] == {"message": "success"}
    
    @patch('requests.post')
    def test_post_endpoint(self, mock_post, test_suite):
        """Test POST endpoint testing"""
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"id": 1, "name": "test"}
        mock_post.return_value = mock_response
        
        result = test_suite.test_post_endpoint("/users", {"name": "test"})
        assert result['status_code'] == 201
        assert result['data']['id'] == 1
    
    @patch('requests.put')
    def test_put_endpoint(self, mock_put, test_suite):
        """Test PUT endpoint testing"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 1, "name": "updated"}
        mock_put.return_value = mock_response
        
        result = test_suite.test_put_endpoint("/users/1", {"name": "updated"})
        assert result['status_code'] == 200
        assert result['data']['name'] == "updated"
    
    @patch('requests.delete')
    def test_delete_endpoint(self, mock_delete, test_suite):
        """Test DELETE endpoint testing"""
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_delete.return_value = mock_response
        
        result = test_suite.test_delete_endpoint("/users/1")
        assert result['status_code'] == 204


class TestQuestion20DeploymentConfig:
    """Test Question 20: Deployment Configuration (5 points)"""
    
    def test_development_config(self):
        """Test development configuration"""
        get_config = question_20_deployment_config()
        config = get_config('development')
        
        assert config is not None
        assert 'DATABASE_URL' in config
        assert 'SECRET_KEY' in config
        assert 'DEBUG' in config
        assert 'PORT' in config
        assert 'ALLOWED_HOSTS' in config
        assert config['DEBUG'] is True
    
    def test_production_config(self):
        """Test production configuration"""
        get_config = question_20_deployment_config()
        config = get_config('production')
        
        assert config is not None
        assert config['DEBUG'] is False
        assert isinstance(config['PORT'], int)
        assert isinstance(config['ALLOWED_HOSTS'], list)
    
    def test_testing_config(self):
        """Test testing configuration"""
        get_config = question_20_deployment_config()
        config = get_config('testing')
        
        assert config is not None
        assert config['DEBUG'] is False
        assert 'test' in config['DATABASE_URL'].lower()
    
    @patch.dict(os.environ, {'SECRET_KEY': 'test-secret', 'PORT': '8080'})
    def test_environment_variable_loading(self):
        """Test loading configuration from environment variables"""
        get_config = question_20_deployment_config()
        config = get_config('development')
        
        assert config['SECRET_KEY'] == 'test-secret'
        assert config['PORT'] == 8080
    
    def test_invalid_environment(self):
        """Test handling invalid environment"""
        get_config = question_20_deployment_config()
        config = get_config('invalid')
        
        # Should handle gracefully, either return default or None
        assert config is None or isinstance(config, dict) 
"""
Backend Development Questions (16-20) - 25 points total
These questions test backend development skills including REST APIs,
database operations, authentication, and testing concepts.
"""

from flask import Flask, request, jsonify
import sqlite3
import bcrypt
import jwt
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any


def question_16_create_rest_api():
    """
    Question 16: Basic REST API (5 points)
    
    Create a Flask REST API with the following endpoints:
    - GET /users - returns list of all users
    - GET /users/<id> - returns specific user by ID
    - POST /users - creates a new user
    - PUT /users/<id> - updates existing user
    - DELETE /users/<id> - deletes user
    
    Use in-memory storage (list/dict) for simplicity.
    Each user should have: id, name, email, created_at
    
    Returns:
        Flask: Configured Flask application
    """
    app = Flask(__name__)
    
    # In-memory storage
    users = []
    next_id = 1
    
    # TODO: Implement the REST API endpoints
    # @app.route('/users', methods=['GET'])
    # def get_users():
    #     pass
    
    # @app.route('/users/<int:user_id>', methods=['GET'])
    # def get_user(user_id):
    #     pass
    
    # @app.route('/users', methods=['POST'])
    # def create_user():
    #     pass
    
    # @app.route('/users/<int:user_id>', methods=['PUT'])
    # def update_user(user_id):
    #     pass
    
    # @app.route('/users/<int:user_id>', methods=['DELETE'])
    # def delete_user(user_id):
    #     pass
    
    return app


class Question17DatabaseManager:
    """
    Question 17: Database Operations (5 points)
    
    Create a database manager class that handles SQLite operations for a simple user table.
    The class should:
    - Initialize and create users table if it doesn't exist
    - Provide methods for CRUD operations (Create, Read, Update, Delete)
    - Handle database connections properly
    - Include error handling
    
    Table schema: users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, created_at TIMESTAMP)
    """
    
    def __init__(self, db_path="users.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database and create users table if it doesn't exist"""
        # TODO: Implement database initialization
        pass
    
    def create_user(self, name: str, email: str) -> Optional[int]:
        """Create a new user and return user ID"""
        # TODO: Implement user creation
        pass
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """Get user by ID"""
        # TODO: Implement get user
        pass
    
    def get_all_users(self) -> List[Dict]:
        """Get all users"""
        # TODO: Implement get all users
        pass
    
    def update_user(self, user_id: int, name: str = None, email: str = None) -> bool:
        """Update user information"""
        # TODO: Implement user update
        pass
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user by ID"""
        # TODO: Implement user deletion
        pass


class Question18AuthenticationSystem:
    """
    Question 18: Authentication System (5 points)
    
    Create an authentication system with the following features:
    - Password hashing using bcrypt
    - JWT token generation and validation
    - User registration and login methods
    - Token expiration handling
    
    Use SECRET_KEY = "your-secret-key-here" for JWT encoding
    """
    
    def __init__(self):
        self.SECRET_KEY = "your-secret-key-here"
        self.users = {}  # In-memory user storage: {email: {password_hash, user_data}}
    
    def hash_password(self, password: str) -> str:
        """Hash a password using bcrypt"""
        # TODO: Implement password hashing
        pass
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify a password against its hash"""
        # TODO: Implement password verification
        pass
    
    def register_user(self, email: str, password: str, name: str) -> bool:
        """Register a new user"""
        # TODO: Implement user registration
        pass
    
    def login_user(self, email: str, password: str) -> Optional[str]:
        """Login user and return JWT token"""
        # TODO: Implement user login and token generation
        pass
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """Verify JWT token and return user data"""
        # TODO: Implement token verification
        pass
    
    def generate_token(self, user_data: Dict) -> str:
        """Generate JWT token for user"""
        # TODO: Implement token generation
        pass


class Question19APITestSuite:
    """
    Question 19: API Testing (5 points)
    
    Create a test suite for testing REST API endpoints.
    This class should provide methods to test common API scenarios:
    - Test successful requests
    - Test error handling
    - Test authentication
    - Test data validation
    
    Use requests library for HTTP calls.
    """
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = None  # Could use requests.Session() for maintaining cookies/headers
    
    def test_get_endpoint(self, endpoint: str, expected_status: int = 200) -> Dict:
        """Test GET endpoint and return response data"""
        # TODO: Implement GET endpoint testing
        pass
    
    def test_post_endpoint(self, endpoint: str, data: Dict, expected_status: int = 201) -> Dict:
        """Test POST endpoint with data"""
        # TODO: Implement POST endpoint testing
        pass
    
    def test_put_endpoint(self, endpoint: str, data: Dict, expected_status: int = 200) -> Dict:
        """Test PUT endpoint with data"""
        # TODO: Implement PUT endpoint testing
        pass
    
    def test_delete_endpoint(self, endpoint: str, expected_status: int = 204) -> Dict:
        """Test DELETE endpoint"""
        # TODO: Implement DELETE endpoint testing
        pass
    
    def test_authentication(self, login_endpoint: str, credentials: Dict) -> str:
        """Test authentication and return token"""
        # TODO: Implement authentication testing
        pass


def question_20_deployment_config():
    """
    Question 20: Deployment Configuration (5 points)
    
    Create a deployment configuration system that:
    1. Loads configuration from environment variables
    2. Provides different configs for development, testing, production
    3. Validates required configuration values
    4. Returns appropriate configuration based on environment
    
    Required config values:
    - DATABASE_URL
    - SECRET_KEY  
    - DEBUG (boolean)
    - PORT (integer)
    - ALLOWED_HOSTS (list)
    
    Returns:
        dict: Configuration dictionary for the specified environment
    """
    import os
    
    def get_config(environment: str = 'development') -> Dict[str, Any]:
        """Get configuration for specified environment"""
        # TODO: Implement configuration loading and validation
        # Base configuration
        config = {
            'development': {
                'DATABASE_URL': os.getenv('DATABASE_URL', 'sqlite:///dev.db'),
                'SECRET_KEY': os.getenv('SECRET_KEY', 'dev-secret-key'),
                'DEBUG': True,
                'PORT': int(os.getenv('PORT', 5000)),
                'ALLOWED_HOSTS': ['localhost', '127.0.0.1']
            },
            'testing': {
                'DATABASE_URL': os.getenv('TEST_DATABASE_URL', 'sqlite:///test.db'),
                'SECRET_KEY': os.getenv('SECRET_KEY', 'test-secret-key'),
                'DEBUG': False,
                'PORT': int(os.getenv('PORT', 5001)),
                'ALLOWED_HOSTS': ['localhost']
            },
            'production': {
                'DATABASE_URL': os.getenv('DATABASE_URL'),
                'SECRET_KEY': os.getenv('SECRET_KEY'),
                'DEBUG': False,
                'PORT': int(os.getenv('PORT', 80)),
                'ALLOWED_HOSTS': os.getenv('ALLOWED_HOSTS', '').split(',')
            }
        }
        
        # TODO: Add validation logic
        # TODO: Return appropriate configuration
        pass
    
    return get_config 
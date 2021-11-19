from typing import Mapping
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import re
import string

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        
        if not password_confirmation:
            raise UserInputError("Password confirmation is required")

        # Tämä uusi
        if password != password_confirmation:
            raise UserInputError("Password and confirmation don't match.")
  
        # Nämä tehtävästä 5
        sopiva_username = '^[a-z][a-z][a-z]+$'
        sopiiko = re.match(sopiva_username, username)

        if not sopiiko:
            raise UserInputError("Not a valid username.")

        sopiva_password = '^(?=.*[a-z])(?=.*[0-9]).{8,}$'
        sopiikopw = re.match(sopiva_password, password)

        if not sopiikopw:
            raise UserInputError("Not a valid password.")



 
user_service = UserService()

from entities.user import User
import re
# debugattavaan tiedostoon tulee tuoda tarvittavat moduulit
import sys, pdb

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        # pysäytetään ohjelman suoritus tälle riville
        # pdb.Pdb(stdout=sys.__stdout__).set_trace()

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        sopiva_username = '^[a-z][a-z][a-z]+$'
        sopiiko = re.match(sopiva_username, username)

        if not sopiiko:
            raise UserInputError("Not a valid username.")

        sopiva_password = '^(?=.*[a-z])(?=.*[0-9]).{8,}$'
        sopiikopw = re.match(sopiva_password, password)

        if not sopiikopw:
            raise UserInputError("Not a valid password.")
            
        
            

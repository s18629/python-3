import json
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.endpoints import HTTPEndpoint
import server.api.users.user_api_services as user_service
import database.database



db = database.database.get_database("db.sqlite")


# notes = sqlalchemy.Table(
#     'notes',
#     metadata,
#     sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
#     sqlalchemy.Column('login', sqlalchemy.String),
#     sqlalchemy.Column('password', sqlalchemy.String)
# )


class Login(HTTPEndpoint):
    async def post(self, request):
        return JSONResponse({'test': 'test123'})


class Register(HTTPEndpoint):
    async def post(self, request):
        data = await Request.json(request)
        login = data["login"]
        password = data["password"]
        # db_len = len(db.execute("SELECT * FROM users WHERE login = ?", (login,)).fetchall())
        #
        # if db_len > 0:
        #     print("sfafaf")

        if not user_service.validate_login(login):
            print("fafaf")

        if not user_service.validate_password(password):
            print("password suck")
            exit(1)

        if not user_service.has_user(db, login):
            print("user is istnieje")


        # if login == "dupa":
        #     print("dupa")

        # return JSONResponse({"login": data["login"],
        #                      "password": data["password"]})

        print(login, password)

        return JSONResponse({'message': "Succes!"}, status_code=200)


class Refresh(HTTPEndpoint):
    pass

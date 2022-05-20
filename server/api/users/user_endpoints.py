from sqlite3 import Cursor

import bcrypt
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.endpoints import HTTPEndpoint


import database.database

db = database.database.get_database("db.sqlite")


class Login(HTTPEndpoint):
    async def post(self, request):
        return JSONResponse({'test': 'test123'})


class Register(HTTPEndpoint):
    async def post(self, request):
        pass


class Refresh(HTTPEndpoint):
    pass

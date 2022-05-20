from starlette.routing import Route

from server.api.users.user_endpoints import Login, Register, Refresh

routes = [
    Route("/login", Login),
    Route("/register", Register),
    Route("/Refresh", Refresh)
]

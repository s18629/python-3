from starlette.applications import Starlette
from starlette.routing import Mount
from server.api.__init__ import routes as api_routes

routes = [
    Mount("/api", routes=api_routes, name="api"),
]



app = Starlette(
        debug=True,
        routes=routes
    )


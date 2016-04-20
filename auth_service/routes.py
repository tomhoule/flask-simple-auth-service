from flask import Blueprint, request, json
from auth_service.exceptions import (
    UnauthenticatedException, UnauthorizedException)

auth = Blueprint('auth', __name__)


def admin_only(view):
    def check_request():
        credentials = request.headers.get("Authenticate", default=None)
        if credentials is not None:
            if credentials == "i am the admin":
                return view()
            else:
                raise UnauthorizedException()
        else:
            raise UnauthenticatedException("Unauthenticated request")
    # raise Exception("heeeey yo")
    return check_request


@auth.route("/")
def hello():
    return "Coucou"


@auth.route("admin")
@admin_only
def admin():
    return "C’est passé"


@auth.errorhandler(UnauthenticatedException)
def handle_unauthenticated(exception):
    return (json.dumps({'error': exception.message}),
            401,
            {'Content-Type': 'application/json'})


@auth.errorhandler(UnauthorizedException)
def handle_unauthorized(exception):
    return (json.dumps({'error': exception.message}),
            403,
            {'Content-Type': 'application/json'})

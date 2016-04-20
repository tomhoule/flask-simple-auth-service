from auth_service.server import app

if __name__ == "__main__": # pragma: no cover
    app.run(host="0.0.0.0", port=5000)

from unittest import main
from coverage import Coverage

if __name__ == "__main__":
    cov = Coverage(source=["./auth_service"], auto_data=True)
    cov.start()

    # Run the tests
    main(module="auth_service.tests")

    cov.stop()
    cov.html_report()

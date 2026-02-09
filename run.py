import os
from app import create_app

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

os.environ["PROJECT_ROOT"] = PROJECT_ROOT


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

from src.controllers.usercontroller import UserController
from src.data.repositories.users import Users
from src.services.authentication.userservices import UserServices

app = Flask(__name__)
user_repo = Users()
user_service = UserServices(user_repo)
user_controller = UserController(user_service)


@app.route('/register', methods=['POST'])
def register_user():
    return user_controller.register()

@app.route('/login', methods=['POST'])
def login():
    return user_controller.login()

if __name__ == '__main__':
    app.run(port=5000, debug=True)

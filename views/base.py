import tornado
from core.logic import User


class BaseView(tornado.web.RequestHandler):
    @property
    def session(self):
        return session

    def get_current_user(self):
        #user_id = self.get_secure_cookie("user")
        #mock signed user
        user_id = 1
        if not user_id:
            return None
        return User.filter(id=user_id)

    def message(self, message='', redirect_to='/'):
        self.render('message.html', {'message': message, 'redirect_to': redirect_to})

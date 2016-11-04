import tornado
from core.models import session, User


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

        return self.session.query(User).filter_by(id=user_id).first()

from base import BaseView


class IndexView(BaseView):
    def get(self):
        self.get_current_user()
        self.render("index.html",)

    def post(self):
        import time
        title = self.get_argument('title', None)
        content = self.get_argument('content', None)
        blog = dict()
        if title and content:
            blog['title'] = title
            blog['content'] = content
            blog['date'] = int(time.time())
            coll = self.application.db.blog
            coll.insert(blog)
            self.redirect('/blog')
        self.redirect('/')

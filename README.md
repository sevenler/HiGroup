# HiGroup
    简介：
    HiGroup是一个打卡小组的后端project, 有用户可以创建小组、加入小组、每日打卡、打卡统计等功能
    这个project并不是一个完整的版本，是后端的一个简版的框架, 当然，它是能调式通过的.

    技术栈: Tornado + SQLAlchemy + Mysql 

    项目结构
        core - 业务核心
            models - ORM model
            logic - 逻辑封装
        requirements - 项目依赖
        static - 静态文件
        templates - 模板文件
        views - request handler
        api - api handler 
        config.py - config
        app.py - 启动文件
        urls.py - 路由


    关于core/logic
    logic层是对core/model层的封装，并对views提供操作方法，
    这是一个典型的MVC设计，业务逻辑都会放到logic层，同时事务、缓存、业务操作日志都会放到这里。

    logic.Group 的典型用法:

        from core.logic import Group
        group = Group.create(title='Join us',  description='join us please')
        group_list = Group.filter(id=0)
        group = group_list[0]
        me = get_currenct_user()
        group.join(me)
        group.checkin(me)
        print group.info()


    views.handler 的典型写法：
        
        from core.logic import Group
        def post(self, group_id):
            me = self.get_current_user()
            group = Group(group_id)
            group.join(me)
            return redirect('/group/%s/'%group.id, group=group.info())

    api.handler 的典型写法:
        
        from core.logic import Group
        def post(self, group_id):
            me = self.get_current_user()
            group = Group(group_id)
            group.join(me)
            return group.info()

    Tips: 
    views和api统一调用core.logic的方法来达到业务在website和api中保持一致
    同时，常见的做法也会在 core.logic 再封装一层conext，每个session会对应实例化一个context
    views和api通过context来调用所有的业务操作，在context的内部有用户登录信息、权限校验、统计等等。
    如果并发提高，需要进行RPC、微服务等架构调整的话，context的设计可以作为一个服务的接口，
    只需要去重构context内部去作分布式的调用就好，views、api一点代码都不需要改.


    logic.logic 的典型内部写法：

        from core.model import Group as GroupModel

        class Group(object):
            def __init__(self, pk, model=None):
                self._pk = pk
                self._model = model
                self._info = None

            def _lazy_load(self):
                #可以在这里添加缓存
                if self._info == None:
                    if self._model == None:
                        self._model = GroupModel()
                    else:
                        self._info = {
                            'title': self._model.title,
                            'descritpion': self._model.description,
                        }

            def info(self):
                self._lazy_load()
                return self._info

            def update(self, title):
                self._lazy_load()
                self._model.title = title
                self._info['title'] = title
                #如果有缓存，需要更新缓存
                #如果有事务一致性需求，可以在这里加上事务
                session.add(self._model)
                session.flush()

            @classmethod
            def create(cls, **kwargs):
                group_model = GroupModel()
                group_model.title = kwargs['title']
                group_model.description = kwargs['description']
                #如果有事务一致性需求，可以在这里加上事务
                session.add(group_model)
                session.flush()

### Run
    pip install requirement/prod.txt
    edit DB_PATH in config.py
    python app.py
    mysql -uuser hi_group < mock.sql
    chrome http://localhost:8002/

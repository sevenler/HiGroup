# HiGroup
    技术栈: Tornado + SQLAlchemy + Mysql 

####初始化项目(2016.11.2)
        
    项目结构
        core - 业务核心
            models - ORM model
        requirements - 项目依赖
        static - 静态文件
        templates - 模板文件
        views - request handler
        app.py - 启动文件
        urls.py - 路径路由

    完成项目结构、Tornado、Mysql调试
    
    
####调试SQLAlchemy(2016.11.4)
    
    添加SQLAlchemy ORM文件(core/models/*), 调试通过


####定义Model & 添加Logic & 添加Views(2016.11.5)

    models/user/User  用户表 
    models/group/Group  小组
    models/group/GroupPartner  小组成员
    models/group/GroupCheckIn  小组打卡

    添加core/logic
    logic层是对model层的封装，并对views提供操作方法，这是一个典型的MVC设计，业务逻辑都会放到logic层，同时事务、缓存、日志都会放到这里。

    Group的用法：
        from core.logic import Group

        group = Group.create(title='Join us',  description='join us please')
        group_list = Group.filter(id=0)
        group = group_list[0]
        me = get_currenct_user()
        group.join(me)
        group.checkin(me)

    添加views/*
        views 调用logic作增删改查


####Finish Debug(2016.11.7)

    

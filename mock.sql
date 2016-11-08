insert into user (id, email, name, description, avatar_url)
values (
    1,
    'johnnyxyz@163.com',
    'daniel.song',
    'cool boy',
    'https://avatars3.githubusercontent.com/u/1610334?v=3&s=466'
);
insert into user (id, email, name, description, avatar_url)
values (
    2,
    'iamxiaoning@gmail.com',
    'WaraId',
    'cool boy',
    'https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-5669879209263104-hp.jpg'
);

insert into groups (id, title, description, max_partner_number, joined_partner_number, user_level_expectation, created_user_id)
values (
    1,
    '雅思强制早起贴',
    '为今年分手的同学创建。自愿加入，时间不等人！',
    50, 2, 5, 1
);
insert into groups (id, title, description, max_partner_number, joined_partner_number, user_level_expectation, created_user_id)
values (
    2,
    'phd香港2017 fall交流小组',
    '小组内会提供各种求职信息，供每位来港的同学选择。',
    50, 0, 0, 1
);

insert into groups (id, title, description, max_partner_number, joined_partner_number, user_level_expectation)
values (
    3,
    'phd香港2017 fall交流小组',
    '小组内会提供各种求职信息，供每位来港的同学选择。',
    50, 0, 0, 1
);

insert into group_partner (group_id, user_id) values (1, 1);
insert into group_partner (group_id, user_id) values (1, 2);

insert into group_check_in (group_id, user_id, checkin_date) values (1, 2, '20160718');
insert into group_check_in (group_id, user_id, checkin_date) values (1, 1, '20160718');
insert into group_check_in (group_id, user_id, checkin_date) values (1, 1, '20160717');

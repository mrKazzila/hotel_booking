register_user_data = [
    # email, password, status code, is_add_in_db
    ('mrrobot2@test.com', '1122eliot', 200, True),
    ('mrrobot2@test.com', '1122eliot', 409, True),
    ('mrrobot3@test.com', '1122eliot', 200, True),
    ('mrrobot', '1122el1ot', 422, False),
    ('', '', 422, False),
    ('mrrobot4@test.com', '1', 422, False),
    ('mrrobot5@test.com', None, 422, False),
    ('@test.com', '1122e', 422, False),
    ('mrrobot5@test.com', '      ', 422, False),  # 6 whitespace
]

add_and_get_booking_data = [
    # room_id, date_from, date_to, book_count, status_code
    (4, '2030-05-01', '2030-05-21', 3, 200),
    (4, '2030-05-01', '2030-05-21', 4, 200),
    (4, '2030-05-01', '2030-05-21', 5, 200),
    (4, '2030-05-01', '2030-05-21', 6, 200),
    (4, '2030-05-01', '2030-05-21', 7, 200),
    (4, '2030-05-01', '2030-05-21', 8, 200),
    (4, '2030-05-01', '2030-05-21', 9, 200),
    (4, '2030-05-01', '2030-05-21', 10, 200),
    (4, '2030-05-01', '2030-05-21', 10, 409),
    (6, '2030-05-01', '2030-05-21', 11, 200),
    (4, '2030-05-01', '2030-05-21', 11, 409),
    (4, '2030-05-21', '2030-05-22', 12, 200),
]

delete_user_booking_by_id_data = [
    # booking_id, status_code
    (3, 200),
    (3, 404),
    (6, 404),
]
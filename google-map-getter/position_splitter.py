from haversine import inverse_haversine, Direction


def get_position_after_moved_east(y1, x1, radius):
    return inverse_haversine((y1, x1), radius, Direction.EAST, unit='m')


def get_position_after_moved_south(y1, x1, radius):
    return inverse_haversine((y1, x1), radius, Direction.SOUTH, unit='m')


def get_position_list(y1, x1, y2, x2, radius):
    now_y, now_x = y1, x1
    position_list = []

    while now_y > y2:
        while now_x < x2:
            noy_y, now_x = get_position_after_moved_east(now_y, now_x, radius / 2)
            position_list.append((now_y, now_x))
        now_x = x1
        now_y, now_x = get_position_after_moved_south(now_y, now_x, radius / 2)

    return position_list

# y1 = 21.04378
# x1 = 105.81020
# y2 = 20.98680
# x2 = 105.86385
# RADIUS = 10000
#
# posi_list = get_position_list(y1, x1, y2, x2, RADIUS)
# print(len(posi_list))
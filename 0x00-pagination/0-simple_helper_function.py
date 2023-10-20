#!/usr/bin/env python3
''' simple helper function'''


def index_range(page: int = 0, page_size: int = 0) -> tuple:
    ''' simple helper function'''
    count_tuple = [0, 0]
    count = 0

    for i in range(page):
        count += 1
        count_all = count * page_size
        curr_page = count_all - page_size

        count_tuple[0] = curr_page
        count_tuple[1] = count_all

    return tuple(count_tuple)

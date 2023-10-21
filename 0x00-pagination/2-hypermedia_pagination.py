#!/usr/bin/env python3
''' class Server '''
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' returning a dict with additional information '''
        assert page > 0
        assert page_size > 0

        # Calculate the start and end indices using the index_range function
        start, end = index_range(page, page_size)

        # Get the dataset
        dataset = self.dataset()

        # Check if the indices are out of range
        if start >= len(dataset):
            return {
                "page_size": 0,
                "page": page,
                "data": [],
                "next_page": None,
                "prev_page": None,
                "total_pages": math.ceil(len(dataset) / page_size)
            }

        return {
            "page_size": page_size,
            "page": page,
            "data": dataset[start:end],
            "next_page": page + 1 if end < len(dataset) else None,
            "prev_page": page - 1 if start > 0 else None,
            "total_pages": math.ceil(len(dataset) / page_size)
        }


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

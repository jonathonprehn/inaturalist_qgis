

import abc 


class INaturalistSearchQuery:

    def __init__(self):
        pass

    @abc.abstractmethod
    def last_query_error(self):
        pass

    @abc.abstractmethod
    def query_page_number(self):
        pass

    @abc.abstractmethod
    def query_max_pages(self):
        pass

    @abc.abstractmethod
    def query_total_results(self):
        pass

    @abc.abstractmethod
    def get_current_page_results(self):
        pass

    @abc.abstractmethod
    def prev_page(self):
        pass

    @abc.abstractmethod
    def next_page(self):
        pass

    @abc.abstractmethod
    def query(self):
        pass



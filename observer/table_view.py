"""An observer by Farseen Ashraf"""
from interface_data_view import IDataView


class TableView(IDataView):
    """The concrete observer"""

    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f"TableView, id: {self._id}")
        self.draw(data)

    def draw(self, data):
        print(f"Drawing a Table using data: {data}")

    def delete(self):
        self._observable.unsubscribe(self._id)

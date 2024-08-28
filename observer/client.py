"""Observer Design Pattern use case example by Farseen Ashraf"""

from data_model import DataModel
from data_controller import DataController
from pie_graph_view import PieGraphView
from bar_graph_view import BarGraphView
from table_view import TableView


# A local data model that the hypothetical external controller updates
data_model = DataModel()

# Add some visualization that uses the dataview
pie_graph_view = PieGraphView(data_model)
bar_graph_view = BarGraphView(data_model)
table_view = TableView(data_model)

# A hypothetical data controller running in a different process
data_controller = DataController()

# A hypothetical external data controller updates some data
data_controller.notify([1, 2, 3])

# A client now removes the local bar graph
bar_graph_view.delete()
print()

# The hypothetical external data controller, updates the data again
data_controller.notify([4, 5, 6])

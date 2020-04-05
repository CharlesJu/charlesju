import plotly.graph_objects as go
import numpy as np
import pandas as pd

fig = go.Figure()

ourLine = pd.DataFrame(columns = ["x_values", "y_values"])
ourLine.set_index("x_values")
ourLine.at[latest, "x_values"] = 0
ourLine.at[latest, "y_values"] = 0
ourLine.at[latest, "x_values"] = 1
ourLine.at[latest, "y_values"] = 1

fig.add_trace(go.Scatter(x = ourLine["x_values"], y = ourLine["y_values"], mode = 'lines+markers', name = 'LSRL'))
fig.write_html('graph.html')

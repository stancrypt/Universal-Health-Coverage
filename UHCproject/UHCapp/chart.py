import plotly.graph_objects as go

def calculate():
    x=[2,34,6,22,66,88,99,556,66,9]
    y=[5,33,66,77,53,6,23,79,43,87]
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))  # Scatter plot with markers
    fig.update_layout(title='Testing a Chart')

    fig.show()  # Display the chart
    
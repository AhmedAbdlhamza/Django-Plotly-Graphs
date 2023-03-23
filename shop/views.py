import plotly.graph_objs as go
from django.shortcuts import render
from plotly.subplots import make_subplots
from django.shortcuts import render
from .models import WeeklyData
import plotly.graph_objs as go
from plotly.subplots import make_subplots



def index(request):
    weekly_data = WeeklyData.objects.all()

    # Process the data for plotting
    dates = [data.date for data in weekly_data]
    sales = [data.sales for data in weekly_data]
    profit = [data.profit for data in weekly_data]
    inventory = [data.inventory for data in weekly_data]
    # Add other parameters here
    # ...

    # Create the graphs
    fig = make_subplots(rows=3, cols=3, shared_xaxes=True, vertical_spacing=0.1, horizontal_spacing=0.1)

    fig.add_trace(go.Scatter(x=dates, y=sales, mode='lines', name='Sales'), row=1, col=1)
    fig.add_trace(go.Scatter(x=dates, y=profit, mode='lines', name='Profit'), row=1, col=2)
    fig.add_trace(go.Scatter(x=dates, y=inventory, mode='lines', name='Inventory'), row=1, col=3)
    # Add other "Critical" parameters here
    # ...
    # Add other "Critical" parameters here
    # ...

    fig.update_layout(title="Critical Parameters", showlegend=False)

    # Create the second figure for "Normal" parameters
    fig2 = make_subplots(rows=3, cols=3, shared_xaxes=True, vertical_spacing=0.1, horizontal_spacing=0.1)

    # Add "Normal" parameters here
    # ...
    # Example:
    fig2.add_trace(go.Scatter(x=dates, y=sales, mode='lines', name='Parameter1'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=dates, y=inventory, mode='lines', name='Parameter2'), row=1, col=2)
    # ...

    fig2.update_layout(title="Normal Parameters", showlegend=False)

    context = {
        'plot': fig.to_html(full_html=False),
        'plot2': fig2.to_html(full_html=False),
    }

    return render(request, 'shop/index.html', context)

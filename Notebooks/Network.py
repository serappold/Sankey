import pandas as pd
import plotly.offline as py
import plotly.graph_objects as go
import os

def make_network():
    # Load data from CSV files
    nodes = pd.read_csv(os.path.join(os.getcwd(), 'Data', '03 Processed', 'nodes.csv'))
    links = pd.read_csv(os.path.join(os.getcwd(), 'Data', '03 Processed', 'links.csv'))

    # Print data to verify
    print(nodes.head())
    print(links.head())

    # Create edges list for network graph
    edges = []
    x = 1
    for _, row in links.iterrows():
        print((nodes.loc[row['FromSystemID'], 'Systems'], nodes.loc[row['SystemID'], 'Systems']))
        edges.append((nodes.loc[row['FromSystemID'], 'Systems'], nodes.loc[row['SystemID'], 'Systems']))
        x = x + 1
    
    # Create network graph
    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=nodes['Systems']),
        link=dict(
            source=[nodes.loc[edge[0], 'Systems'] for edge in edges],
            target=[nodes.loc[edge[1], 'Systems'] for edge in edges])))

    # Define layout
    fig.update_layout(title='System to System Element Flow', font=dict(size=20))

    # Generate HTML file
    try:
        py.plot(fig, validate=True, filename=os.path.join(os.getcwd(), 'Reports', 'Systems_network.html'))
        print('HTML file generated successfully.')
    except Exception as e:
        print('Error:', e)

    print('Completed.')

# Call the function


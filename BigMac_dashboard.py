from dash import Dash
import dash
from dash import dcc, html
import plotly.express as px
from data import load_big_mac_data

df_big_mac_top_5, df_big_mac = load_big_mac_data()

app = Dash(name='big_mac')

fig = px.bar(df_big_mac_top_5,
             x='countries',
             y='dollar_price',
             labels={"countries": "Country", "dollar_price": "Dollar price"},
             title="Big Mac Index Top 5",
             template="simple_white")

fig_scatter = px.scatter(df_big_mac,
                         x='country_code',
                         y='dollar_price',
                        labels={"country_code": "currencies", "dollar_price": "Dollar price"},
                        template="simple_white",
                        title="Price of a Big Mac in dollars",
                         )

app.layout = html.Div([
                html.Div([dcc.Graph(figure=fig),
                       dcc.Graph(figure=fig_scatter)])
])

if __name__ == '__main__':
    app.run_server(debug=True)

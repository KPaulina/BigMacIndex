from dash import Dash
from dash import dcc, html
import plotly.express as px
from data import load_big_mac_data, get_top_5_countries_with_highest_big_mac_index, sort_by_the_highest_value

df_big_mac = load_big_mac_data()
df_big_mac = sort_by_the_highest_value(df_big_mac)
df_big_mac_top_5 = get_top_5_countries_with_highest_big_mac_index(df_big_mac)

app = Dash(name='big_mac')
server = app.server

fig_big_mac_index_top_5 = px.bar(df_big_mac_top_5,
                                 x='countries',
                                 y='dollar_price',
                                 labels={"countries": "Countries", "dollar_price": "Dollar price"},
                                 title="Big Mac Index Top 5",
                                 template="simple_white")

fig_big_macs_price_in_dollars = px.scatter(df_big_mac,
                                           x='country_code',
                                           y='dollar_price',
                                           labels={"country_code": "Countries", "dollar_price": "Dollar price"},
                                           title="Price of a Big Mac in dollars",
                                           template="simple_white")

app.layout = html.Div([
                html.Div([dcc.Graph(figure=fig_big_mac_index_top_5),
                          dcc.Graph(figure=fig_big_macs_price_in_dollars)])
])

if __name__ == '__main__':
    app.run_server(debug=True)

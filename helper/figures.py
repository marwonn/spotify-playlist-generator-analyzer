import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
import plotly.express as px

def make_figures(data, track_name, popularity):

    # Build Figure Section ----------------------------------------------
    categories = ["energy", "liveness", "speechiness",	"acousticness",	"instrumentalness", "danceability",	"valence"]
    
    r = data.mean()
    # Avg audio features of the TOP 500 Rolling Stones Magazine
    r2 = [0.601546, 0.215710, 0.064273, 0.345752, 0.037234, 0.554010, 0.638210]
    # Avg audio features of the TOP Tracks 2020 Germany
    r3 = [0.658820, 0.169402, 0.148086, 0.223102, 0.019515, 0.737580, 0.539320]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=r,
        theta=categories,
        fill='toself',
        name='Your playlist profile',
        fillcolor="red"
    ))
    fig.add_trace(go.Scatterpolar(
        r=r2,
        theta=categories,
        fill='toself',
        fillcolor="green",
        name='TOP 500 Rolling Stones Magazine Profile',
        opacity = 0.4,
        visible='legendonly'
    ))
    fig.add_trace(go.Scatterpolar(
        r=r3,
        theta=categories,
        fill='toself',
        fillcolor='blue',
        name='TOP Tracks 2020 Germany',
        opacity = 0.4,
        visible='legendonly'
    ))

    fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                    )),
                showlegend=True,
                title="Your music profile",
                title_x=0.5,
                font=dict(
                    family="Arial",
                    size=12,
                    color="black"),
                legend=dict(
                    orientation="v",
                    y=-0.45,
                    x=0.3
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
                )

    fig.update_traces(mode="none", selector=dict(type='scatterpolar'))

    config = dict({'displaylogo': False,
                    'scrollZoom': True,
                    'displayModeBar': False
               })

    figure = plot(fig, config=config, output_type='div')

    # Violin Figure Section ----------------------------------------------------------------
    data_violin = {"tracks": track_name,
                   "popularity": popularity}

    df_violin = pd.DataFrame(data_violin, columns = ['tracks', 'popularity'])

    fig_violin = px.violin(df_violin["popularity"], box=True,# draw box plot inside the violin
                    points='outliers', # can be 'outliers', 'all', or False
                )

    fig_violin.update_layout(title="Popularity of your Music",
                             title_x=0.5,
                             paper_bgcolor='rgba(0,0,0,0)',
                             plot_bgcolor='rgba(0,0,0,0)'
                            )

    config_violin = dict({'displaylogo': False,
                          'scrollZoom': True,
                          'displayModeBar': False
                        })

    fig_violin_plot = plot(fig_violin, config=config_violin, output_type='div')

    return figure, fig_violin_plot
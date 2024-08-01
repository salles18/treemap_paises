import pandas as pd
import plotly.express as px


data = {
    'Country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico'],
    'Population': [1444216107, 1393409038, 332915073, 276361783, 225199937, 213993437, 211400708, 166303498, 145912025, 130262216],
    'Area': [9600000, 3287000, 9370000, 1900000, 881000, 8516000, 923768, 147570, 17098242, 1964375]  # Área em km²
}


df = pd.DataFrame(data)


fig = px.treemap(df, 
                 path=['Country'], 
                 values='Population',
                 title='População de Países no Mundo',
                 color='Population', 
                 color_continuous_scale='Viridis',
                 hover_data={'Country': True, 'Population': True, 'Area': True})


fig.update_traces(
    hovertemplate="<b>%{label}</b><br>Population: %{value:,}<br>Area: %{customdata[1]:,} km²<extra></extra>"
)


fig.write_html("treemap_population_interactive.html")


fig.show()

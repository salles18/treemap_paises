import pandas as pd
import plotly.express as px

# Dados fictícios de população de países
data = {
    'Country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico'],
    'Population': [1444216107, 1393409038, 332915073, 276361783, 225199937, 213993437, 211400708, 166303498, 145912025, 130262216]
}

# Criar um DataFrame
df = pd.DataFrame(data)

# Criar o treemap
fig = px.treemap(df, 
                 path=['Country'], 
                 values='Population',
                 title='População de Países no Mundo',
                 color='Population', 
                 color_continuous_scale='Viridis')

# Salvar o treemap como um arquivo HTML
fig.write_html("treemap_population.html")

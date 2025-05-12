import pandas as pd
import plotly.express as px
import preswald

# Load dataset
# Make sure region_01.csv is at data/region_01.csv
df = pd.read_csv('data/region_01.csv')

# Display app title and total record count
preswald.text("# Region 01 Incident Dashboard")
preswald.text(f"Total records: {len(df)}")

# Show the first 10 rows of the dataset
preswald.text("## Data Preview (first 10 rows)")
preswald.table(df.head(10))

# Simple filter: only incidents in months > 6 (July–December)
filtered = df[df['imonth'] > 6]
preswald.text(f"## Filtered Data (imonth > 6): {len(filtered)} records")
preswald.table(filtered.head(10))

# Visualization 1: Scatter plot (month vs. day)
preswald.text("## Incidents by Month and Day")
fig_scatter = px.scatter(
    filtered,
    x='imonth',
    y='iday',
    color='country_txt',
    title='Incidents by Month and Day',
    labels={'imonth': 'Month', 'iday': 'Day', 'country_txt': 'Country'},
    hover_data=['city', 'region_txt']
)
fig_scatter.update_traces(marker=dict(size=8, opacity=0.7))
fig_scatter.update_layout(template='plotly_white')
preswald.plotly(fig_scatter)

# Visualization 2: Bar chart of incidents per month
preswald.text("## Incident Counts by Month")
month_counts = filtered['imonth'].value_counts().sort_index().reset_index()
month_counts.columns = ['Month', 'Incidents']
fig_bar = px.bar(
    month_counts,
    x='Month',
    y='Incidents',
    title='Number of Incidents by Month (Months > 6)',
    labels={'Incidents': 'Number of Incidents'}
)
fig_bar.update_layout(template='plotly_white', xaxis_tickmode='linear')
preswald.plotly(fig_bar)

# Visualization 3: Yearly trend line
preswald.text("## Yearly Incident Trend")
year_counts = df['iyear'].value_counts().sort_index().reset_index()
year_counts.columns = ['Year', 'Incidents']
fig_line = px.line(
    year_counts,
    x='Year',
    y='Incidents',
    title='Incidents per Year',
    labels={'Incidents': 'Number of Incidents'}
)
fig_line.update_layout(template='plotly_white')
preswald.plotly(fig_line)

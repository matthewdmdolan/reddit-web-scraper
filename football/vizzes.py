import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('database.db')
c = conn.cursor()

#c.execute("SELECT COUNT(*) FROM PopularPostInfo")
#print(c.fetchone())

# Execute the SQL command
df = pd.read_sql("SELECT * FROM PopularPostInfo", conn)
# Ensure the time column is interpreted as datetime
df['time'] = pd.to_datetime(df['time'])

print(df.head())

# Ensure the time column is interpreted as datetime
df['time'] = pd.to_datetime(df['time'])

# Create a 'month-year' column
df['month-year'] = df['time'].dt.to_period('M')

print(df.columns)

# Group by 'subreddit' and count the number of titles
df_grouped = df.groupby('subreddit').size().sort_values(ascending=False)

# Take the top 10 popular subreddits
top_subreddits = df_grouped.head(10)

# Plot the data
top_subreddits.plot(kind='bar')

plt.title('Top 10 Popular Subreddits')
plt.xlabel('Subreddit')
plt.ylabel('Number of Titles')

plt.show()

# Close the connection
conn.close()
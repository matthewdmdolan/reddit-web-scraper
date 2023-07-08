# import xml element tree
import xml.etree.ElementTree as ET

# give the connection parameters
# user name is root
# password is empty
# server is localhost
# database name is database
import xml.etree.ElementTree as ET
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS PopularPostInfo (
        id INTEGER PRIMARY KEY,
        title TEXT,
        user TEXT,
        comments TEXT,
        subreddit TEXT,
        content_link TEXT,
        time TEXT)
''')

# reading xml file , file name is posts.xml
tree = ET.parse('/Users/mattdolan/PycharmProjects/ScrapyWebScraper/posts.xml')

# In our xml file 'item' is the root for all data.
xml_data = tree.findall('item')

print("Number of items found: ", len(xml_data))

# Retrieving the data and insert into table
for i in xml_data:
    title = i.find('title/value').text
    user = i.find('user/value').text
    comments = i.find('comments/value').text
    subreddit = i.find('subreddit/value')
    subreddit = subreddit.text if subreddit is not None else None
    content_link = i.find('content_link/value').text
    time = i.find('time/value').text

    print(title, user, comments, subreddit, content_link, time) # To see what data is going to be inserted

    # Execute the SQL command
    c.execute(
        "INSERT INTO PopularPostInfo (title, user, comments, subreddit, content_link, time) VALUES (?, ?, ?, ?, ?, ?)",
        (title, user, comments, subreddit, content_link, time))

# Commit the changes and close the connection
conn.commit()
conn.close()

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Execute the SQL command
c.execute("SELECT * FROM PopularPostInfo")

# Fetch all the rows
rows = c.fetchall()

print("Number of rows in the table: ", len(rows))

for row in rows:
    print(row)

conn.close()



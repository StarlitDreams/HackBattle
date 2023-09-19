from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

#set up mathplot lib
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')

# Read yt_key and save it into a variable
with open('yt_key.txt', 'r') as f:
    api_key = f.read()
channel_id = 'UCX6OQ3DkcsbYNE6H8uQQuVA'

# Build the service
youtube = build('youtube', 'v3', developerKey=api_key)

# Function to get channel statistics
def get_channel_statistics(youtube, channel_id):
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics', 
        id=channel_id)
    response = request.execute()
    
    data = dict(
        Channel_name=response['items'][0]['snippet']['title'],
        Subscribers=response['items'][0]['statistics']['subscriberCount'],
        Views=response['items'][0]['statistics']['viewCount'],
        Total_Videos=response['items'][0]['statistics']['videoCount'],
        description=response['items'][0]['snippet']['description'],
        country=response['items'][0]['snippet']['country']
    )
    return data
     
channel_statistics = get_channel_statistics(youtube, channel_id)

# Create a DataFrame from the dictionary
channel_data = pd.DataFrame([channel_statistics])

# Drop the 'description' and 'country' columns
channel_data = channel_data.drop(columns=['description', 'country'])

# Setting the correct data types for each column
channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['Total_Videos'] = pd.to_numeric(channel_data['Total_Videos'])

# Print the resulting DataFrame
sns.set(rc={'figure.figsize':(11.7,8.27)})
ax = sns.barplot(x='Channel_name', y='Subscribers', data=channel_data)
plt.show()  # Display the plot

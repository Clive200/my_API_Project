import os
import googleapiclient.discovery

def main():
   
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyBXy2z08-9QwL_tYge_UJsiTw9Kd2BlB9g"  # Replace with your actual API key

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",
        maxResults=1
    )
    response = request.execute()

    if 'items' in response:
        video = response['items'][0]
        title = video['snippet']['title']
        channel = video['snippet']['channelTitle']
        publish_date = video['snippet']['publishedAt']
        view_count = video['statistics']['viewCount']

        print(f"Title: {title}")
        print(f"Channel: {channel}")
        print(f"Published Date: {publish_date}")
        print(f"View Count: {view_count}")

if __name__ == "__main__":
    main()

## end of document

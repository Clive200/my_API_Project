

import os
import googleapiclient.discovery

def main():
    # Set up the YouTube API client
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyBXy2z08-9QwL_tYge_UJsiTw9Kd2BlB9g"  # Replace with your actual API key

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

    # Make a request to get the details of a video
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",
        maxResults=1
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()

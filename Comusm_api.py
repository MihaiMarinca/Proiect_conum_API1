from googleapiclient.discovery import build
import pandas as pd


# Function to fetch video information using YouTube Data API
def fetch_video_info(video_id, api_key):
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        response = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        )
        video_info = response.execute()['items'][0]
        return video_info
    except Exception as e:
        print("Error fetching video information:", e)
        return None


# Function to process video information into a pandas DataFrame
def process_video_info(video_info):
    if video_info is None:
        return None
    title = video_info['snippet']['title']
    view_count = video_info['statistics']['viewCount']
    likes = video_info['statistics']['likeCount']
    data = {
        'Title': [title],
        'Views': [view_count],
        'Likes': [likes]
    }
    df = pd.DataFrame(data)
    return df


# Example usage
def main():
    video_id = input("Enter the YouTube video ID: ")
    api_key = input("Enter your YouTube Data API key: ")

    video_info = fetch_video_info(video_id, api_key)
    df = process_video_info(video_info)
    if df is not None:
        print("Video report:")
        print(df)
        df.to_csv("video_report.csv", index=False)
    else:
        print("Failed to generate video report.")

if __name__ == "__main__":
    main()

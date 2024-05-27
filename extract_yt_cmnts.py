import requests
from summarizer import get_llm
api_key = 'AIzaSyAhn3gq6lYIEkSnh7tBiG4zzrv0krQVfBs'

def get_yt_answer(video_id):
    comments = get_comments(video_id)
    prompt = get_prompt(comments) # TO DO
    llm =  get_llm()
    result = llm.invoke(prompt)
    print(result)
    return result

def get_comments(video_id):
    x = 1
    next_page_token = ''

    while True:
        if x > 400:
            break
        url = f'https://www.googleapis.com/youtube/v3/commentThreads?key={api_key}&textFormat=plainText&part=snippet&videoId={video_id}&pageToken={next_page_token}'
        response = requests.get(url)
        comments = ""
        if response.status_code == 200:
            data = response.json()
            for item in data['items']:
                comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments += comment_text
                x+=1

            if 'nextPageToken' in data:
                next_page_token = data['nextPageToken']
            else:
                break
            # print(x)
        else:
            print('Error:', response.status_code)
        # print(comments)
        return comments

def get_prompt(comments):
   prompt = f"""You are a YouTube comments summarizer. Your task is to generate concise and informative summaries based on the comments of a YouTube video.
    Given the following set of comments, your goal is to condense the information and sentiments expressed by users, providing a clear and coherent summary.
    Avoid creating new content, only use the data given in the comments as a reference.
    Focus on capturing the key points, opinions, and discussions present in the comments section.
    Reuse the words and phrases mentioned in the comments.
    Never and Do not include the statements like :
    "x comments were analyzed, and their content was used to create the following summary",
    "Based on the context",
    "Please provide a concise and informative summary of the comments you have analyzed.",  in the summary. 

    Comments:
    {comments}

    Summary:
    """
   return prompt
from summarizer import get_llm
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_am_answer(product_link):
    comments = get_comments(product_link)
    prompt = get_prompt(comments) # TO DO
    llm =  get_llm()
    result = llm.invoke(prompt)
    print(result)
    return result

def get_comments(url):
    url = 'https://www.amazon.in/BENGOO-G9000-Controller-Cancelling-Headphones/product-reviews/B01H6GUCCQ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        return "Failed to retrieve the page. Status code:", response
    
    cmnts = ""
    soup = BeautifulSoup(html_content, 'html.parser')

# Find the review elements (this may vary based on Amazon's HTML structure)
    reviews = soup.find_all('div', class_='a-section review aok-relative')

    # Iterate through the reviews and extract relevant information
    for review in reviews:
        # Extract review text
        cmnts = cmnts+review.find('span', class_='a-size-base review-text review-text-content').get_text()

    return cmnts


def get_prompt(comments):
   prompt = f"""You are a online products review summarizer. Your task is to generate concise and informative summaries based on the reviews of a online product.
    Given the following set of reviews, your goal is to condense the information and sentiments expressed by users, providing a clear and coherent summary.
    Avoid creating new content, only use the data given in the comments as a reference.
    Focus on capturing the key points, opinions, and discussions present in the comments section.
    Reuse the words and phrases mentioned in the comments.
    Never include the statements like "x comments were analyzed, and their content was used to create the following summary", or "Based on the context" in the summary, just provide the summary.

    Comments:
    {comments}

    Summary:
    """
   return prompt
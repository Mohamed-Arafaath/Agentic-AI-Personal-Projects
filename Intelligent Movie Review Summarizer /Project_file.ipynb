# Movie Review Summarizer 
import openai
import os
from openai import OpenAI

SERPAPI_KEY = "cf267c28f7b48fec4e4b809598199fae37c625e613103b596ceb6005fc4e0d40"
openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Solution 1: Using google-search-results package (most common)
def fetch_google_reviews_v1(movie_name, language="English", max_results=25):
    try:
        from serpapi import GoogleSearch
        
        search = GoogleSearch({
            "q": f"{movie_name} {language} movie reviews",
            "hl": "en",
            "num": max_results,
            "api_key": SERPAPI_KEY
        })
        
        results = search.get_dict()
        return process_search_results(results, max_results)
    
    except ImportError:
        print("❌ GoogleSearch import failed")
        return None
    except Exception as e:
        print(f"❌ SerpAPI v1 error: {e}")
        return None

# Common function to process search results
def process_search_results(results, max_results):
    reviews_text = ""
    review_count = 0
    
    # Check knowledge graph for reviews first
    if "knowledge_graph" in results and "reviews" in results["knowledge_graph"]:
        for review in results["knowledge_graph"]["reviews"]:
            if "snippet" in review and review_count < max_results:
                reviews_text += f"- {review['snippet']}\n"
                review_count += 1
    
    # Check organic results (limit to remaining slots)
    if "organic_results" in results and review_count < max_results:
        remaining_slots = max_results - review_count
        for item in results["organic_results"][:remaining_slots]:
            if "snippet" in item:
                reviews_text += f"- {item['snippet']}\n"
                review_count += 1
    
    return reviews_text or "No reviews found."

def user_prompt_for_reviews(movie_name, language, review_text):
    return f"""
You are analyzing Google user reviews for the movie '{movie_name}' in {language}.
Here are the reviews:
{review_text}

Summarize exactly in this format with these 5 titles mentioned below:
1. ✅ Positives (min 5 bullet points detailed)
2. ❌ Negatives (min 5 bullet points detailed)
3. Comparision with other movies / if its a remake / or if its a copy (min 5 bullet points detailed)
4. 💡 Takeaways (story, direction, visuals, etc.) (min 5 bullet points detailed)
5. Praising and complaints about the case (min 5 bullet points detailed)
4. ⭐ Average rating if mentioned 

Respond in **Markdown** format.
"""

# Updated main function with fallback
def summarize_movie_reviews(movie_name, language="English", max_results=25):
    reviews = fetch_google_reviews(movie_name, language, max_results)
    if not reviews.strip() or "failed" in reviews.lower():
        return "No reviews found."
    
    messages = [
        {"role": "system", "content": "You are a review summarizer. Respond in Markdown."},
        {"role": "user", "content": user_prompt_for_reviews(movie_name, language, reviews)}
    ]
    
    response = openai.chat.completions.create(
            model="deepseek-r1:1.5B",  
            messages=messages,
            max_tokens=1000, 
            temperature=0.7
        )
    return response.choices[0].message.content

result = summarize_movie_reviews("Kalki 2898 AD", "Telugu", max_results=25)
display(Markdown(result[pos + len(keyword):].strip()))

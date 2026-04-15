import requests


TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
HEADERS = {"User-Agent": "TrendPulse/1.0"}


CATEGORIES = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

def categorize(title):
    title_lower = title.lower()
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw.lower() in title_lower:
                return category
    return "uncategorized"

def main():
  
    ids = requests.get(TOP_STORIES_URL, headers=HEADERS).json()[:500]

    results = []
    for story_id in ids:
        story = requests.get(ITEM_URL.format(story_id), headers=HEADERS).json()
        if story and "title" in story:
            category = categorize(story["title"])
            results.append({
                "id": story_id,
                "title": story["title"],
                "category": category
            })

    for r in results[:10]: 
        print(r)

if __name__ == "__main__":
    main()
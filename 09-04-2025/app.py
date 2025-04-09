from flask import Flask, render_template
import requests  # Make sure to install this first with: pip install requests

app = Flask(__name__)

def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"Fetched quote: {data['content']} - {data['author']}")  # Debug logging
            return data
        print(f"API error: Status {response.status_code}")
        return None
    except Exception as e:
        print(f"API request failed: {str(e)}")
        return None

@app.route('/')
def home():
    quote = get_random_quote()
    if not quote:
        print("Using fallback quotes")
        fallback_quotes = [
            {"content": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela"},
            {"content": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
            {"content": "Your time is limited, don't waste it living someone else's life.", "author": "Steve Jobs"},
            {"content": "If life were predictable it would cease to be life, and be without flavor.", "author": "Eleanor Roosevelt"},
            {"content": "If you look at what you have in life, you'll always have more.", "author": "Oprah Winfrey"},
            {"content": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
            {"content": "Spread love everywhere you go.", "author": "Mother Teresa"},
            {"content": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
            {"content": "Tell me and I forget. Teach me and I remember. Involve me and I learn.", "author": "Benjamin Franklin"},
            {"content": "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.", "author": "Helen Keller"},
            {"content": "Whoever is happy will make others happy too.", "author": "Anne Frank"},
            {"content": "Do not go where the path may lead, go instead where there is no path and leave a trail.", "author": "Ralph Waldo Emerson"},
            {"content": "You will face many defeats in life, but never let yourself be defeated.", "author": "Maya Angelou"},
            {"content": "The purpose of our lives is to be happy.", "author": "Dalai Lama"},
            {"content": "Only a life lived for others is a life worthwhile.", "author": "Albert Einstein"},
            {"content": "You only live once, but if you do it right, once is enough.", "author": "Mae West"},
            {"content": "Never let the fear of striking out keep you from playing the game.", "author": "Babe Ruth"},
            {"content": "Life is either a daring adventure or nothing at all.", "author": "Helen Keller"},
            {"content": "Many of life's failures are people who did not realize how close they were to success when they gave up.", "author": "Thomas A. Edison"},
            {"content": "If you want to live a happy life, tie it to a goal, not to people or things.", "author": "Albert Einstein"}
        ]
        import random
        quote = random.choice(fallback_quotes)
    return render_template('index.html', 
                         content=quote['content'],
                         author=quote['author'])

if __name__ == '__main__':
    app.run(debug=True)

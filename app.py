from flask import Flask, render_template_string
import random
import secrets

app = Flask(__name__)

# Core data pools for the randomizer
FOOD_OPTIONS = [
    "Santa Fe Chicken Sandwich with extra fries",
    "Traditional Mandi meal served with fresh yogurt",
    "Spicy Box Master sandwich from the local spot",
    "A hot Latte and a pastry from the local coffee shop",
    "South Asian full meal served on a banana leaf"
]

TECH_QUOTES = [
    "Simplicity is the soul of efficiency. — Austin Freeman",
    "Before software can be reusable it first has to be usable. — Ralph Johnson",
    "Make it work, make it right, make it fast. — Kent Beck",
    "Programs must be written for people to read, and only incidentally for machines to execute. — Abelson & Sussman"
]

# HTML Base Template using basic layout structures
BASE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Python Randomizer Portal</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; background: #0f172a; color: #f8fafc; padding: 2rem; margin: 0; }
        .container { max-width: 600px; margin: 0 auto; }
        .card { background: #1e293b; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-bottom: 1.5rem; border: 1px solid #334155; }
        h1 { color: #38bdf8; font-size: 1.75rem; margin-top: 0; }
        .result-box { background: #0f172a; padding: 1rem; border-radius: 8px; border-left: 4px solid #38bdf8; margin: 1rem 0; font-size: 1.1rem; min-height: 1.5rem; }
        .btn { display: inline-block; background: #38bdf8; color: #0f172a; padding: 0.75rem 1.5rem; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 0.95rem; }
        .btn:hover { background: #7dd3fc; }
        .nav-links { margin-top: 2rem; border-top: 1px solid #334155; padding-top: 1rem; }
        .nav-links a { color: #94a3b8; text-decoration: none; margin-right: 1rem; font-size: 0.9rem; }
        .nav-links a:hover { color: #38bdf8; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h1>{{ title }}</h1>
            <p>Flask matched this URL route and executed the corresponding Python function dynamically.</p>
            <div class="result-box">
                {{ result }}
            </div>
            <a href="{{ current_route }}" class="btn">Run Again</a>
        </div>
        
        <div class="nav-links">
            <a href="/">Menu Generator</a>
            <a href="/quote">Tech Quotes</a>
            <a href="/token">Secure Crypt-Token</a>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    selected_food = random.choice(FOOD_OPTIONS)
    return render_template_string(
        BASE_HTML, 
        title="Random Menu Selection", 
        result=selected_food, 
        current_route="/"
    )

@app.route("/quote")
def quote():
    selected_quote = random.choice(TECH_QUOTES)
    return render_template_string(
        BASE_HTML, 
        title="Random Developer Wisdom", 
        result=selected_quote, 
        current_route="/quote"
    )

@app.route("/token")
def token():
    # Uses cryptographically secure random token generation
    secure_token = f"dev_token_{secrets.token_hex(16)}"
    return render_template_string(
        BASE_HTML, 
        title="Secure System Token", 
        result=secure_token, 
        current_route="/token"
    )

if __name__ == "__main__":
    # Runs the local development server on port 5000
    app.run(host="127.0.0.1", port=5000, debug=True)
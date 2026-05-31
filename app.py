from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { 
            font-family: -apple-system, BlinkMacSystemFont, sans-serif; 
            background-color: #121212; 
            color: #ffffff; 
            text-align: center; 
            padding-top: 15vh; 
        }
        .timer-box { 
            font-size: 2.5rem; 
            margin-top: 20px; 
            background: #1e1e1e; 
            padding: 30px; 
            border-radius: 15px; 
            display: inline-block; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.5); 
            border: 1px solid #333; 
        }
        .labels { 
            font-size: 0.8rem; 
            color: #888; 
            text-transform: uppercase; 
            margin-top: 10px; 
            letter-spacing: 2px; 
        }
        .highlight { color: #0A84FF; }
    </style>
</head>
<body>

    <h1>Countdown to <span class="highlight">October 31st</span></h1>
    <div class="timer-box">
        <div id="countdown">Calculating...</div>
        <div class="labels">Days | Hours | Minutes | Seconds</div>
    </div>

    <script>
        // Set the precise target date here
        var countDownDate = new Date("Oct 31, 2026 00:00:00").getTime();

        var x = setInterval(function() {
            var now = new Date().getTime();
            var distance = countDownDate - now;

            var days = Math.floor(distance / (1000 * 60 * 60 * 24));
            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Output the result to the HTML element
            document.getElementById("countdown").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

            // If the countdown is over, print a message
            if (distance < 0) {
                clearInterval(x);
                document.getElementById("countdown").innerHTML = "HAPPY BIRTHDAY!";
                document.getElementById("countdown").style.color = "#FF453A"; // Changes text to iOS Red
            }
        }, 1000);
    </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True)

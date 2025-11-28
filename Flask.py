from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1> I AM AT HOME PAGE</h1>
    <h2> I am running Flask</h2>
    <p>Go to <a href='/about'>About Page</a> to know about nature.</p>
    """

@app.route("/about")
def about():
    return """
    <html>
    <head>
        <title>About Nature</title>
        <style>
            body {
                background-color: #e0ffe0;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #228B22;
                color: white;
                text-align: center;
                padding: 20px;
            }
            h1 {
                text-align: center;
                color: #006400;
            }
            p {
                margin: 20px;
                font-size: 18px;
                line-height: 1.6;
                color: #333333;
                text-align: justify;
            }
            .image-container {
                text-align: center;
                margin: 20px;
            }
            img {
                width: 60%;
                border-radius: 10px;
                box-shadow: 0 0 10px gray;
            }
            footer {
                background-color: #228B22;
                color: white;
                text-align: center;
                padding: 10px;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
            a {
                color: white;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>About Nature</h1>
        </header>

        <div class="image-container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/62/Nature_-_Drenthe%2C_The_Netherlands_%2834825907811%29.jpg" alt="Nature Image">
        </div>

        <p>
            Nature is the heart of our planet. It includes forests, rivers, mountains, wildlife, and the air we breathe. 
            Every part of nature works together to maintain balance and sustain life on Earth. Protecting it is not just
            our duty but our survival.
        </p>
        <p>
            Trees give us oxygen, rivers quench our thirst, and forests provide home to millions of species.
            When we care for nature, we care for ourselves — because we are part of it.
        </p>

        <footer>
            <p>Back to <a href="/">Home</a> | Made with ❤️ using Flask</p>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)

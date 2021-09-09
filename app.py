from flask import Flask, render_template
from parse import getParsedDF
from dashboard.dashapp import init_dashboard

app = Flask(__name__)
app = init_dashboard(app)

@app.route("/")
def home():

    return render_template(
        "index.html",
        title="Stocks Chart",
        
    )

if __name__ == '__main__':
    app.run(debug=True)

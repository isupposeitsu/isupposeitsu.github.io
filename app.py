from flask import Flask, render_template

app = Flask(__name__)

# Mock data for paintings (replace it with your actual data)
paintings_data = [
    {"title": "Painting 1", "description": "Description for Painting 1"},
    {"title": "Painting 2", "description": "Description for Painting 2"},
    # Add more paintings data as needed
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/paintings')
def paintings():
    return render_template('paintings.html', paintings=paintings_data)

if __name__ == '__main__':
    app.run(debug=True)
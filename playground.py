from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
print(__name__)


@app.route('/play/<val>/<color>', methods=['GET'])
def generate_boxes(val, color):
  return render_template('playground.html', color=color, _iter = range(int(val)))




if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.

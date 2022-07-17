# bulid my flask app for electron configuration of the peridoic table elements
from flask import Flask, render_template, request
from mendeleev import element
app = Flask(__name__)

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        element_name = request.form['element_name']
        element_object = element(element_name)
        element_electrons = element_object.ec
        atomic_number= element_object.atomic_number
        return render_template('index.html', element_name=element_name, element_electrons=element_electrons, atomic_number=atomic_number)
    else:
        return render_template('index.html')

# run   the app
if __name__ == '__main__':
    app.run(debug=True)

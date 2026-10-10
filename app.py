from flask import Flask, render_template, request, redirect

app = Flask(__name__)

employees = []

@app.route('/')
def home():
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']

        employees.append({
            'name': name,
            'department': department
        })

        return redirect('/')

    return render_template('add.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/about')
def About():
    return render_template('aboutus.html')


@app.route('/contact', methods=['GET', 'POST'])
def Contact():
    if request.method == 'POST':
        name = request.form['name']
        # print("hello", name)
        email = request.form['email']
        gender = request.form['gender']
        password = request.form['password']
        pa = ''
        for i in range(len(password)):
            pa = pa + '*'
        # print( email ,gender, password)
        return f"Ok your contacts details have been saved checkk the details below\nname:{name}, email:{email}, gender:{gender}, password:{pa}"
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)
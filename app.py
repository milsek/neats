from flask import Flask, render_template, request, jsonify
import niit.NeatEncoder as encoder
import niit.Neat as niit
app = Flask(__name__)
neat = None

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/flappy-bird', methods = ['GET', 'POST'])
def flappy_bird():
    param  = request.args.get('param', None)

    if request.method == 'POST':
        print("I got this: ")
        print(request.form['data'])
        return "OK", 200
    if param == "1":
        neat = niit.Neat(5, 2, 50)
        for unit in neat.get_units():
            unit.get_genome().mutate_connection()
            unit.get_genome().mutate_connection()
            unit.get_genome().mutate()
            unit.get_genome().mutate()
        data = encoder.encode(neat.units)
        return data
    return render_template("flappy-bird.html")

@app.route('/running-dinosaur')
def running_dinosaur():
    return render_template("flappy-bird.html")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)
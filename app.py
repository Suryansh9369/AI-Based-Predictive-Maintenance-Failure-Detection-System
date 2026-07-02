from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get values from the form
    air_temp = float(request.form["air_temperature"])
    process_temp = float(request.form["process_temperature"])
    rotational_speed = float(request.form["rotational_speed"])
    torque = float(request.form["torque"])
    tool_wear = float(request.form["tool_wear"])

    # Temporary prediction
    prediction = "Machine is Healthy"

    return render_template("home.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, redirect, url_for, request
from flask import render_template
from adt import Region, RegionPower
from main import main_f

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def menu():
    if request.method == "GET":
        return render_template("menu.html")

    if request.method == "POST":

        k = 0
        size = float(request.form['size'])

        region1 = request.form['city']

        try:
            month = int(request.form["month"])
        except ValueError:
            month = request.form["month"]
        k += float(request.form["k"])

    try:
        request.form["get_result"]
        reg = Region(region1)
        regPow = RegionPower(k, size)
        regPow.set_region(reg)
        regPow.get_html(month)
        return redirect(url_for('result'))
    except KeyError:
        pass

    try:
        request.form["get_map"]
        main_f(size, k, month, region1)
        return redirect(url_for('map'))
    except KeyError:
        pass


@app.route("/map", methods=["GET"])
def map():
    """Renders the map."""
    return render_template("my_map.html")


@app.route("/result", methods=["GET"])
def result():
    """Renders the result."""
    return render_template("result.html")


if __name__ == '__main__':
    app.run()

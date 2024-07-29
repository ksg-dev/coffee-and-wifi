from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from form import CafeForm
import csv
from cafes import Cafe


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = []
        for value in form.data.values():
            new_row.append(value)
        new_row = new_row[:7]
        print(new_row)
        with open("cafe-data.csv", "a", newline="\n", encoding="utf8") as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []

        for row in csv_data:
            list_of_rows.append(row)
    headings = list_of_rows[0]
    cafe_objs = []
    for cafe in list_of_rows[1:]:
        cafe_obj = Cafe(name=cafe[0], location_link=cafe[1], open=cafe[2], close=cafe[3], coffee=cafe[4], wifi=cafe[5], power=cafe[6])
        cafe_objs.append(cafe_obj)
    return render_template('cafes.html', cafes=cafe_objs, heads=headings)


if __name__ == '__main__':
    app.run(debug=True)

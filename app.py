from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired



class AddressEntryForm(FlaskForm):
    name = StringField()

class AddressesForm(FlaskForm):
    """A form for one or more addresses"""
    addresses = FieldList(FormField(AddressEntryForm), min_entries=1)

app = Flask(__name__)
app.config['SECRET_KEY'] = "You"


@app.route('/')
@app.route('/index')
def index():
    user_addresses = [
        {"name": "First Address"},
        {"name": "Second Address"},
    ]
    form = AddressesForm(addresses=user_addresses)
    return render_template("edit.html", form=form)


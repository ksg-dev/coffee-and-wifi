from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SubmitField, RadioField, URLField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = URLField('Location Link', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Close Time', validators=[DataRequired()])
    coffee_rating = RadioField(label='Coffee Quality: Worst ✘ ----- ☕️☕️☕️☕️☕️ Best',
                               choices=["✘", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
                               validators=[DataRequired()]
                               )
    wifi_rating = RadioField(label='Wifi Strength: Worst ✘ ----- 💪💪💪💪💪 Best',
                             choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                             validators=[DataRequired()]
                             )
    power_rating = RadioField(label='Power Outlet Availability: Worst ✘ ----- 🔌🔌🔌🔌🔌 Best',
                              choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                              validators=[DataRequired()]
                              )
    submit = SubmitField('Submit')
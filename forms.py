from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    Gender = SelectField(
        label="Gender (Male=0, Female=1)",
        choices=[
            ('0', '0'),
            ('1', '1')
        ],
        validators=[DataRequired()]
    )
    Age = SelectField(
        label="Age (0=18-34, 1=35-50, 2=51-64, 3=65+)",
        choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')],
        validators=[DataRequired()]
    )
    History = SelectField(
        label="History (0=No, 1=Yes)",
        choices=[('0', '0'), ('1', '1')],
        validators=[DataRequired()]
    )
    Patient = StringField(
        label="Patient ID",
        validators=[DataRequired()]
    )
    TakeMedication = SelectField(
        label="Take Medication (0=No, 1=Yes)",
        choices=[('0', '0'), ('1', '1')],
        validators=[DataRequired()]
    )
    Severity = SelectField(
        label="Severity (0=Mild, 1=Moderate, 2=Severe)",
        choices=[('0', '0'), ('1', '1'), ('2', '2')],
        validators=[DataRequired()]
    )
    BreathShortness = SelectField(
        label="Breath Shortness (0=No, 1=Yes)",
        choices=[('0', '0'), ('1', '1')],
        validators=[DataRequired()]
    )
    VisualChanges = SelectField(
        label="Visual Changes (0=No, 1=Yes)",
        choices=[('0', '0'), ('1', '1')],
        validators=[DataRequired()]
    )
    NoseBleeding = SelectField(
        label="Nose Bleeding (0=No, 1=Yes)",
        choices=[('0', '0'), ('1', '1')],
        validators=[DataRequired()]
    )
    Whendiagnoused = SelectField(
        label="When Diagnosed (0=<1 Year, 1=1-5 Years, 2=>5 Years)",
        choices=[('0', '0'), ('1', '1'), ('2', '2')],
        validators=[DataRequired()]
    )
    Systolic = SelectField(
        label="Systolic (0=100+, 1=111-120, 2=121-130, 3=130+)",
        choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')],
        validators=[DataRequired()]
    )
    Diastolic = SelectField(
        label="Diastolic (0=70-80, 1=81-90, 2=91-100, 3=100+, 4=130+)",
        choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
        validators=[DataRequired()]
    )
    ControlledDiet = SelectField(
        label="Controlled Diet (0=No, 1=Yes)",
        choices=[('0', '0'), ('1', '1')],
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")

from flask_wtf import FlaskForm
from matplotlib.pyplot import title
from wtforms import BooleanField, RadioField, IntegerField, SubmitField,FloatField
from wtforms.validators import InputRequired
from wtforms.widgets import html5


class FieldsRequiredForm(FlaskForm):
    """Require all fields to have content. This works around the bug that WTForms radio
    fields don't honor the `DataRequired` or `InputRequired` validators.
    """
    class Meta:
        def render_field(self, field, render_kw):
            if field.type == "_Option":
                render_kw.setdefault("required", True)
            return super().render_field(field, render_kw)


class DiagnoseForm(FieldsRequiredForm):
    age = IntegerField('Age',
                       widget=html5.NumberInput(min=1, max=140),
                       validators=[InputRequired()])
    sex = RadioField('Label',
                        choices=[(1, 'Male'),
                                 (0, 'Female')],
                        validators=[InputRequired()])
    
    fbs = BooleanField('fbs')
    restecg = BooleanField('restecg')
    exang = BooleanField('exang')
    cp = IntegerField('cp',
                       widget=html5.NumberInput(min=0, max=3),
                       validators=[InputRequired()])
    trestbps = IntegerField('trestbps',
                       widget=html5.NumberInput(min=0, max=200),
                       validators=[InputRequired()])
    chol = IntegerField('chol',
                        widget=html5.NumberInput(min=0, max=600),
                       validators=[InputRequired()])
    thalach = IntegerField('thalach',
                        widget=html5.NumberInput(min=0, max=250),
                       validators=[InputRequired()])
    oldpeak = FloatField('oldpeak',
                           widget=html5.NumberInput(min=0, max=7.0),
                       validators=[InputRequired()])
    slope= IntegerField('slope',
                          widget=html5.NumberInput(min=0, max=2),
                       validators=[InputRequired()])
                                                
    ca = IntegerField('ca',
                      widget=html5.NumberInput(min=0, max=4),
                       validators=[InputRequired()])
    thal = IntegerField('thal',
                        widget=html5.NumberInput(min=0, max=3),
                       validators=[InputRequired()]) 
    submit = SubmitField('Get result')

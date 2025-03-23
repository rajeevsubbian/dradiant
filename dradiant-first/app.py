from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'radiansecretkey'  # Change this for security
Bootstrap(app)

# Contact Form
class ContactForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Your Email", validators=[DataRequired(), Email()])
    subject = SelectField("Subject", choices=[
        ('admission', 'Admission Inquiry'),
        ('tour', 'Schedule a Tour'),
        ('curriculum', 'Curriculum Questions'),
        ('other', 'Other')
    ])
    message = TextAreaField("Your Message", validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField("Send Message")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Simulate sending an email (print to console instead)
        print(f"Name: {form.name.data}")
        print(f"Email: {form.email.data}")
        print(f"Subject: {form.subject.data}")
        print(f"Message: {form.message.data}")

        flash("Your message has been sent! Our team will get back to you soon.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", form=form)

@app.route("/programs")
def programs():
    return render_template("programs.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, flash, url_for
from dw.forms import ContactForm, LoginForm, RegistrationForm, PublicForm
from dw.models import Contact, User, Pforms
from dw import app, db

@app.route("/")

@app.route("/home")
def home():
  return render_template('home.html',title='Home')

@app.route("/about")
def about():
  return render_template('about.html', title='About Me')

@app.route('/work')
def work():
    return render_template('work.html', title='work')

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit() and request.method == 'POST':
        contact = Contact(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(contact)
        db.session.commit()
        flash("thank you for reaching out, your message has been deilvered")
        return redirect('/contact')
    elif request.method == 'POST':
        flash("please enter a valid email id Thank you")
        return redirect ('/contact')
    return render_template('contact.html', form=form)

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm(request.form)
  if form.validate_on_submit() and request.method == 'POST':
    user = User(username=form.username.data, password=form.password.data, email=form.email.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful!')
    return redirect(url_for('registered'))

  return render_template('register.html',title='Register',form=form)

@app.route("/registered", methods=['GET'])
def registered():
  return render_template('registered.html', title='Thanks!')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        flash('You\'ve successfully logged in')
        return redirect(url_for('publicforms'))
    return render_template('login.html', form=form)

@app.route("/publicforms", methods=['GET','POST'])
def publicforms():
    form = PublicForm()
    if form.validate_on_submit():
        pforms = Pforms(username=current_user.username, message=form.message.data)
        db.session.add(pforms)
        db.session.commit()
        flash("Your post has been added.")
    messages = Pforms.query.all()
    return render_template('pforms.html', form=form, messages=messages)
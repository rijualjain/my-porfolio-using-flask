from flask import Flask, render_template, request, redirect, flash, url_for 
from dw.forms import ContactForm  
from dw.models import Contact
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



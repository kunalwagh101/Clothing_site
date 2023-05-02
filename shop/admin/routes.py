from flask import render_template,request,session,redirect,flash ,url_for
from shop import app, db ,bcrypt
from shop.admin.form import RegistrationForm ,Loginform
from shop.admin.models import User
import os

@app.route('/')
def admin():
    return render_template("admin/index.html" ,title= "admin page")





@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)

        user = User(username = form.username.data,
                     email = form.email.data,
                    password= hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome { user.username }  thank you for registering' ,"success")
        return redirect(url_for('admin'))
    return render_template('admin/register.html', form=form, title= "Registration form")


@app.route('/Login', methods=['GET','POST'])
def login():
    form = Loginform(request.form)
    if request.method == 'POST' and form.validate():
        user =User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] =  form.email.data
            flash(f'Welcome {user.username} you are now logged in ',"success")
            return redirect(request.args.get('next') or url_for('admin'))
        else :
            flash("wrong email or password","danger")

    return render_template("admin/login.html",form = form ,title = "Login form")
        



      

       
   
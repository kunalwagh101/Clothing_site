from shop.products.models import Brand, Category 
from flask import Flask ,render_template, redirect , request ,flash
from shop import app ,db
from shop.products.forms import AddproductForm





@app.route("/addbrand", methods =['GET','POST'])
def addbrand() :
    if request.method == "POST" :
        brand_name = request.form.get("brand")
        print("brand_name = " ,brand_name)
        brand = Brand( name = brand_name)
        db.session.add(brand)
        flash( f'Brand {brand_name}  added succesfully !','success')
        db.session.commit()
        return redirect('addbrand')


    return render_template("products/addbrand.html",brands ='brands')
    




@app.route("/addcat", methods =['GET','POST'])
def addcat() :
    if request.method == "POST" :
        cat_name = request.form.get("category")
        print("brand_name = " ,cat_name)
        cat = Category( name = cat_name)
        db.session.add(cat)
        flash( f'Category {cat_name}  added succesfully !','success')
        db.session.commit()
        return redirect('addcat')


    return render_template("products/addbrand.html")
    

@app.route('/addproduct') 
def addproduct() :
    form = AddproductForm(request.form)
    return render_template("products/addproduct.html",form = form)


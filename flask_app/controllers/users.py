from flask_app import app
from flask import render_template,request, redirect
from flask_app.models.user import User

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html",users=users)
            


@app.route("/create")
def create():

    return render_template('create.html')

@app.route("/show/<int:id>")
def show(id):
# Create class method to bring back specfic user from database 
    data = {
        'id': id
    }
    user=User.get_1(data)
    return render_template('show.html', user=user)



# this route gets me to edit page and pass id 
@app.route('/edit/<int:id>')
def edit_update(id):

    data = {
        "id":id
    }
    # User.edit_update(data)
    # return redirect('/')
    user=User.get_1(data)
    return render_template('edit.html', user=user)


# updating user route
@app.route('/edit/<int:id>/update', methods=['POST'])
def get_update(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    user=User.update(data)
    # return render_template("index.html",user=user)
    return redirect('/')



@app.route('/create', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # above because of User class
    # Don't forget to redirect after saving to the database.
    return redirect('/')

# Delete a user 
@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        "id": id
    }
    user= User.delete_user(data)
    return redirect('/')
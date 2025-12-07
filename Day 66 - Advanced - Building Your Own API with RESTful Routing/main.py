from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///H:/100_Days_Of_Python_Coding_Angela_Yu/Day 66 - Advanced - Building Your Own API with RESTful Routing/instance/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} # type: ignore

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

## But GET is allowed by default on all routes.
# So this is much simpler:

@app.route("/random")
def get_random_cafe():
     result = db.session.execute(db.select(Cafe))
     all_cafes = result.scalars().all()
     random_cafe = random.choice(all_cafes)
     return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify (cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    # Note, this may get more than one cafe per location
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"), # type: ignore
            map_url=request.form.get("map_url"), # type: ignore
            img_url=request.form.get("img_url"), # type: ignore
            location=request.form.get("loc"), # type: ignore
            has_sockets=bool(request.form.get("sockets")), # type: ignore
            has_toilet=bool(request.form.get("toilet")), # type: ignore
            has_wifi=bool(request.form.get("wifi")), # type: ignore
            can_take_calls=bool(request.form.get("calls")), # type: ignore
            seats=request.form.get("seats"), # type: ignore
            coffee_price=request.form.get("coffee_price"), # type: ignore
        )

        # Add new cafe to the db
        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response={"success": "Successfully added the new cafe."}), 201

    except Exception as e:
        # Rollback the session in case of error
        db.session.rollback()
        return jsonify(response={"error": f"An error occurred: {str(e)}"}), 500
    
# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.session.get(entity=Cafe, ident=cafe_id)  # Returns None if cafe_id is not found
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200



# HTTP DELETE - Delete Record
# Deletes a cafe with a particular id. Change the request type to "Delete" in Postman
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        try:
            cafe = db.session.get(entity=Cafe, ident=cafe_id)  # Returns None if cafe_id is not found
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)



"""
     Turn our random_cafe SQLAlchemy Object into a JSON. This process is called serialization.
     Flask has a serialisation helper method built-in called jsonify() . 
     But we have to provide the structure of the JSON to return.

     But in most cases, you might just want to return all the data you have on a particular record and
     it would drive you crazy if you had to write out all that code for every route.

    So another method of serialising our database row Object to JSON is by first converting it
      to a dictionary and then using jsonify() to convert the dictionary 
      (which is very similar in structure to JSON) to a JSON.

      # CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    return jsonify(cafe=random_cafe.to_dict())


or 

     return jsonify(cafe={
        #Omit the id from the response
        # "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        
        #Put some properties in a sub-category
        "amenities": {
          "seats": random_cafe.seats,
          "has_toilet": random_cafe.has_toilet,
          "has_wifi": random_cafe.has_wifi,
          "has_sockets": random_cafe.has_sockets,
          "can_take_calls": random_cafe.can_take_calls,
          "coffee_price": random_cafe.coffee_price,
        }
    })

    

Full PUT Update Endpoint

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(app)

# Example Cafe model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/update-cafe/<int:cafe_id>", methods=["PUT"])
def update_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": "Sorry, a cafe with that ID was not found."}), 404

    data = request.get_json()

    # Required fields for full update
    required_fields = [
        "name", "map_url", "img_url", "location", "seats",
        "has_toilet", "has_wifi", "has_sockets", "can_take_calls", "coffee_price"
    ]

    # Check if all fields are provided
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify(error={"Missing Fields": f"You must provide all fields: {', '.join(missing_fields)}"}), 400

    # Update all fields
    try:
        cafe.name = data["name"]
        cafe.map_url = data["map_url"]
        cafe.img_url = data["img_url"]
        cafe.location = data["location"]
        cafe.seats = data["seats"]
        cafe.has_toilet = data["has_toilet"]
        cafe.has_wifi = data["has_wifi"]
        cafe.has_sockets = data["has_sockets"]
        cafe.can_take_calls = data["can_take_calls"]
        cafe.coffee_price = data["coffee_price"]

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify(error={"Database Error": str(e)}), 500

    return jsonify(success="Cafe updated successfully", updated_cafe={
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price
    }), 200

🧾 Example PUT Request (JSON Body)

URL:

http://127.0.0.1:5000/update-cafe/3


Body:

{
  "name": "Cafe Horizon",
  "map_url": "https://goo.gl/maps/horizon",
  "img_url": "https://images.com/horizon.jpg",
  "location": "Downtown District",
  "seats": "40",
  "has_toilet": true,
  "has_wifi": true,
  "has_sockets": false,
  "can_take_calls": true,
  "coffee_price": "$4.00"
}

🧠 Key Differences from PATCH version
Feature	PATCH version	PUT version
Partial updates	✅ Allowed	❌ Not allowed
Requires all fields	❌	✅ Yes
Missing fields cause error	❌	✅ 400 Bad Request
Behavior	Update only provided fields	Overwrite entire record

Would you like me to also show a variant that accepts form-data (not JSON) — e.g., for updates via an

     """
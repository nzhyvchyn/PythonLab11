from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from Main import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://iotuser:iotuser@localhost:3306/iot-test-db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class WaterSport(db.Model):
    __tablename__ = 'WaterSport'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=80))
    amount_of_members = db.Column(db.Integer)
    need_of_sport_equipment = db.Column(db.String(length=80))
    purpose_of_sport = db.Column(db.String(length=80))

    def __init__(self,
                 name, amount_of_members,
                 need_of_sport_equipment,
                 purpose_of_sport):
        self.name = name;
        self.amount_of_members = amount_of_members;
        self.need_of_sport_equipment = need_of_sport_equipment;
        self.purpose_of_sport = purpose_of_sport;

    def __str__(self):
        return "{" + "name='" + str(self.name) + '\'' \
               + ", amount_of_members='" + str(self.amount_of_members) + '\'' \
               + ", need_of_sport_equipment=" + str(self.need_of_sport_equipment) \
               + ", purpose_of_sport=" + str(self.purpose_of_sport) \
                + "}"

class WaterSportSchema(ma.Schema):
    class Meta:
        fields = ('name', 'amount_of_members', 'need_of_sport_equipment', 'purpose_of_sport')

water_sport_schema = WaterSportSchema()
water_sports_schema = WaterSportSchema(many=True)
db.create_all()

@app.route("/waterSports", methods=["POST"])
def add_water_sport():
    name = request.get_json()["name"]
    amount_of_members = request.get_json()["amount_of_members"]
    need_of_sport_equipment = request.get_json()["need_of_sport_equipment"]
    purpose_of_sport = request.get_json()["purpose_of_sport"]
    new_water_sport = WaterSport(name, amount_of_members,
                 need_of_sport_equipment,
                 purpose_of_sport)
    db.session.add(new_water_sport)
    db.session.commit()
    return jsonify(request.json)

@app.route("/waterSports", methods=["GET"])
def get_water_sports():
    all_water_sports = WaterSport.query.all()
    return_info = water_sports_schema.dump(all_water_sports)
    return jsonify(return_info.data)

@app.route("/waterSports/<id>", methods=["GET"])
def get_water_sports_by_id(id):
    water_sport = WaterSport.query.get(id)
    return water_sports_schema.jsonify(water_sport)

@app.route("/waterSports/<id>", methods=["PUT"])
def replace_water_sport(id):
    water_sport = WaterSport.query.get(id)
    water_sport.name = request.json["name"]
    water_sport.amount_of_members = request.json["amount_of_members"]
    water_sport.need_of_sport_equipment = request.json["need)of_sport_equipmnet"]
    water_sport.purpose_of_sport = request.json["purpose_of_sport"]
    db.session.commit()
    return water_sport_schema.jsonify(water_sport)


@app.route("/waterSports/<id>", methods=["DELETE"])
def delete_water_sport(id):
    water_sport = WaterSport.query.get(id)
    db.session.delete(water_sport)
    db.session.commit()
    return water_sport_schema.jsonify(water_sport)

if __name__ == '__main__':
    app.run()

from models.WaterSports import WaterSports


class Windsurfing(WaterSports):

        def __init__(self, name, amount_of_members,
               need_of_sport_equipment, is_olympic_sport,
               purpose_of_sport, rating, sail_square, speed_of_sportsman):
            super(Windsurfing, self).__init__(name, amount_of_members,
               need_of_sport_equipment, is_olympic_sport,
               purpose_of_sport, rating)
            self.sail_square = sail_square
            self.speed_of_sportsman = speed_of_sportsman


        def __str__(self):
            return "Windsurfing" + super(WaterSports, self).__str__() \
           + ", sail square=" + str(self.sail_square) +\
           ", speed of sportsman=" + str(self.speed_of_sportsman) + "}"

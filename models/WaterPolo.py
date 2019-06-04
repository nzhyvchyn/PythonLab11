from models.WaterSports import WaterSports


class WaterPolo(WaterSports):

        def __init__(self, name, amount_of_members,
               need_of_sport_equipment, is_olympic_sport,
               purpose_of_sport, rating, target_number, team_members):
            super(WaterPolo, self).__init__(name, amount_of_members,
               need_of_sport_equipment, is_olympic_sport,
               purpose_of_sport, rating)
            self.target_number = target_number
            self.team_members = team_members

        def __str__(self):
            return "WaterPolo" + super(WaterSports, self).__str__() \
                       + ", target numbers=" + str(self.target_number) + \
                       ", team members=" + str(self.team_members) + "}"


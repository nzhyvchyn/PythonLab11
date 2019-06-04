from models.WaterSports import WaterSports


class Aquajogging(WaterSports):

        def __init__(self, name, amount_of_members,
               need_of_sport_equipment, is_olympic_sport,
               purpose_of_sport, rating, is_streams_on_tv):
            super(Aquajogging, self).__init__(name, amount_of_members,
               need_of_sport_equipment, is_olympic_sport,
               purpose_of_sport, rating)
            self.is_streams_on_tv = is_streams_on_tv

        def __str__(self):
            return "Aquajogging" + super(WaterSports, self).__str__() \
                       + ", is streams on TV=" + str(self.is_streams_on_tv) + \
                       + "}"

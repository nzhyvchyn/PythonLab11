from models.WaterSports import WaterSports


class Swimming(WaterSports):

        def __init__(self, name, amount_of_members,
               need_of_sport_equipment, is_olympic_sport,
               purpose_of_sport, rating, pool_length):
            super(Swimming, self).__init__(name, amount_of_members,
               need_of_sport_equipment, is_olympic_sport,
               purpose_of_sport, rating)
            self.pool_length = pool_length

        def __str__(self):
            return "Swimming" + super(WaterSports, self).__str__() \
                       + ", pool length=" + str(self.pool_length) + \
                       + "}"

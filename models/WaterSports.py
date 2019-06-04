from models.Rating import Rating


class WaterSports:

    def __init__(self,
                 name, amount_of_members,
                 need_of_sport_equipment, is_olympic_sport,
                 purpose_of_sport, rating):
        self.name = name;
        self.amount_of_members = amount_of_members;
        self.need_of_sport_equipment = need_of_sport_equipment;
        self.is_olympic_sport = is_olympic_sport;
        self.purpose_of_sport = purpose_of_sport;
        self.rating = rating;

        def __str__(self):
            return ', '.join()
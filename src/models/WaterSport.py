

class WaterSport:

    def __init__(self, name="", purpose_of_sport="", is_olympic_sport=False,
                 sport_price=None, amount_of_members=0):
        self.name = name
        self.purpose_of_sport = purpose_of_sport
        self.is_olympic_sport = is_olympic_sport
        self.sport_price = sport_price
        self.amount_of_members = amount_of_members

    def __str__(self):
        return "{" + "name='" + self.name + '\'' \
               + ", purpose_of_sport='" + str(self.purpose_of_sport) + '\'' \
               + ", is olympic sport=" + str(self.is_olympic_sport) \
               + ", sport_price=" + str(self.sport_price) \
               + ", members_number=" + str(self.amount_of_members) \

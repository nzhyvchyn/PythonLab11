from src.models.WaterSport import WaterSport


class Windsurfing(WaterSport):

    def __init__(self,  name="", purpose_of_sport="", is_olympic_sport=False,
                 sport_price=None, amount_of_members=0, field_width=0, field_length=0):
        super().__init__(name, purpose_of_sport, is_olympic_sport,
                 sport_price, amount_of_members)
        self.field_width = field_width
        self.field_length = field_length

    def __str__(self):
        return "Windsurfing" + super().__str__() \
               + ", field_width=" + str(self.field_width) \
               + ", field_length=" + str(self.field_length) + "}"

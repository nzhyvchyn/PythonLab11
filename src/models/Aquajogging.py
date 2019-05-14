from src.models.WaterSport import WaterSport


class Aquajogging(WaterSport):

    def __init__(self, name="", purpose_of_sport="", is_olympic_sport=False,
                 sport_price=None, amount_of_members=0, tables_number=0):
        super().__init__(name, purpose_of_sport, is_olympic_sport,
                 sport_price, amount_of_members)
        self.tables_number = tables_number

    def __str__(self):
        return "Aquajogging" + super().__str__() \
               + ", tables_number=" + str(self.tables_number) + "}"

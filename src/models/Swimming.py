from src.models.WaterSport import WaterSport


class Swimming(WaterSport):

    def __init__(self,  name="", purpose_of_sport="", is_olympic_sport=False,
                 sport_price=None, amount_of_members=0, pools_number=0, average_pool_volume=0):
        super().__init__(name, purpose_of_sport, is_olympic_sport,
                 sport_price, amount_of_members)
        self.pools_number = pools_number
        self.average_pool_volume = average_pool_volume

    def __str__(self):
        return "Swimming" + super().__str__() \
               + ", pools_number=" + str(self.pools_number) \
               + ", average_pool_volume=" + str(self.average_pool_volume) + "}"

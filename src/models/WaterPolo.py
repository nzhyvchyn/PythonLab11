from src.models.WaterSport import WaterSport


class WaterPolo(WaterSport):

    def __init__(self,  name="", purpose_of_sport="", is_olympic_sport=False,
                 sport_price=None, amount_of_members=0, average_track_distance=0, tracks_number=0):
        super().__init__(name, purpose_of_sport, is_olympic_sport,
                 sport_price, amount_of_members)
        self.average_track_distance = average_track_distance
        self.tracks_number = tracks_number

    def __str__(self):
        return "WaterPolo" + super().__str__() \
               + ", average_track_distance=" + str(self.average_track_distance) \
               + ", tracks_number=" + str(self.tracks_number) + "}"

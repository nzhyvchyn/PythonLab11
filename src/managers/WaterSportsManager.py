class WaterSportsManager:

    def __init__(self, water_sports):
        self.water_sports = list(water_sports)

    def find_by_members_number(self, max):
        return [waterSport for waterSport in self.water_sports
                if (waterSport.amount_of_members <= max)]

    def sort_by_sport_name(self, water_sports, reverse):
        water_sports.sort(key=lambda waterSport: waterSport.name, reverse=reverse)

    def sort_by_sport_price(self, water_sports, reverse):
        water_sports.sort(key=lambda waterSport: waterSport.sport_price, reverse=reverse)

    def print_sport_buildings_info(self, water_sports):
        for waterSports in water_sports:
            print(waterSports)

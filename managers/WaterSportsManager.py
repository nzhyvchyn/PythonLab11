class WaterSportsManager:

    def __init__(self, water_sports):
        self.water_sports = list(water_sports)

    def find_by_members_number(self, min, max):
        return [sport for sport in self.sport_buildings
                if (min <= sport.amount_of_members <= max)]

    def sort_by_sport_kind(self, water_sports):
        water_sports.sort(key = lambda sport: sport.purpose_of_sport.value)

    def sort_by_sport_name(self, water_sports):
        water_sports.sort(key = lambda sport: sport.name.value)

    def print_water_sports_info(self, water_sports):
        for sport in water_sports:
            print(sport)

    # def __init__(self, water_sports):
    #     self.water_sports = list(water_sports)
    #
    # def find_by_members_number(self, min, max):
    #     return [sports for sports in self.water_sports
    #             if (min <= water_sports.amount_of_members <= max)]
    #
    # def sort_by_sport_purpose (self, water_sports):
    #     water_sports.sort(lambda sports: sports.name.value)
    #
    # def sort_by_sport_name(self, water_sports, reverse=false):
    #     water_sports.sort(lambda sports: sports.name.value, reverse=reverse)
    #
    # def print_water_sports_info(self, water_sports):
    #     for sports in water_sports:
    #         print(sports)



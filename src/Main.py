from src.managers.WaterSportsManager import WaterSportsManager
from src.models.Swimming import Swimming
from src.models.WaterPolo import WaterPolo
from src.models.Aquajogging import Aquajogging
from src.models.Windsurfing import Windsurfing
from src.models.PurposeOfSport import PurposeOfSport


def main():

    manager = WaterSportsManager(create_water_sports_list())
    selected_sports = manager.find_by_members_number(5)
    manager.sort_by_sport_name(selected_sports, False)
    # manager.sort_by_sport_price(selected_sports, False)
    manager.print_sport_buildings_info(selected_sports)


def create_water_sports_list():
    water_sports = list()

    water_sports.append(Swimming("Swimming", PurposeOfSport.WELLNESS, False, 100,
                                        6, 8, 20))
    water_sports.append(WaterPolo("Water polo", PurposeOfSport.COMPETITION, True,
                                               50, 3, 3000, 10))
    water_sports.append(Aquajogging("Aquajogging", PurposeOfSport.REHABILITATION, True, 200,
                                    4, 10))
    water_sports.append(Windsurfing("Windsurfing", PurposeOfSport.COMPETITION, False, 300,
                                         1, 30, 70))

    return water_sports


main()

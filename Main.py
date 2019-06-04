from managers.WaterSportsManager import WaterSportsManager
from models.Aquajogging import Aquajogging
from models.Rating import Rating
from models.Swimming import Swimming
from models.WaterPolo import WaterPolo
from models.WaterSports import WaterSports
from models.Windsurfing import Windsurfing


def main():
    print("\tWater Sports\n")

    manager = WaterSportsManager(create_water_sports_list())
    selected_sports = manager.find_by_members_number(0, 5)
    manager.sort_by_sport_name(selected_sports)
    manager.print_water_sports_info(selected_sports)


def create_water_sports_list():
    sport_buildings = list()

    sport_buildings.append(Swimming("Swimming", 3, false,
             false, "Wellness", Rating.HIGH, 50))
    sport_buildings.append(WaterPolo("Water polo", 6,
              true, true, "Recreational", Rating.HIGH, 10, 20))
    sport_buildings.append(Aquajogging("Aquajogging", 4, false, true,
                "Recreational", true, Rating.HIGH))
    sport_buildings.append(Windsurfing("Windsurfing", 1, false, true,
                "Competition", Rating.HIGH))


    return sport_buildings


# Execution point
if __name__ == '__main__':
    main()






# from managers.WaterSportsManager import WaterSportsManager;
# 
# def main():
# 
#     manager = WaterSportsManager(create_watersports_info())
#     water_sports = manager.find_by_members_number(0, 5)
#     manager.sort_by_sport_purpose(water_sports)
#     manager.sort_by_sport_name(true, water_sports)
#     manager.print_water_sports_info(water_sports)
# 
# 
# def create_watersports_info():
#     water_sports = list()
# 
#     water_sports.append(Swimming("Swimming", 3, false,
#                 false, "Wellness", 50, Rating.AVERAGE))
#     water_sports.append(WaterPolo("Water polo", 6,
#                 true, true, 2,7, "Wellness", Rating.HIGH))
#     water_sports.append(Aquajogging("Aquajogging", 4, false, true,
#                 "Recreational", true, Rating.HIGH))
#     water_sports.append(Windsurfing("Windsurfing", 1, false, true,
#                 "Competition", 20, 40, Rating.LOW))
# 
#     return water_sports
# 
# if __name__ == '__main__':
#     main()
import json

import folium

from adt import Region, RegionPower


def main_f(size, k, month, region):
    """Main function to draw a map."""
    my_map = folium.Map(zoom_start=6.3, location=[49.038358, 31.451240])

    cities = ['Chernihiv', 'Chernivtsi', 'Crimea', 'Dnipropetrovsk', 'Donetsk',
              'Ivano-Frankivsk', 'Kharkiv', 'Kherson', 'Khmelnytskyy', 'Kiev', 'Kirovohrad',
              'Luhansk', 'Lviv', 'Mykolayiv', 'Odessa', 'Poltava', 'Rivne', 'Sumy', 'Ternopil',
              'Vinnytsya', 'Volyn', 'Zakarpattia', 'Zaporizhzhya', 'Zhytomyr', 'Cherkasy']
    ukr_cities = ["Чернігів", "Чернівці", "Сімферополь", "Дніпро", "Донецьк", "Івано-Франківськ",
                  "Харків", "Херсон", "Хмельницький", "Київ", "Кропивницький", "Луганськ", "Львів",
                  "Миколаїв", "Одеса", "Полтава", "Рівне", "Суми", "Тернопіль",
                  "Вінниця", "Луцьк", "Ужгород", "Запоріжжя", "Житомир", "Черкаси"]
    print(len(ukr_cities) == len(cities))
    ix = 0
    fg1 = folium.FeatureGroup(name="regions")
    for city in range(len(cities)):

        reg = Region(ukr_cities[city])
        regPow = RegionPower(k, size)
        regPow.set_region(reg)
        path = f"your_path/{cities[city]}.json"
        geojson = folium.GeoJson(json.load(open(path, encoding='UTF-8')))
        popup = folium.Popup(f"{regPow.get_power(month)} кВт*год/день")
        popup.add_to(geojson)
        geojson.add_to(my_map)

        ix += 1

    my_map.save('your_path/templates/my_map.html')


if __name__ == "__main__":
    main_f(10000, 1, 1, "Тернопіль")

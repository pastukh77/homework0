from bs4 import BeautifulSoup
from urllib.request import urlopen


def url_to_soup():
    """Converts url to soup using module BeautifulSoup.
    Returns soup."""
    url = "https://www.artenergy.com.ua/novosti/karta-solnechnoi-insoliatsii-ukrainy"
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    return soup


def soup_to_dict():
    """Converts soup using url_to_soup() to dictionary with regions
    and monthly levels of solar insolation.
    Returns regions_dict."""
    soup = url_to_soup()
    content_lst = []

    for element in soup.find_all('td'):
        content_lst.append(f"{element.text}")

    content_lst = content_lst[14:]
    ukrainian_regions = ["Сімферополь", "Вінниця", "Луцьк", "Дніпро",
                         "Донецьк", "Житомир", "Ужгород", "Запоріжжя", "Івано-Франківськ",
                         "Київ", "Кропивницький", "Луганськ", "Львів", "Миколаїв", "Одеса",
                         "Полтава", "Рівне", "Суми", "Тернопіль", "Харків", "Херсон",
                         "Хмельницький", "Черкаси", "Чернігів", "Чернівці"]
    regions_dict = dict()

    for index in range(len(ukrainian_regions)):
        month_dict = dict()

        for ix in range(12):
            month_dict[ix + 1] = float((content_lst[index * 14 + ix + 1]).replace(",", "."))
            if ix == 11:
                month_dict["Річний"] = float(content_lst[index * 14 + 13].replace(",", "."))

        content_lst[index * 14] = ukrainian_regions[index]
        regions_dict[content_lst[index * 14]] = month_dict

    return regions_dict


def represent():
    """Represents the dictionary of regions got by soup_to_dict() method."""
    regions_dict = soup_to_dict()
    ukrainian_regions = ["Сімферополь", "Вінниця", "Луцьк", "Дніпро",
                         "Донецьк", "Житомир", "Ужгород", "Запоріжжя", "Івано-Франківськ",
                         "Київ", "Кропивницький", "Луганськ", "Львів", "Миколаїв", "Одеса",
                         "Полтава", "Рівне", "Суми", "Тернопіль", "Харків", "Херсон",
                         "Хмельницький", "Черкаси", "Чернігів", "Чернівці"]
    for region in ukrainian_regions:
        print(region, ": ", regions_dict[region], sep="")


if __name__ == "__main__":
    represent()

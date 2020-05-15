from soup import soup_to_dict
from wind import df_to_dict


class Region:
    """Represents a ukrainian region"""

    def __init__(self, region: str):
        """Constructor method, initializes attribute:
        region: name of ukrainian region."""
        self.region = region
        try:
            self.insolation = soup_to_dict()[region]
            self.wind = df_to_dict()[region]
        except KeyError:
            raise InvalidRegion("There is no such a region in Ukraine.")

    def get_insolation(self, month="Річний"):
        """Returns monthly insolation level.
        Returns the average annual value by default. """
        return self.insolation[month]

    def get_wind_speed(self, month="Річний"):
        """ Returns average monthly wind speed.
        Returns the average annual speed by default """
        return round(self.wind[month], 1)

    def __str__(self):
        """Constructor method, represents region as string."""
        return self.region


class RegionPower:
    """Represents solar power calculations of regions."""

    def __init__(self, coefficient, roof_size):
        """Constructor method, initializes attributes:
                region: ukrainian region, Region object;
                coefficient: coefficient of the angle of inclination of the roof to the horizon and the angle of
                rotation of the roof to the south (azimuth);
                roof_size: size of the roof."""
        self.region = None
        self.koefficient = coefficient
        self.roof_size = roof_size
        self.place = None

    def set_region(self, region: Region) -> None:
        """Sets the region value."""
        self.region = region

    def change_size(self, new_size: float) -> None:
        """Changes size of the roof."""
        self.roof_size = new_size

    def get_region(self) -> str:
        """Returns the name of region."""
        return self.region

    def get_power(self, month="Річний") -> float:
        """Calculates and returns solar powor of region. Annual value by default."""
        power = self.koefficient * self.roof_size * self.region.get_insolation(month)
        return round(power, 1)

    def top_power(self, month="Річний") -> str:
        """Creates top of regions of country by solar power. Returns string."""
        regions = list(soup_to_dict().keys())
        result = dict()
        for el in regions:
            new_region = RegionPower(self.koefficient, self.roof_size)
            new_region.set_region(Region(el))
            power = new_region.get_power(month)
            result[el] = power

        sorted_dict = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
        key_list = list(sorted_dict.keys())
        values_list = list(sorted_dict.values())
        size = len(key_list)

        self.place = size - key_list.index(str(self.region))
        top = ""
        for ix in range(size):
            top += f"{ix + 1}. {key_list[size - ix - 1]}:" \
                   f"{round(values_list[size - ix - 1], 1)}{' <- Ваш регіон ' if ix == self.place - 1 else ''}\n "
        return top

    def get_wind(self, month="Річний") -> float:
        """Returns the average speed of wind of the region"""
        return self.region.get_wind_speed(month)

    def grater_power(self, other_region, month="Річний") -> bool:
        """Returns True if region has grater solar power then other_region, else False."""
        return True if self.get_power(month) > other_region.get_power(month) else False

    def __str__(self):
        """Constructor method, represents RegionPower object as string."""
        return f"Ви обрали область, обласний центр якої: {str(self.region)}\nЗа обраний Вами період часу, дана " \
               f"система могла би отримати від сонячного випромінювання " \
               f"{str(self.get_power())} МВт*год\nТакож на ефективність системи впливатиме вітер, тому пропонуємо " \
               f"розглянути Вам середньомісячну(річну) швидкість вітру в обраному Вами регіоні: " \
               f"{str(self.get_wind())} м/c\nДля кращого розуміння перспектив Вашого регіону просимо проаналізувати, " \
               f"яка кількість сонячного випромінювання була би отримана за умов Вашого будинку в інших областях " \
               f"України (один. виміру: МВТ*год)\n{self.top_power()}"


class InvalidRegion(Exception):
    pass


if __name__ == "__main__":
    # example:
    r = RegionPower(0.7, 10)
    r.set_region(Region("Кропивницький"))
    print(r)

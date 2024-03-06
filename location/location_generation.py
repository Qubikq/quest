from random import randint


# Шаблоны локаций
class Forest:
    def __init__(self, environment="Зачарованный лес", indoor="False"):
        self.indoor = indoor
        self.environment = environment


class Desert:
    def __init__(self, environment="Запретная пустыня", indoor="False"):
        self.indoor = indoor
        self.environment = environment


class Atlantida:
    def __init__(self, environment="Затерянный город Атлантиды", indoor="False"):
        self.indoor = indoor
        self.environment = environment


class DarkCaves:
    def __init__(self, environment="Темные пещеры", indoor="True"):
        self.indoor = indoor
        self.environment = environment


class Ruines:
    def __init__(self, environment="Древние руины", indoor="False"):
        self.indoor = indoor
        self.environment = environment


class Mountains:
    def __init__(self, environment="Мистические горы", indoor="False"):
        self.indoor = indoor
        self.environment = environment


class Manor:
    def __init__(self, environment="Поместье с привидениями", indoor="True"):
        self.indoor = indoor
        self.environment = environment


class HiddenTemple:
    def __init__(self, environment="Скрытый храм", indoor="True"):
        self.indoor = indoor
        self.environment = environment


class FrozenWasteland:
    def __init__(self, environment="Замерзшая пустошь", indoor="False"):
        self.indoor = indoor
        self.environment = environment


class EmeraldIsles:
    def __init__(self, environment="Изумрудные острова", indoor="False"):
        self.indoor = indoor
        self.environment = environment


# Массив всех локаций
environment_pool = [Forest, Desert, Atlantida, DarkCaves, Ruines, Mountains, Manor, HiddenTemple,
                    FrozenWasteland, EmeraldIsles]


# Шаблоны погоды
class Sunny:
    def __init__(self, weather="Солнечно"):
        self.weather = weather


class Rainy:
    def __init__(self, weather="Идёт дождь"):
        self.weather = weather


class Stormy:
    def __init__(self, weather="Шторм"):
        self.weather = weather


class Foggy:
    def __init__(self, weather="Туман"):
        self.weather = weather


class Snowy:
    def __init__(self, weather="Идёт снег"):
        self.weather = weather


class Hailstorm:
    def __init__(self, weather="Идёт град"):
        self.weather = weather


class Blizzard:
    def __init__(self, weather="Вьюга"):
        self.weather = weather


class Windy:
    def __init__(self, weather="Ветренно"):
        self.weather = weather


class Misty:
    def __init__(self, weather="Неясно"):
        self.weather = weather


class Thunderstorm:
    def __init__(self, weather="Гроза"):
        self.weather = weather


# Массив вариантов погоды
weather_pool = [Sunny, Rainy, Stormy, Foggy, Snowy, Hailstorm, Blizzard, Windy, Misty, Thunderstorm]


# Шаблоны баффов
class Energetic:
    def __init__(self, baff='Энергичный'):
        self.baff = baff

    def baff_info(self):
        print('Увеличивает скорость передвижения персонажа')


class Protected:
    def __init__(self, baff='Защищенный'):
        self.baff = baff

    def baff_info(self):
        print('Увеличивает защиту персонажа, снижая получаемый урон.')


class Strong:
    def __init__(self, baff='Сильный'):
        self.baff = baff

    def baff_info(self):
        print('Увеличивает силу атаки персонажа')


class Agile:
    def __init__(self, baff='Ловкий'):
        self.baff = baff

    def baff_info(self):
        print('Увеличивает шанс уклонения от атак врагов')


class Focused:
    def __init__(self, baff='Сосредоточенный'):
        self.baff = baff

    def baff_info(self):
        print('Повышает точность атак персонажа.')


class Resilient:
    def __init__(self, baff='Живучий'):
        self.baff = baff

    def baff_info(self):
        print('Увеличивает количество здоровья или стойкость персонажа.')


class Calm:
    def __init__(self, baff='Успокоенный'):
        self.baff = baff

    def baff_info(self):
        print('Уменьшает время восстановления способностей персонажа')


class FleetFooted:
    def __init__(self, baff='Шустрые ноги'):
        self.baff = baff

    def baff_info(self):
        print('Позволяет персонажу дальше перемещаться в бою и лучше уворачиваться от атак.')


class Berserk:
    def __init__(self, baff='Берсерк'):
        self.baff = baff

    def baff_info(self):
        print('Увеличивает скорость атаки и урон персонажа, но снижает защиту.')


class Inspired:
    def __init__(self, baff='Вдохновленный'):
        self.baff = baff

    def baff_info(self):
        print('Увеличивает все характеристики персонажа на некоторое время.')


# Массив баффов
baff_pool = [Energetic, Protected, Strong, Agile, Focused, Resilient, Calm, FleetFooted, Berserk, Inspired]


# Шаблоны дебаффов
class DenseFog:
    def __init__(self, debaff='Густой туман'):
        self.debaff = debaff

    def debaff_info(self):
        print('Снижает видимость, усложняя ориентацию и сражение.')


class ShakingGround:
    def __init__(self, debaff='Тряска'):
        self.debaff = debaff

    def debaff_info(self):
        print('Уменьшает точность атак и наносимый урон персонажа.')


class Darkness:
    def __init__(self, debaff='Погружение во мрак'):
        self.debaff = debaff

    def debaff_info(self):
        print('Понижает уровень освещенности, что затрудняет восприятие окружающей среды.')


class DenseAtmosphere:
    def __init__(self, debaff='Густая атмосфера'):
        self.debaff = debaff

    def debaff_info(self):
        print('Уменьшает скорость передвижения персонажа из-за тяжелой или загрязненной атмосферы.')


class ToxicFumes:
    def __init__(self, debaff='Ядовитые испарения'):
        self.debaff = debaff

    def debaff_info(self):
        print('Причиняют периодический урон здоровью персонажа.')


class HazardousCurrents:
    def __init__(self, debaff='Опасные течения'):
        self.debaff = debaff

    def debaff_info(self):
        print('Увеличивают время перемещения или усложняют прохождение через определенные участки.')


class TimeDistortion:
    def __init__(self, debaff='Искажение времени'):
        self.debaff = debaff

    def debaff_info(self):
        print('Уменьшает скорость перемещения или реакции персонажа из-за аномальных временных эффектов.')


class SwampyMarsh:
    def __init__(self, debaff='Мерзкое болото'):
        self.debaff = debaff

    def debaff_info(self):
        print('Замедляет передвижение и повышает вероятность увязнуть в грязи.')


class EntangledPaths:
    def __init__(self, debaff='Запутанные путы'):
        self.debaff = debaff

    def debaff_info(self):
        print('Затрудняют прохождение местности из-за переплетенной растительности или преград.')


class TemperatureFluctuations:
    def __init__(self, debaff='Температурные колебания'):
        self.debaff = debaff

    def debaff_info(self):
        print(
            'Воздействуют на здоровье или способности персонажа в зависимости от изменений температуры окружающей среды.')


# Массив дебаффов
debaff_pool = [DenseFog, ShakingGround, Darkness, DenseAtmosphere, ToxicFumes, HazardousCurrents, TimeDistortion,
               SwampyMarsh, EntangledPaths, TemperatureFluctuations]


# Шаблоны мобов
class Goblin:
    def __init__(self, enemy='Гоблин'):
        self.enemy = enemy


class Orc:
    def __init__(self, enemy='Орк'):
        self.enemy = enemy


class Witch:
    def __init__(self, enemy='Ведьма'):
        self.enemy = enemy


class Dragon:
    def __init__(self, enemy='Дракон'):
        self.enemy = enemy


class MonstrousWolf:
    def __init__(self, enemy='Чудовищный волк'):
        self.enemy = enemy


class Zombie:
    def __init__(self, enemy='Зомби'):
        self.enemy = enemy


class Vampire:
    def __init__(self, enemy='Вампир'):
        self.enemy = enemy


class GiantSpider:
    def __init__(self, enemy='Гигантский паук'):
        self.enemy = enemy


class MagicGolem:
    def __init__(self, enemy='Волшебный голем'):
        self.enemy = enemy


class ElvenArcher:
    def __init__(self, enemy='Эльфийский лучник'):
        self.enemy = enemy


# Массив противников
enemy_pool = [Goblin, Orc, Witch, Dragon, MonstrousWolf, Zombie, Vampire, GiantSpider, MagicGolem, ElvenArcher]


# Главный шаблон для локации
class Location:
    def __init__(self, environment, indoor, weather, baff, debaff, enemy):
        self.environment = environment
        self.indoor = indoor
        if self.indoor == 'True':
            self.weather = 'В укрытии'
        else:
            self.weather = weather
        self.baff = baff
        self.debaff = debaff
        self.enemy = enemy

    def info(self):
        if self.indoor == 'True':
            weather = 'вы в укрытии'
        else:
            weather = f'погода - {self.weather}'
        print(
            f'Вы попадете в локацию под названием "{self.environment}", {weather}, вы находитесь под баффов - {self.baff} и дебаффом {self.debaff}. Впереди вы видите - {self.enemy}')


PreLocation = environment_pool[randint(0, 9)]()

RandLocation = Location(PreLocation.environment, PreLocation.indoor,
                        weather_pool[randint(0, 9)]().weather,
                        baff_pool[randint(0, 9)]().baff,
                        debaff_pool[randint(0, 9)]().debaff, enemy_pool[randint(0, 9)]().enemy)

RandLocation.info()

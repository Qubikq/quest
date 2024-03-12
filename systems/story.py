from random import randint


class MinorInjury:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Травма {self.name}, Описание: {self.description}"


# Creating 10 minor injuries
minor_injuries = [
    MinorInjury("Ссадина", "Небольшая ссадина на коже."),
    MinorInjury("Слегка поврежденный палец", "Палец немного поврежден, но не слишком серьезно."),
    MinorInjury("Мышечный растяжения", "Легкое растяжение мышцы."),
    MinorInjury("Небольшой ушиб", "Ушиб, вызывающий незначительную боль."),
    MinorInjury("Легкое порезание", "Порез на коже, который не требует особого вмешательства."),
    MinorInjury("Небольшой ожог", "Легкий ожог, вызывающий дискомфорт, но не наносящий серьезного вреда."),
    MinorInjury("Небольшой вывих", "Легкий вывих сустава."),
    MinorInjury("Слегка растянутая связка", "Легкое растяжение связки, вызывающее дискомфорт."),
    MinorInjury("Небольшое ушибленное место", "Место, где небольшая часть тела была ударена и покраснела."),
    MinorInjury("Небольшая ссадина", "Небольшая ссадина на поверхности кожи."),
]

# Example usage:
for injury in minor_injuries:
    print(injury)

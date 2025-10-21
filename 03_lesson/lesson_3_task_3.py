from address import Address
from mailing import Mailing

#Заполните поля класса адресами (to_address и from_address), трек-номером (track) и стоимостью (cost).
to_address = Address ("629735", "Nadym", "Zvereva", "47", "17")
from_address = Address("777777", "Moskow", "Shabolovka", "38", "a")

mail = Mailing(to_address, from_address, 189, "s22G33" )

#Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, 
# <дом> -<квартира>. Стоимость <стоимость> рублей.
print(
    f"Отправление {mail.track} из {mail.from_address.index}, "
    f"{mail.from_address.city}, {mail.from_address.stret}, {mail.from_address.dom} - "
    f"{mail.from_address.kv} в {mail.to_address.index}, {mail.to_address.city} "
    f"{mail.to_address.stret}, {mail.to_address.dom} - "
    f"{mail.to_address.kv}. "
    f"Стоимость {mail.cost} рублей."
)
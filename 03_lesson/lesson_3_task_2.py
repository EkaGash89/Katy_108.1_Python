from smartphone import Smartphone

catalog = [
    Smartphone("Aple", 12, "+7-999-000-11-22"),
    Smartphone("Samsyng", "C 25", "+7-888-000-33-44"),
    Smartphone("Nokia", "C00", "+7-777-000-55-66")
]

for Smartphone in catalog:
    print(f"{Smartphone.marka} - {Smartphone.model} - {Smartphone.nomer}")
import termtables as table

t_header = ["Category", "Choice"]
t_data = [
    ["Weapons", 1],
    ["Potions", 2],
    ["Health", 3],
]
table.print(
    t_data,
    header=t_header,
    style=table.styles.double_thin
)

t_weapon = ["Weapons", "Damage", "Choise"]
t_weaponData = [
    ["Knife", "Between 0-6", 1],
    ["Sword","Between 1-12", 2],
    ["Bomb","Between 6-7", 3],
]
table.print(
    t_weaponData,
    header=t_weapon,
    style=table.styles.double_thin
)

#Ändra inventory till en table men inte Shoppen!
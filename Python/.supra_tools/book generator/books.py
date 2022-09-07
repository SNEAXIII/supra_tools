from color import *

saut_ligne = ("_______________", Bordeau, "")

livre = (
    ("Four", Bordeau, "/fill 18 -3 7 13 -3 -8 minecraft:furnace replace stone"),
    (saut_ligne),
    ("Stone", Bordeau, "/fill 18 -3 7 13 -3 -8 minecraft:stone replace furnace"),
    (saut_ligne),
    ("Wagonet", Bordeau, "/kill @e[type= minecraft:hopper_minecart ]"),
)

titre = "Outils"
auteur = "Baloche"
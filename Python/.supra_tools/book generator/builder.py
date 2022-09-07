from books import *


with open("command.txt", "w") as f:
    f.write("/give @p written_book{pages:['[\"\",")
    for index, elem in enumerate(livre):
        if not elem[2]:
            f.write("{" + f"\"text\":\"{elem[0]}\",\"color\":\"{elem[1]}\"" + "}")
        else:
            f.write(
                "{" + f"\"text\":\"{elem[0]}\",\"color\":\"{elem[1]}\",\"clickEvent\":" + "{\"action\":" + "\"run_command\",\"value\":\""+f"{elem[2]}"+"\"}}")
        if index != len(livre) - 1:
            f.write(",{\"text\":\"\\\\n\",\"color\":\"reset\"},")

    f.write(f"]'],title:{titre},author:{auteur}" + "}")

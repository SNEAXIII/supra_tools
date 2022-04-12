from chiffrobalise import secret

phrase_ = "j'aime pas faire la pousierre sur mon burreau"  # a completer
clee = "treize"

chiff = secret(phrase_, clee)

chiff.show()

chiff.switch()

chiff.show()

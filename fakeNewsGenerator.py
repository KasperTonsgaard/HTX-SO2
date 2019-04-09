import fakeNewsSubFunctions as gm
import random


def GenerateFakeArticles():
    output = []
    output.append([gm.GiveMeFakePaludan(), "Police"])
    output.append([gm.GiveMeFakePutin(), "War"])
    output.append([gm.GiveMeFakeMusk(), "Elon Musk"])
    output.append([gm.GiveMeFakeTrump(), "Trump"])
    output.append([gm.GiveMeFakeNetflix(), "Netflix"])
    output.append([gm.GiveMeFakeDisney(), "Disney"])
    output.append([gm.GiveMeFakeRandomStuff(), "Random Stuff"])
    output.append([gm.GiveMeFakeWar(), "War"])
    output.append([gm.GiveMeFakeKimKanyeWest(), "Kanye"])
    output.append([gm.GiveMeFakeKimJongUn(), "North Korea"])
    output.append([gm.GiveMeFakeCelebritties(), "Celebrities"])
    output.append([gm.GiveMeFakePiaK(), "Politics"])
    #output.append([gm.GiveMeFakeJeppeK(), "Jeppe K"])
    output.append([gm.GiveMeFakeYahyaHassan(), "Police"])
    output.append([gm.GiveMeFakePewDiePie(), "Youtube"])
    random.shuffle(output)
    #output.append([gm.GiveMeFakeVejr(), "Vejr"])
    return output #Returner en liste, der indeholder 14 lister, som hver indeholder "Overskrift" og "Emne".

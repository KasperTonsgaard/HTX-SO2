import random


def GiveMeFakeNetflix():
    name = ["Netflix", "The largest streaming platform", "Big Flix", "The streaming platform Netflix", "streaming platform"]

    action = [" announces", " announced", " reveals", " revealed", " publishes",
              " published", " issues", " issued", " advertises", " advertised"]

    addDelete = [" the addition of", " the deletion of", " the reappearence of"]

    filling = [" a new", " an old", " a great", " a fan favorite"]

    genres = [" horror-", " comedy-", " action-", " adventure-", " drama-", " fantasy-"]

    kind = ["movie", "series", "TV series", "blockbuster movie"]

    filling2 = [" through", " on", " via", " using"]

    media = [" Facebook.", " Instagram.", " Snapchat.", " Twitter.",
             " Youtube.", " Vimeo.", " Reddit.", " TikTok.", " LinkedIn."]
    x1 = random.randint(0, len(name) - 1)
    x2 = random.randint(0, len(action) - 1)
    x3 = random.randint(0, len(addDelete) - 1)
    x4 = random.randint(0, len(filling) - 1)
    x5 = random.randint(0, len(genres) - 1)
    x6 = random.randint(0, len(kind) - 1)
    x7 = random.randint(0, len(filling2) - 1)
    x8 = random.randint(0, len(media) - 1)
    sentence = name[x1] + action[x2] + addDelete[x3] + filling[x4] + genres[x5] + kind[x6] + filling2[x7] + media[x8]

    return sentence


def GiveMeFakeDisney():
    import random
    word1 = ["Anonymous Disney worker",
                   "Disney director Alan Braverman",
                   "Head of Disney Channel",
                   "Shocked Disney fans"]

    word2 = ["reveals that",
             "was very angry because",
             "was extremely happy because"]

    word3 = ["the new Star Wars movie will be canceled",
             "Disney has gone bankrupt",
             "Mickey Mouse will be in the new Avengers movie"]

    rand1 = word1[random.randint(0, 3)]
    rand2 = word2[random.randint(0, 2)]
    rand3 = word3[random.randint(0, 2)]

    return "{} {} {}.".format(rand1, rand2, rand3)


def GiveMeFakeKimJongUn():
    noun = ['Kim Jong Un ', 'North Korea ', 'The leader of North Korea ', 'The supreme leader of North Korea ', 'The dictator of North Korea ']
    verb = ['has ', 'is ']
    action = ['declared war on ', 'declared peace with ', 'dropped a nuke on ', 'spoken about ', 'going to support ', 'declaring war on ', 'going to nuke ']
    country = ['China', 'Denmark', 'USA', 'Japan', 'South Korea', 'India']
    topics = ['Climate', 'War', 'Alliances', 'Donald Trump']

    a = random.randint(0, 4)
    b = random.randint(0, 1)
    if b == 0:
        c = random.randint(0, 2)
    else:
        c = random.randint(3, 6)
    if c == 3 or c == 4:
        if random.randint(0, 1) == 0:
            randlist = country
            d = random.randint(0, 5)
        else:
            randlist = topics
            d = random.randint(0, 3)
    else:
        randlist = country
        d = random.randint(0, 5)

    return "{}{}{}{}.".format(noun[a], verb[b], action[c], randlist[d])


def GiveMeFakeWar():
    import random

    ord1 = ["Last night, ", "Last friday evening, ", "On the 8th of February, ", "Last thursday, ", "Yesterday, ",
            "On the 1st of April, ", "A few hours ago, "]

    ord2 = ["Denmark ", "NATO ", "Russia ", "North Korea ", "The US ", "The UN ", "Kazakhstan ", "Uzbekistan ",
            "a small rebellion ", "China ", "ISIS ", "an Islamic terror organisation "]

    ord3 = ["declared war on ", "nuked ", "launched a missile strike on ", "canceled trade with ", "bombed ",
            "engaged in military combat with ", "marched their troops into ", "allegedly sent spies to ",
            "publicly executed a journalist from ", "invaded ", "took control of the airspace over "]

    ord4 = ["Germany: ", "South Korea: ", "Japan: ", "Brazil: ", "Spain: ", "Sweden: ", "Norway: ", "Mexico: ",
            "The United Kingdom: ", "Ireland: ", "Vietnam: ", "South Africa: ", "Italy: ", "France: ", "Canada: ",
            "Ukraine: "]

    ord5 = ["This will SHOCK you!", "You WON'T BELIEVE what happened next!", "Angela Merkel is OUTRAGED!",
            "Hitler would NOT approve!", "Is this the end of the world?", "Obama is ashamed...",
            "You HAVE to read this!", "Here's what this means for you", "No one saw this coming!", "Trump is amused"]

    fakeNews = (ord1[random.randint(0, len(ord1) - 1)]) + (ord2[random.randint(0, len(ord2) - 1)]) + (ord3[random.randint(0, len(ord3) - 1)]) + (ord4[random.randint(0, len(ord4) - 1)]) + (ord5[random.randint(0, len(ord5) - 1)])

    return fakeNews


def GiveMeFakeTrump():
    import random
    word1 = ["Trump","Donald Trump","Mr. President","The President of USA","Mr. Trump","The president"]
    word2 = ["anounces", "calls", "talks about", "kisses", "hugs", "smells", "texts", "bans", "denies","adopts","rejects","launches missiles towards",]
    word3 = ["Pakistan","the middle east","Kim jong un","North korea","Denmark","Hillary Clinton","Mexico","mexicans","Trump tower","New york","Europe","Russia","Putin"]
    word4 = ["at", "in the middle of","near","following"]
    word5 = ["The Grammys", "The Oscars", "a party", "a gas station", "a bar visit"," a press conference"]

    sentences = [word1[random.randint(0, len(word1) - 1)],
                 word2[random.randint(0, len(word2) - 1)],
                 word3[random.randint(0, len(word3) - 1)],
                 word4[random.randint(0, len(word4) - 1)],
                 word5[random.randint(0, len(word5) - 1)]]

    return " ".join(sentences)


def GiveMeFakePutin():
    yyyy = random.randint(1970, 2019)
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    putin = ['Putin', 'Vladimir Vladimirovich Putin', 'President of Russia', 'President of Russian Federation', 'Leader of the Russian Federation', 'Russian president Vladimir Putin']
    action = ['was', "had been"]
    done = ['killed by', 'shot by', "murdered by"]
    thing = ['people from USA', 'Trump', 'people from the Middle east', "Obama", "Steve Jobs"]
    reason = ['because of', "for the sake of", "thanks to"]
    person = ['Poland', 'Denmark', 'France', 'England', "Germany", "Sweden", "Norway", "Japan", "Canada", "Vietnam"]

    monthNumber = random.randint(0, 11)
    putinNumber = random.randint(0, len(putin)-1)
    actionNumber = random.randint(0, len(action)-1)
    doneNumber = random.randint(0, len(done)-1)
    thingNumber = random.randint(0, len(thing)-1)
    reasonNumber = random.randint(0, len(reason)-1)
    personNumber = random.randint(0, len(person)-1)
    mo = month[monthNumber]
    pu = putin[putinNumber]
    ac = action[actionNumber]
    do = done[doneNumber]
    th = thing[thingNumber]
    re = reason[reasonNumber]
    pe = person[personNumber]

    return "In " + str(mo) + " " + str(yyyy) + " " + str(pu) + " " + str(ac) + " " + str(do) + " " + str(th) + " " + str(re) + " " + str(pe)


def GiveMeFakeMusk():
    A = ['Elon Musk', 'Musk', 'Tesla CEO', 'SpaceX CEO', 'Tesla CEO Elon Musk', 'SpaceX CEO Elon Musk', 'Paypal Founder'
         , 'Paypal Founder Elon Musk']

    B = ['has said that', 'states that', 'thinks that', 'tweets that']

    says = ['North Korea', 'Tesla', 'Donald Trump', 'Barack Obama', 'Neil Armstron' , 'Competitors', 'The ISS', 'Denmark'
           ,'Islamic Terrorists', 'Venezuela']

    says2 = ['will', 'is', 'wants', 'wants to']

    will = ['reach Mars', 'reach the Moon', 'reach the Sun', 'explode', 'fail', 'dominate the market', 'kill democracy',
                'take over the world', 'reach Mars by'+ str(random.randint(2,50)+2019), 'remove all water on Earth']

    si = ['undermining democracy', 'winning', 'losing', 'planning to expand', 'taking over the world', 'socialist']

    wants = ['communism', 'a cleaner environment', 'a new capital in the US', 'more']

    wantsto = ['destroy democacy', 'take over the world', 'be carbon-neutral by ' + str(random.randint(2,50)+2019),
               'reach Mars by' + str(random.randint(2,50)+2019), 'reach Mars', 'reach the Moon', 'reach the Sun',
                'explore the Alpha Centauri System']

    x = random.randint(0, 3)
    if x == 0:
        return A[random.randint(0, 7)] + ' ' + B[random.randint(0, 3)] + ' ' + says[random.randint(0, 9)] + ' ' + says2[0] + ' ' + will[random.randint(0, 9)]
    if x == 1:
        return A[random.randint(0, 7)] + ' ' + B[random.randint(0, 3)] + ' ' + says[random.randint(0, 9)] + ' ' + says2[1] + ' ' + si[random.randint(0, 5)]
    if x == 2:
        return A[random.randint(0, 7)] + ' ' + B[random.randint(0, 3)] + ' ' + says[random.randint(0,9)] + ' ' + says2[2] + ' ' + wants[random.randint(0, 3)]
    if x == 3:
        return A[random.randint(0, 7)] + ' ' + B[random.randint(0, 3)] + ' ' + says[random.randint(0,9)] + ' ' + says2[3] + ' ' + wantsto[random.randint(0, 7)]


def GiveMeFakePiaK ():
    who = ["Pia Kjærsgård ", "Pia K. ", "Fru Kjærsgård ", "P. Kjærsgård ", "The previous DF general ",
           "That woman with the penis lamp ", "The DF woman known for her hair and nose "]
    when = ["has over the course of the past few days ", "spend a year trying to ",
            "has stated that she soon will attempt to ", "will in the year 2030 ", "reveals that she'd love to ",
            "will never ever ", "is angry because she ", "doesn't like kids because she once saw them ",
            "has a penis lamp because she "]
    what = ["shot ", "shit ", "blackmail ", "slap ", "peber spray ", "kill ", "cooked ", "eat "]
    whatTwo = ["a potato. ", "a durum. ", "a child. ", "seventy school kids on their way home. ", "the jews. "]
    comment = ["The UN is not amused.", "Lars Lykke approves.", "You won't believe what happened next.",
               "Only one percent of educated students know how."]
    sentence = who[random.randint(0, who.__len__() - 1)] + when[random.randint(0, when.__len__() - 1)] + what[random.randint(0, what.__len__() - 1)] + whatTwo[random.randint(0, whatTwo.__len__() - 1)] + comment[random.randint(0, comment.__len__() - 1)]
    return sentence


def GiveMeFakeYahyaHassan():
    Name = ["Yahya Hassan", "Yahya", "Yahya H.", "The poet righter Yahya Hassan", "Well know Yahya Hassan",
            "Once again Yahya Hassan"]
    two = ["have shot", "have given his views on", "shoots", "rapes", "posts new video on FaceBook, dissing"]

    three = ["Rasmus Paludan", "Pia Kjærsgaard", "Lars Løkke", "Donald Trump", "Bill Gates", "Elon Musk", "Mirsad",
             "Some Nibba from the hood", "Some nibba", "An Alabama Nibba", "My Nibba", "A Wibba"]
    four = ["because", "after"]
    five = ["Rasmus Paludan", "Pia Kjærsgaard", "Lars Løkke", "Donald Trump", "Bill Gates", "Elon Musk", "Mirsad",
            "Some nibba from the hood", "Some nibba", "An Alabama Nibba", "My Nibba", "A Wibba"]
    six = ["told him to shut up", "threatend him", "likes Pia K", "called him a nibba", "told him to",
           "was about to stab him with a knife", "shot him in the foot"]
    return Name[random.randint(0,len(Name)-1)] + " " + two[random.randint(0,len(two)-1)] + " " + three[random.randint(0,len(three)-1)] + " " + four[random.randint(0,len(four)-1)] + " " + five[random.randint(0,len(five)-1)] + " " + six[random.randint(0,len(six)-1)]


def GiveMeFakePewDiePie():

    timeLocPastT = ["Last Sunday", "Yesterday", "Last Week", "Last Month", "Last Friday Night",
                    "Saturday Night", "At an Important Meeting", "At Comic-Con", "Recently",
                    "A Long Time Ago, in a Galaxy far far away", "At an Annual Alien Meetup",
                    "In The Alley Behind McDonalds", "In a local Starbucks Bathroom",
                    "In a White Van Parked Behind Toys'R'us", "In a forest in Japan", "On DR. Phil"]

    timeLocPreT = ["", "at an Important Meeting", "At Comic-Con", "At an Annual Alien Meetup",
                   "In an Alley Behind McDonalds", "In a local Starbucks Bathroom",
                   "In a White Van Parked Behind Toys'R'us",
                   "In a forest in Japan"]

    pewd = ["PewDiePie", "Youtube Star: Felix Pew Kjellberg", "Felix Kjellberg", "Legendary YouTuber, PewDiePie"]

    labelledPastT = ["Called", "Described"]

    peopleStuff = ["Donald Trump", "Spiderman", "Kanye West", "Keanu Reeves", "Taylor Swift", "Putin", "Tony Stark",
                   "Some Feminists", "Spongebob", "Thanos", "Papa Smurf", "Adolf Hitler", "Elon Musk",
                   "Queen Elizabeth"]

    peopleJ = ["Donald Trump", "Spiderman", "Kanye West", "Keanu Reeves", "Taylor Swift", "Putin", "Tony Stark",
               "Some Feminists", "Spongebob", "Thanos", "Papa Smurf", "Adolf Hitler", "Elon Musk", "Queen Elizabeth"]

    labels = ["the Worst Redhead to Ever Walk the Planet", "a Wierd Looking Carpet Stain", "a Delicious Meal",
              "a Retarded Version of Communism", "a Beautiful Meme", "an Annoying Piece of Moldy Cheese",
              "the Centerpoint of Shitty Music", "the Pinnacle of Humanity", "an Excellent Hair Conditioner",
              "a Noble Pain in the Rear End", "a Perfection of Weeb Culture", "the Peak of Human Evolution",
              "a Brown Stain on Life", "an Insult to Anime"]

    injuryPastT = ["Was Injured", "Died", "Almost Died", ]

    injuryAccPastT = ["in a HotWheels-Car Crash", "in the Crash of a remote controlled model plane.",
                      "in a Gay-Sex Related Accident", "in a Weird Accident",
                      "in a Bathtub Whirlpool", "In a Kid-sized Waterslide", "when he Attempted to Fistfight Shaggy",
                      "when he got a Bottle of Shampoo Stuck in his Mouth",
                      "when T-Series Passed him for the 5th time."]

    announcePastT = ["Said", "Announced", "Revealed", "Disclosed", "Tweeted"]

    announcePreT = ["Announces", "Says", "Reveals"]

    hapRelPeople = ["he was Assaulted by", "he Always had a Crush on", "he Never Actually Liked", "he Actually Hates",
                    "he once had an Affair with", "he is Actually Related to", "he is Addicted to",
                    "he once Switched Places with his Twin Sister:", "he has Adopted", ]

    hapEnd = ["That he is actually a time traveler from " + str(random.randint(30, 250) + 2019),
              "That he Believes the Earth is a Green and Blue Space-potato",
              "That he is addicted to Blueberry Marmalade",
              "That he Still Wears a Diaper when he Sleeps", "That he is Secretly Involved with your Mom",
              "That he is from a Species of Aliens who Eat Memes", "That he was Gay all Along",
              "That T-Series is Actually Controlled by Himself", "That he Cries Himself to Sleep Every Night."]

    timeA = ["Just", "Recently"]

    comment = ["Agrees.", "Approves.", "is in Disbelief.", "Couldn't be more Happy.", "is furious.",
               "Wants nothing to do with it.", "Thinks this might be the end of life as we know it." ,
               "Reminds him Jesus is Watching"]

    choice = random.randint(1,9)
    PewOut = []


    if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 9:
        x = random.randint(0,len(timeLocPastT)-1)
        PewOut.append(timeLocPastT[x])

    if choice == 5 or choice == 6:
        x = random.randint(0,len(timeLocPreT)-1)
        PewOut.append(timeLocPreT[x])

    x = random.randint(0, len(pewd)-1)
    PewOut.append(pewd[x])

    if choice == 7 or choice == 8:
        x = random.randint(0, len(timeA)-1)
        PewOut.append(timeA[x])

    if choice == 5 or choice == 6:
        x = random.randint(0, len(announcePreT) - 1)
        PewOut.append(announcePreT[x])

    if choice == 3 or choice == 4 or choice == 7 or choice == 8:
        x = random.randint(0, len(announcePastT) - 1)
        PewOut.append(announcePastT[x])

    if choice == 4 or choice == 6 or choice == 7:
        x = random.randint(0, len(hapEnd) - 1)
        PewOut.append(hapEnd[x])

    if choice == 3 or choice == 5 or choice == 8:
        x = random.randint(0, len(hapRelPeople) - 1)
        PewOut.append(hapRelPeople[x])

    if choice == 2:
        x = random.randint(0, len(injuryPastT)-1)
        PewOut.append(injuryPastT[x])

    if choice == 2:
        x = random.randint(0, len(injuryAccPastT)-1)
        PewOut.append(injuryAccPastT[x])

    if choice == 1:
        PewOut.append(labelledPastT[0])

    if choice == 9:
        PewOut.append((labelledPastT[1]))

    if choice == 1 or choice == 3 or choice == 5 or choice == 8 or choice == 9:
        x = random.randint(0, len(peopleStuff) - 1)
        PewOut.append(peopleStuff[x])

    if choice == 9:
        PewOut.append("as")

    if choice == 1 or choice == 9:
        x = random.randint(0, len(labels) - 1)
        PewOut.append(labels[x])

    if random.randint(1,2) == 1 :
        x = random.randint(0, len(peopleJ) - 1)
        PewOut.append(", "+ peopleJ[x])

        x = random.randint(0, len(comment) - 1)
        PewOut.append(comment[x])

    return " ".join(PewOut)


def GiveMeFakeKimKanyeWest():
    A = ["Kanye West", "Kim Kardashian West", "Kim K", "Kim Kardashian", "Kanye", "Kim", "Kim K. W.", "Kanye West", "Kanye W"]

    B = ["is", "is not", "runs", "sleeps", "talks", "shops", "was", "was not",]

    C = ["naked", "upset", "drunk", "high as fuck", "sober", "poor", "sweet", "gay"]

    D = ["for"]

    E = ["presidential election", "the mother-in-law", "pewdiepie", "another penny", "Stan Lee", "Mirsad", "Angela Merkel", "uber-driver", "sex therapist", "second husband", "drake" ]

    F = ["because" ]

    G = ["jesus said so", "yeezy shoes have been canceled", "nike bought adidas", "keeping up with the kardashians has been canceled"]

    H = ["and"]

    I = ["Donald Trump gave a check to Bernie Sanders for being his unknown older brother", "snoopy left the peanuts", "Tom and Jerry separated after unhappy marriage for 78 years", "NASA exploded an atomic bomb on the sun", "Vegans secret god is a cannibal", "Donald Trump was getting married to and mexican", "Hillary Clinton got dumped by Donald Trump after he became president", "Drake have been through a gender transition after Gods plan failed", "yeezy have been designed by a puma designer", "the pove quits job as pove after his late sundays with vodka and children was discovered", "McDonalds goes full vegan, only chicken on the menu"]

    a = random.randint(0, 8)
    b = random.randint(0, 7)
    c = random.randint(0, 7)
    d = random.randint(0, 0)
    e = random.randint(0, 10)
    f = random.randint(0, 0)
    g = random.randint(0, 3)
    h = random.randint(0, 0)
    i = random.randint(0, 10)


    minString = A[a] + " " + B[b] + " " + C[c] + " " + D[d] + " " + E[e] + " " + F[f] + " " + G[g] + " " + H[h] + " " + I[i]

    return minString


def GiveMeFakeCelebritties():
    A = ["Rihanna", "Lukas Graham", "Kylie Jenner", "Zendaya", "Tom Holland", "Ariana Grande", "Fie Laursen",
    "Cristiano Ronaldo", "Scarlett Johansson", "Justin Bieber", "Beyoncé Knowles", "Taylor Swift", "Jennifer Lopez",
    "Kim Kardashian"]

    B = ["are", "need", "should be", "could be", "became", "criticized", "are calling", "pinches",
    "own", "love", "have been", "hate"]

    C = ["a comedian", "the coach of FC Barcelona", "the president of the USA", "the leader of EU", "the leader of FN",
    "KKK members", "ISIS members"]

    D = ["and love it", "and hate it", "and hide it", "and deny it", "beside a mall", "next to McDonald's"]

    a = random.randint(0, 13)
    b = random.randint(0, 11)
    c = random.randint(0, 6)
    d = random.randint(0, 5)


    MySentense = A[a] + " " + B[b] + " " + C[c] + " " + D[d] + "."

    return MySentense


def GiveMeFakeRandomStuff():
    part1 = [
        "The world's most important kitten ",
        "The friendly old lady down the road ",
        "Somebody unimportant ",
        "That guy everyone know is a murder ",
        "Every dog on the planet ",

        "Fox News ",
        "Gays ",
        "He who must not be named ",
        "That guy, who have declared himself an independent county, ",
        "The greatest teacher ever "
    ]


    part2 = [
        "have imposed sanctions against ",
        "have taken a new stance on ",
        "was killed last night by ",
        "declared that smocking is good because of ",
        "have saved the world from certain doom by the use of ",

        "have declared war against ",
        "have imposed taxes on ",
        "tried to kill every cat on the planet by using ",
        "have taken over the world by the extraordinary use of ",
        "have taken over BBC with the creative use of "
    ]
    part3 = [
        "USA. ",
        "something called cuteness. ",
        "Russia. ",
        "collective wishing one thing come true. ",
        "everything. ",

        "white people. ",
        "logic. ",
        "world peace. ",
        "AIDS. ",
        "fake news. "
    ]
    part4 = [
        "NATO is not amused.",
        "UN approves. ",
        "NATO approves. ",
        "Trump desires to do the same. ",
        "UN is not amused. ",

        "This is not a joke. ",
        "The UN is furious.",
        "NATO is furious.",
        "Trump is amused.",
        "UN approve hole heartily."
    ]

    a = len(part1) - 1
    b = len(part2) - 1
    c = len(part3) - 1
    d = len(part4) - 1
    re = part1[random.randint(0, a)] + part2[random.randint(0, b)] + part3[random.randint(0, c)] \
         + part4[random.randint(0, d)]
    return re


def GiveMeFakePaludan():
    import random
    noun = ["soldier of the freedom ", "protector of the weak ", "community guardian ", "Light of the danes ", "Rasmus Paludan "]
    verb = ['has ', 'is ']
    action = ['burnt the koraan ', 'blown up a muske in ', 'burnt a koraan in ', 'sentenced too jail for ', 'going to support ', 'declaring war on ', 'going to nuke ']
    country = ['China', 'Denmark', 'USA', 'Japan', 'South Korea', 'India']
    topics = ['racisim', 'terrorisim', 'stupidity ', 'Donald Trump']

    a = random.randint(0, 4)
    b = random.randint(0, 1)
    if b == 0:
        c = random.randint(0, 2)
    else:
        c = random.randint(3, 6)
    if c == 3 or c == 4:
        if random.randint(0, 1) == 0:
            randlist = country
            d = random.randint(0, 5)
        else:
            randlist = topics
            d = random.randint(0, 3)
    else:
        randlist = country
        d = random.randint(0, 5)

    return noun[a] + verb[b] + action[c] + randlist[d]

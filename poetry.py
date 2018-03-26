from random import choice

noun = ["history", "way", "art", "world", "information", "map", "two",
        "family", "government", "health", "system", "computer", "meat", "year",
        "thanks", "music", "person", "reading", "method", "data", "food", "understanding",
        "theory", "law", "bird", "literature", "problem", "software", "control", "knowledge",
        "power", "ability", "economics", "love", "internet", "television", "science",
        "library", "nature", "fact", "product", "idea", "temperature", "investment",
        "area", "society", "activity", "story", "industry", "media", "thing", "oven",
        "community", "definition", "safety", "quality", "development", "language", "people"
    ]
adjective = [ "able", "bad", "best", "better", "big", "black", "certain", "clear",
              "different", "early", "easy", "economic", "federal", "free", "full", "good",
              "great", "hard", "high", "human", "important", "international", "large",
              "late", "little", "local", "long", "low", "major", "military", "national",
              "new", "old", "only", "other", "political", "possible", "public", "real",
              "recent", "right", "small", "social", "special", "strong", "sure", "true",
              "white", "whole", "young"
    ]
adverb = ["up", "so", "out", "just", "now", "how", "then", "more", "also", "here",
          "well", "only", "very", "even", "back", "there", "down", "still", "in", "as",
          "too", "when", "never", "really", "most" 
    ]
verb = ["ask", "be", "become", "begin", "call", "can", "come", "could", "do", "feel", "find",
        "get", "give", "go", "have", "hear", "help", "keep", "know", "leave", "let", "like",
        "live", "look", "make", "may", "mean", "might", "move", "need", "play", "put", "run",
        "say", "see", "seem", "should", "show", "start", "take", "talk", "tell", "think",
        "try", "turn", "use", "want", "will", "work", "would"
    ]
preposition = ["at", "from", "into", "during", "including", "until", "against", "among",
               "throughout", "despite", "towards", "upon", "concerning", "of", "to", "in",
               "for", "on", "by", "about", "like", "through", "over", "before", "between",
               "after", "since", "without", "under", "within", "along", "following", "across",
               "behind", "beyond", "plus", "except", "but", "up", "out", "around", "down",
               "off", "above", "near", "with"
    ]
def makePoem():
    n1 = choice(noun)
    n2 = choice(noun)
    n3 = choice(noun)
    while n1 == n2:
        choice(noun)
    while n1 == n3 or n2 == n3:
        choice(noun)
    #select three nouns
        
    v1 = choice(verb)
    v2 = choice(verb)
    v3 = choice(verb)
    while v1 == v2:
        choice(verb)
    while v1 == v3 or v2 == v3:
        choice(verb)
    #select three verbs
        
    adj1 = choice(adjective)
    adj2 = choice(adjective)
    adj3 = choice(adjective)
    while adj1 == adj2:
        choice(adjective)
    while adj1 == adj3 or adj2 == adj3:
        choice(adjective)
    #select three adjectives
        
    adv1 = choice(adverb)
    #select adverb
    
    p1 = choice(preposition)
    p2 = choice(preposition)
    while p1 == p2:
        choice(preposition)
    #select two prepositions
        
    if "aeiou".find(adj1[0]) == True:
        A = "An"
    else:
        A = "A"
    if "aeiou".find(adj3[0]) == True:
        a = "an"
    else:
        a = "a"
    #switch between a/an depending on vowels

    print(f"{A} {adj1} {n1}")

    print(f"\n{A} {adj1} {n1} {v1} {p1} the {adj2} {n2}")
    print(f"{adv1}, the {n1} {v2}")
    print(f"the {n2} {v3} {p2} {a} {adj3} {n3}")

print(makePoem())




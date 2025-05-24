import json
import random
with open("FacetCalculator/FacetRanges.json","r") as file:
    full = json.load(file)

global kitshort
global regularshort
global regular
global kit

regular = full["normal_traits"]
regularshort = regular.keys()

kit = full["kit_traits"]
kitshort = kit.keys()

def regularfacets():
    print(regularshort)
    print("Which trait do you want? All lowercase.")
    trait = input()
    traitfacets = regular[trait]
    print(traitfacets)
    law = traitfacets["lawfulness"]
    social = traitfacets["sociability"]
    mad = traitfacets["aggression"]
    stable = traitfacets["stability"]

    lawval = random.randint(law[0],law[1])
    print("lawfulness:" , lawval)

    socialval = random.randint(social[0],social[1])
    print("sociability:" , socialval)

    madval = random.randint(mad[0],mad[1])
    print("agression:" , madval)

    stableval = random.randint(stable[0],stable[1])
    print("stability:" , stableval)

def kitfacets():
    print(kitshort)
    print("Which trait do you want? All lowercase.")
    trait = input()
    traitfacets = kit[trait]
    print(traitfacets)
    law = traitfacets["lawfulness"]
    social = traitfacets["sociability"]
    mad = traitfacets["aggression"]
    stable = traitfacets["stability"]

    lawval = random.randint(law[0],law[1])
    print("lawfulness:" , lawval)

    socialval = random.randint(social[0],social[1])
    print("sociability:" , socialval)

    madval = random.randint(mad[0],mad[1])
    print("agression:" , madval)

    stableval = random.randint(stable[0],stable[1])
    print("stability:" , stableval)

print("A adult or kit trait? 1 for adult and 2 for kit.")
onetwo = input()
if onetwo == "2":
    kitfacets()
else:
    regularfacets()
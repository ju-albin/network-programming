import math


def textToByteArray(txt, encoding="ASCII"):
    try:
        converted = bytearray(txt, encoding)
    except Exception as e:
        print(e, "\n")
        return

    print(f"Length before conversion: {len(txt)} \n"
          f"Length after conversion: {len(converted)}")

    print(f"Before conversion: {txt} \n"
          f"After conversion: {converted}")

    for int in converted:
        print(int)

    print("\n")


# 9.1.1
textToByteArray("ABC abc")

# 9.1.2
textToByteArray("ÅÄÖ")

# 9.1.3
textToByteArray("ÅÄÖ", "LATIN-1")

# 9.1.4
textToByteArray("ÅÄÖ", "UTF-8")

# 9.2.1
with open("exempeltext.txt", "r", encoding="LATIN-1" ) as reader:
    txt = reader.read()
    byteArr = bytearray(txt, "utf-8")

    print(f"Length before conversion: {len(txt)} \n"
          f"Length after conversion: {len(byteArr)} \n")


# 9.2.2
def makeHisto(byteArr):
    histo = [0] * 256
    for byte in byteArr:
        histo[byte] += 1
    return histo

histo = makeHisto(byteArr)
print(histo)

def makeProb(histo):
    total = sum(histo)
    if total == 0:
        return [0.0] * len(histo)
    return [count / total for count in histo]

prob = makeProb(histo)
print(prob)

def entropi(prob):
    h = 0.0
    for p in prob:
        if p > 0.0:
            h += p * math.log2(1.0 / p)
    return h


h = entropi(prob) # bits per symbol
min_bytes = (len(byteArr) * h) / 8 # Antal * bits per symbol / 8 (för att göra om till byte)

print("Entropi: ", h)
print("Minsta teoretiska storlek: ", min_bytes) #


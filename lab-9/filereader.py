import math
import random
import zlib

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


# 9.2.3
theCopy = byteArr.copy()
random.shuffle(theCopy)

print("Är orginalet oförändrat? ", byteArr != theCopy)

# 9.2.4
code = (zlib.compress(theCopy))

print ("Compress lyckades? ", theCopy != code)

bits_copy = len(code) * 8
bits_per_symbol_copy = bits_copy / len(theCopy)
print(f"theCopy komprimerad: {len(code)} bytes. {bits_copy} bitar. {bits_per_symbol_copy} bitar/symbol")

orig_code = zlib.compress(byteArr)
bits_orig = len(orig_code) * 8
bits_per_symbol_orig = bits_orig / len(byteArr)
print(f"byteArr komprimerad: {len(orig_code)} bytes. {bits_orig} bitar. {bits_per_symbol_orig} bitar/symbol")

print(f"A. Datasource entropi: {h}. B. zlib of theCopy {bits_per_symbol_copy}. C. zlib of byteArr {bits_per_symbol_orig}")
print(f"Max: {max(bits_per_symbol_copy, bits_per_symbol_orig, h)}")
print(f"Min: {min(bits_per_symbol_copy, bits_per_symbol_orig, h)}")

# 9.2.5
t1 = """I hope this lab never ends because
it is so incredibly thrilling!"""
t10 = 10 * t1

t1_bytes = bytearray(t1, "utf-8")
t10_bytes = bytearray(t10, "utf-8")

t1_compressed = zlib.compress(t1_bytes)
t10_compressed = zlib.compress(t10_bytes)

print(f"t1: {len(t1_bytes)} bytes -> komprimerad: {len(t1_compressed)} bytes")
print(f"t10: {len(t10_bytes)} bytes -> komprimerad: {len(t10_compressed)} bytes")

bits_t1_compressed = len(t1_compressed) * 8
bits_per_symbol_t1_compressed = bits_t1_compressed / len(t1_bytes)
print(f"t1: {bits_per_symbol_t1_compressed:.4f} bitar/symbol")

bits_t10_compressed = len(t10_compressed) * 8
bits_per_symbol_t10_compressed = bits_t10_compressed / len(t10_bytes)
print(f"t10: {bits_per_symbol_t10_compressed:.4f} bitar/symbol")
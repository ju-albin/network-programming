# 9.1.1
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

    for char in converted:
        print(char)
    print("\n")

textToByteArray("ABC abc")

# 9.1.2
textToByteArray("ÅÄÖ")

# 9.1.3
textToByteArray("ÅÄÖ", "LATIN-1")

# 9.1.4
textToByteArray("ÅÄÖ", "UTF-8")

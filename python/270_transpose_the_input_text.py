def transpose(text, text2):
    try:
        for i in range(0, max(len(str(text)), len(str(text2)))):
           print(f"{text[i]}{text2[i]}")

    except IndexError:
        if len(text) != len(text2):
            if len(text) < len(text2):
                for j in range(0, len(text2) - len(text)):
                   print(f" {text2[len(text) + j]}")

            if len(text2) < len(text):
                for j in range(0, len(text) - len(text2)):
                   print(f"{text[len(text2) + j]} ")



transpose("somerr", "text.")
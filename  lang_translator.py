from deep_translator import GoogleTranslator

print("===== LANGUAGE TRANSLATION TOOL =====")

text = input("Enter text: ")
source = input("Source language (english, hindi, french): ")
target = input("Target language (english, hindi, french): ")

try:
    translated = GoogleTranslator(
        source=source.lower(),
        target=target.lower()
    ).translate(text)

    print("\nOriginal Text:", text)
    print("Translated Text:", translated)

except Exception as e:
    print("Error:", e)
import time
import os
from deep_translator import GoogleTranslator
from gtts import gTTS

# 1. Supported languages dictionary configuration
LANGUAGES = {
    1: ["English", "en"],
    2: ["Hindi", "hi"],
    3: ["French", "fr"],
    4: ["Spanish", "es"],
    5: ["German", "de"],
    6: ["Italian", "it"],
    7: ["Japanese", "ja"],
    8: ["Chinese", "zh-CN"],
    9: ["Russian", "ru"],
    10: ["Arabic", "ar"]
}

def display_menu():
    """Renders the terminal-based User Interface menu for language selection."""
    print("\n" + "=" * 65)
    print("      INTERNSHIP PROJECT: ADVANCED LANGUAGE TRANSLATION TOOL")
    print("=" * 65)
    print(" [Features Included: API Translation, Text-to-Speech, Copy Output]")
    print("-" * 65)
    for key, value in LANGUAGES.items():
        print(f"  {key}. {value[0]:<12}", end="" if key % 3 != 0 else "\n")
    print("\n" + "=" * 65)

def get_language_choice(prompt_message):
    """Handles and validates the user input for source and target languages."""
    while True:
        try:
            choice = int(input(prompt_message))
            if choice in LANGUAGES:
                return LANGUAGES[choice]  # Returns: [Language_Name, Language_Code]
            print("[!] Invalid input. Please choose a number from the list.")
        except ValueError:
            print("[!] Please enter a valid numeric choice.")

def handle_optional_features(translated_text, target_code):
    """Implements optional deliverables: Text-to-Speech and Clipboard Copy block."""
    while True:
        print("\n" + "-" * 40)
        print(" Optional Features Available:")
        print(" 1. Listen to translated audio (Text-to-Speech)")
        print(" 2. Generate copyable text block")
        print(" 3. Skip / Translate new text")
        print("-" * 40)
        
        opt_choice = input("Select an option (1/2/3): ").strip()
        
        if opt_choice == '1':
            try:
                print("[*] Generating audio stream via gTTS API... Please wait...")
                tts = gTTS(text=translated_text, lang=target_code, slow=False)
                tts.save("translated_audio.mp3")
                print("[✓] Audio file successfully compiled as 'translated_audio.mp3'!")
                print("    (The file is ready to play in your local workspace directory)")
            except Exception as audio_err:
                print(f"[!] Text-to-Speech conversion failed: {audio_err}")
                
        elif opt_choice == '2':
            print("\n[✓] Clipboard Copy Allocation Block:")
            print(f"--- COPIED TEXT AREA START ---\n{translated_text}\n--- COPIED TEXT AREA END ---")
            print("[*] You can now manually select and copy the string block displayed above.")
            
        elif opt_choice == '3':
            break
        else:
            print("[!] Invalid selection. Please choose 1, 2, or 3.")

def main():
    """Main execution flow managing the lifecycle of the translation utility."""
    while True:
        display_menu()
        
        # UI Requirement: Source and target language initialization
        source_name, source_code = get_language_choice("Select Source Language (Number): ")
        target_name, target_code = get_language_choice("Select Target Language (Number): ")
        
        # Validation to prevent identical structural processing
        if source_code == target_code:
            print("\n[!] Error: Source and Target languages cannot be identical. Please re-select.")
            time.sleep(1)
            continue
            
        # UI Requirement: Extracting data payload from user input
        text_to_translate = input(f"\nEnter text in [{source_name}] to translate: ").strip()
        
        if not text_to_translate:
            print("[!] Empty string payload detected. Aborting current execution context...")
            time.sleep(1)
            continue
            
        # API Requirement: Processing payload transmission and parsing JSON response
        try:
            print("\n[*] Initializing asynchronous request to Google Translate API wrapper...")
            time.sleep(0.5)
            
            # Executing deep_translator core logic
            translated_response = GoogleTranslator(source=source_code, target=target_code).translate(text_to_translate)
            
            # UI Requirement: Rendering structured output directly onto the standard out console
            print("\n" + "═" * 50)
            print(f" ORIGINAL [{source_name.upper()}]: {text_to_translate}")
            print("-" * 50)
            print(f" TRANSLATED [{target_name.upper()}]: {translated_response}")
            print("═" * 50)
            
            # Triggering non-mandatory auxiliary operations
            handle_optional_features(translated_response, target_code)
            
        except Exception as api_error:
            print("\n[!] Critical API runtime connection failure.")
            print(f"    Exception Logs: {api_error}")
            print("[*] Verify system environment network configurations and retry.")
            
        # Program execution loop control
        exit_choice = input("\nDo you want to process another text sequence? (y/n): ").strip().lower()
        if exit_choice != 'y':
            print("\nExiting Internship Translation Tool execution loop. Termination complete. Goodbye!")
            break

if __name__ == "__main__":
    main()

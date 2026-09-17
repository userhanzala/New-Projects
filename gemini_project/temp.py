from colorama import init, Fore, Back, Style
init(autoreset=True)
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

query = input(f"{Fore.CYAN}Gemini: {Fore.RESET}")
history = "User= " + query
client = genai.Client()

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=history
    )
    print(f"{Fore.CYAN}Triangulating")
    for i in range(3):
        print(Fore.CYAN + ".", end="", flush=True)
        time.sleep(1)
    print()
    print(Fore.CYAN + "Gemini Replies: \n\n", interaction.output_text)
    print()
    history = history + "Assistant: "
    query = input(f"{Fore.CYAN}Gemini: {Fore.RESET}")
    history = history + "User: " + query
    if (query == "") or (query == "exit") or (query == "cls"):
        break

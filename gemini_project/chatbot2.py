from colorama import init, Fore, Back, Style
init(autoreset=True)
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()
query = input(f"{Fore.CYAN}Gemini: {Fore.RESET}")
client = genai.Client()

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=query,
        generation_config={
            "temperature":0.8,
            "top_k": 10,
            "max_output_tokens": 500}
    )
    print(f"{Fore.CYAN}Triangulating")
    for i in range(3):
        print(Fore.CYAN + ".", end="", flush=True)
        time.sleep(1)
    print()
    print(Fore.CYAN + "Gemini Replies: \n\n", interaction.output_text)
    print()
    query = input(f"{Fore.CYAN}Gemini: {Fore.RESET}")
    if (query == "") or (query == "exit") or (query == "cls"):
        break

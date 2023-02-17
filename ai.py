import requests
import json
import uuid
from colorama import Fore, init

init(autoreset=True)

url = "https://api.nam.icu/v2/beta/conversation"

chat = []

chatId = uuid.uuid4()

while True:
    question = input(f"{Fore.CYAN}You{Fore.RESET}: ")
    post = {
        "chat_id": str(chatId),
        "prompt": question,
        "chat_data": json.dumps(chat),
    }
    answer = ""
    res = requests.post(url, data=post)
    data = json.loads(res.text)
    answer = data["answer"]
    print(f"{Fore.GREEN}HEUSC{Fore.RESET}:{Fore.LIGHTYELLOW_EX}{answer}")
    chat.append({"question": question, "answer": answer})

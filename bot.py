import requests

TOKEN = "8714851298:AAGKCUSpmK0AZta8Na1GzOCVOl3BKRXNmms"
CHAT_ID = "-1003082238044"
SHEET_ID = "1fqFRd-11r4tpoVQA2bDa5WYK8a8ZnaIdQE90_jv4jg0"

INDEX_FILE = "index.txt"

def get_prompts():
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"
    response = requests.get(url)
    
    lines = response.text.split("\n")
    prompts = [line.strip() for line in lines if line.strip()]
    
    return prompts

def get_index():
    try:
        with open(INDEX_FILE, "r") as f:
            return int(f.read().strip())
    except:
        return 0

def save_index(index):
    with open(INDEX_FILE, "w") as f:
        f.write(str(index))

def send_prompt():
    prompts = get_prompts()
    index = get_index()

    prompt = prompts[index % len(prompts)]

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": prompt
    }

    requests.post(url, data=data)

    save_index(index + 1)

if __name__ == "__main__":
    send_prompt()

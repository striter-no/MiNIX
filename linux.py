from gpt import *
import json as jn

config = jn.load(open('gpt_conf.json'))
chat = Chat(
    model=models_stock.claude_3_5_sonnet,
    provider=provider_stock.PollinationsAI
)

if __name__ == "__main__":
    chat.setSystemQuery(config['sys-prompt'])
    
    while True:
        cmd = input("$ ")

        ans = chat.addMessage(cmd)
        print(ans)
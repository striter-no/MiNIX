from src.gpt import *
import json as jn
import argparse

config = jn.load(open('./configs/gpt_conf.json'))
current_os = "Linux Ubuntu 20.04 LTS"

chat = Chat(
    model=models_stock.claude_3_5_sonnet,
    provider=provider_stock.PollinationsAI
)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='MiNIX - the OS emulator based on LLM')
    parser.add_argument('-o', '--os', type=str, help='Select a OS ', default=current_os)
    parser.add_argument('-m', '--model', type=str, choices=[
        'gpt-4o-mini', 
        'claude-3.5-sonnet', 
        'o1', 
        'deepseek-v3',
        'llama-3.1-405b',
        'o3-mini'
    ], help='Select a GPT model', default='claude-3.5-sonnet')
    args = parser.parse_args()

    chat.setModel(args.model)
    chat.setSystemQuery(config['sys-prompt'])
    
    while True:
        cmd = input("$ ")

        ans = chat.addMessage(cmd)
        print(ans)
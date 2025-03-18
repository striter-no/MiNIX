from src.gpt import *
from typing import List, Union
import json as jn
import re
import argparse

config = jn.load(open('./configs/gpt_conf.json'))
current_os = "Linux Ubuntu 20.04 LTS"

chat = Chat(
    model=models_stock.claude_3_5_sonnet,
    provider=provider_stock.PollinationsAI
)

def xml_parser(content: str) -> dict[str, Union[str, dict]]:
    # Remove leading/trailing whitespace and normalize newlines
    content = content.strip().replace('\n', '')
    
    # Pattern to match tags with their content
    pattern = r'<([^>]+)>(.*?)</\1>'
    matches = re.findall(pattern, content)
    
    result = {}
    for tag, inner_content in matches:
        # If inner content contains tags, parse recursively
        if re.search(r'<[^>]+>', inner_content):
            result[tag] = xml_parser(inner_content)
        else:
            result[tag] = inner_content.strip()
    
    return result

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
    chat.setSystemQuery(config['sys-prompt'] + args.os)
    
    ans = chat.addMessage("!на место команды поставь пробел, а только префикс и путь. этот запрос одноразовый") + '\n'
    parsed = xml_parser(ans)
    print(ans,parsed)

    prefix = parsed["prefix"]
    while True:
        cmd = input(f"{prefix} ")

        ans = chat.addMessage(cmd) + '\n'
        # print(ans)

        try:
            parsed = xml_parser(ans)
            if len(parsed["out"].strip()) > 0 and len(parsed["out"]) > 0:
                print(f"{parsed["out"].replace('\\n', '\n').replace('\\\\N', '\\n')}")

            prefix = parsed["prefix"]
        except Exception as ex:
            print(f"Error: {ex}")
            print(f"---\n{ans}")
from g4f import ChatCompletion
from g4f import models as models_stock
from g4f import Provider as provider_stock
from g4f import Model as modelType
from g4f import ProviderType as providerType
import g4f
import os

class Chat:
    def __init__(self, model: modelType = models_stock.gpt_4o_mini, provider: providerType = provider_stock.Pizzagpt, input_tokens_limit=512_000) -> None:
        self.messages: list[tuple[str, str]] = []
        self.input_tokens_limit = input_tokens_limit
        self.systemQuery: str = ""
        self.model = model
        self.provider = provider
        self.client = g4f.Client(provider=self.provider, model=self.model)
        self.asy_client = g4f.AsyncClient(provider=self.provider, model=self.model)
    
    def _get_images(self, paths: list[str]) -> list[list[bytes, str]]:
        return [[open(path, "rb"), os.path.basename(path)] for path in paths]

    def addMessage(self, query: str, images: list[str] = [], noProvider: bool = False, specified_model: (str | g4f.Model | None) = None) -> str:
        all_messages: list[dict[str, str]] = [{
            "role": "system",
            "content": self.systemQuery
        }]

        for msg in self.messages:
            
            all_messages.append({
                "role": "user",
                "content": msg[0]
            })

            all_messages.append({
                "role": "assistant",
                "content": msg[1]
            })

        all_messages.append({
            "role": "user",
            "content": query
        })

        if not noProvider:
            response = self.client.chat.completions.create(
                messages=all_messages,
                images=self._get_images(images),
                max_tokens=self.input_tokens_limit,
                ignore_working=True,
                model=specified_model if not (specified_model is None) else self.model
            )
        else:
            response = self.client.chat.completions.create(
                messages=all_messages,
                images=self._get_images(images),
                max_tokens=self.input_tokens_limit,
                provider=None,
                model=specified_model if not (specified_model is None) else self.model
            )
        resp_text = response.choices[0].message.content
        
        self.messages.append((query, resp_text))
        return resp_text
    
    async def addMessageAsync(self, query: str, images: list[str] = [], noProvider: bool = False, specified_model: (str | g4f.Model | None) = None) -> str:
        all_messages: list[dict[str, str]] = [{
            "role": "system",
            "content": self.systemQuery
        }]

        for msg in self.messages:
            
            all_messages.append({
                "role": "user",
                "content": msg[0]
            })

            all_messages.append({
                "role": "assistant",
                "content": msg[1]
            })

        all_messages.append({
            "role": "user",
            "content": query
        })

        if not noProvider:
            response = await self.asy_client.chat.completions.create(
                messages=all_messages,
                images=self._get_images(images),
                ignore_working=True,
                model=specified_model if not (specified_model is None) else self.model,
                max_tokens=128000
            )
        else:
            response = await self.asy_client.chat.completions.create(
                messages=all_messages,
                images=self._get_images(images),
                provider=None,
                model=specified_model if not (specified_model is None) else self.model,
                max_tokens=128000
            )
        resp_text = response.choices[0].message.content
        
        self.messages.append((query, resp_text))
        return resp_text

    def fastRequest(self, query: str, images: list[str] = [], addToContext: bool = False, noProvider: bool = False, specified_model: (str | g4f.Model | None) = None) -> str:
        all_messages = [{
            "role": "system",
            "content": self.systemQuery
        }, {
            "role": "user",
            "content": query
        }]

        if not noProvider:
            response = self.client.chat.completions.create(
                all_messages,
                ignore_working=True,
                images=self._get_images(images),
                model=specified_model if not (specified_model is None) else self.model
            )
        else:
            response = self.client.chat.completions.create(
                messages=all_messages,
                images=self._get_images(images),
                provider=None,
                model=specified_model if not (specified_model is None) else self.model
            )
        resp_text = response.choices[0].message.content

        if addToContext:
            self.messages.append((query, resp_text))
        
        return resp_text
    
    def setSystemQuery(self, query: str):
        self.systemQuery = query
    
    def setModel(self, model: modelType):
        self.model = model

    def clearContext(self):
        self.messages = []

    def clearSystemQuery(self):
        self.systemQuery = ""
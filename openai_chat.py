import openai
import configparser
from time import sleep
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

config = configparser.ConfigParser()

try:
    config.read("C:\\openai_client.conf")
    api_token = config.get('openai', 'token')
except:
    print("Error: File does not exist ~/.config/openai_client.conf")
    print("Creating a new configuration file...\n")
    sleep(3)
    print("Finished, you can enter your token by editing ~/.config/openai_client.conf")
    config["openai"] = {
            "token": ""
        }
    with open("C:\\openai_client.conf", "w") as archivo_config:
        config.write(archivo_config)
    
    exit(1)

openai.api_key = api_token

class ChatSession:
    def __init__(self):
        self.history = []

    def remember(self, message):
        self.history.append(message)

    def respond(self, message):
        self.remember(message)
        model_engine = "text-davinci-002"
        prompt = " ".join(self.history)
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        self.remember(message)
        return message

session = ChatSession()

print("""
      Welcome to OpenAI Chat CLI !\n
Source code => github.com/Yisus7u7/openai-cli-client
Creator => Yisus7u7 
Windows Port => Ivancasg
Version => 1.0-stable
write \"exit()\" to exit chat
      """)

while True:
    message = input("You: ")

    if message == "exit()":
        print("Leaving...")
        exit(0)

    response = session.respond(message)
    
    # Resaltar la sintaxis de la respuesta usando Pygments
    highlighted_response = highlight(response, PythonLexer(), TerminalFormatter())

    # Imprimir la respuesta del modelo resaltada
    print("OpenAI: \n" + highlighted_response)

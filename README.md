openai-cli-client: a best OpenAI terminal client, writen in python

# Preview
![image](https://user-images.githubusercontent.com/64093255/218856689-2449f1b5-8724-4693-9bef-e2beaa915a59.png)


# Features
- Remember messages
- Interactive chat
- Syntactic highlighting (basic)

# Installation

In Linux OS:

Needs:

- python-openai
- python-pygments
- python-pyxdg

and run in the project dir:

```bash
sudo make install

```

In Android (Termux)

```bash
pkg install python clang build-essential python-pip git
```

```bash
pip install openai pygments pyxdg

```

```bash
git clone --depth 1 https://github.com/Yisus7u7/openai-cli-client; cd openai-cli-client

```

```bash

make PREFIX=$PREFIX OPTDIR=$PREFIX/opt all
```

In Windows:

```bash

pip install openai
pip install configparse
pip install pygments
```

# Run chat

use `openai-cli-client` command for open chat

# OpenAI Token

You need [OpenAI token](https://platform.openai.com/docs/introduction/tokens) for works

Add your token by editing `~/.config/openai_client.conf`
If the file does not exist, the first time you run the program will be created.

**example**

```bash
[openai]
token = YOU_TOKEN_HERE
```

# Contribute

- You can help by sending changes and improvements to the repository
- Share 
- Leave your star :3

Thank you for using!

# Discord Bot with Gemini Language Model API Integration

## Overview

Colisa bot allows users to generate text responses using Google's Gemini API and provides basic bot functionalities like `ping` and `help`. The bot is built using the `discord.py` library and leverages the `google.generativeai` module for AI-generated content.

## Table of Contents

-   [Installation](#installation)
-   [Configuration](#configuration)
-   [Features](#features)
    -   [Bot Connection](#bot-connection)
    -   [Gemini Commands](#gemini-commands)
    -   [General Commands](#general-commands)
-   [Code Walkthrough](#code-walkthrough)
    -   [Imports](#imports)
    -   [Gemini API Configuration](#gemini-api-configuration)
    -   [Bot Initialization](#bot-initialization)
    -   [Event Handlers](#event-handlers)
    -   [Commands](#commands)
-   [Running the Bot](#running-the-bot)
-   [Future Improvements](#future-improvements)

## Installation

Before running the bot, you need to install the required libraries. Use the following commands to install them:

`pip install discord.py
pip install google-generativeai` 

## Configuration

The bot uses environment keys for security. You need to set up the following keys:

1.  **Discord Bot Token** (`discordkey`): The token used to authenticate your bot with the Discord API.
2.  **Gemini API Key** (`geminikey`): The API key used to access Google's Gemini language model API.

Create a `keys.py` file and store these keys:


`discordkey = 'your_discord_bot_token'
geminikey = 'your_gemini_api_key'` 

## Features

### Bot Connection

The bot connects to Discord using `discord.py`. It has a custom activity status and listens for messages with specific commands. The bot is set up with the following configurations:

-   **Prefix**: Commands are triggered by the prefix `-`.
-   **Status**: The bot shows a custom activity that guides users to use the `--help` command.

### Gemini Commands

The bot can generate AI-based responses using Google's Gemini API. Users can input a prompt, and the bot will return a generated response.

### General Commands

The bot also includes general-purpose commands such as `ping` and `help`.

## Code Walkthrough

### Imports

The program imports necessary modules and libraries:

-   `discord` and `discord.ext.commands` for the bot functionalities.
-   `os` for environment variable handling.
-   `random` for random number generation.
-   `google.generativeai` for interacting with the Gemini language model API.
-   Custom imports: `keys` for storing the API keys, and `embeds` for custom embed messages.

### Gemini API Configuration

The bot configures the Gemini API using the provided API key from the `keys.py` file.

`genai.configure(api_key=geminikey)
model = genai.GenerativeModel('gemini-pro')` 

### Bot Initialization

The bot is initialized with specific intents, such as `message_content`, which allows the bot to read message content.

`intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', case_insensitive=True, activity=discord.CustomActivity(name="Use '--help' for help"), status=discord.Status.online, intents=intents)` 

The bot version is stored as a variable for easy reference.

### Event Handlers

#### `on_ready`

This event triggers when the bot successfully connects to Discord.

`@bot.event
async def on_ready():
    print(f'Entramos como {bot.user}')` 

### Commands

#### `gerar_resposta`

This function generates a response using the Gemini API but is not directly used in the bot commands.

`def gerar_resposta(messages):
    model.generate_content(messages)` 

#### `g`

This command triggers the Gemini API to generate a response based on the user's input prompt.


`@bot.command(name="-")
async def g(ctx, *, prompt: str):
    final = model.generate_content(prompt)
    await ctx.send(final.text)` 

#### `h`

This command sends an embedded help message to the user.



`@bot.command(name="-help")
async def h(ctx):
    await ctx.send(embed=helpe)` 

#### `teste`

This command responds with "Testing" to confirm that the bot is working.

`@bot.command()
async def teste(ctx='teste'):
    await ctx.send("Testing")` 

#### `ping`

This command responds with "pong!" to check the bot's responsiveness.


`@bot.command()
async def ping(ctx='ping'):
    await ctx.send("pong!")` 

### Running the Bot

To run the bot, simply execute the Python script:

`python main.py` 

Make sure that your `discordkey` and `geminikey` are properly configured in the `keys.py` file.

## Future Improvements

-   **Error Handling**: Implement error handling for API requests and bot commands to improve robustness.
-   **Command Enhancements**: Add more commands to increase the bot's functionality, such as fetching data from external APIs.
-   **User Management**: Add features like role-based command permissions for more control over who can use certain commands.
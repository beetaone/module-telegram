# Telegram

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Telegram                           |
| Version        | v1.0.0                                |
| DockerHub  | [weevenetwork/telegram](https://hub.docker.com/r/weevenetwork/telegram) |
| authors        | Jakub Grzelak                    |

***
## Table of Content

- [Telegram](#telegram)
  - [Description](#description)
  - [Creating Telegram Bot](#creating-telegram-bot)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
***

## Description

This modules sends messages and notifications to a selected Telegram chat. It requires setting up Telegram Bot. Additionally, we recommend running this module together with our [Message Composer](https://github.com/weeve-modules/message-composer) module that helps in writing alerts within weeve Edge Application.

## Creating Telegram Bot

Getting your Telegram Bot **TOKEN**:
1. Open your telegram app and search for BotFather. (A built-in Telegram bot that helps users create custom Telegram bots)
2. Type `/newbot` to create a new bot
3. Give your bot a name and a username
4. Copy your new Telegram bot’s token in the message received from BotFather

Getting your Telegram Bot **CHAT ID**:
1. Send your Telegram bot a message (any random message - if you don’t send your Telegram bot a message, your results in the next step might be empty)
2. Run this Python script to find your chat ID

```python
import requests
TOKEN = "YOUR TELEGRAM BOT TOKEN"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
```

3. Copy the chat ID from a JSON object received in the previous step.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Token    | TOKEN         | string   | Your Telegram bot token.            |
| Chat ID    | CHAT_ID         | string  | Your chat with bot ID.            |
| Message Label    | MESSAGE_LABEL         | string  | Label in incoming data that holds the message to be sent.            |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "alertMessage": "Device hf238hf23h7 (in Berlin) measured temperature 12 on 2022-09-25 15:35:17.31234"
}
```

## Output

Message send to the selected Telegram chat. Given the above input, message will be `Device hf238hf23h7 (in Berlin) measured temperature 12 on 2022-09-25 15:35:17.31234`.

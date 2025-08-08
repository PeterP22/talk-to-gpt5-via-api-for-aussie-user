# GPT-5 Chat Application 🤖

A simple Python application to interact with OpenAI's GPT-5 model via API. Features a personalized chat interface with Australian-friendly greetings and full support for GPT-5's advanced parameters.

## Features

- 💬 Interactive chat interface with GPT-5
- 🎯 Personalized greetings (customizable in code)
- 🎛️ Full control over GPT-5 parameters:
  - **Verbosity**: Control response detail (low/medium/high)
  - **Reasoning Effort**: Adjust reasoning depth (minimal/low/medium/high)
  - **Text Format**: Choose output format (text/json_object/json_schema)
- 📝 Conversation history maintained throughout session
- 🔄 Clear command to reset conversation
- ⚡ Simple and lightweight

## Prerequisites

- Python 3.7 or higher
- OpenAI API key with GPT-5 access
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/PeterP22/talk-to-gpt5-via-api-for-aussie-user.git
cd talk-to-gpt5-via-api-for-aussie-user
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
```

4. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

## Configuration

You can customize the following parameters in your `.env` file:

| Parameter | Options | Default | Description |
|-----------|---------|---------|-------------|
| `MODEL_NAME` | gpt-5, gpt-5-mini, gpt-5-nano | gpt-5 | The GPT-5 model variant to use |
| `MAX_TOKENS` | Integer | 2000 | Maximum tokens in response |
| `TEMPERATURE` | 0.0 - 2.0 | 0.7 | Response creativity/randomness |
| `VERBOSITY` | low, medium, high | medium | Response detail level |
| `TEXT_FORMAT` | text, json_object, json_schema | text | Output format |
| `REASONING_EFFORT` | minimal, low, medium, high | medium | Reasoning depth |

## Usage

Run the application:
```bash
python main.py
```

### Commands

- Type your message and press Enter to chat
- `clear` - Reset the conversation history
- `exit` - Quit the application
- `Ctrl+C` - Quick exit

### Example Session

```
$ python main.py
G'day Peter! Connected to gpt-5
I'm here to help you with any questions you have.
Type 'exit' to quit, 'clear' to reset conversation
--------------------------------------------------

Peter: What's the best way to learn Python?
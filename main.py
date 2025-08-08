import os
import sys
from typing import List
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class GPT5Chat:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key or api_key == 'your_openai_api_key_here':
            print("Error: Please set your OpenAI API key in the .env file")
            sys.exit(1)
        
        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv('MODEL_NAME', 'gpt-5')
        self.max_tokens = int(os.getenv('MAX_TOKENS', '2000'))
        self.temperature = float(os.getenv('TEMPERATURE', '0.7'))
        self.verbosity = os.getenv('VERBOSITY', 'medium')  # low, medium, high
        self.text_format = os.getenv('TEXT_FORMAT', 'text')  # text, json_object, json_schema
        self.reasoning_effort = os.getenv('REASONING_EFFORT', 'medium')  # minimal, low, medium, high
        self.conversation_history: List[str] = []
        
        self.system_prompt = """You are a helpful AI assistant. The user's name is Peter. 
        Always address him by name when appropriate. You're here to assist Peter with 
        any questions or tasks he has. Be friendly, knowledgeable, and helpful."""
        
    def add_message(self, content: str):
        self.conversation_history.append(content)
    
    def get_response(self, user_input: str) -> str:
        # Build the full prompt with conversation history
        full_prompt = self.system_prompt + "\n\n"
        for msg in self.conversation_history:
            full_prompt += msg + "\n"
        full_prompt += f"Peter: {user_input}\nAssistant:"
        
        try:
            # GPT-5 uses the new responses endpoint
            response = self.client.responses.create(
                model=self.model,
                input=full_prompt,
                text={
                    "verbosity": self.verbosity,
                    "format": self.text_format
                },
                reasoning_effort=self.reasoning_effort
            )
            
            assistant_message = response.choices[0].text
            self.add_message(f"Peter: {user_input}")
            self.add_message(f"Assistant: {assistant_message}")
            return assistant_message
            
        except Exception as e:
            error_msg = str(e)
            
            # Handle quota errors
            if "insufficient_quota" in error_msg or "429" in error_msg:
                return ("It looks like there's a quota issue with your OpenAI account. "
                       "Please check:\n"
                       "1. Your billing is set up at https://platform.openai.com/account/billing\n"
                       "2. You have credits available\n"
                       "3. Your API key is valid and active")
            
            return f"Error: {error_msg}"
    
    def clear_history(self):
        self.conversation_history = []
        print("Conversation history cleared.")
    
    def run(self):
        print(f"G'day Peter! Connected to {self.model}")
        print("I'm here to help you with any questions you have.")
        print("Type 'exit' to quit, 'clear' to reset conversation")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\nPeter: ").strip()
                
                if user_input.lower() == 'exit':
                    print("See you later, Peter!")
                    break
                
                if user_input.lower() == 'clear':
                    self.clear_history()
                    continue
                
                if not user_input:
                    continue
                
                print(f"\nAssistant: ", end="")
                response = self.get_response(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\nSee you later, Peter!")
                break
            except Exception as e:
                print(f"\nError: {str(e)}")

if __name__ == "__main__":
    chat = GPT5Chat()
    chat.run()
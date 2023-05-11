
import logging
import os
import sys
from dotenv import load_dotenv
from OctoAiCloudLLM import OctoAiCloudLLM
from langchain import LLMChain, PromptTemplate
from llama_index import LLMPredictor

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory
os.chdir(current_dir)

# Set up logging configuration
logging.basicConfig(level=logging.CRITICAL)

# Load environment variables
load_dotenv()

# This code is used to interactively ask questions to the language model.
# It uses the OctoAI cloud language model to generate responses.

def handle_exit():
    """Print a goodbye message and exit the program."""
    print("\nGoodbye!\n")
    sys.exit(1)

def ask():
    """Interactively ask questions to the language model."""
    print("Loading...")
    
    # Load necessary values from environment
    endpoint_url = os.getenv("ENDPOINT_URL")

    # Set up the language model and predictor
    llm = OctoAiCloudLLM(endpoint_url=endpoint_url)
    llm_predictor = LLMPredictor(llm=llm)

    # Define a prompt template
    template = "{question}"
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Set up the language model chain
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    # Clear the screen
    os.system("clear")

    print("Ready! Let's start the conversation")
    print("Press Ctrl+C to exit\n")

    # Provide an example prompt and response
    example_question = "Who is Leonardo Davinci?"
    print("Example \n\nPrompt:", example_question, "\n\nResponse:", llm_chain.run(example_question))
        
    try:
        while True:
            # Collect user's prompt
            user_prompt = input("\nPrompt: ")
            if user_prompt.lower() == "exit":
                handle_exit()

            # Generate and print the response
            response = llm_chain.run(user_prompt)
            response = str(response).lstrip("\n")
            print("Response: " + response)
    except KeyboardInterrupt:
        handle_exit()

if __name__ == "__main__":
    ask()

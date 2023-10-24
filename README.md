# LLM endpoint chat

Load a PDF file and ask questions via llama_index, LangChain and a LLM endpoint hosted on OctoAI

## Instructions

- Install the requirements

```bash
pip install -r requirements.txt -U
```
### Environment setup

To run our example app, there are four simple steps to take:

- Clone the Llama-2-7b demo template to your OctoAI account by visiting <https://octoai.cloud/models/llama-2-7b-chat-demo> then clicking "Deploy Endpoint."
   - If you want to use a different LLM model you can select another demo [template](https://octoai.cloud/templates). You can also containerize the model and make a custom OctoAI endpoint yourself, by following [Build a Container from Python]<https://docs.octoai.cloud/docs/create-custom-endpoints-from-python-code> and [Create a Custom Endpoint from a Container]<https://docs.octoai.cloud/docs/create-custom-endpoints-from-a-container>
-  Paste your Endpoint URL in a file called `.env` in the root directory of the project.

```bash
ENDPOINT_URL=<your Endpoint URL here>
```

- Get an API Token from [your OctoAI account page](https://octoai.cloud/settings).
- Paste your API key in a file called `.env` in the root directory of the project.

```bash
OCTOAI_API_TOKEN=<your key here>
```

- Run `chat_main.py` script to chat with the LLM hosted endpoint.
```bash
python3 chat_main.py
```

or 
- Select a file from the menu or replace the default file `file.pdf` with the PDF you want to use.
- Run `pdf_qa_main.py` script to ask questions about your pdf file via llama_index, LangChain and the hosted endpoint.
```
python3 pdf_qa_main.py
```
- Ask any questions about the content of the PDF. 
<br>


For detailed setup steps, please see https://docs.octoai.cloud/docs/setup-steps-for-the-qa-app
<br>
<br>


### Credits:
This work was inspired by the [chatPDF repo](https://github.com/gabacode/chatPDF)

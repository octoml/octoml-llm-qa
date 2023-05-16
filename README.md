# LLM endpoint chat

Load a PDF file and ask questions via llama_index, LangChain and a DollyV2 endpoint hosted on the OctoAI.Cloud

## Instructions

- Install the requirements

```bash
pip install -r requirements.txt -U
```

- Clone the dolly-demo template by visiting <https://octoai.cloud/templates/dolly-demo> then clicking "Clone Template"

- Paste your Endpoint URL in a file called `.env` in the root directory of the project.

```bash
Endpoint_URL=<your Endpoint URL here>
```

- Get an OctoAI Cloud API Token from [Octoai.cloud](https://octoai.cloud/settings).

- Paste your API key in a file called `.env` in the root directory of the project.

```bash
OCTOAI_API_TOKEN=<your key here>
```

- Select a file from the menu or replace the default file `file.pdf` with the PDF you want to use.

- Run `chat_main.py` script to chat with the Dolly hosted endpoint.
- Run `pdf_qa_main.py` script to ask questions about your pdf file via llama_index, LangChain and the Dolly hosted endpoint on OctoAI cloud.

```bash
python3 chat_main.py
```
or 
```
python3 pdf_qa_main.py
```

- Ask any questions about the content of the PDF. 
<br>
<br>


### Credits:
This work was inspired by the [chatPDF repo](https://github.com/gabacode/chatPDF)

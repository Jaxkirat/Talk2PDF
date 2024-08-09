# Talk2PDF

Talk2PDF is an interactive chatbot application that allows users to upload PDF files and ask questions about their content. It uses a Retrieval Augmented Generation (RAG) model to extract and provide relevant information from the uploaded PDFs.

## Demo

Watch the demo video to see how Talk2PDF works in action:


https://github.com/Jaxkirat/Talk2PDF/assets/77850299/336dac3b-32ad-4136-9113-4d1fac44d8b1


## Features

- Upload PDF files and extract their text content.
- Ask questions about the uploaded PDF and get accurate answers.
- Utilizes OpenAI's language model for generating responses.
- Stores and loads document embeddings to enhance performance.

## Technologies Used

- [Streamlit](https://streamlit.io/) for the web application interface.
- [LangChain](https://python.langchain.com/) for text processing and embedding.
- [OpenAI](https://platform.openai.com/docs/models) for language model integration.
- [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Talk2PDF.git
    cd Talk2PDF
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the project root directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run main.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Use the sidebar to learn more about the application.

4. Upload a PDF file and start asking questions about its content.

## Project Structure

- `main.py`: The main application script.
- `requirements.txt`: List of dependencies.
- `.env`: Environment variables file (not included in the repository, create it manually).

## Disclaimer

Please note that software dependencies listed in `requirements.txt` can become outdated over time. It is advisable to periodically review and update the dependencies to ensure compatibility and security.

## Future Improvements

- Improve the user interface to be more dynamic and futuristic.
- Add support for multiple languages.
- Enhance the error handling and feedback mechanisms.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [OpenAI](https://platform.openai.com/docs/models)
- [FAISS](https://github.com/facebookresearch/faiss)

---

Created by [Jaskirat Singh](https://Github.com/Jaxkirat)

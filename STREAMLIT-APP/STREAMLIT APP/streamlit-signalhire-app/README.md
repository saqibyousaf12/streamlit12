# Streamlit SignalHire App

This project is a Streamlit web application that utilizes the SignalHire Person API to retrieve person data, display the results on the frontend, and store the data in the backend.

## Project Structure

```
streamlit-signalhire-app
├── src
│   ├── app.py
│   ├── api
│   │   └── signalhire_client.py
│   ├── backend
│   │   └── storage.py
│   └── utils
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd streamlit-signalhire-app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up your SignalHire API key:**
   Make sure to have your SignalHire API key ready. You will need to provide it when prompted in the application.

## Usage Instructions

1. **Run the Streamlit application:**
   ```
   streamlit run src/app.py
   ```

2. **Access the application:**
   Open your web browser and go to `http://localhost:8501`.

3. **Search for candidates:**
   Enter the required information in the input fields and submit the form to retrieve candidate data from the SignalHire API.

4. **View results:**
   The results will be displayed on the frontend, and the retrieved data will be stored in the backend for future reference.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
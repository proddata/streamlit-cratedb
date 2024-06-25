# Streamlit with CrateDB Cloud

This Streamlit app allows you to execute SQL queries against a CrateDB Cloud database and display the results interactively.


## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/proddata/streamlit-cratedb-example.git
    cd streamlit-cratedb-example
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your secrets. Create a `secrets.toml` file in the `.streamlit` directory:

    ```toml
    [secrets]
    db_username = "crate"
    db_password = ""
    db_host = "localhost"
    db_port = "4200"
    ```

## Running the App

1. Start the Streamlit app:

    ```sh
    streamlit run main.py
    ```

2. Open your web browser and go to `http://localhost:8501` to interact with the app.

## Usage

- Enter your SQL query in the provided editor.
- Click the "Execute Query" button to run the query.
- View the results in the table displayed below the editor.

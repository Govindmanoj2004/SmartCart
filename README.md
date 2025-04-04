# Django Project

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <project_directory>
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Project

1. Apply database migrations:
   ```sh
   python manage.py migrate
   ```

2. Start the development server:
   ```sh
   python manage.py runserver
   ```

3. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```


## License
This project is licensed under the MIT License.


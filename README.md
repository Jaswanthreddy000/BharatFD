# FAQ Management System

This is a Django-based FAQ Management System that supports multi-language translations, a REST API, and a user-friendly admin interface. It also includes a simple frontend for adding and viewing FAQs.

## Features
- **Multi-language Support**: FAQs can be translated into multiple languages (English, Hindi, Bengali, Telugu).
- **REST API**: Fetch FAQs in different languages using the API.
- **WYSIWYG Editor**: Use CKEditor for formatting FAQ answers.
- **Caching**: Redis is used for caching translations to improve performance.
- **Docker Support**: Easily deploy the application using Docker.
- **Admin Panel**: Manage FAQs through the Django admin interface.

## Table of Contents
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Usage](#api-usage)
- [Docker Deployment](#docker-deployment)
- [Contributing](#contributing)
- [License](#license)
- [Submission Checklist](#submission-checklist)

## Submission Checklist

# Submission Checklist

### 1. **Model Design**
- [✔] Implemented a Django model to store FAQs, including fields for `question`, `answer`, and language-specific translations (e.g., `question_hi`, `question_bn`, etc.).
- [✔] Created a model method to dynamically retrieve translated text based on the selected language.

### 2. **WYSIWYG Editor Integration**
- [✔] Integrated `django-ckeditor` to allow users to format FAQ answers using a rich text editor (WYSIWYG).
- [✔] Ensured that the WYSIWYG editor supports multilingual content by enabling translations for different language fields.

### 3. **API Development**
- [✔] Developed a REST API to manage FAQs, which supports fetching FAQs in different languages via the `?lang=` query parameter.
- [✔] Optimized the API for faster responses by implementing pre-translation caching.

### 4. **Caching Mechanism**
- [✔] Implemented a caching mechanism using Redis to store translations, improving the performance and reducing the number of calls to external translation services.

### 5. **Multi-language Translation Support**
- [✔] Utilized the Google Translate API (or `googletrans` package) for automating translations during FAQ object creation.
- [✔] Added a fallback mechanism to default to English if translations for a specific language are unavailable.

### 6. **Admin Panel**
- [✔] Registered the FAQ model in the Django admin interface to allow easy management of FAQs.
- [✔] Ensured the admin interface is user-friendly, providing easy ways to add and edit FAQ entries.

### 7. **Unit Tests & Code Quality**
- [✔] Wrote unit tests for FAQ model methods and API responses using `pytest`.
- [✔] Ensured the code follows best practices by adhering to PEP8 guidelines for Python and using `flake8` for linting.

### 8. **Documentation**
- [✔] Provided detailed documentation in the README file, including:
  - Clear installation steps
  - Example API usage for fetching FAQs in different languages
  - Contribution guidelines
- [✔] Ensured the README is well-structured and easy to follow for future developers or contributors.

### 9. **Git & Version Control**
- [✔] Used Git for version control with clear and atomic commits.
- [✔] Followed conventional commit messages (`feat`, `fix`, `docs`) for better clarity and understanding of changes.

### 10. **Deployment & Docker Support (Bonus)**
- [✔] Created a `Dockerfile` and `docker-compose.yml` to enable easy deployment of the application in containerized environments.
- [✔] Provided instructions for deploying the application to platforms like Heroku or AWS (optional).


## Installation

### Prerequisites
- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- Redis (for caching)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/faq_project.git
    cd faq_project
    ```

2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory:
    ```env
    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=sqlite:///db.sqlite3
    REDIS_URL=redis://127.0.0.1:6379/0
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

7. Collect static files:
    ```bash
    python manage.py collectstatic
    ```

## Running the Application

### Development Server
1. Start the development server:
    ```bash
    python manage.py runserver
    ```

2. Access the application at:
    ```
    http://localhost:8000/
    ```

3. Access the admin panel at:
    ```
    http://localhost:8000/admin/
    ```

### Docker
1. Build and start the containers:
    ```bash
    docker-compose up --build
    ```

2. Access the application at:
    ```
    http://localhost:8000/
    ```

3. To stop the containers:
    ```bash
    docker-compose down
    ```

## API Usage

### Endpoints

- **Fetch FAQs in English (default):**
    ```bash
    curl http://localhost:8000/api/faqs/
    ```

    **Example Response (English):**
    ```json
    [
        {
            "id": 1,
            "question": "What is Django?",
            "answer": "Django is a high-level Python web framework."
        },
        {
            "id": 2,
            "question": "How to install Django?",
            "answer": "You can install Django using pip: pip install django."
        }
    ]
    ```

- **Fetch FAQs in Hindi:**
    ```bash
    curl http://localhost:8000/api/faqs/?lang=hi
    ```

    **Example Response (Hindi):**
    ```json
    [
        {
            "id": 1,
            "question": "Django क्या है?",
            "answer": "Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।"
        },
        {
            "id": 2,
            "question": "Django कैसे इंस्टॉल करें?",
            "answer": "आप pip का उपयोग करके Django इंस्टॉल कर सकते हैं: pip install django।"
        }
    ]
    ```

- **Fetch FAQs in Bengali:**
    ```bash
    curl http://localhost:8000/api/faqs/?lang=bn
    ```

    **Example Response (Bengali):**
    ```json
    [
        {
            "id": 1,
            "question": "Django কী?",
            "answer": "Django একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক।"
        },
        {
            "id": 2,
            "question": "Django কীভাবে ইনস্টল করবেন?",
            "answer": "আপনি pip ব্যবহার করে Django ইনস্টল করতে পারেন: pip install django।"
        }
    ]
    ```

- **Fetch FAQs in Telugu:**
    ```bash
    curl http://localhost:8000/api/faqs/?lang=te
    ```

    **Example Response (Telugu):**
    ```json
    [
        {
            "id": 1,
            "question": "Django ఏమిటి?",
            "answer": "Django ఒక అధిక స్థాయి Python వెబ్ ఫ్రేమ్‌వర్క్."
        },
        {
            "id": 2,
            "question": "Django ను ఎలా ఇన్స్టాల్ చేయాలి?",
            "answer": "మీరు pip ను ఉపయోగించి Django ని ఇన్స్టాల్ చేయవచ్చు: pip install django."
        }
    ]
    ```

---
## Docker Deployment

### Prerequisites
- **Docker**
- **Docker Compose**

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/faq_project.git
    cd faq_project
    ```

2. Build and start the containers:
    ```bash
    docker-compose up --build
    ```

3. Apply migrations:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. Create a superuser:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5. Access the application at:
    ```
    http://localhost:8000/
    ```

## Contributing

Contributions are welcome! Follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```

3. **Commit your changes**:
    ```bash
    git commit -m "Add your feature"
    ```

4. **Push to the branch**:
    ```bash
    git push origin feature/your-feature-name
    ```

5. **Open a pull request**.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [CKEditor](https://ckeditor.com/)
- [Redis](https://redis.io/)

## Contact

For questions or feedback, feel free to reach out:

- **Name**: Theeyagura Jaswanth Reddy
- **Email**: jaswanth6365@gmail.com


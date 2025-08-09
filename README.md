# Django Tweet Posting App

## Overview
This Django application allows users to post tweets with optional images. It features a content filter that prohibits certain words (`shit`, `fuck`, `bobo`) in tweets.

## Features
- Post tweets up to 280 characters
- Upload an image with each tweet
- Content filtering to block inappropriate words
- Simple success confirmation page

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (`venv` recommended)

## Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
````

### 2. Create and activate a virtual environment

* On Linux/macOS:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* On Windows:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the media directory for uploaded images

```bash
mkdir media
```

### 5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Access the app

Open your browser and navigate to:

```
http://127.0.0.1:8000/
```

---

## Usage

* Fill in the tweet content (max 280 characters).
* Optionally upload an image.
* Click **Tweet** to post.
* If your tweet contains banned words (`shit`, `fuck`, or `bobo`), you will receive an error message.
* After a successful post, you will see a confirmation page.

---

## Notes

* Uploaded images are stored in the `media/` directory.
* The `media/` folder and the `db.sqlite3` database file are excluded from this repository.
* The project uses SQLite by default for simplicity.
* This project is intended for development/testing purposes.

---

## Files Excluded from Repository

* `venv/` (virtual environment)
* `db.sqlite3` (database file)
* `media/` (uploaded media files)

---

## Requirements

* All Python dependencies are listed in `requirements.txt`.
* To regenerate after adding dependencies, run:

  ```bash
  pip freeze > requirements.txt
  ```

---

## License

This project is for educational purposes.

```

Just replace `<your-repo-url>` and `<your-repo-folder>` with your actual repository URL and folder name!
```

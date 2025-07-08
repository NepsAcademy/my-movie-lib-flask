# My Movie Library (Dynamic Version) 🎬

Welcome to the dynamic version of **My Movie Library**\! This is the official example project for the [**Web Development with Python and Flask Course at Neps Academy**]([https://neps.academy](https://neps.academy/br/course/3093)).

The goal of this project is to evolve a static HTML/CSS website into a fully functional dynamic web application. We use Python and the Flask microframework to handle backend logic, render templates dynamically, process forms, and persist data in a `.csv` file.

This repository serves as a guide and a completed example for students of the course.

## 🚀 Features

- **Dynamic Movie Listing:** The home page reads from a `.csv` file and dynamically generates the movie card grid.
- **Dynamic Detail Pages:** A single template is used to generate a unique detail page for any movie, using dynamic routes (e.g., `/movie/1`).
- **Add New Reviews:** A fully functional form that accepts user input via `POST` requests.
- **Data Persistence:** New movie reviews are permanently saved to the `movies.csv` file.

## 🛠️ Technologies & Concepts

This project was built using a combination of frontend and backend technologies:

- **Python:** The core backend programming language.
- **Flask:** A lightweight web framework used to build the server, handle routes, and render templates.
- **Jinja:** The template engine used by Flask to dynamically generate HTML.
- **HTML5:** For structuring the content with a focus on semantics.
- **CSS3:** For all styling, layout (Flexbox), and responsiveness (Media Queries).

## 📁 Project Structure

The project follows the standard Flask application structure:

```
my-movie-lib-flask/
│
├── app.py                    # The main Flask application file
├── movies.csv                # Our simple "database" file
│
├── templates/                # Folder for all HTML templates
│   ├── layout.html           # The base layout for all pages
│   ├── index.html
│   ├── add-review.html
│   └── movie-details.html
│
└── static/                   # Folder for static assets
    ├── css/
    │   └── style.css
    └── assets/
        └── images/
            └── mlib-icon.svg
```

## 🖥️ How to Run Locally

To run this project on your local machine, you need to have **Python** and **pip** installed. Then, follow these steps:

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/NepsAcademy/my-movie-lib-flask.git
    ```

2.  **Navigate to the project directory:**

    ```sh
    cd my-movie-lib-flask
    ```

3.  **(Recommended) Create and activate a virtual environment:**

    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install the necessary dependencies:**

    ```sh
    pip install Flask
    ```

5.  **Run the Flask application:**

    ```sh
    python app.py
    ```

6.  **Open your web browser** and go to the following address:
    `http://127.0.0.1:5000`

And you're all set\! You can now interact with your local version of the web application.

## 🙏 Acknowledgments

This project is part of the educational curriculum at **[Neps Academy](https://neps.academy)**. All design assets and project specifications were provided by Neps Academy to create a complete, hands-on learning experience.

from setuptools import setup

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "BOOKS-Recommender-System-using-Machine-Learning"
AUTHOR_USER_NAME = "VarunSingh"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit','numpy']

setup(
    name = SRC_REPO,
    version = "0.0.1",
    author = AUTHOR_USER_NAME,
    decription = "A small package for BOOK Recommender System",
    long_description = long_description, long_description_content_type = "text/markdown",
    url = f"https://github.com/VarunSingh31/BookRecommendationSystem.git",
    author_email = "varunsingh3125@gmail.com",
    package = [SRC_REPO],
    python_requires = ">=3.7",
    install_requires = LIST_OF_REQUIREMENTS
)
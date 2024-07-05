#!/usr/bin/env python3
""" A script for basic flask integration"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the application.
        Attributes:
        Languages (list): List of supported languages.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """_summary_

    Returns:
        _type_: _description_
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello():
    """This function returns the rendered template for the index.html page.

    Returns:
        The rendered template for the index.html page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()

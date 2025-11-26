# Bino Dictionary API — External API Connector (Flask)

A simple and production-ready External API Connector built using Flask, integrating with the open Dictionary API.
This project fulfills the requirement of creating an API that connects to an external service, processes the response, and returns clean JSON.

# Live URL:
https://bino-dictionary-api.onrender.com

# GitHub Repository:
https://github.com/kotanarayanareddy/bino-dictionary-api

# Project Overview

This API allows users to search for the meaning of any English word.
It fetches results from the DictionaryAPI.dev external API, processes the data, and exposes a simple and clean response through /search.

This demonstrates:

External API consumption

Flask backend creation

JSON response formatting

Error handling

Deployment on Render

Production WSGI server (Gunicorn)

# Features

/ — Health check endpoint

/search?word=hello — Search word meaning

Clean structured JSON response

Error handling for missing or invalid words

Lightweight and fast

Fully deployed and publicly accessible

Tech Stack

Python 3

Flask

Requests

Gunicorn

Render (Hosting)

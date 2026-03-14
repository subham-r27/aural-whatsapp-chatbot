Aural Essence WhatsApp Chatbot

A simple WhatsApp chatbot for lead capture and automated responses built using FastAPI and WhatsApp Cloud API.

This chatbot automatically replies to user messages with predefined responses and stores the user's phone number and message in a database for lead tracking.

Overview

The chatbot is designed for Aural Essence, a B2B supplier of pure hydrosols and essential oils used by skincare, aromatherapy, and wellness brands.

When a user sends a message on WhatsApp:

The message is received through the WhatsApp Cloud API webhook

The backend processes the message

The user's phone number and message are stored in a database

The chatbot replies with predefined responses such as products, samples, pricing, etc.

Features

Automated WhatsApp responses

Lead capture (phone number + message)

Keyword-based chatbot responses

Lightweight FastAPI backend

SQLite database for storing leads

Simple and easy to extend
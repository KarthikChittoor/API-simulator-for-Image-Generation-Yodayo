# API Simulator - Use third party APIs as your own - Image Generation API is chosen as a sample

## Overview

This project demonstrates how to use third-party APIs as our own by automating browser interactions. With growing security measures in modern browsers—such as session tokens, X-CSRF tokens, and cookies—it has become increasingly difficult to use third-party APIs directly. This solution automates the interaction with an existing web service, allowing us to simulate its API for image generation.

The example here uses **Yodayo**, a real image generation service, to simulate API calls for generating images based on user-provided prompts. While this method is slow, it serves as a proof of concept and opens the path to more possibilities for AI-controlled machines. Future work will involve building an AI system (via a large language model) that autonomously controls a computer, effectively mimicking human actions.

## Output
**https://drive.google.com/file/d/15FGBYJuyCrTKFjzSeAt_QlAejGa2f5Ym/view?usp=drive_link**

### Key Features:
- Automates the process of navigating a website, inputting a prompt, and generating an image.
- Uses browser automation tools like **PyAutoGUI** to simulate keyboard and mouse actions.
- Simulates API behavior by scraping and interacting with web-based services directly.
- Returns the generated image URL to the user.

## How The Chosen Image Generator Works

Yodayo is an image generation service that creates images based on text prompts. In this project, instead of using their official API, we simulate the process by automating the interaction with their web interface. The automation includes:
1. Opening the Yodayo website.
2. Typing in a user-defined prompt (e.g., "samurai, black dress, katana, red eyes, black hair, white background").
3. Clicking the necessary buttons to trigger the image generation (like selecting the model,spells,effects,etc.).
4. Scraping the resulting image URL from the browser.

## Installation

For more details on setting up and running the project, please refer to the **how-to-run.txt** file.

## How Yodayo is Simulated

While Yodayo provides an API for image generation, security measures in modern browsers (such as session handling and cookies) make it difficult to use third-party APIs directly. This project simulates the API by automating browser actions using **PyAutoGUI** and **Pygetwindow** to interact with the Yodayo website. We simulate typing the prompt, clicking the necessary buttons, and copying the generated image URL to return to the user.

This approach is slow, but it opens the door to more possibilities for future work involving AI-controlled systems.

## Future Work

In the future, we aim to:
- Implement a system where a **Large Language Model (LLM)** can autonomously control computer actions, mimicking human behavior.
- Explore ways to speed up this automation process and make it more reliable.
- Develop a fully automated API interface by controlling a browser through AI instead of scripting specific actions.

## Important Notes
- **Yodayo** is an existing service for image generation.
- The code here simulates the use of their API by automating web browser interactions.
- The approach used in this project can be slow, but it offers a foundation for more advanced AI-controlled systems.



import subprocess
import pyautogui
import pyperclip
import time
import pygetwindow as gw
from flask import Flask, request, jsonify

app = Flask(__name__)

def setup_chrome(): 
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    # Check if Chrome is already running
    try:
        chrome_window = gw.getWindowsWithTitle("Google Chrome")[0]  # Get the first Chrome window
        
        # If Chrome is running, make it fullscreen and then move it to the left half of the screen
        chrome_window.activate()  # Bring Chrome to the front
        chrome_window.maximize()  # Make it fullscreen
        time.sleep(1)  # Wait for Chrome to be maximized
        pyautogui.hotkey('win', 'left')  # Move the Chrome window to the left half
        print("Chrome was already running. Brought it to the front and positioned it.")
    except IndexError:
        # If Chrome is not running, open it
        subprocess.Popen([chrome_path])  # Launch Chrome
        time.sleep(3)  # Wait for Chrome to open
        pyautogui.hotkey('win', 'left')  # Move Chrome to the left half of the screen
        print("Chrome was not running. Launched and positioned it to the left half.")

def generate_image(prompt):
    print("received prompt:", prompt)
    default_prompt = "(masterpiece), best quality, expressive eyes, perfect face"
    
    # Navigate and interact with the browser
    pyautogui.click(335, 75)
    pyautogui.typewrite("https://yodayo.com/text-to-image")
    time.sleep(1)  # Wait for browser to read URL
    pyautogui.typewrite(["enter"])
    
    time.sleep(10)  # Wait for the page to load
    
    # Enter the prompt and generate the image
    pyautogui.click(633, 560)
    pyautogui.typewrite(['backspace'] * len(default_prompt))  # Delete old text
    pyautogui.typewrite(f"{prompt}")  # Append the prompt
    time.sleep(7)    # Wait for the prompt to be updated
    pyautogui.click(484, 965)
    
    time.sleep(15)  # Wait for the image to generate
    
    # Copy the generated image's link
    pyautogui.click(480, 613, button='right')
    pyautogui.click(609, 747)
    
    # Get the generated image's link from the clipboard
    time.sleep(2)  # Wait to ensure clipboard is updated
    copied_text = pyperclip.paste()
    return copied_text

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    try:
        # Generate the image and get the URL
        image_url = generate_image(prompt)
        return jsonify({"image_url": image_url}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    setup_chrome()  # Make sure Chrome is launched and positioned correctly
    app.run(host='0.0.0.0', port=5000)

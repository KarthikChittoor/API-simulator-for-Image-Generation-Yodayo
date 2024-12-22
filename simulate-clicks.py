import pyautogui
import time
import pyperclip

def generate_image(prompt):
    # Navigate and interact with the browser
    pyautogui.click(335, 75)
    pyautogui.typewrite("https://yodayo.com/text-to-image")
    time.sleep(1)  # Wait for browser to read URL
    pyautogui.typewrite(["enter"])
    
    time.sleep(5)  # Wait for the page to load
    
    # Enter the prompt and generate the image
    pyautogui.click(633, 560)
    pyautogui.typewrite(f",{prompt}") 
    pyautogui.click(484, 965)
    
    time.sleep(15)  # Wait for the image to generate
    
    # Copy the generated image's link
    pyautogui.click(480, 613, button='right')
    pyautogui.click(609, 747)
    
    # Get the generated image's link from the clipboard
    time.sleep(1)  # Wait to ensure clipboard is updated
    copied_text = pyperclip.paste()
    return copied_text

# Interactive loop
while True:
    user_input = input("Enter your prompt (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    
    try:
        image_link = generate_image(user_input)
        print("Generated Image Link:", image_link)
    except Exception as e:
        print(f"An error occurred: {e}")

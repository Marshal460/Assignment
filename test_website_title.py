from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up options for Brave Browser
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Update this path to your Brave browser location

options = Options()
options.binary_location = brave_path

# Set up the WebDriver using WebDriver Manager for ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open the browser and navigate to the website
    driver.get("https://www.example.com")
    
    # Get the title of the page
    title = driver.title
    
    # Verify the title
    assert title == "Example Domain", f"Title mismatch: Expected 'Example Domain', got '{title}'"
    
    print("Test Passed: The title is correct.")
except AssertionError as e:
    print(f"Test Failed: {e}")
finally:
    # Close the browser
    driver.quit()

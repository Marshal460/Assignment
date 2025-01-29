from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  

options = Options()
options.binary_location = brave_path


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
   
    driver.get("https://www.example.com")
    
    
    title = driver.title
    
    
    assert title == "Example Domain", f"Title mismatch: Expected 'Example Domain', got '{title}'"
    
    print("Test Passed: The title is correct.")
except AssertionError as e:
    print(f"Test Failed: {e}")
finally:
    # Close the browser
    driver.quit()

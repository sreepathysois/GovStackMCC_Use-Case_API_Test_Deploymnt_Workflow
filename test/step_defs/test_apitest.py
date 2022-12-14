import pytest
import json 
import requests
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#options = Options()

#options.headless = True

#driver = webdriver.Chrome("/usr/bin/chromedriver", options=chrome_options)


#driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)



#driver = webdriver.Chrome()


 
# Constants
 
#API_HOME = 'http://172.16.51.57:8000/home/'
#API_HOME = 'http://localhost:8000/home/'
API_HOME = 'http://3.91.148.253:8000/home/'
 
# Scenarios
 
scenarios('../features/apitest.feature')
 
# Fixtures
 
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    #driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
    #driver.get("https://google.com/") 
    #driver = webdriver.Firefox()
    #driver.get("http://www.qxf2.com")

    #b = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver 
    driver.quit()

@given('the API URL home page is queried', target_fixture='ddg_response')
def ddg_response():
    params = {'format': 'json'}
    response = requests.get(API_HOME)
    return response


# Then Steps



@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code


@when(parsers.parse('the response contains welcome json data'))
def ddg_response_contents():
    # A more comprehensive test would check 'RelatedTopics' for matching phrases
    response = requests.get(API_HOME)  
    print(response)
    json_data = response.json()
    assert json_data['EligibalityCriteria'][1] == 'IncomeCertificate' 


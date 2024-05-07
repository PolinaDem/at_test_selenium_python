# Autotests

## Table of Contents

- Autotests
  - Table of Contents
  - Description
  - Projects
  - Installation instructions
  - Contact information
    
## Description
Autotests that check web elements and processes in the Chrome browser. 
- Language used: Python, 
- Library used: Selenium, 
- Framework: Pytest.
- Source of portals for frontend: https://the-internet.herokuapp.com/,
- Source of portals for backend: http://restful-booker.herokuapp.com/
  ⚠️ The API comes pre-loaded with 10 records for work with and resets itself every 10 minutes back to that default state.

## Projects

| Project | File name    | Description    |
| :-----: | :---: | :---: |
| FE |    |     |
| [Basic authentication](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_basic_authentication.py) | test_basic_authentication | Authorization via web request |
| [Broken images](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_broken_images.py) | test_broken_images | Find broken images and return their count |
| [Challenging DOM](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_Challenging_DOM.py) | test_Challenging_DOM | Find the best locators in a table with no helpful locators, and a canvas element |
| [Checkbox](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_checkbox.py) | test_checkbox | Check checkbox |
| [Click button](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_click_button.py) | test_click_button | Check click button |
| [Digest authentication](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_digest_authentication.py) | test_digest_authentication | - |
| [Disappearing elements](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_disappearing_elements.py) | test_disappearing_elements | Elements on a page change by disappearing/reappearing on each page load |
| [Dropdown list](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_dropdown_list.py) | test_dropdown_list | Check dropdown |
| [Dynamic content](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_dynamic_content.py) | test_dynamic_content | Content updated after refresh |
| [Dynamic controls](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_dynamic_controls.py) | test_dynamic_controls | Elements are changed asynchronously |
| [Dynamically loaded page elements](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_dynamically_loaded_page_elements.py) | test_dynamically_loaded_page_elements | Adding explicit and implicit expectation of elements  |
| [Exit intent](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_exit_intent.py) | test_exit_intent | Mouse out of the viewport pane and see a modal window appear |
| [Entry ad](https://github.com/PolinaDem/at_test_selenium_python/blob/main/entry_ad.py) | entry_ad | Pop-up displays an ad on page load |
| [File download](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_file_download.py) | test_file_download | - |
| [File upload](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_file_upload.py) | test_file_upload | Upload by button and by modal window on the page |
| [Floating menu](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_floating_menu.py)   |  test_floating_menu  |  The menu moves along with the page scroll. Parameterization is implemented   |
| [Login page](https://github.com/PolinaDem/at_test_selenium_python/blob/main/test_login_page.py)   | test_login_page   |  Login into the secure area   |
|    |    |     |
| BE |    |     |
| [Create token](https://github.com/PolinaDem/at_test_selenium_python/blob/main/API/create_token.py) |  create_token  | Method: POST   |
| [Get booking](https://github.com/PolinaDem/at_test_selenium_python/blob/main/API/get_booking.py) |  get_booking  |  Use url parameter. Method: GET   |
| [Get booking ids](https://github.com/PolinaDem/at_test_selenium_python/blob/main/API/get_booking_ids.py) |  get_booking_ids  | Method: GET    |
| [Create booking](https://github.com/PolinaDem/at_test_selenium_python/blob/main/API/create_booking.py)   |  create_booking  | Method: POST    |
| [Update booking](https://github.com/PolinaDem/at_test_selenium_python/blob/main/API/update_booking.py)   | update_booking   | Take token from another file, use cookie and url parameter. Method: PUT    |
| [Partial update booking](https://github.com/PolinaDem/at_test_selenium_python/blob/main/API/partial_update_booking.py)   | partial_update_booking   | Take token from another file, use cookie and url parameter. Method: PATCH    |
| [Delete booking](https://github.com/PolinaDem/at_test_selenium_python/blob/main/API/delete_booking.py)   | delete_booking   | Take token from another file, use cookie and url parameter. Method: DELETE    |

## Installation instructions
How to start working on tests with **Selenium** you can discover [here](https://www.selenium.dev/documentation/). \
How to start working on tests with **Pytest** you can discover [here](https://docs.pytest.org/en/7.1.x/announce/release-7.0.1.html). \
How to start working on tests with **Python** you can discover [here](https://docs.python.org/3.6/tutorial/). 

Python 3.6\
Pytest 7.0.1

## Contact information
Polina Demina\
pp.demina@gmail.com

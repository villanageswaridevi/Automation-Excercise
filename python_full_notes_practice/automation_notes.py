"""
1. What is Selenium?
====================
Ans: Selenium is an open-source automation tool used to test web applications automatically.

It controls the browser and performs the actions like:
--> clicking the buttons
--> Entering text
--> Navigating pages
--> validating the pages
Selenium mainly automates web browsers

2. Components in selenium:
==========================
1. selenium IDE:
--> Selenium IDE is browser extension it is used to record and play back the test cases.
--> It is mainly used by beginners who do not knowing the programming.

2. selenium webdriver:
--> Selenium webdriver is the main component of selenium used to automate browsers using programming languages.
--> And it is directly communicates with the browsers.
--> EX: chrome, firefox, edge, safari

3. selenium grid:
--> Selenium grid is used to run the test cases in multiple machines and browsers at the same time.
This is called parallel testing.
--> Example: suppose we have 100 test cases
Without grid:
--> Run on one browser
--> It will take 2 hours
With grid:
--> Run on multiple browsers
--> It will take 20 minutes.
4. selenium RC:
--> Selenium RC stands for remote control.
--> Selenium RC was the old version of Selenium used before webdriver.
--> It required a server to communicate with the browser.

3. Locators in selenium:
======================
1. ID:
--> ID locator is used to find the element on the web page loading "ID" attribute of the web page
fastest, use when we have unique.
2. Name:
--> use if ID is not available
3. Class_Name:
--> Used for group the element
4. Tag_name:
--> Used for HTML tags like <input>, <a> etc..
5. Link_Text:
--> Matches for exact link text
6. Partial_Link_Text:
--> Matches a part of link text
7. CSS_SELECTOR:
--> Powerful and short syntax
8. XPATH:
--> Powerful but compared to CSS_SELECTOR XPATH is slower, and supports only for complex like inputs and buttons

4. Waits in selenium:
=====================
1. implicitly wait:
--> It is a global wait, once we set this can be applicable for all the locators for the session.
--> Implicit wait tells to selenium to wait for a certain amount of time before throwing an exception
if an element is not found.

2. Explicitly wait:
--> This can perform for an expected condition
--> Explicit wait tells selenium to wait for a specific condition to occur before proceeding.
Example conditions:
--> Element clickable
--> Element visible
--> Element present

3. fluent wait:
--> fluent wait is similar to explicit wait but provides more control.

5. differences between find_element and find_elements
=====================================================
1. find_element():
--> It is used find only one element on the web page.
--> It returns only a single web element
--> If the element is not found it will throw an exception like NoSuchElementException.
2. find_elements():
--> It is used find multiple elements
--> It returns list of Web elements.
--> If the element are not found, it will throw an empty list (no error)

6. differences between quit() and close()?
=======================================
1.Quit():
--> closes all the windows and tabs.
--> Ends the webdriver session completely.
2. Close():
--> closes current window or tab only.
--> If multiple tabs are open, the remain open.

7. Differences between relative XPATH and absolute XPATH?
1. Relative XPATH:
--> starts directly from any element in DOM (Document Object Model)
--> Begins with // (double slash)

2. Absolute XPATH:
--> Starts from top of HTML node
--> Begins with single slash /

8. Differences between CSS_SELECTOR and XPATH?
--> CSS_SELECTOR is faster and simpler but XPATH is more powerful and flexible
because it can navigate both forward and backward in the DOM(Document object model)





"""

print("Bye")
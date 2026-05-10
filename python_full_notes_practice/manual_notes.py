"""
1. what is python?
===================
Ans: Python is a programming language.
Python is an object-oriented language, high level language & scripting language.
Python uses .py extension
And it is a user-friendly language like easy to understand, easy to write a code compare to
other programming language.

2. Characteristics of python:
=============================
--> Easy to learn and read -
English like syntax. It is easy for beginners to understand and write.

--> Interpreted language -
Python code executed line by line.
No need to compile before running the code.

--> Dynamically typed language -
no need to declare data types.

--> Object - oriented language -
Everything in python is an object.
It will support classes, inheritance and Polymorphism.

--> Platform - independent Language -
Python can run on any operating systems like (windows, linux and macOS) without modifications.

--> Open source -
Python is free to download and use.



3. Data types:
==============
--> Immutable data types -
Int - It can have whole numbers. Once we define we can't able to change throughout the program execution.

string - String is define by using single quotes or double quotes, and once we define we can't able to change
throughout the program execution.

Tuple - tuple is immutable data type, once we define we can't able to change throughout the program execution
tuple is defined by using parenthesis () and separated by the coma.

--> Mutable data types -
List - List is defined by using square brackets, and it is changeable that means we can add, remove the items in
the list after it has been created.

Dictionary - dict is defined by using curly braces, and dictionary can store the data values in key-value pairs.
And it won't allow duplicate, and it is changeable that means we can add remove the items in the dictionary
after it has been created.

Set - Set is defined by using curly braces, and it can store multiple items in a single variables.
and it won't allow duplicates, once set is created we cannot change the items,but we can remove and add the new items.

*** type casting -
converting one object to another object/ data type
ex - int, str, tuple, list, dict, set

int only can convert into str



4 . Slicing:
============
sequence[start : stop : step]

start - where the index slicing begins
stop - where the index slicing ends
step - how many elements to skip

5. Shallow copy and Deep copy:
==============================
--> Shallow copy - Shallow copy copies the outer objects, but inner objects still shared.
--> Deep copy - Deep copy copies both inner and outer objects, making a fully independent copy.

"""
"""

manual testing interview questions
==================================

1. What is software testing?
============================
Ans: 
--> Software testing is the process of checking an software application to find the errors, bugs and defects
verify that the software works according to the requirements.

2. Manual Testing:
==================
--> Manual testing is a type of software testing where a human tester manually checks an application for defects
without using automation tools and scripts. 
--> Instead of writing the code test the software, the tester:
1. Execute the test cases manually.
2. clicks through the application.
3. Enter the data.
4. compares actual results and expected results.
5. Reports the bugs or issues.

3. SDLC ( Software Development Life Cycle):
===========================================
--> SDLC is process and it is used to develop in a systematic and structured way.
--> And it is a step by step process followed to design, develop, test and maintain the software.
--> The main goal of SDLC is to produce high-quality software that meet user requirements
within the time & budget.

Phases of SDLC:
1. Requirement analysis:
--> collect the requirements from the client or stakeholders
2. Planning:
--> Estimate time, budget and resources.
--> Decide project schedule and team members
3. Design:
--> create the software architecture and system design
--> Decide how the application will be built
4. Coding:
--> Developers write the actual code to build the application.
5. Testing:
--> Testers checks the software for bugs or defects.
--> To checks the application works correctly.
6. Development:
--> The application released to users or production environment.
7. Maintenance: 
--> Fix bugs after release
--> Add new feature
--> Improve performance.

4. STLC (Software Testing Life Cycle):
======================================
--> It is a step by step process followed during testing of software to ensure quality and correctness.
--> It is just like a SDLC is for development and STLC for testing.

Phases of STlC:
1. Requirement analysis
2. Test plan
3. Test case design
4. Test environment setup
5. Test execution
6. Test reporting & Tracking
7. Test closure

5. Bug life cycle:
==================
--> Bug life cycle is also called as defect life cycle is the journey of bug/defect
from the moment it is found until it is fixed and closed.

Phases of Bug life cycle:
1. New - Tester reports the bug
2. Assigned - Bug assigned to the developer
3. Open - Developer checks the bug
4. Fixed - Developer fix the bug
5. Retest - Tester tests again
6. Verified - Bug works properly
7. Closed - Bug closed

6. Testing Techniques:
======================
1. Boundary value analysis:
--> Values range checked min values, max values, and mid values like that.
2. Equivalent partition:
--> Application are divided into chunks like that.
3. Decision table:
--> Top to bottom of application of a tree type
like home page, Account page, contact details, About page etc..
4. Error guessing:
--> Randomly we can guess the error in the application.
5. Use case testing: 
--> Use design for pattern

7. Types of testing:
====================
1. Functional testing:
--> Functional testing is a type of software testing where testers verify that the function of the application 
works according to the specified requirements.

Types of functional testing:
1. Unit testing: 
--> Testing individual components or modules of the application.
2. Integration testing:
--> Testing how different modules work together.
3. System testing:
--> Testing the complete application as a whole.
4. User acceptance testing:
--> Testing done by the end users or clients to confirm that the application meets their requirements.
5. Regression testing:
--> Testing the application again after changes or bug fixes to ensure existing functionality still works.
6. Smoke Testing:
--> Basic testing performed to check whether major functionalities are working.
7. Sanity testing:
--> Quick testing done after small changes or bug fixes.

2. Non-functional testing:
--> Non functional testing is a type of testing used to chack how well a system performs.

Types of Non-functional testing:
1. Performance testing:
--> Checks the speed and responsiveness of the system.
2. Load testing:
--> Checks how the application behaves when many users use it at the same time.
3. Stress testing:
--> Tests the system beyond its limit to see how it behaves under extreme load.
Ex: 10,000 users accessing a website at a time.
4. Security testing:
--> Checks whether the system is protected from hackers and unauthorized access.
5. Usability testing:
--> Checks whether the application is easy to use for users.
6.  Compatibility testing:
--> Cheks whether the application works on different browsers, devices, and operating systems.
7. Reliability testing:
--> checks whether the application works consistently without failures for a long time.

8. Differences between severity and priority?
=============================================
1. Severity:
--> How serious/ impactful a defect is on the application.
--> And it is decided by mostly tester/ QA Team.
--> mainly focus: impact on the system.
Example: 
--> App crashes when clicking save - "High Severity"
--> A spelling mistake in about us page - "Low severity"

2. Priority:
--> How urgent it is to fix the defect.
--> And it is decided by product owner/ manager/ client.
--> mainly focus: Effect on business/ market timelines.
Example: 
--> Company logo is wrong in home page - "High Priority"
--> A crash in rarely used feature - "Low priority" but "High severity"

9. What is a agile process? Scrum / Agile ceremonies?
=====================================================
1. Agile Process:
--> Agile is a flexible software development approach that delivers software in small
interactions with continues feedback.
2. Agile ceremonies:
--> Sprint planning (plan work)
--> Daily stand-up (daily progress check)
-->Sprint reviews (demo to stakeholders)
--> Sprint Retrospective (improvement discussion)
3. Scrum:
--> Scrum board is a visual board used in Agile to track the sprint tasks (like To do, In progress, Done)
--> Scrum board will be set up by the scrum master, development team will be updates it daily.

10. Test plan, Test scenarios?
==============================
1. Test plan:
--> A test plan is a detailed document that will explains what to test, how to test, who will test and
when to test will be done by the specific project or release.
2. Test scenarios:
--> Test scenarios is a real-world situations that describes what to test in an application like
logging in, adding items into cart
3. Traceability matrix:
--> Traceability matrix is a document that maps requirement with their test cases to complete test coverage
and track the requirement has been verified.









 









 

























"""

print("done")
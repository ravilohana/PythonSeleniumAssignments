# PythonSeleniumAssignments

### Assignment 1

- Login VWO.com
- 93npu2yyb0@esiix.com
- Wingify@123


### Assignment 2

- Login to https://katalon-demo-cura.herokuapp.com/ and Make Appointment


### Assignment 3


- Login to the HR Module
- https://awesomeqa.com/hr/web/index.php/auth/login
- Username - admin
- Password - Hacker@4321


## Tech Stack (PythonPackages used)
1. Python
2. Pytest Testing Framework
3. Reports - Allure Report, Pytest-html


#### To run the test from the project directory commands with HTML report

    ` pytest  -v -s --html="Report.html" `


#### To run the test from the project directory commands with HTML report and allure reports

    ` pytest  -v --capture sys --html="Report.html" --alluredir=../../allureReports/allure_results `
    
 - To generate the allure reports command

   


    ` allure serve .\allureReports\allure_results\ `
    

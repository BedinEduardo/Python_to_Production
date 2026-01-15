
--> Idiomatic code means in software is wheter or not your code conforms to standard style patterns.
--> Naming convetions - Snake style, Cammel style
--> Python, Java --> Object Oriented --> Classes, functions, variables, parameters, argumentos...
--> Hiring decision
--> Refactoring code
--> Reability increases our abillity to change the program, which is what Clean Code is all about.
--> Clean Code: spend less time debugging
--> Clean Code fundamentally us an organized way of designiring the products that you write Anyway.
--> Clean code is secury, and easy to change.
--> Readibility
--> Programming languages doesn't enforce you to use a particular style.
--> Mantaining a consistent style across de code

## https://peps.python.org/pep-0008/
* What the code should look like --> easy to understand --> readbility counts

## https://google.github.io/styleguide/pyguide.html
* importing libraries --> Standard style

#Cleand Code is
* Easy to mantain
* easy to understood
  * Low congnitive load
  * low learning curve
* safe/secure
* correct (it works)
* relevant
* high subjective

How do you get there:
*use good variable names

## Best Practices of Python Style
--> Clean code --> proce goog codes
--> Guides line
--> Descriptive Variables
--> Avoid mess in program - code
--> Global variables
--> State based bugs - Main errors - problems
--> Path to control the flow --> able to errors
--> Divide the code into classes and functions --> classes about entire functionalities --> functions about special functionalities.
--> Define right function formats and description
--> Make useful comments - not all
--> the code shoudl be readble enough to do not need comments
--> A useful comment is explain what some choise was done, not explain what is happening
--> Useful variables, functions, and classses descriptions
--> A useful function should have cleary inputs to generate clearly outputs - better to understand what the code does
--> A pure function is a function whose logic is entirely based on the functions inputs. The function produces is enterely a function of that function inputs --> functional programming.
--> https://github.com/rootski-io/rootski/pull/56 --> Feature/experiment with dynamobd --> https://ericriddoch.notion.site/Introduction-to-Continuous-Integration-and-best-practices-for-PRs-983d1f13cab949d193b12c8859022a4f

--> Code Quality: Does it works? --> You are not a compiler, you are just a person who read code
--> Qualitier reviwer --> automated test 
--> Automated set fo tests for your junior developer --> Can prove that they made the changes and the tests sitll pass --> haven't broken anything.
--> Can I understand it? --> code functional, but nobody understand what is happening in the code.
--> Is it safe? Do we even want this change ?
--> Code Review --> pull request --> pretty descriptive messages
--> Read code --> modifications
--> test the project --> specific hardware.
--> Giant codes - several and complex tests
--> What kind of features they want to request?
--> Large pull request is bad --> divide the pull request in small parts --> small modifications to produce small tests and better understing about what are happening in the code (project)
from flask import Flask

app = Flask(__name__)
print(__name__)


udemy_data = [
  {
    'Day 1': {
      'main_heading': ' Working with Variables in Python to Manage Data',
      'all_title': [
        "What you're going to get from this course",
        'START HERE',
        'Downloadable Resources and Tips for Taking the Course',
        'Day 1 Goals: what we will make by the end of the day',
        'FAQ: Can I Use PyCharm/VSCode/ Another Local Code Editor?',
        'Printing to the Console in Python',
        'Join our Class on Auditorium',
        '[Interactive Coding Exercise] Printing',
        'String Manipulation and Code Intelligence',
        '[Interactive Coding Exercise] Debugging Practice',
        'The Python Input Function',
        '[Interactive Coding Exercise] Input Function',
        'Python Variables',
        '[Interactive Coding Exercise] Variables',
        'Variable Naming',
        'Variable Naming Quiz',
        'Day 1 Project: Band Name Generator',
        'Congratulations! Well done!'
      ]
    }
  },
  {
    'Day 2': {
      'main_heading': ' Understanding Data Types and How to Manipulate Strings',
      'all_title': [
        'Day 2 Goals: what we will make by the end of the day',
        'Python Primitive Data Types',
        'Data Types Quiz',
        'Type Error, Type Checking and Type Conversion',
        '[Interactive Coding Exercise] Data Types',
        'Mathematical Operations in Python',
        '[Interactive Coding Exercise] BMI Calculator',
        'Number Manipulation and F Strings in Python',
        '[Interactive Coding Exercise] Life in Weeks',
        'Mathematical Operations Quiz',
        'Day 2 Project: Tip Calculator',
        'You are already in the top 50%'
      ]
    }
  },
  {
    'Day 3': {
      'main_heading': ' Control Flow and Logical Operators',
      'all_title': [
        'Day 3 Goals: what we will make by the end of the day',
        'Get Access to the Monthly App Brewery Newsletter',
        'Control Flow with if / else and Conditional Operators',
        '[Interactive Coding Exercise] Odd or Even? Introducing the Modulo',
        'Nested if statements and elif statements',
        '[Interactive Coding Exercise] BMI 2.0',
        '[Interactive Coding Exercise] Leap Year',
        'Multiple If Statements in Succession',
        '[Interactive Coding Exercise] Pizza Order Practice',
        'Logical Operators',
        '[Interactive Coding Exercise] Love Calculator',
        'Day 3 Project: Treasure Island',
        'Share and Show off your Project!'
      ]
    }
  },
  {
    'Day 4': {
      'main_heading': ' Randomisation and Python Lists',
      'all_title': [
        'Day 4 Goals: what we will make by the end of the day',
        'Random Module',
        '[Interactive Coding Exercise] Heads or Tails',
        'Understanding the Offset and Appending Items to Lists',
        '[Interactive Coding Exercise] Banker Roulette - Who will pay the bill?',
        'IndexErrors and Working with Nested Lists',
        'List and IndexError Quiz',
        '[Interactive Coding Exercise] Treasure Map',
        'Day 4 Project: Rock Paper Scissors',
        'Programming is like going to the Gym'
      ]
    }
  },
  {
    'Day 5': {
      'main_heading': ' Python Loops',
      'all_title': [
        'Day 5 Goals: what we will make by the end of the day',
        'Using the for loop with Python Lists',
        '[Interactive Coding Exercise] Average Height',
        '[Interactive Coding Exercise] High Score',
        'for loops and the range() function',
        '[Interactive Coding Exercise] Adding Even Numbers',
        '[Interactive Coding Exercise] The FizzBuzz Job Interview Question',
        'Day 5 Project: Create a Password Generator',
        'Hard Work and Perseverance beats Raw Talent Every Time'
      ]
    }
  },
  {
    'Day 6': {
      'main_heading': ' Python Functions & Karel',
      'all_title': [
        'Day 6 Goals: what we will make by the end of the day',
        'Defining and Calling Python Functions',
        'The Hurdles Loop Challenge',
        'Indentation in Python',
        'Code Indentation Quiz',
        'While Loops',
        'Hurdles Challenge using While Loops',
        'Jumping over Hurdles with Variable Heights',
        'Final Project: Escaping the Maze',
        'Why is this *so* Hard?! Can I really do this?'
      ]
    }
  },
  {
    'Day 7': {
      'main_heading': ' Hangman',
      'all_title': [
        'Day 7 Goals: what we will make by the end of the day',
        'How to break a Complex Problem down into a Flow Chart',
        'Challenge 1 - Picking a Random Words and Checking Answers',
        "Challenge 1 Solution - How to Check the User's Answer",
        'Challenge 2 - Replacing Blanks with Guesses',
        'Challenge 2 Solution - How to Replace the Blanks',
        'Challenge 3 - Checking if the Player has Won',
        'Challenge 3 Solution - How to Check if the Player Won',
        "Challenge 4 - Keeping Track of the Player's Lives",
        "Challenge 4 Solution - How to Keep Track of the Player's Lives",
        'Challenge 5 - Improving the User Experience',
        'Challenge 5 Solution - How to Add ASCII Art and Improve the UI',
        'The Benefits of Daily Practice'
      ]
    }
  },
  {
    'Day 8': {
      'main_heading': ' Function Parameters & Caesar Cipher',
      'all_title': [
        'Day 8 Goals: what we will make by the end of the day',
        'Functions with Inputs',
        'Positional vs. Keyword Arguments',
        '[Interactive Coding Exercise] Paint Area Calculator',
        '[Interactive Coding Exercise] Prime Number Checker',
        'Caesar Cipher Part 1 - Encryption',
        'Caesar Cipher Part 2 - Decryption',
        'Caesar Cipher Part 3 - Reorganising our Code',
        'Caesar Cipher Part 4 - User Experience Improvements & Final Touches',
        'How You Can *Stay* Motivated'
      ]
    }
  },
  {
    'Day 9': {
      'main_heading': ' Dictionaries, Nesting and the Secret Auction',
      'all_title': [
        'Day 9 Goals: what we will make by the end of the day',
        'The Python Dictionary: Deep Dive',
        '[Interactive Coding Exercise] Grading Program',
        'Nesting Lists and Dictionaries',
        '[Interactive Coding Exercise] Dictionary in List',
        'Python Dictionaries Quiz',
        'The Secret Auction Program Instructions and Flow Chart',
        'Solution and Complete Code for the Secret Auction Program',
        'Motivation and the Accountability Trick'
      ]
    }
  },
  {
    'Day 10': {
      'main_heading': ' Functions with Outputs',
      'all_title': [
        'Day 10 Goals: what we will make by the end of the day',
        'Functions with Outputs',
        'Multiple return values',
        '[Interactive Coding Exercise] Days in Month',
        'Docstrings',
        'Functions Quiz',
        'Calculator Part 1: Combining Dictionaries and Functions',
        'Print vs. Return',
        'While Loops, Flags and Recursion',
        'Calculator Finishing Touches and Bug Fixes',
        "How to Get a Good Night's Sleep"
      ]
    }
  },
  {
    'Day 11': {
      'main_heading': ' The Blackjack Capstone Project',
      'all_title': [
        'Day 11 Goals: what we will make by the end of the day',
        'Blackjack Program Requirements and Game Rules',
        'Hint 4 & 5 Solution Walkthrough',
        'Hint 6-8 Solution Walkthrough',
        'Hint 9 Solution Walkthrough: Refactoring and calling calculate_score()',
        'Hint 10-12 Solution Walkthrough',
        'Hint 13 Solution Walkthrough',
        'A Solid Foundation goes a Long Way'
      ]
    }
  },
  {
    'Day 12': {
      'main_heading': ' Scope & Number Guessing Game',
      'all_title': [
        'Namespaces: Local vs. Global Scope',
        'Does Python Have Block Scope?',
        'How to Modify a Global Variable',
        'Python Constants and Global Scope',
        'Scope Quiz',
        'Introducing the Final Project: The Number Guessing Game',
        'Solution & Walkthrough to the Number Guessing Game',
        "Don't be too hard on yourself"
      ]
    }
  },
  {
    'Day 13': {
      'main_heading': ' Debugging: How to Find and Fix Errors in your Code',
      'all_title': [
        'Describe the Problem',
        'Reproduce the Bug',
        'Play Computer and Evaluate Each Line',
        'Fixing Errors and Watching for Red Underlines',
        'Squash bugs with a print() Statement',
        'Bringing out the BIG Gun: Using a Debugger',
        'Final Debugging Tips',
        '[Interactive Coding Exercise] Debugging Odd or Even',
        '[Interactive Coding Exercise] Debugging Leap Year',
        '[Interactive Coding Exercise] Debugging FizzBuzz',
        'Building Confidence'
      ]
    }
  },
  {
    'Day 14': {
      'main_heading': ' Higher Lower Game Project',
      'all_title': [
        'Introduction & Program Requirements for the Higher Lower Game',
        'Solution & Walkthrough of the Higher Lower Game',
        'Study Tip: Set Reminders in Your Calendar to Review'
      ]
    }
  },
  {
    'Day 15': {
      'main_heading': ' Local Development Environment Setup & the Coffee Machine',
      'all_title': [
        'Installing Python Locally on Your Computer',
        'Download PyCharm for Windows or Mac',
        "PyCharm's Charming Features (while you wait for the download to finish)",
        'How to Install PyCharm on Windows',
        'Installing PyCharm on Mac',
        'Introduction & Requirements for the Coffee Machine Project',
        'Solution & Walkthrough for the Coffee Machine Code',
        "Location, Location, Location - Pavlov's Coding Corner"
      ]
    }
  },
  {
    'Day 16': {
      'main_heading': ' Object Oriented Programming (OOP)',
      'all_title': [
        'Why do we need OOP and how does it work?',
        'How to use OOP: Classes and Objects',
        'Constructing Objects and Accessing their Attributes and Methods',
        'How to Add Python Packages and use PyPi',
        'Practice Modifying Object Attributes and Calling Methods',
        'Python Objects Quiz',
        'Building the Coffee Machine in OOP',
        'Walkthrough and Solution for the OOP Coffee Machine',
        "Don't forget to review occasionally"
      ]
    }
  },
  {
    'Day 17': {
      'main_heading': ' The Quiz Project & the Benefits of OOP',
      'all_title': [
        'Day 17 Goals: what we will make by the end of the day',
        'How to create your own Class in Python',
        'Working with Attributes, Class Constructors and the __init__() Function',
        'Adding Methods to a Class',
        'Quiz Project Part 1: Creating the Question Class',
        'Quiz Project Part 2: Creating the List of Question Objects from the Data',
        'Quiz Project Part 3: The QuizBrain and the next_question() Method',
        'Quiz Project Part 4: How to continue showing new Questions',
        'Quiz Project Part 5: Checking Answers and Keeping Score',
        'The Benefits of OOP: Use Open Trivia DB to Get New Questions',
        'Run for that Bus!'
      ]
    }
  },
  {
    'Day 18': {
      'main_heading': ' Turtle & the Graphical User Interface (GUI)',
      'all_title': [
        'Day 18 Goals: what we will make by the end of the day',
        'Understanding Turtle Graphics and How to use the Documentation',
        'Turtle Challenge 1 - Draw a Square',
        'Importing Modules, Installing Packages, and Working with Aliases',
        'Turtle Challenge 2 - Draw a Dashed Line',
        'Turtle Challenge 3 - Drawing Different Shapes',
        'Turtle Challenge 4 - Generate a Random Walk',
        'Python Tuples and How to Generate Random RGB Colours',
        'Turtle Challenge 5 - Draw a Spirograph',
        'The Hirst Painting Project Part 1 - How to Extract RGB Values from Images',
        'The Hirst Painting Project Part 2 - Drawing the Dots',
        'Space out your study sessions and stay consistent'
      ]
    }
  },
  {
    'Day 19': {
      'main_heading': ' Instances, State and Higher Order Functions',
      'all_title': [
        'Day 19 Goals: what we will make by the end of the day',
        'Python Higher Order Functions & Event Listeners',
        'Challenge: Make an Etch-A-Sketch App',
        'Object State and Instances',
        'Understanding the Turtle Coordinate System',
        'Turtle Coordinate System Quiz',
        "Aaaand, we're off to the races!",
        'Expand on the Solutions'
      ]
    }
  },
  {
    'Day 20': {
      'main_heading': ' Build the Snake Game Part 1: Animation & Coordinates',
      'all_title': [
        'Day 20 Goals: what we will make by the end of the day',
        'Screen Setup and Creating a Snake Body',
        'Animating the Snake Segments on Screen',
        'Create a Snake Class & Move to OOP',
        'How to Control the Snake with a Keypress',
        'Programming is not Memorising'
      ]
    }
  },
  {
    'Day 21': {
      'main_heading': ' Build the Snake Game Part 2: Inheritance & List Slicing',
      'all_title': [
        'Day 21 Goals: what we will make by the end of the day',
        'Class Inheritance',
        'Inheritance Quiz',
        'Detect Collisions with Food',
        'Create a Scoreboard and Keep Score',
        'Detect Collisions with the Wall',
        'Detect Collisions with your own Tail',
        'How to Slice Lists & Tuples in Python',
        'Stay motivated by remembering the reason you signed up'
      ]
    }
  },
  {
    'Day 22': {
      'main_heading': ' Build Pong: The Famous Arcade Game',
      'all_title': [
        'Day 22 Goals: what you will make by the end of the day',
        'Set up the Main Screen',
        'Create a Paddle that responds to Key Presses',
        'Write the Paddle Class and Create the Second Paddle',
        'Write the Ball Class and Make the Ball Move',
        'Add the Ball Bouncing Logic',
        'How to Detect Collisions with the Paddle',
        'How to Detect when the Ball goes Out of Bounds',
        'Score Keeping and Changing the Ball Speed',
        'Picturing fears: even the worst-case scenario is not so scary'
      ]
    }
  },
  {
    'Day 23': {
      'main_heading': ' The Turtle Crossing Capstone Project',
      'all_title': [
        'Day 23 Goals: what you will make by the end of the day',
        'Choose Your Difficulty',
        'How to use the Starter Code',
        'Step 1 - Check out how the game play works',
        'Step 2 - Break down the Problem',
        'Solution to Step 3 - Create the Player Behaviour',
        'Solution to Step 4 - Create the Car Behaviour',
        'Solution to Step 5 - Detect when the Turtle collides with a Car *squish*',
        'Solution to Step 6 - Detect when the Player has reached the other side',
        'Solution to Step 7 - Add the Scoreboard and Game Over sequence',
        'This course is not about typing out code'
      ]
    }
  },
  {
    'Day 24': {
      'main_heading': ' Files, Directories and Paths',
      'all_title': [
        'Day 24 Goals: what you will make by the end of the day',
        'Add a High Score to the Snake Game',
        'How to Open, Read, and Write to Files using the "with" Keyword',
        'Challenge: Read and Write the High Score to a File in Snake',
        'Understand Relative and Absolute File Paths',
        'File Paths Quiz',
        'Introducing the Mail Merge Challenge',
        'Solution & Walkthrough for the Mail Merge Project',
        "What's the correct solution? What's the best answer? What's the right way?"
      ]
    }
  },
  {
    'Day 25': {
      'main_heading': ' Working with CSV Data and the Pandas Library',
      'all_title': [
        'Day 25 Goals: what we will make by the end of the day',
        'Reading CSV Data in Python',
        'DataFrames & Series: Working with Rows & Columns',
        'The Great Squirrel Census Data Analysis (with Pandas!)',
        'U.S. States Game Part 1: Setup',
        'U.S. States Game Part 2: Challenge with .csv',
        'U.S. States Game Part 3: Saving Data to .csv'
      ]
    }
  },
  {
    'Day 26': {
      'main_heading': ' List Comprehension and the NATO Alphabet',
      'all_title': [
        'Day 26 Goals: what you will make by the end of the day',
        'How to Create Lists using List Comprehension',
        '[Interactive Coding Exercise] Squaring Numbers',
        '[Interactive Coding Exercise] Filtering Even Numbers',
        '[Interactive Coding Exercise] Data Overlap',
        'Apply List Comprehension to the U.S. States Game',
        'How to use Dictionary Comprehension',
        '[Interactive Coding Exercise] Dictionary Comprehension 1',
        '[Interactive Coding Exercise] Dictionary Comprehension 2',
        'How to Iterate over a Pandas DataFrame',
        'Introducing the NATO Alphabet Project',
        'Solution & Walkthrough for the NATO Alphabet Project'
      ]
    }
  },
  {
    'Day 27': {
      'main_heading': ' Tkinter, *args, **kwargs and Creating GUI Programs',
      'all_title': [
        'Day 27 Goals: what we will make by the end of the day',
        'History of GUI and Introduction to Tkinter',
        'Creating Windows and Labels with Tkinter',
        'Setting Default Values for Optional Arguments inside a Function Header',
        'Default Values Quiz',
        '*args: Many Positional Arguments',
        '**kwargs: Many Keyword Arguments',
        'Optional Arguments, *args and **kwargs Quiz',
        'Buttons, Entry, and Setting Component Options',
        'Other Tkinter Widgets: Radiobuttons, Scales, Checkbuttons and more',
        'Tkinter Layout Managers: pack(), place() and grid()',
        'Mile to Kilometers Converter Project'
      ]
    }
  },
  {
    'Day 28': {
      'main_heading': ' Tkinter, Dynamic Typing and the Pomodoro GUI Application',
      'all_title': [
        'Day 28 Goals: what we will make by the end of the day',
        'How to work with the Canvas Widget and Add Images to Tkinter',
        "Challenge - Complete the Application's User Interface (UI)",
        'Add a Count Down Mechanism',
        'Dynamic Typing Explained',
        'Setting Different Timer Sessions and Values',
        'Adding Checkmarks and Resetting the Application'
      ]
    }
  },
  {
    'Day 29': {
      'main_heading': ' Building a Password Manager GUI App with Tkinter',
      'all_title': [
        'Day 29 Goals: what we will make by the end of the day',
        'Challenge 1 - Working with Images and Setting up the Canvas',
        'Challenge 2 - Use grid() and columnspan to Complete the User Interface',
        'Solution to the Creating the Grid Layout',
        'Challenge 3 - Saving Data to File',
        'Dialog Boxes and Pop-Ups in Tkinter',
        'Generate a Password & Copy it to the Clipboard'
      ]
    }
  },
  {
    'Day 30': {
      'main_heading': ' Errors, Exceptions and JSON Data: Improving the Password',
      'all_title': [
        'Day 30 Goals: what you will make by the end of the day',
        'Catching Exceptions: The try catch except finally Pattern',
        'Raising your own Exceptions',
        '[Interactive Coding Exercise] IndexError Handling',
        '[Interactive Coding Exercise] KeyError Handling',
        'Code Exercise: Exception Handling in the NATO Phonetic Alphabet Project',
        'Write, read and update JSON data in the Password Manager',
        'Challenge 1 - Handling Exceptions in the Password Manager',
        'Challenge 2 - Search for a Website in the Password Manager'
      ]
    }
  },
  {
    'Day 31': {
      'main_heading': ' Flash Card App Capstone Project',
      'all_title': [
        'Day 31 Goals: what you will make by the end of the day',
        'Step 1 - Create the User Interface (UI) with Tkinter',
        'Solution & Walkthrough for Creating the UI',
        'Step 2 - Create New Flash Cards',
        'Solution & Walkthrough for Creating New Flash Cards',
        'Step 3 - Flip the Cards!',
        'Solution & Walkthrough for Flipping Cards',
        'Step 4 - Save Your Progress',
        'Solution & Walkthrough for Saving Progress'
      ]
    }
  },
  {
    'Day 32': {
      'main_heading': ' Intermediate+ Send Email (smtplib) & Manage Dates (datetime)',
      'all_title': [
        'Day 32 Goals: what we will make by the end of the day',
        'A Note About the Next Lesson: Google SMTP Port',
        'How to Send Emails with Python using SMTP',
        'Working with the datetime Module',
        'Challenge 1 - Send Motivational Quotes on Mondays via Email',
        'Automated Birthday Wisher Project Challenge',
        'Solution & Walkthrough for the Automated Birthday Wisher',
        'Run Your Python Code in the Cloud!'
      ]
    }
  },
  {
    'Day 33': {
      'main_heading': ' ISS Overhead Notifier',
      'all_title': [
        'Day 33 Goals: what you will make by the end of the day',
        'What are Application Programming Interfaces (APIs)?',
        'API Endpoints and Making API Calls',
        'Working with Responses: HTTP Codes, Exceptions & JSON Data',
        'Challenge - Build a Kanye Quotes App using the Kanye Rest API',
        'Understand API Parameters: Match Sunset Times with the Current Time',
        'ISS Overhead Notifier Project - Challenge & Solution'
      ]
    }
  },
  {
    'Day 34': {
      'main_heading': ' Creating a GUI Quiz App',
      'all_title': [
        'Day 34 Goals: what you will make by the end of the day',
        'Trivia Question API Challenge',
        'Solution & Walkthrough for getting Trivia Questions',
        'Unescaping HTML Entities',
        'Class based Tkinter UI',
        'Python Typing & Showing the Next Question in the GUI',
        'Python Typing: Type Hints and Arrows ->',
        'Check the Answer',
        'Give Feedback to the Player, Keep Score and Fix the Bugs =)'
      ]
    }
  },
  {
    'Day 35': {
      'main_heading': ' Intermediate+ Keys, Authentication & Environment Variables: Send SMS',
      'all_title': [
        'Day 35 Goals: what you will make by the end of the day',
        'What is API Authentication and Why Do We Need to Authenticate Ourselves?',
        'Using API Keys to Authenticate and Get the Weather from OpenWeatherMap',
        'Challenge - Check if it Will Rain in the Next 12 Hours',
        'Sending SMS via the Twilio API',
        'Use PythonAnywhere to Automate the Python Script',
        'Understanding Environment Variables and Hiding API Keys'
      ]
    }
  },
  {
    'Day 36': {
      'main_heading': ' Intermediate+ Stock Trading News Alert Project',
      'all_title': [
        'Day 36 Goals: what you will make by the end of the day',
        'Choose Your Destiny!',
        'Solution & Walkthrough for Step 1 - Check for Stock Price Movements',
        'Solution & Walkthrough for Step 2 - Get the News Articles',
        'Solution & Walkthrough for Step 3 - Send the SMS Messages'
      ]
    }
  },
  {
    'Day 37': {
      'main_heading': ' Intermediate+ Habit Tracking Project: API Post Requests & Headers',
      'all_title': [
        'Day 37 Goals: what you will make by the end of the day',
        'HTTP Post Requests',
        'Advanced Authentication using an HTTP Header',
        'Challenge: Add a Pixel to the Habit Tracker using a Post Request',
        "Autofilling today's date using strftime",
        'How to use HTTP Put and Delete Requests'
      ]
    }
  },
  {
    'Day 38': {
      'main_heading': ' Intermediate+ Workout Tracking Using Google Sheets',
      'all_title': [
        'Day 38 Goals: what you will make by the end of the day',
        'Step 1 - Setup API Credentials and Google Spreadsheet',
        'Step 2 - Get Exercise Stats with Natural Language Queries',
        'Step 3 - Setup Your Google Sheet with Sheety',
        'Step 4 - Saving Data into Google Sheets',
        'Step 5 - Authenticate Your Sheety API',
        'Step 6 - Environment Variables in Repl.it'
      ]
    }
  },
  {
    'Day 39': {
      'main_heading': ' Intermediate+ Capstone Part 1: Flight Deal Finder',
      'all_title': [
        'Day 39 Goals: what you will make by the end of the day',
        'Step 1 - Choose Your Path and Download the Starting Project',
        'Step 2 - Use Sheety to Read and Write Data to the Google Sheet',
        'Step 3 - Get the IATA Codes using the Kiwi Partners API',
        'Step 4 - Search for Cheap Flights',
        'Step 5 - If Flight Price Lower than in Google Sheet send an SMS'
      ]
    }
  },
  {
    'Day 40': {
      'main_heading': ' Intermediate+ Capstone Part 2: Flight Club',
      'all_title': [
        'Day 40 Goals: what you will make by the end of the day',
        'Step 1 - Create the Customer Acquisition Code',
        'Step 2 - Download the Starting Project',
        'Step 3 - Exception Handling for Destinations without Flights',
        'Step 4 - Destinations without Direct Flights',
        'Step 5 - Email all our customers'
      ]
    }
  },
  {
    'Day 41': {
      'main_heading': ' Introduction to HTML',
      'all_title': [
        'How Does the Internet Actually Work?',
        'How Do Websites Actually Work?',
        'Download the Required Software',
        'What is HTML?',
        'HTML Heading Elements',
        'HTML Paragraph Elements',
        'Self Closing Tags',
        'Day 41 Project - Movie Ranking'
      ]
    }
  },
  {
    'Day 42': {
      'main_heading': ' Intermediate HTML',
      'all_title': [
        'HTML Boilerplate',
        'The List Element',
        'Nesting and Indentation',
        'Anchor Elements',
        'Image Elements',
        'Day 42 Project - Birthday Invite Website'
      ]
    }
  },
  {
    'Day 43': {
      'main_heading': ' Introduction to CSS',
      'all_title': [
        'Why do we need CSS?',
        'How to add CSS',
        'CSS Quiz',
        'CSS Selectors',
        'Day 43 Project - Colour Vocab Website'
      ]
    }
  },
  {
    'Day 44': {
      'main_heading': ' Intermediate CSS',
      'all_title': [
        'CSS Colours',
        'Font Properties',
        'Inspecting CSS',
        'The CSS Box Model - Margin, Padding and Border',
        'Day 44 Project - Motivational Poster Website'
      ]
    }
  },
  {
    'Day 45': {
      'main_heading': ' Intermediate+ Web Scraping with Beautiful Soup',
      'all_title': [
        'Day 45 Goals: what you will make by the end of the day',
        'Parsing HTML and Making Soup',
        'Finding and Selecting Particular Elements with BeautifulSoup',
        'Beautiful Soup Exercises',
        'Scraping a Live Website',
        'Is Web Scraping Legal?',
        '100 Movies that You Must Watch'
      ]
    }
  },
  {
    'Day 46': {
      'main_heading': ' Intermediate+ Create a Spotify Playlist using the Musical Time Machine',
      'all_title': [
        'Day 46 Goals: what you will make by the end of the day',
        'Step 1 - Scraping the Billboard Hot 100',
        'Step 2 - Authentication with Spotify',
        'Step 3 - Search Spotify for the Songs from Step 1',
        'Step 4 - Creating and Adding to Spotify Playlist'
      ]
    }
  },
  {
    'Day 47': {
      'main_heading': ' Intermediate+ Create an Automated Amazon Price Tracker',
      'all_title': [
        'Day 47 Goals: what you will make by the end of the day',
        'Step 1 - Use BeautifulSoup to Scrape the Product Price',
        'Step 2 - Email Alert When Price Below Preset Value'
      ]
    }
  },
  {
    'Day 48': {
      'main_heading': ' Intermediate+ Selenium Webdriver Browser and Game Playing Bot',
      'all_title': [
        'Day 48 Goals: what you will make by the end of the day',
        'How to Install & Set Up Selenium',
        'How to Find and Select Elements on a Website with Selenium',
        'Challenge: Use Selenium to Scrape Website Data',
        'Challenge: Use Selenium in a Blank Project & Scrape a Different Piece of Data',
        'How to Automate Filling Out Forms and Clicking Buttons with Selenium',
        'The Cookie Clicker Project',
        'Challenge: Create an Automated Game Playing Bot'
      ]
    }
  },
  {
    'Day 49': {
      'main_heading': ' Intermediate+ Automating Job Applications on LinkedIn',
      'all_title': [
        'Day 49 Goals: what you will make by the end of the day',
        'Step 1 - Setup Your LinkedIn Account',
        'Step 2 - Automatically Login',
        'Step 3 - Apply for a Job',
        'Step 4 - Apply for all the jobs'
      ]
    }
  },
  {
    'Day 50': {
      'main_heading': ' Intermediate+ Auto Tinder Swiping Bot',
      'all_title': [
        'Day 50 Goals: what you will make by the end of the day',
        'Step 1 - Setup your account on Tinder',
        'Step 2 - Navigate to Login Page',
        'Step 3 - Login with Facebook',
        'Step 4 - Dismiss all requests',
        'Step 5 - Hit Like!'
      ]
    }
  },
  {
    'Day 51': {
      'main_heading': ' Intermediate+ Internet Speed Twitter Complaint Bot',
      'all_title': [
        'Day 51 Goals: what you will make by the end of the day',
        'Step 1 - Setup Your Twitter Account',
        'Step 2 - Create a Class',
        'Step 3 - Get Internet Speeds',
        'Step 4 - Building a Twitter Bot to Tweet at your Internet Provider'
      ]
    }
  },
  {
    'Day 52': {
      'main_heading': ' Intermediate+ Instagram Follower Bot',
      'all_title': [
        'Day 52 Goals: what you will make by the end of the day',
        'Step 1 - Get Your Instagram Credentials',
        'Step 2 - Create a Class',
        'Step 3 - Login to Instagram',
        'Step 4 - Find the followers of the target account',
        'Step 5 - Follow all the followers'
      ]
    }
  },
  {
    'Day 53': {
      'main_heading': ' Data Entry Job Automation',
      'all_title': [
        'Day 53 Goals: what you will make by the end of the day',
        'Web Scraping and Data Entry Capstone Project Requirements',
        'Hints & Solution'
      ]
    }
  },
  {
    'Day 54': {
      'main_heading': ' Intermediate+ Introduction to Web Development with Flask',
      'all_title': [
        'Understanding Backend Web Development with Python',
        'Create your First Web Server with Flask',
        'Understand the Command Line on Windows and Mac',
        '__name__ and __main__ : Special Attributes built into Python',
        'Python Functions as First Class Objects: Passing & Nesting Functions',
        'Understanding Python Decorator Functions and the @ Syntax',
        '[Interactive Coding Exercise] Create your own Python Decorator'
      ]
    }
  },
  {
    'Day 55': {
      'main_heading': ' Intermediate+ HTML & URL Parsing in Flask and the Higher Lower Game',
      'all_title': [
        'Day 55 Goals: what you will make by the end of the day',
        'Working Flask URL Paths and the Flask Debugger',
        'Rendering HTML Elements with Flask',
        'Challenge: Use Python Decorators to Style HTML Tags',
        'Advanced Decorators with *args and **kwargs',
        '[Interactive Coding Exercise] Advanced Decorators',
        'Final Project - Higher or Lower URLs'
      ]
    }
  },
  {
    'Day 56': {
      'main_heading': ' Intermediate+ Rendering HTML/Static files and Using Website Templates',
      'all_title': [
        'Day 56 Goals: what you will make by the end of the day',
        'Rendering HTML Files with Flask',
        'Serving Static Files using Flask',
        'How to Use Website Templates to Speed Up Web Development',
        'Final Project - Name Card Website Template',
        'Solution and Walkthrough for the Name Card Final Project'
      ]
    }
  },
  {
    'Day 57': {
      'main_heading': ' Intermediate+ Templating with Jinja in Flask Applications',
      'all_title': [
        'Day 57 Goals: what you will make by the end of the day',
        'Using Jinja to Produce Dynamic HTML Pages',
        'Challenge: Combining Jinja Templating with APIs',
        'Multiline Statements with Jinja',
        'URL Building with Flask',
        'Blog Capstone Project Part 1 - Templating'
      ]
    }
  },
  {
    'Day 58': {
      'main_heading': ' Web Foundation Bootstrap',
      'all_title': [
        "Day 58 Goals: What You'll Learn By the End of Today",
        'What is Bootstrap?',
        'Bootstrap Layout',
        'Bootstrap Components',
        'Day 58 Project - A Startup Website for TinDog'
      ]
    }
  },
  {
    'Day 59': {
      'main_heading': ' Adding Styling',
      'all_title': [
        "Day 59 Goals: What you'll make by the end of today",
        'Step 1 - Download the starting project',
        'Step 2 - Get the home page to work',
        'Step 3 - Fix the header and footer',
        'Step 4 - Using Jinja Include for Render Templates',
        'Step 5 - Make the About and Contact Pages Work',
        'Step 6 - Fetch and render the blog posts from an API',
        'Step 7 - Rendering Individual Posts'
      ]
    }
  },
  {
    'Day 60': {
      'main_heading': ' Make POST Requests with Flask and HTML Forms',
      'all_title': [
        'Day 60 goals - Make the Contact Form Work',
        'HTML Forms Revision - Creating a Form from Scratch',
        'Handle POST Requests with Flask Servers',
        'POST Requests in Flask Solution',
        'Getting the Contact Form to Work',
        'Sending Email with smtplib'
      ]
    }
  },
  {
    'Day 61': {
      'main_heading': 'WTForms',
      'all_title': [
        'Day 61 Goals: Building Advanced Forms',
        'Installing Flask-WTF',
        'Creating Forms with Flask-WTF',
        'Code Improvements for Our WTForms',
        'Adding Validation to Forms with Flask-WTF',
        'Receiving Form Data with WTForms',
        'Inheriting Templates Using Jinja2',
        'Using Bootstrap-Flask as an Inherited Template',
        'Bootstrap-Flask Supports WTForms'
      ]
    }
  },
  {
    'Day 62': {
      'main_heading': ' Coffee & Wifi Project',
      'all_title': [
        'Download the Starting Project',
        'Look at the Desired Final Product',
        'Check Off Each Requirement'
      ]
    }
  },
  {
    'Day 63': {
      'main_heading': ' Databases and with SQLite and SQLAlchemy',
      'all_title': [
        'Day 63 Goals: Creating a Virtual Bookshelf',
        'Download the Starting Project',
        'Make the Website Work',
        'What Happens When You Refresh the Server?',
        'SQLite Databases',
        'SQLAlchemy',
        'CRUD Operations with SQLAlchemy',
        'Build a SQLite Database into the Flask Website'
      ]
    }
  },
  {
    'Day 64': {
      'main_heading': ' My Top 10 Movies Website',
      'all_title': [
        "Day 64 Goals: What We'll Build",
        'Download the Starting Project',
        'Requirement 1 - Be Able to View Movie List Items',
        "Requirement 2 - Be Able to Edit a Movie's Rating and Review",
        'Requirement 3 - Be Able to Delete Movies from the Database',
        'Requirement 4 - Be Able to Add New Movies Via the Add Page',
        'Requirement 5 - Be Able to Sort and Rank the Movies By Rating'
      ]
    }
  },
  {
    'Day 65': {
      'main_heading': ' How to Create a Website that People will Love',
      'all_title': [
        'Introduction to Web Design',
        'Understanding Color Theory',
        'Understanding Typography and How to Choose Fonts',
        'Manage ATTENTION with effective User Interface (UI) Design',
        'User Experience (UX) Design',
        "Web Design in Practice - Let's apply what we've learnt!"
      ]
    }
  },
  {
    'Day 66': {
      'main_heading': ' Building Your Own API with RESTful Routing',
      'all_title': [
        'Day 66 Goals: Build Your Own REST API Service',
        'What is REST?',
        'Download the Starting Project',
        'HTTP GET - a Random Cafe',
        'HTTP GET - All the Cafes',
        'HTTP GET - Find a Cafe',
        'Postman - The all in one API Testing Tool',
        'HTTP POST - A New Cafe',
        'HTTP PUT vs. PATCH',
        "HTTP PATCH - A Cafe's Coffee Price",
        "HTTP DELETE - A Cafe that's Closed",
        'Build Documentation for Your API'
      ]
    }
  },
  {
    'Day 67': {
      'main_heading': ' RESTful Routing',
      'all_title': [
        'Day 67 Goals: Building a RESTful Blog with Editing!',
        'Download the Starting Project',
        'Requirement 1 - Be Able to GET Blog Post Items',
        'Requirement 2 - Be Able to POST a New Blog Post',
        'Requirement 3 - Be Able to Edit Existing Blog Posts',
        'Requirement 4- Be Able DELETE Blog Posts'
      ]
    }
  },
  {
    'Day 68': {
      'main_heading': ' Authentication with Flask',
      'all_title': [
        'Day 68 Goals - Login and Registering Users with Authentication',
        'What is Authentication?',
        'Download the Starting Project',
        'Register New Users',
        'Downloading Files',
        'Encryption and Hashing',
        'How to Hack Passwords 101',
        'Salting Passwords',
        'Hashing and Salting Passwords using Werkzeug',
        'Authenticating Users with Flask-Login',
        'Flask Flash Messages',
        'Passing Authentication Status to Templates'
      ]
    }
  },
  {
    'Day 69': {
      'main_heading': ' Adding Users',
      'all_title': [
        'Day 69 Goals - Adding Users to Our Blog Project',
        'Download the Starting Project',
        'Requirement 1 - Register New Users',
        'Requirement 2 - Login Registered Users',
        'Requirement 3 - Protect Routes',
        'Creating Relational Databases',
        'Requirement 4 - Allow Any User to Add Comments to BlogPosts'
      ]
    }
  },
  {
    'Day 70': {
      'main_heading': ' Git, Github and Version Control',
      'all_title': [
        'The Terminal - use either VS Code or PyCharm',
        'Install Git Bash on Windows',
        'Introduction to Version Control and Git',
        'Version Control using Git and the Command Line',
        'Github and Remote Repositories',
        'Gitignore',
        'Cloning',
        'Branching and Merging',
        'Optional Git Challenge',
        'Forking and Pull Requests'
      ]
    }
  },
  {
    'Day 71': {
      'main_heading': ' Deploying Your Web Application',
      'all_title': [
        'Day 71 Goals - Learn to Deploy Your Website',
        'Add a .gitignore file (or download the starting files)',
        'Use git to add version control to your project',
        'Use environment variables to store sensitive information',
        'Setup a WSGI server with gunicorn',
        'Push to your remote on Github',
        'Sign up to a hosting provider and create your web service',
        'Upgrade SQLite Database to PostgreSQL'
      ]
    }
  },
  {
    'Day 72': {
      'main_heading': ' Data Exploration with Pandas: College Major v.s. Your Salary',
      'all_title': [
        'Day 72 Goals: what you will make by the end of the day',
        'Getting Set Up for Data Science',
        'Upload the Data and Read the .csv File',
        'Preliminary Data Exploration and Data Cleaning with Pandas',
        'Accessing Columns and Individual Cells in a Dataframe',
        'Solution: Highest and Lowest Earning Degrees',
        'Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk',
        'Solution: Degrees with the Highest Potential',
        'Grouping and Pivoting Data with Pandas',
        'Learning Points & Summary'
      ]
    }
  },
  {
    'Day 73': {
      'main_heading': ' Data Visualisation with Matplotlib: Programming Languages',
      'all_title': [
        'Day 73 Goals: what you will make by the end of the day',
        'Download and Open the Starter Notebook',
        'Solution: Preliminary Data Exploration',
        'Solution: Analysis by Programming Language',
        'Data Cleaning: Working with Time Stamps',
        'Data Manipulation: Pivoting DataFrames',
        'Data Visualisation with Matplotlib',
        'Multi-Line Charts with Matplotib',
        'Smoothing out Time-Series Data',
        'Programming Language Data Analysis',
        'Learning Points & Summary'
      ]
    }
  },
  {
    'Day 74': {
      'main_heading': ' Aggregate & Merge Data with Pandas: Analyse the LEGO Dataset',
      'all_title': [
        'Day 74 Goals: what you will make by the end of the day',
        'Use HTML Markdown to Make Your Notebook Look Pretty',
        'Solution: Exploring the LEGO Brick Colours',
        'Find the Oldest and Largest LEGO Sets',
        'Visualise the Number of Sets Published over Time',
        'How to use the Pandas .agg() function',
        'Superimposing Line Charts with Separate Axes',
        'Scatter Plots: Average Number of Parts per LEGO Set',
        'Relational Database Schemas: Primary and Foreign Keys',
        'How to Merge DataFrames and Create Bar Charts',
        'Learning Points & Summary'
      ]
    }
  },
  {
    'Day 75': {
      'main_heading': ' Google Trends Data: Resampling and Visualising Time Series',
      'all_title': [
        'Day 75 Goals: what you will make by the end of the day',
        'Data Exploration - Making Sense of Google Search Data',
        'Data Cleaning - Resampling Time Series Data',
        'Data Visualisation - Tesla Line Charts in Matplotlib',
        'Using Locators and DateFormatters to generate Tick Marks on a Time Line',
        'Data Visualisation - Bitcoin: Line Style and Markers',
        'Data Visualisation - Unemployment: How to use Grids',
        'Data Visualisation - Unemployment: The Effect of New Data',
        'Learning Points & Summary'
      ]
    }
  },
  {
    'Day 76': {
      'main_heading': ' Beautiful Plotly Charts & Analysing the Android App Store',
      'all_title': [
        'Day 76 Goals: what you will make by the end of the day',
        'Data Cleaning: Removing NaN Values and Duplicates',
        'Preliminary Exploration: The Highest Ratings, Most Reviews, and Largest Size',
        'Data Visualisation with Plotly: Create Pie and Donut Charts',
        'Numeric Type Conversions for the Installations & Price Data',
        'Plotly Bar Charts & Scatter Plots: The Most Competitive & Popular App Categories',
        'Extracting Nested Column Data using .stack()',
        'Grouped Bar Charts and Box Plots with Plotly',
        'Learning Points & Summary'
      ]
    }
  },
  {
    'Day 77': {
      'main_heading': 'Dimensional Arrays',
      'all_title': [
        'Day 77 Goals: what you will make by the end of the day',
        "NumPy's ndarray - Incredible Power at Your Fingertips!",
        'Generating and Manipulating ndarrays',
        'Broadcasting, Scalars and Matrix Multiplication',
        'Manipulating Images as ndarrays',
        'Learning Points & Summary'
      ]
    }
  },
  {
    'Day 78': {
      'main_heading': ' Linear Regression and Data Visualisation with Seaborn',
      'all_title': [
        'Day 78 Goals: what you will make by the end of the day',
        'Explore and Clean the Data',
        'Investigate the Films that had Zero Revenue',
        'Filter on Multiple Conditions: International Films',
        'Seaborn Data Visualisation: Bubble Charts',
        'Floor Division: A Trick to Convert Years to Decades',
        'Plotting Linear Regressions with Seaborn',
        'Use scikit-learn to Run Your Own Regression',
        'Learning Points & Summary'
      ]
    }
  },
  {
    'Day 79': {
      'main_heading': ' Analysing the Nobel Prize with Plotly, Matplotlib & Seaborn',
      'all_title': [
        'Day 79 Goals: what you will make by the end of the day',
        'Update Packages in Google Colab & Explore and Clean the Dataset',
        'plotly Bar & Donut Charts: Analyse Prize Categories & Women Winning Prizes',
        'Using Matplotlib to Visualise Trends over Time',
        'A Choropleth Map and the Countries with the Most Prizes',
        'Create Sunburst Charts for a Detailed Regional Breakdown of Research Locations',
        'Unearthing Patterns in the Laureate Age at the Time of the Award',
        'Learning Points & Summary'
      ]
    }
  },
  {
    'Day 80': {
      'main_heading': 'Tests & Distributions',
      'all_title': [
        'Day 80 Goals: what you will make by the end of the day',
        'Preliminary Data Exploration and Visualising Births & Deaths at Vienna Hospital',
        'Analysing the Yearly Data Split By Clinic',
        'The Effect of Handwashing',
        'Visualising Distributions and Testing for Statistical Significance',
        'Learning Points & Summary'
      ]
    }
  },
  {
    'Day 81': {
      'main_heading': ' Predict House Prices',
      'all_title': [
        'Day 81 Goals: what you will make by the end of the day',
        'Solution & Learning Points'
      ]
    }
  },
  {
    'Day 82': {
      'main_heading': ' [Python Scripting]',
      'all_title': [
        'The Road to Becoming a Professional Developer',
        'Text to Morse Code Converter'
      ]
    }
  },
  {
    'Day 83': {
      'main_heading': ' [Python Web Development]',
      'all_title': [
        'Where are the Videos and the Solution Code?',
        'Portfolio Website'
      ]
    }
  },
  {
    'Day 84': {
      'main_heading': ' [Python Scripting]',
      'all_title': [
        'Tic Tac Toe'
      ]
    }
  },
  {
    'Day 85': {
      'main_heading': ' [GUI]',
      'all_title': [
        'Image Watermarking Desktop App'
      ]
    }
  },
  {
    'Day 86': {
      'main_heading': ' [GUI]',
      'all_title': [
        'Typing Speed Test'
      ]
    }
  },
  {
    'Day 87': {
      'main_heading': ' [Game]',
      'all_title': [
        'Breakout Game'
      ]
    }
  },
  {
    'Day 88': {
      'main_heading': ' [Web Development]',
      'all_title': [
        'Cafe and Wifi Website'
      ]
    }
  },
  {
    'Day 89': {
      'main_heading': ' [Web Development]',
      'all_title': [
        'Todo List'
      ]
    }
  },
  {
    'Day 90': {
      'main_heading': ' [GUI Desktop App]',
      'all_title': [
        'Disappearing Text Writing App'
      ]
    }
  },
  {
    'Day 91': {
      'main_heading': ' [HTTP Requests & APIs]',
      'all_title': [
        'Convert PDF to Audiobook'
      ]
    }
  },
  {
    'Day 92': {
      'main_heading': ' [Image Processing & Data Science]',
      'all_title': [
        'Image Colour Palette Generator'
      ]
    }
  },
  {
    'Day 93': {
      'main_heading': ' [Web Scraping]',
      'all_title': [
        'Custom Web Scraper'
      ]
    }
  },
  {
    'Day 94': {
      'main_heading': ' [GUI Automation]',
      'all_title': [
        'Automate the Google Dinosaur Game'
      ]
    }
  },
  {
    'Day 95': {
      'main_heading': ' [Game]',
      'all_title': [
        'Space Invaders'
      ]
    }
  },
  {
    'Day 96': {
      'main_heading': ' [HTTP Requests & APIs]',
      'all_title': [
        'Custom API Based Website'
      ]
    }
  },
  {
    'Day 97': {
      'main_heading': ' [Web Development]',
      'all_title': [
        'An Online Shop'
      ]
    }
  },
  {
    'Day 98': {
      'main_heading': ' [Python Automation]',
      'all_title': [
        'Custom Automation'
      ]
    }
  },
  {
    'Day 99': {
      'main_heading': ' [Data Science]',
      'all_title': [
        'Analyse and Visualise the Space Race'
      ]
    }
  },
  {
    'Day 100': {
      'main_heading': ' [Data Science]',
      'all_title': [
        'Analyse Deaths involving Police in the United States'
      ]
    }
  },
  {
    'Final Stretch': {
      'main_heading': 'Final Stretch',
      'all_title': [
        'Recording of our Live AMA (aka AAA - Ask Angela Anything)',
        'Study With Me',
        'Bonus Lecture: Check out my other courses'
      ]
    }
  }
]

@app.route("/python100days")
def say_bye():
    return udemy_data


if __name__== "__main__":
    # This requires stopping and starting the server for changes to take effect
    # app.run()
    # instead run with debug on
    app.run(debug=True)
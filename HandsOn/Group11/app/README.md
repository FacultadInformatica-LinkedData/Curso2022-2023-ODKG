# Madrid Commemorative Plaques

The application allows users to locate on a map the different commemorative plaques in Madrid. 
By hovering over each plaque icon, a window with general information about the relevant historical person will be displayed.
In addition, links to pages with more important information about the historical person will be included.

## User's interface
![User UI](../img/cap.png?raw=true)

## Installation and use
1. **Python** and **pip** are required (please, use Python 3, for your own good).
2. Using a virtual environment is VERY recommended.
   1. First, install the module (**virtualenv**) with your distributon packet manager 
   2. Then, create a new virtual environment with the command `virtualenv app_env`
   3. And now, enter the virtual environment by running `source ./app_env/bin/activate`
3. Install the required dependecies using the command `pip install -r requirements.txt`
4. Deploy the Helio server
5. Establish the following environment variables in the app directory
   1. *APP_HOST* (default: 127.0.0.1)
   2. *APP_PORT* (default: 8080)
   3. *HELIO_SERVER*
6. Deploy the web-app with the command `python run.py`

## License:
[Creative Commons 2.5 (CC BY-NC 2.5 ES)](https://creativecommons.org/licenses/by-nc/2.5/es/)

## Simple Example of Django Abstract Classes

### Using the example from the Django Project documentation [Abract Base Classes](https://docs.djangoproject.com/en/3.2/topics/db/models/#abstract-base-classes)

### Clone project
`$ git clone git@github.com:diek/AbstractDjango.git`


### Move into project folder
`$ cd AbstractDjango`

### Create a virtual environment (this can be created elsewhere if you prefer, and understand how)
`$ python3 -m venv _env`

### Activate the virtual environment you have just created
* Linux & Mac  (Zsh/Bash, Fish)
`$ source _env/bin/activate`
`$ source _env/bin/activate.fish`

* Windows
`C:\workspace>_env\Scripts\activate.bat`


### Install Development Requirements
`$ pip install -r requirements.txt`

### Environment Variables
1. Rename `.env.example` => `.env`
1. Edit SECRET_KEY

### Add project tables and intitial data to database
1.    `$ ./manage.py migrate student_tracker`
1.    `$ ./manage.py migrate`


### Load data related to student_tracker
1.    `$ ./manage.py loaddata student_data.json`
1.    `$ ./manage.py loaddata teacher_data.json`

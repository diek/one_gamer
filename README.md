## Simple Example of Multiple Choice Quiz

### Clone project into your workspacee
`$ git clone git@github.com:diek/one_gamer.git`

### Move into project folder
`$ cd one_gamer`

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
1.    `$ ./manage.py migrate gamerr`
1.    `$ ./manage.py migrate`


### Load data related to gamee
1.    `$ ./manage.py loaddata quiz`
1.    `$ ./manage.py loaddata question`
1.    `$ ./manage.py loaddata answer`

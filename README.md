# fb-clone
A clone of facebook as full stack project.

## Server

` service postgres  status `
1. Check postgres server status

` sudo service postgresql start `
2. Start postgresql server

` sudo su - postgres `
3. Connect postgresql

#### sqlalchemy

` create_engine('postgresql://username:password@host:port/database') `

## Login
Note: Google onSignIn function not working with adblock/ghostery

## Run Site
Run the site with ` python3 facebook.py `
Browse site at ` http://localhost:8000 `

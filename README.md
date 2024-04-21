# demo

## Requirements
- Docker
- Everything else should just work...

##Building the demo

1. Using the Makfile run `make build`  this will run the docker-compose files to create the database container and the webapp container.
2. Running `make up` will start the web app and database. 
3. The database is initially created with a few models/tables
4. The database is seeded with a few providers to populate the start point drop down, Gusto, ADP Run, and Bamboo HR
5. Visit in browser on 127.0.0.1:8000

## General Application Flow

1. A user can select from a list of providers to connect to.
2. Upon selecting a provider the appserver checks if we have information saved in the database (namely the api-key [real world this would be in vault, KMS, etc]), if not it will provision a sandbox per the Finch API Sandbox documentation and save the API Key for re-use on subsequent calls and sessions (assuming the db container is not tore down)
3. Upon clikcing submit we load a company details page that's a dynamically built table based on the returned data. The goal behind it being dynamic is that irrespective of the returned values, we will display all available data. 
4. Above the company's information there's a direcotry button (placed at the top as the table could become long, depending on amount of data)
5. The directory page pre-populates a dropdown with employee information, upon selecting an employee we want to dynamically load additional information about that employee - individual and employment details.

## Future Work

1. Add authentication (was going to start this up front, but had to leave it off)
2. Commit response to the database so that we don't need to keep things in memory and can periodically check data freshness using epoch timestamps.
3. Add support for updating and creating employee records (form fields, etc)
4. 
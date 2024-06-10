# Demo
## Requirements
- Podman
- Everything else should just work...
Building the Demo
1. Using the Makefile, run make build. This will run the docker-compose files to create the database container and the webapp container.
2. Run make up to start the web app and database.
3. The database is initially created with a few models/tables.
4. The database is seeded with a few providers to populate the starting point dropdown: Gusto, ADP Run, and Bamboo HR.
5. Visit the application in your browser at 127.0.0.1:8000.
## General Application Flow
1. A user can select from a list of providers to connect to.
2. Upon selecting a provider, the app server checks if the information (namely the API key) is saved in the database. In a real-world scenario, this would be stored securely in a vault, KMS, etc. If the information is not found, the app server provisions a sandbox per the Finch API Sandbox documentation and saves the API key for reuse on subsequent calls and sessions (assuming the database container is not torn down).
3. Upon clicking submit, the user is directed to a company details page that displays a dynamically built table based on the returned data. The goal behind the dynamic table is to display all available data, regardless of the specific values returned.
4. Above the company's information, there is a directory button (placed at the top as the table could become long, depending on the amount of data).
5. The directory page pre-populates a dropdown with employee information. Upon selecting an employee, additional details about that employee (individual and employment details) are dynamically loaded.
## Future Work
1. Add authentication (this was initially planned but had to be left out).
2. Commit responses to the database so that data can be persisted without relying on in-memory storage. This allows for periodic checks of data freshness using epoch timestamps.
3. Add all relevant models, to the database for storing, reducing api calls made / prevent everything from being in memory only.

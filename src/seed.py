# seed.py
from database import db_session
from models import Provider


def seed_providers():

    # Define the initial provider data
    providers = [
        Provider(finch_id='gusto', name='Gusto'),
        Provider(finch_id='adp_run', name='ADP Run'),
        Provider(finch_id='bamboo_hr', name='Bamboo HR'),
        # Add more providers as needed
    ]

    # Add the providers to the session
    db_session.add_all(providers)

    # Commit the changes to the database
    db_session.commit()

    # Close the session
    db_session.close()

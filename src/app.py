from flask import Flask, render_template
from flask import flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database import db_session
from models import Provider, Company, Individual
import requests
from functools import wraps



#create db
from database import init_db
from seed import seed_providers

#Give the db some time
db_ready = False 
while not db_ready: 
    try:
        init_db()
        db_ready = True
        
    except:
        pass
seed_providers()

BASE_API= 'https://sandbox.tryfinch.com/api/employer/'




app = Flask(__name__)


# # Index
@app.route('/')
def index():
    providers = db_session.query(Provider).all()

    if len(providers) > 0:
        return render_template('home.html', providers=providers)
    else:
        msg = 'No Providers Found' 
        return render_template('home.html', msg=msg)

@app.route('/submit_provider', methods=['POST'])
def submit_provider():
    selected_provider = request.form['option']
    flash(f'Selected Provider: {selected_provider}')
    return redirect(url_for('company', provider=selected_provider))

@app.route('/company/<provider>', methods=['GET'])
def company(provider):
    provider_record = db_session.query(Provider).filter(Provider.name == provider).first()
    
    if provider_record.finch_api_key is not None:
        response = requests.get(BASE_API + '/company', headers={"Authorization": "Bearer %s" % provider_record.finch_api_key,
        "Content-Type": "application/json"})
        if response.status_code == 200:
            company_record = response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
        return render_template('company.html', company_record=company_record)
    
    else:
        api_key = get_new_api_key(provider_record.finch_id)
        
        #save api key to reuse if we keep db up
        provider_record.finch_api_key =  api_key
        db_session.commit()

        response = requests.get(BASE_API + '/company', headers={"Authorization": "Bearer %s" % api_key,
        "Content-Type": "application/json"})
        
        if response.status_code == 200:
            company_record = response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
        return render_template('company.html', company_record=company_record)
    
@app.route('/company/<provider>/directory', methods=['POST','GET'])
def retrieve_directory(provider):
    print(provider)
    api_key = db_session.query(Provider).filter(Provider.name == provider).first().finch_api_key
    response = requests.get(BASE_API + '/directory', headers={"Authorization": "Bearer %s" % api_key, "Content-Type": "application/json"})

    if response.status_code == 200:
        directory_records = response.json()
        return render_template('directory.html', directory_records=directory_records)
    else:
        print(f"Request failed with status code {response.status_code}")
        return "Request failed"



def get_new_api_key(provider):
    url = "https://sandbox.tryfinch.com/api/sandbox/create"
    headers = {
    "Content-Type": "application/json"
    }
    data = {
    "provider_id": "%s" % provider,
    "products": ["company", "directory", "individual", "employment"],
    "employee_size": 35
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return "New API Key not retrieved"


if __name__ == '__main__':
    app.secret_key='randomsecretkeyforsecurity'
    app.run(host='0.0.0.0',port=8000,debug=True)
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load datasets
investors_df = pd.read_csv('investors.csv')
incubators_df = pd.read_csv('incubators.csv')

def preprocess_datasets(df, startup_input, entity_type):
    df['Industry Match'] = df['Industry'].str.lower() == startup_input['industry'].lower()
    df['Stage Match'] = df['Stage'].str.lower() == startup_input['stage'].lower()

    if entity_type == 'Investor':
        df['Funding Match'] = (
            (df['Minimum Investment'] <= startup_input['funding']) 
            & (df['Maximum Investment'] >= startup_input['funding'])
            if startup_input['funding'] else True
        )
    else:  # Incubators
        df['Funding Support Match'] = df['Funding Support'].str.lower() == 'yes'

    return df

def match_startup(startup_input):
    investors = preprocess_datasets(investors_df.copy(), startup_input, 'Investor')
    incubators = preprocess_datasets(incubators_df.copy(), startup_input, 'Incubator')

    matches = {'Industry': [], 'Stage': [], 'Potential': []}

    if startup_input['preferred_entity'] == 'Investor':
        matches['Industry'] = investors[investors['Industry Match']].to_dict(orient='records')
        matches['Stage'] = investors[investors['Stage Match']].to_dict(orient='records')
        matches['Potential'] = investors[
            investors['Industry Match'] & investors['Stage Match'] & investors['Funding Match']
        ].to_dict(orient='records')
    else:
        matches['Industry'] = incubators[incubators['Industry Match']].to_dict(orient='records')
        matches['Stage'] = incubators[incubators['Stage Match']].to_dict(orient='records')
        matches['Potential'] = incubators[
            incubators['Industry Match'] & incubators['Stage Match'] & incubators['Funding Support Match']
        ].to_dict(orient='records')

    return matches

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    startup_input = {
        'name': request.form['name'],
        'industry': request.form['industry'],
        'stage': request.form['stage'],
        'preferred_entity': request.form['preferred_entity'],
        'funding': int(request.form['funding']) if request.form.get('funding') else 0,
        'needs_funding': request.form['needs_funding'] == 'Yes',
    }

    matches = match_startup(startup_input)
    return render_template(
        'result.html', 
        preferred_entity=startup_input['preferred_entity'], 
        final_matches=matches
    )

if __name__ == '__main__':
    app.run(debug=True)

from pathlib import Path
from sklearn.externals import joblib

import pandas as pd
import constants

CURRENT_DIR = Path(__file__).parent.absolute()


def test_trained_model__with_given_attibutes(attributes_type):
    MODEL_PATH = CURRENT_DIR / 'model' / \
        f'gradient_boosting_classifier_{attributes_type}.pkl'
    PIPELINE_PATH = CURRENT_DIR / 'pipeline' / \
        f'transform_pipeline_{attributes_type}.pkl'

    # Load the model
    model = joblib.load(MODEL_PATH)

    # Load the pipeline
    preprocess_pipeline = joblib.load(PIPELINE_PATH)

    # Create the pandas DataFrame
    df = pd.DataFrame(constants.test_data[attributes_type],
                      columns=constants.test_data[attributes_type].keys())

    X_test = preprocess_pipeline.transform(df)

    output = model.predict(X_test)
    formatted_output = ["no" if x == 0 else "yes" for x in output]
    print(formatted_output)


test_trained_model__with_given_attibutes(constants.all)
test_trained_model__with_given_attibutes(constants.bank_data)

"""
Run tests on the data.  Used when submitting the answer.
"""

import argparse
from algo import Algorithm
import pandas as pd
import settings
from sklearn.metrics import mean_squared_error
import math
import pep8
from StringIO import StringIO
import sys
import time
import json

# Parse input arguments.
parser = argparse.ArgumentParser(description='Test code to see if it works.')
parser.add_argument('train_file', type=str, help='The training file to use.')
parser.add_argument('prediction_file', type=str, help='The file to make predictions on.')
parser.add_argument('--write', default=False, help='Whether to write results to a file.', action="store_const", const=True, dest="write")

if __name__ == "__main__":
    args = parser.parse_args()

    # Read the training file.
    with open(args.train_file) as f:
        train_df = pd.read_csv(f)

    with open(args.prediction_file) as f:
        prediction_df = pd.read_csv(f)

    start = time.time()
    # Initialize and train the algorithm.
    alg = Algorithm()
    alg.train(train_df, settings.PREDICTION_COLUMN)

    predictions = alg.predict(prediction_df)

    # Find how long it took to execute.
    execution_time = time.time() - start
    print("Execution time was {0} seconds.\n".format(execution_time))

    # We're using RMSE as a metric.
    error = math.sqrt(mean_squared_error(predictions, prediction_df[settings.PREDICTION_COLUMN]))
    print("Found root mean squared error of: {0}\n".format(error))

    # Setup a buffer to capture pep8 output.
    buffer = StringIO()
    sys.stdout = buffer

    # Initialize and run a pep8 style checker.
    pep8style = pep8.StyleGuide(ignore="E121,E123,E126,E226,E24,E704,E501")
    pep8style.input_dir(settings.BASE_DIR)
    report = pep8style.check_files()

    # Change stdout back to the original version.
    sys.stdout = sys.__stdout__

    pep8_results = buffer.getvalue()
    if report.total_errors > 0:
        print("Pep8 violations found!  They are shown below.")
        print("----------------------")
        print(pep8_results)

    # Write all the results to a file if needed.
    if args.write:
        write_data = {
            "error": error,
            "execution_time": execution_time,
            "pep8_results": pep8_results
        }
        with open(settings.RESULTS_FILE, "w+") as f:
            json.dump(write_data, f)

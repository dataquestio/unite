"""
This file exists to show how the data set was split into training, validation, and test sets.
"""

import pandas as pd
import settings
import numpy as np
import math


if __name__ == "__main__":
    # Open the raw data file that contains all the rows.
    with open(settings.RAW_DATA_FILE) as f:
        data = pd.read_csv(f)

    # Randomly shuffle the dataset.
    data.reindex(np.random.permutation(data.index))
    # Get rid of the old index column.
    data = data.iloc[:,1:]

    # Set a subset size -- valid set and test set are each 25% of the data, train set is 50%.
    subset_size = math.floor(data.shape[0] / 4)

    # Split the data up into sets.
    valid_set = data.iloc[:subset_size]
    test_set = data.iloc[subset_size:(subset_size*2)]
    train_set = data.iloc[(subset_size*2):]

    # Write all of the sets to their respective files.
    with open(settings.TRAIN_DATA_FILE, "w+") as f:
        train_set.to_csv(f, index=False)

    with open(settings.VALID_DATA_FILE, "w+") as f:
        valid_set.to_csv(f, index=False)

    with open(settings.TEST_DATA_FILE, "w+") as f:
        test_set.to_csv(f, index=False)

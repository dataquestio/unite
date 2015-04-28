Unite
----------------

**What is this?**   This is an open data science contest.  The goal is to learn through collaboration.  Anyone is welcome to participate, and there are many different ways to do so.

**What will we be doing?** The ultimate goal is to predict the scores given to products by reviewers on amazon based on the text of the reviews.

**How can I participate?** Anyone can contribute, and this includes improving the algorithm, adding in visalizations, commenting on code, refactoring, starting discussions, and other helpful things you think of.  To get started, just fork the repo and open a pull request.  All code is written in python 2.7.

**How will we be scored?** Everyone will accumulate points based on their contributions.  You can find the point leaderboard [here](http://unite.dataquest.io/f/leaderboard/dataquestio/unite).  Points are assigned based on a few criteria, including opening a pull request (PR), having a PR merged, and having a lower error rate than anyone else. The contest will run until July 31st.  The total prize pool for the top 3 finishers is 400 dollars.

### The problem

We'll be predicting the score (0-5) given to a product by an amazon reviewer based on the text and summary of the review.  The data is originally from the Stanford Large Network Dataset Collection.  

We'll be using root mean squared error as the evaluation metric.  The algorithm performance will be evaluated by a continuous integration server using a hidden test set.  Whenever you open a pull request, the server will check your code.

### Why make this

This is an experiment to see if we can help people learn and improve their practical data science skills through open contests.

How to get started
-------------------

Getting started is a pretty simple process.  Before you get started, you should have python 2.7 installed.  Using a virtualenv is optional but recommended.

1. Fork this repo to your github account.
2. Clone your fork locally (`git clone git@github.com:YOUR_USERNAME/unite.git`)
3. Get into the unite folder (`cd unite`)
4. Install the python requirements (`pip install -r requirements.txt`)
5. Run the tests on the validation set (`python test.py data/train.txt data/valid.txt`)
    * This will train the current algorithm using the training set, and then make predictions on the validation set.
    * It will also run pep8 to check code quality.
6. Add your contributions!  Make the code better.
7. When you're ready, and the tests pass, make a PR from your fork to the main repo.
    * If your code takes more than 15 minutes to run, it will result in an error when the server runs it.
    * The maximum available memory for your code is 4 gigs.
8. Your PR will automatically get picked up by the server, and your code will be run.  After it is finished running, the status of the PR will be updated, reflecting whether or not the code passed.

Point Assignment
------------------

Right now, you get:

* 2 points for opening a PR.
* 10 points if your error is lower than the global minimum (across all open, unmerged, and merged PRs)
    * Note: You have to open a PR to get this -- just working on a fork isn't enough.
    * This also applies to pushes to existing PRs.
* 4 points for getting a PR merged.

Opening too many PRs or pushing without meaningful contributions can result in disqualification.

File structure
-------------------

* `data` -- this folder contains the raw training and validation data.
    * `train.txt` -- raw training data.
    * `valid.txt` -- raw validation data. 
* `algo.py` -- this contains the main algorithm class that is used to train and evaluate.
    * The algorithm doesn't have to be restricted to this file -- feel free to make other files and import from them.
* `settings.py` -- this contains various settings that can be called from other modules.
* `split_data.py` -- this file documents how the data was originally split up and anonymized.
    * Don't edit this file.
* `test.py` -- this file allows you to test the error rate of your approach, and is used to evaluate your submission.
    * Don't edit this file -- it's used to compute error.

Merge conflicts
------------------

We'll be merging pull requests on a "first reasonable pull request will be merged" basis.  This will probably lead to cases where later PRs can't be merged due to conflicts.  If this happens, you can update your PR after rebasing onto master.

If you want to work on a unique approach on your own unmergeable fork, you can feel free to do that and open a PR -- this will enable you to get the 10 points for lowest error, but will prevent you from getting any merge points.

Suggestions?
-------------------

This is an experiment and will likely evolve a lot over time.  If you have any questions or suggestions, please open an issue.  You can also think of the issues as a discussion board to talk about new approaches.

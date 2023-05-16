# <center> Lab4: Supervised Learning Algorithm. </center>

## MileStones

- [Ok ] Clarifications

- [OK ] Naive Bayes Algorithm

- [OK ] KNN Algorithm

- [ ] K-means

---
## Clarification

This a program demonstrating two supervised learning algorithms: kNN and Naive Bayes', and K-means clustering.

---


## class


## APIs (Use Cases)

---

## Inputs (applies to both Supervised Learning algorithms)

Both the test and training file will be a csv file where each line represents one 'record'.  There will be no header line.

The last entry in a row is the label, and can be any alphanumeric identifier including '_', the rest of the entries are integer extracted features. e.g.

1,5,7,3,ocean_view

In this case there are 4 predictive attributes.

Note: every line in both files should have the same number of columns or it is an error.

Also: There will be no null entries for predictive attributes to worry about.

---

## kNN (using euclidean distance-squared, weighted)

For k-nearest neighbor, there is no training, you just parse and load the file into memory, then use it for classification.

As discussed in class, for each each test point you compute the distance to each training point, picking the K nearest ones and they then

"vote" on the classification using a weight of 1 over the distance.  For distance we will use euclidean squared between two points:

For example of there are 3 predictive attributes: D(1, y1, z1>, 2,y2, z2>) = (z2-z1)2 + (y2-y1)2 + (x2-x1)2

You then compare the predicted label to the actual one and record for later metrics.

## Naive Bayes'

For training you should load the training file into memory, but then compute all of the conditional and pure probabilities in advance (including laplacian smoothing if applicable).

Then when doing predictions on the test file, you do the argmax as per class to predict a label, recording versus the actual one for later metrics.

## kMeans Algorithm [Extra Credit-only]

`learn -train some-input.txt 0,500 200,200 1000,1000`

KMeans is inferred from the number of centroids provides, so 3 in the above example.

Note: the centroids are separate args with "," and should be of the same dimensionality as the data

The training file will be a csv consisting of integer data points in any N dimensional plane

Each line will contain N comma-separated integer points plus a final alphanumeric 'label' used for printing

The points should all have the same N dimensions which also match the given centroids.

The number of centroids "K" is inferred from the command-line input.

Run kMeans using the chosen distance function, alternating clustering and re-computing centroids until the centroids converge and do not change.

kMeans Output
The program should output the final centroids using cluster-number aliases (C1, C2, C3, ...), and then print how the inputs were clustered by label.

Output

Both algorithms should record: true positives, false positives, and negatives so that you can compute precision and recall.

Once the test set has been evaluated you then print out precision and recall as frequencies in fraction form.  e.g. (Also see examples)

*Label=A Precision=2/3 Recall=2/3*

*Label=B Precision=2/3 Recall=2/3*


---

## Compiling
To Compile my program:


- I'm using python3 for this Lab.
- Need to first install `pip3 install pandas==1.4.2`
- main.py is my main generator.

- train : the training file (more below)
- test : the testing data file (not used in kMeans)
- K : if > 0 indicates to use kNN and also the value of K (if 0, do Naive Bayes')
- C : if > 0 indicates the Laplacian correction to use (0 means don't use one)
- [optional] a -v verbose flag that outputs each predicted vs actual label (could be useful for testing, but not required)
- d e2 or d manh [EC-only] indicating euclidean distance squared or manhattan distance to use
- arguments(EC-only): if a list of centroids is provided those should be used for kMeans

Note: 

- it is illegal for both K and C to be greater than 0 (they both default to 0)

- In this program, I assume all the input file is well formatted. 

eg:

`python3 main.py -t 0.0001 -i 100 some-input.txt`

`python3 main.py -d 0.9 -t 0.0001 -i 150 input.txt`

`python3 main.py -m -tol 0.0001 -i 150 input.txt`

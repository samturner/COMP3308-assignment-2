#COMP3308 Assignment 2 Report

## 1. Aim

The aim of this study was to demonstrate an understanding of Bayesian Networks and inference. The concept of Bayesian Networks are extremely important because they model variables and their relationships over a given domain. As such, they can be used to answer probabilistic queries about a domain. Bayesian Networks are a method for applying Bayes' Theorem to complex problems thus making them simpler to understand.


## 2. Methodology
 *Bayesian Network* - A Bayesian Network is a probabilistic graphical model that represents a set of random variables (shown as nodes on the graph), and their probabilistic dependencies (represented as graph edges). Bayesian Networks are directed, acyclic graphs.

*Variable Elimination* - Allows us to significantly improve the performance of inference by enumeration by eliminating repeated calculations. Variable elimination works by doing summations over each variable only for those portions of the expression that depend on a variable. This allows us to 'explain away' variables one at a time.

*Likelihood Weighting* - A useful method in Bayesian inference that allows us to avoid the inefficiency of rejecting samples by only generating events that are consistent with the evidence. Each event if weighed by the likelihood that it agrees with the evidence.

## 3. Results and Discussion

## Question 1

**a) Construct and show the equivalent graphical model**

The Bayesian Network for this relationship can be shown below:

![Fig 1. Bayesian Network](comp_3308_2_diag_1.png)

Where:

$$$m$$$ - Metastatic Cancer;

$$$b$$$ - Brain Tumor;

$$$i$$$ - Increased Serum Calcium;

$$$c$$$ - Coma and

$$$s$$$ - Severe Headaches

**b) What is the prior probability of coma $$$P(C)$$$?**

The prior probability of Coma is:

$$
P(C) = 0.296
$$

and therefore:

$$
P(\neg C) = 0.704
$$


**c) What is the probability of metastatic cancer given the patient has severe headaches and has not fallen into a coma?**

The probability of metastatic cancer given the patient has severe headaches and has not fallen into a coma is:

$$
P(M | S = true ,C = false) = 0.102
$$

**d) What is the Markov Blanket of Coma?**

$$$C$$$ has no child nodes, therefore the Markov Blanket for $$$C$$$ is the parent nodes of $$$C$$$, $$$B$$$ and $$$I$$$.

**e) Are increased total serum calcium and brain tumor independent given coma? Explain.**

Any node is conditionally independent of its children given its parents. Therefore, as Increased Serum Calcium $$$I$$$ and Brain Tumor $$$I$$$ have Coma $$$C$$$ as a common child, they are not independent, $$$C$$$ relies on the inputs of $$$I$$$ and $$$B$$$.

**f) What is the probability of fallen into a coma given the patient has metastatic cancer?**

The probability that a patient is in a coma given they have metastatic cancer is:

$$P(C| m = true) = 0.206$$

## Question 2

**a)**

Show that the equation:

$$
P(C, X_i,..., X_n) = P(C) \prod_{i=1}^{n}P(x_i|c)
$$

Satisfies the independence assumption of the graph which is that: $$$X_i,...,X_n$$$ are *conditionally independent* given $$$C$$$.

Intuitively, this is because there are no edges connecting each child node of $$$C$$$, implying that each node $$$X_i,...,X_n$$$ are conditionally independent given $$$C$$$.

## Question 3

**a) List your random variables, explain the meaning of each, etc...**

![Fig. 2 - Car Diagnosis](comp_3308_2_diag2.png)

For this network, we have decided to model a car system. There are six random variables that are to be included, these are:

**Battery** $$$B$$$ - The state of the battery, it can have three possible states: *high*, *medium* or *low*. Prior probabilities of $$$B$$$ are as follows:

$$P(B = high) = 0.5$$
$$P(B = low) = 0.35$$
$$P(B = empty) = 0.15$$

**Radio** $$$R$$$ - The state of the radio, it can have two possible states: *on* or *off*. Conditional probabilities of $$$R$$$ are as follows:

$$P(R | B = high) = 0.383$$
$$P(R | B = low) = 0.27$$
$$P(R | B = empty) = 0.115$$

**Lights** $$$L$$$ - The state of the lights of the car, it can have three possible states: *bright*, *dim* or *off*. Conditional probabilities of $$$L$$$ are as follows:

$$P(L = bright | B = high) = 0.8$$
$$P(L = dim | B = high) = 0.1$$
$$P(L = off | B = high) = 0.1$$

$$P(L = bright | B = low) = 0.4$$
$$P(L = dim | B = low) = 0.5$$
$$P(L = off | B = low) = 0.1$$

$$P(L = bright | B = empty) = 0$$
$$P(L = dim | B = empty) = 0$$
$$P(L = off | B = empty) = 1$$

**Engine** $$$E$$$ - The state of the engine, it can have two possible states, either *on* or *off*. Conditional probabilities of $$$E$$$ are as follows:

$$P(E | F = high, B = high) = 0.86$$
$$P(E | F = high, B = low) = 0.09$$
$$P(E | F = high, B = empty) = 0.05$$

$$P(E | F = low, B = high) = 0.8$$
$$P(E | F = low, B = low) = 0.18$$
$$P(E | F = low, B = empty) = 0.02$$

$$P(E | F = empty, B = high) = 0.02$$
$$P(E | F = empty, B = low) = 0.01$$
$$P(E | F = empty, B = empty) = 0$$

**Fuel** $$$F$$$ - The state of the fuel in the car, it can have three possible states, either *high*, *low*, or *empty*. Prior probabilities of $$$F$$$ are as follows:

$$P(F = high) = 0.624$$
$$P(F = low) = 0.192$$
$$P(F = empty) = 0.184$$

**b) Explain the methodology used to construct such a network**

When beginning to construct the network, we decided on the Random Variables that would be needed, as indicated in part a of this question. The set of these variables, denoted by $$$S$$$ is shown below.

$$
S = {B, L, R, E, F, G}
$$

We then decided on sensible conditional and prior probabilities for these random variables. To construct the graph, from each random variable in $$$S$$$ we had to select a minimal set of parents that satisfy:

$$
P(X_i| X_{i-1},...,X_1) = P(X_i | Parents(X_i))
$$

This then resulted in the network that can be seen in *part a*. When selecting the values for conditional probabilities of each node, we had to make sure the independence assertion still held true.

Finally, we used `JavaBayes` to visualise and check our working and assumptions.

## Question 4

After building our graphical model in JavaBayes and observing `sprinkler` and `wetgrass` we received the following result:

$$P(cloudy | sprinkler, wetgrass) \approx 0.175$$

**For $$$N = 10$$$:**

* **Mean** -  0.048195
* **Standard Deviation** - 0.0152372285866

**For $$$N = 100$$$:**

* **Mean** - 0.04870908
* **Standard Deviation** - 0.00472681598474

**For $$$N = 1000$$$:**

* **Mean** - 0.048574179
* **Standard Deviation** - 0.00158516205259

**For $$$N = 5000$$$:**

* **Mean** - 0.048587418
* **Standard Deviation** - 0.000684174009208

As you can see, the mean in each case varies quite significantly from the result of $$$0.175$$$ that we received from JavaBayes. We found it difficult to verify if this was due to a bug in our code as we weren't sure how to test it correctly.

## 4. Conclusions

In conclusion, we found that Bayesian Networks and their associated algorithms such as *variable elimination* and *likelihood weighting* are great for learning and inference. The fact that they are a graphical model means that they are relatively easy to work with and understand. 

Our investigation needs further work, particularly for question four. We need to devise a way to be able to test our code to make sure that the results that we are getting are correct. To do this, we need to generate some test cases of known probabilities that we can compare with our output.

## 5. Reflection

In doing this assignment the most important thing we learned was about methods for inference in Bayesian Networks, namely *variable elimination* and *likelihood weighting* and the benefits and disadvantages of each. We learned that *variable elimination* (exponential complexity) is generally less efficient than *likelihood weighting* but may be appropriate for use with small data sets.

We also learned the methodology for constructing Bayesian Networks given a problem domain. We now understand the importance of outlining your random variables and constructing a network such that they mirror the independence criteria outlined in the domain.

## 6. How to Run
To run our code, simply use:
`python q4.py <m> <n>` where `m` is the number of runs, and `n` is the number of samples in each run. The program should output in the following format:

	starting m runs of n samples
	
	computed in <run time>
	len: <m>
	avg: <average probability>
	std: <standard deviation>

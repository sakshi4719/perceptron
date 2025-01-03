# Perceptron Model and Code Explanation

### What is a Perceptron?
- A **perceptron** is a basic machine learning model used for binary classification.
- It computes a weighted sum of input values, adds a bias, and passes the result through an activation function (often a step function).
- The output is a class label (typically 1 or -1), and the model learns by adjusting weights and bias during training to correctly classify input data.

### Code
- The perceptron starts with weights (`w1`, `w2`) and bias (`b`) initialized to zero.
- For each input sample (`x1[i]`, `x2[i]`), the perceptron calculates the weighted sum (`y_in`), then applies the activation function (`signum`) to decide the output (`y`).
- If the output (`y`) does not match the expected target (`t[i]`), the weights and bias are updated based on the learning rate (`alpha`), target (`t[i]`), and inputs.
- This process repeats until the model converges (no more updates to weights and bias).

I have implemented perceptron models for the AND gate, OR gate and a function specified in a textbook.

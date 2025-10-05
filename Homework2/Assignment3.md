 ### Chapter 5: Linear Regression

This chapter introduces the most fundamental regression model in supervised learning - linear regression. The core idea is to find a straight line or hyperplane that best represents the data trend to predict the output result.
The book first explains the structure of the model and the meaning of its parameters, and takes the least square method as the optimization objective to obtain the optimal parameters by minimizing the square error between the predicted values and the true values.
Subsequently, the author explained the convexity characteristics of the cost function from a geometric perspective and demonstrated the optimization process using the gradient descent method.
Through 3D image examples, readers can intuitively see the relationship between parameter variations and error surfaces.
At the end of this chapter, a Python implementation of linear regression is also presented. It adopts a modular programming approach, separating the model calculation from the cost function, which is convenient for subsequent expansion.


### Chapter 6: Linear Two-Class Classification

This chapter extends the idea of linear regression to binary classification tasks.
The author first explains the limitations of directly using regression methods for classification, and then introduces a logistic regression model and the Sigmoid function to establish classification boundaries.
The core cost function adopted is cross-entropy, whose convexity makes the model more likely to converge and obtain a stable solution.
The book explains the advantages of cross-entropy in dealing with classification problems by comparing the shapes of different cost functions.
Finally, this chapter deduces the gradient of cross-entropy and Hessian, and demonstrates the convergence process from the initial state to the optimal classification boundary using the gradient descent method.



### Chapter 7: Linear Multi-Class Classification

This chapter further extends logistic regression to multi-classification scenarios.
A one-to-many approach is adopted to train a classifier for each category respectively, and fusion rules are used to determine the final prediction result.
The book demonstrates through geometric diagrams how multiple linear decision boundaries divide regions in the input space, thereby achieving the distinction of multiple categories.
At the same time, it explains how the distance between the sample and each decision boundary reflects the confidence level of classification.
The chapter also introduces the matrix representation method and training process of the model, making multi-class logistic regression more systematic both in theory and implementation.


### Chapter 9: Feature Engineering and Selection

This chapter focuses on the construction and selection of features, that is, how to improve model performance through reasonable feature representation.
The author introduces a variety of feature engineering methods, including single-hot coding, bag-of-words model, histogram features of images and audio, as well as feature scaling, etc.
This chapter also explains the application of regularization and Boosting techniques in feature selection, illustrating how they enhance the generalization ability of the model and prevent overfitting.
In addition, the book compares the different characteristics of three dimensionality reduction methods: feature selection, principal component analysis, and clustering, emphasizing the significant role of features in the interpretability and efficiency of the model.


### Chapter 10: Principles of Nonlinear Feature Engineering

This chapter introduces how to extend a linear model into a nonlinear one to deal with more complex data patterns.
The author proposes that by introducing nonlinear feature transformations (such as square terms, sine functions, etc.), the original linear relationship can be presented in a linear form in the new feature space.
The book illustrates with multiple examples, including fitting wave data with a sine function and reproducing Galileo's experimental results on free fall through quadratic functions.
This chapter also introduces the implementation of nonlinear regression in Python, demonstrating how to define models and feature transformations with a general structure.
Finally, it is pointed out that the cost function of nonlinear models is usually non-convex, so the optimization process is more challenging and requires more cautious parameter adjustment and initialization.



### Chapter 11: Principles of Feature Learning

This chapter transitions from manual feature design to automatic feature learning, exploring how machines can automatically discover feature representations suitable for tasks through the training process.
The author points out that when the data structure is complex or has a high dimension, artificially designed features are often insufficient, so algorithms are needed to automatically learn more effective representations.
The book introduces three main types of feature learning methods: fixed-shape nonlinear functions, learnable parametric models (such as neural networks), and decision tree structures based on partitioning.
This chapter also presents two key concepts, model capacity and optimization degree, to balance underfitting and overfitting.
By adjusting the model complexity and the number of training rounds, the best results can be achieved between performance and generalization.
The chapter concludes by emphasizing that the core objective of feature learning is to enable machines to automatically extract useful information in various tasks, laying the foundation for higher-level deep learning models.
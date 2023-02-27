https://towardsdatascience.com/meta-labeling-and-stacking-f17a7f9804ec
Unbalanced data?
- Stratified sampling
- don't use confusion matrix/ROC
- 

As the dataset is highly unbalanced, the parameter `stratify =data_y`from scikit-learn’s `train_test_split()` function comes so handily. Data is split in a stratified fashion in a blink.


Explore uncorrelated models in an ensemble model
- log reg
- lightbgm
- dnn


Precision and Recall

-   Precision = TruePositives / (TruePositives + FalsePositives)

Fully Connected Neural Networks

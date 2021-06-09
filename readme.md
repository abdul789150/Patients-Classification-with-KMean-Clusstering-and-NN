
# ML Model for Detecting if Patient is Sick or Healthy¶
## Breif Description about Problem Statment and its Solution
For creating an ML model to detect is patient is sick or not we have given `4 dataset` files ( `BloodPressure.csv`, `Glucose.csv`, `Oximetry.csv`, `Weight_Height.csv` ). Below are the given steps which have been taken to solve the problem and build a ML model:

- **Step1:** `Merging Data Files`
    - For a single patient we have multiple set of data in all these 4 files. So for a complete set of data for a  single patient, we have to merge these files according to `Patient id` which is `Patient column` and `Date Column` is also important in mergining the data files. **We will merge each patient's data which have been recorded on same date**. This step has been done in `Merging Files` script.  
    

- **Step2:** `Data Cleaning`
    - Now after step 1, we have a complete dataset, but now we have some missing entries and outliers in the dataset. So for this purpose we will clean the dataset. We will first compute and remove the missing values and then we will check the outliers. For checking outliers we will use `Z function` and for outliers visualization we will be using `box plot` provided by `seaborn library`.


- **Step3:** `Feature Analysis`
    - In this step we will use correlation analysis to analyze all the features which are given in the dataset. We have **removed 2 features** after correlation analysis which are `Patient` and `Date`, they both have same values on different rows which effected their correlation analysis result very badly. So after deleting them we will be using 9 features for Training and Testing the Model.
    
    
- **Step4:** `K-means Clustring`
    - As you know we don't have label/target/class of data. So in this case it is best to use unsupervised learning models so we can detect the clusters in the dataset. Each cluster will have different class/label. In our case we have 2 different classes to detect `Sick` and `Healthy`, so we have 2 clusters of data.
    
    
- **Step5:** `Neural Network`
    - After applying K-means clustring we got 2 clusters of data and then we merged the class/label of each cluster with the dataset. Now we have a dataset with class/label, so we will train `Neural Networks` model to detect which patient is healthy/sick. Before applying `Neural Networks` we will scale and convert the data and we will split the dataset into training and teseting subsets.
    - We will define a `Neural Network` architecture which we will use to detect healthy/sick patients.
    - We will use `cross validation` technique to prevent overfitting.
    - After all these steps we will train and test the model.
    
    
- **Step6:** `Saving information`
    - For our last presentation step we will need to save some of the information in files. We will store the `Neural Network model` to predict the classes, `Training and Testing scores`, `Each Feature Maximum value` which will be used to scale the data when we will predict the classes.
    

- **Step7:** `Model Presentation`
    - For model presentation we will be using `Dash by Plotly`. Dash is python library same as Shiny which is for R language. Model presentation files are provided in `Model Presentation Folder`. 
For running the project you will need to install the following libraries:


## Libraries you need to install
you will be able to install the libraris by using pip:
Example: pip install numpy

* dash
* dash_bootstrap_components 
* keras
* tensorflow (latest version)
* numpy
* pandas
* seaborn
* scipy
* sklearn
* IPython (maybe it will be preinstalled in you OS, but still check that before running the project)
* matplotlib


## Project files Information
The project consists of 3 main files

* Merging Files
* ML model
* predictions.py (in data_presentation folder) 

Merging Files is the first part of the project, then after that ML model file will help to compute
results and in the last pedictions.py will help to present the data in a web page, for running 
predictions.py file simply write this command on your terminal/commandLine
```
python predictions.py
```
After running this command wait a bit so that the file will load all the libraries 
and then it will show you the link in the terminal/command Line to access the webpage.

# Senior Capstone Project: Hotspot Detection Module

Below are instructions on how to run our hotspot detection module

## To Run the Module On a Set Of Images:

### Data Preparation

To train and validate the algorithm, organize your data into two main directories:

    Training Data: Contains images and corresponding labels.
    Validation Data: Contains images and corresponding labels for validation.

Both the training and validation folders must contain directories with the same structure. Ensure that label files have the same file extension as the image files they correspond to.


### Configuration

Create a .yaml configuration file to specify paths and classes. This file should include:

    path: The base directory path that contains your datasets.
    train: Relative path from the base directory to the training directory.
    val: Relative path from the base directory to the validation directory.
    classes: A dictionary mapping class numbers to labels.

Refer to the example .yaml file (data.yaml) provided in this repository for guidance.


### Running the Provided Scripts

To train the model, execute the training script which will prompt you to input the path to your .yaml file:

    python train.py 


To run the algorithm, simply run the provided run script (in tools/run.py)

    python run.py


## To Run the Module on Continuous Input From a Thermal Camera:

You can use the same steps as stated above to train the algorithm but to run the algorithm use:

    python capture.py





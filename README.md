Clustering Algorithms: Fuzzy C-Means and K-Means
This repository contains implementations of two popular clustering algorithms: Fuzzy C-Means (FCM) and K-Means. The code is written in Python and includes test cases to demonstrate the functionality of both algorithms. Users can customize parameters such as the number of clusters, colors, and more within the source code to experiment with different clustering scenarios.
Prerequisites
Before running the code, ensure the following Python libraries are installed to avoid errors:

numpy: For numerical computations and array operations.
Pillow: For image processing (if applicable).
matplotlib: For visualizing clustering results.
colorsys: For handling color conversions in visualizations.
scikit-fuzzy: For implementing the Fuzzy C-Means algorithm.

You can install these dependencies using pip:
pip install numpy Pillow matplotlib colorsys scikit-fuzzy

Installation

Clone this repository to your local machine:git clone https://github.com/your-username/your-repo-name.git

Navigate to the project directory:cd your-repo-name

Install the required dependencies:pip install -r requirements.txt

Alternatively, install the libraries individually as listed in the Prerequisites section.

Usage

Running the Algorithms:

The repository includes source code for both Fuzzy C-Means and K-Means algorithms.
Example test cases are provided to showcase the clustering results.
To run a specific algorithm, execute its respective Python script:python fcm_clustering.py

python kmeans_clustering.py

Customizing Parameters:

You can modify parameters such as the number of clusters, colors, and other settings directly in the source code.
Refer to the comments within the code for guidance on adjusting these parameters.

Visualizing Results:

The scripts use matplotlib to generate visualizations of the clustering results.
Outputs can be customized (e.g., colors, plot styles) by editing the relevant code sections.

Testing
The repository includes several test cases for both algorithms. These test cases demonstrate the clustering process on sample datasets. To run the tests:
python test_fcm.py
python test_kmeans.py

You can examine the output visualizations to verify the correctness of the clustering results.
Notes

Ensure all dependencies are installed to avoid runtime errors.
The algorithms are flexible and allow experimentation with different datasets and parameters.
For large datasets, adjust the number of clusters and other hyperparameters to achieve optimal results.

Contributing
Contributions are welcome! If you have suggestions, bug fixes, or improvements:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

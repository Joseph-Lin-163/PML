import numpy as np

class Perceptron(object):
	"""Perceptron classifier.
	Parameters
	----------
	lr : float
		Learning rate (0.0 <= lr <= 1.0)
	num_iter : int
		Passes over training set

	Attributes
	----------
	w_ : 1d-array
		Weights after fitting.
	errors_ : list
		Number of misclassiciations in every epoch

	"""

	def __init__(self, lr=0.01, num_iter=10):
		self.lr = lr
		self.num_iter = num_iter

	def fit(self, X, y):
		"""Fit training data.

		Parameters
		----------
		X : {array-like}, shape = [n_samples, n_features]
			Training vectors, where n_samples is the number of samples and 
			n_features is the number of features.
		y : array-like, shape = [n_samples]
			Target values.

		Returns
		self : object

		"""
		self.w_ = np.zeros(1 + X.shape[1])
		self.errors_ = []

		for _ in range(self.num_iter):
			errors = 0
			for xi, target in zip(X, y):
				update = self.lr * (target - self.predict(xi))
				self.w_[1:] += update * xi
				self.w_[0] += update
				errors += int(update != 0.0)
			self.errors_.append(errors)
		return self

	def net_input(self, X):
		"""Calculate net input"""
		return np.dot(X, self.w_[1:]) + self.w_[0]

	def predict(self, X):
		"""Return class label after unit step"""
		return np.where(self.net_input(X) >= 0.0, 1, -1)
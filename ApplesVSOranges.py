from sklearn import tree

# features are the data - [weight, texture] - 0 = Bumpy / 1 = Smooth
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# labels identifies if it is an apple (0) or orange (1)
labels = [0, 0, 1, 1]

# classifier - clf.fit = training algorithm. 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# test case 
print(clf.predict([[160, 0]]))




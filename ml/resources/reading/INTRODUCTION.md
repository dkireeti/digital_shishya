
## ML General Process
    ML - running a model on the data to do prediction

### ML 
	1. Supervised Learning - when you have label (Y is label Spam Yes or No)
	2. Unsupervised  - Y is not defined.

### Models - Should be differentiable 
	Linear Models
		Y = ax+b
	Quadratic
		y = ax^2+bx+c 

 

### Process 
	1. Plot the data.
	2. Choose the Model
		Linear Model y = a0x0+a1x1+a2x2+......+b
	2. Clean Up & Prep  the Data.
		Model do not understand text, text -> to tokens/encoding(numbers)
		Normalisation
			Day Heat - 70C
			Humidity - 123
	3. Co-relation - y,x0,x1,x2 - Feature Engineering
	4. Training 80-20 Ratio
		Gradient Decent
	5. Assessing the Model Quality
		False Positive,
		Accuracy > 80%
		Accuracy > 95%	- Over Fit 
	6. Release to PROD
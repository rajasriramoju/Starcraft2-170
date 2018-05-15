

train_d = np.array([[0,0], [0,1], [1,0], [1,1]])
tar_d = np.array([[0], [1], [1], [0]])

model = Sequential()
model.add(Dense(50, input_dim=10, activation='tanh'))
model.add(Dense(50, input_dim=10, activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(train_d, tar_d, epochs=1000)
		
model.evaluate(train_d, tar_d)

print model.predict(np.array([[0,0]]))
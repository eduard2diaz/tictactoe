import keras

model = keras.models.Sequential()
model.add(keras.Input(shape=(9,)))
model.add(keras.layers.Dense(9, activation='sigmoid'))


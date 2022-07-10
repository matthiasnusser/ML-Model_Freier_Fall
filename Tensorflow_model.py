import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


# Arrays initalisieren
time = np.linspace(0, 12 , num = 13)
velocity = np.zeros(13)
for i in np.ndindex(np.shape(velocity)):
    velocity[i] = 9.81 * time[i]
#Training data
time_training = time[0:8]
velocity_training = velocity[0:8]

# Setup model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(loss = 'mean_squared_error',
    optimizer = tf.keras.optimizers.Adam(0.1))
training = model.fit(time_training, velocity_training, epochs = 500,
    verbose = False)
predicted_data = model.predict([8, 9, 10, 11, 12])

print(predicted_data)   # Vorhersage des Modells ausgeben

# Zusammenführen der Arrays um ML-Modell ab Sekunde 8 zu plotten
predicted_data_reshaped = np.reshape(predicted_data, 5)
prediction_joint = np.concatenate((velocity_training, predicted_data_reshaped))

# Fehlerfunktion plotten
fig, ax1 = plt.subplots()
plt.plot(training.history['loss'])
plt.xlabel('Epoche')
plt.ylabel('Loss')
plt.grid(True)

# Korrekte Funktion und ML-Modell plotten
fig, ax2 = plt.subplots()
plt.plot(time, velocity, prediction_joint)
ax2.legend(['Modell v=gt', 'Vorhersage ML-Modell'])
plt.xlabel('Zeit')
plt.ylabel('Geschwindigkeit')
plt.grid(True)
plt.show()

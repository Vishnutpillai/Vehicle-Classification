import tensorflow as tf


model=tf.keras.models.load_model(
    "best_vehicle_model.h5",
    compile=False
)


model.save("vehicle_model.keras")

print("converted")
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential, save_model
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report
from sklearn.utils.class_weight import compute_class_weight
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import regularizers
import numpy as np

#### Split the data into features (X) and target variable (y)
X = pivot_data4[['accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z']]
y = pivot_data4['motion_encoded']

#### Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#### Further split the training data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

#### Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

#### Define the model with L1 regularization
model = Sequential([
    Dense(64, activation='relu', kernel_regularizer=regularizers.l1(0.001), input_shape=(X_train_scaled.shape[1],)),
    Dropout(0.5),
    BatchNormalization(),
    Dense(64, activation='relu', kernel_regularizer=regularizers.l1(0.001)),
    Dropout(0.5),
    BatchNormalization(),
    Dense(len(np.unique(pivot_data4['motion_encoded'])), activation='softmax')
])

#### Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#### Encode class labels
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)

#### Compute class weights using the encoded labels
class_weights = compute_class_weight(class_weight='balanced', classes=np.unique(y_train_encoded), y=y_train_encoded)

#### Create a class weight dictionary
class_weight_dict = dict(zip(le.transform(le.classes_), class_weights))

#### Define early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=5)

#### Train the model with class weights and early stopping
history = model.fit(X_train_scaled, y_train_encoded, epochs=20, validation_data=(X_val_scaled, y_val), class_weight=class_weight_dict, callbacks=[early_stopping])

#### Save the model
file_path = "/Users/emilkoch/Desktop/2Tango/messenger/research/Model_Save/motion.keras"
save_model(model, file_path)

#### Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test)
print("Test Accuracy:", test_accuracy)

#### Make predictions
y_pred_prob = model.predict(X_test_scaled)
y_pred = np.argmax(y_pred_prob, axis=1)

#### Calculate precision, recall, and F1 score
report = classification_report(y_test, y_pred)
print(report)
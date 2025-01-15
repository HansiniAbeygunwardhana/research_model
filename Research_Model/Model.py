# -*- coding: utf-8 -*-
"""best_with_plots_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JRGONzodtQK9ccrogoF1wEN6LAJr9wRW
"""

from google.colab import drive
drive.mount('/content/drive')
newfeaturepath = '/content/drive/MyDrive/NewFeature'

!apt-get install ffmpeg
!pip install opencv-python dlib
!pip install keras-tuner --upgrade

import pandas as pd
import os

# Load the CSV file with personality trait scores
label_csv_path = os.path.join(newfeaturepath, 'csv_labels.csv')
label_df = pd.read_csv(label_csv_path)

# Convert categorical trait values to numeric values
# trait_mapping = {'Low': 0, 'Moderate': 1, 'High': 2}
# for trait in ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Emotional_Stability']:
#     label_df[trait] = label_df[trait].map(trait_mapping)

# Create a dictionary mapping from video filename to label array
label_dict = {}
for index, row in label_df.iterrows():
    clip_id = row['clip_id']
    traits = [row['Openness'], row['Conscientiousness'], row['Extraversion'], row['Agreeableness'], row['Emotional_Stability']]
    label_dict[clip_id] = traits

print(label_dict)

import dlib
import cv2
import os

# Paths to the required files within the predefined folder
shape_predictor_path = os.path.join(newfeaturepath, 'shape_predictor_68_face_landmarks.dat')
caffe_model_path = os.path.join(newfeaturepath, 'res10_300x300_ssd_iter_140000.caffemodel')
deploy_prototxt_path = os.path.join(newfeaturepath, 'deploy.prototxt')

# Check if necessary model files exist
if not os.path.exists(shape_predictor_path):
    raise FileNotFoundError("Dlib shape predictor model not found. Please ensure it is available in the specified path.")
if not os.path.exists(caffe_model_path) or not os.path.exists(deploy_prototxt_path):
    raise FileNotFoundError("Caffe model or deploy prototxt file not found. Please ensure both files are available in the specified path.")

# Initialize face detector and landmark predictor
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(shape_predictor_path)

# Load OpenCV DNN face detector
net = cv2.dnn.readNetFromCaffe(deploy_prototxt_path, caffe_model_path)

# Path to the video clips folder
video_folder_path = '/content/drive/My Drive/Video Annotate/'
output_frames_path = '/content/drive/MyDrive/NewFeature/'

label_dict = {
    # "clip_001.mp4": [1, 0, 0, 1, 1],  # Example label for 5 traits
    # Add labels for each clip
          "clip_001.mp4": [1, 1, 0, 1, 2],
          "clip_002.mp4": [2, 2, 0, 1, 2],
          "clip_003.mp4": [2, 2, 1, 1, 2],
          "clip_004.mp4": [0, 0, 0, 0, 1],
          "clip_005.mp4": [1, 0, 0, 0, 2],
          "clip_006.mp4": [1, 2, 1, 2, 2],
          "clip_007.mp4": [1, 2, 2, 1, 2],
          "clip_008.mp4": [2, 2, 2, 2, 2],
          "clip_009.mp4": [1, 1, 2, 2, 1],
          "clip_010.mp4": [1, 1, 1, 1, 2],
          "clip_011.mp4": [2, 2, 2, 2, 2],
          "clip_012.mp4": [2, 1, 1, 2, 2],
          "clip_013.mp4": [0, 0, 1, 1, 2],
          "clip_014.mp4": [1, 1, 1, 2, 2],
          "clip_015.mp4": [0, 0, 0, 0, 1],
          "clip_016.mp4": [2, 2, 2, 2, 2],
          "clip_017.mp4": [1, 1, 1, 2, 0],
          "clip_018.mp4": [2, 2, 2, 2, 2],
          "clip_019.mp4": [2, 2, 1, 1, 2],
          "clip_020.mp4": [2, 2, 2, 2, 2],
          "clip_021.mp4": [1, 0, 1, 1, 2],
          "clip_022.mp4": [2, 2, 1, 1, 1],
          "clip_023.mp4": [1, 1, 1, 1, 1],
          "clip_024.mp4": [2, 2, 2, 1, 2],
          "clip_025.mp4": [2, 2, 2, 1, 1],
          "clip_026.mp4": [2, 2, 2, 2, 2],
          "clip_027.mp4": [2, 2, 2, 2, 2],
          "clip_028.mp4": [2, 2, 2, 2, 1],
          "clip_029.mp4": [2, 2, 2, 2, 2],
          "clip_030.mp4": [2, 2, 1, 1, 2],
          "clip_031.mp4": [1, 2, 2, 1, 1],
          "clip_032.mp4": [2, 2, 2, 1, 2],
          "clip_033.mp4": [0, 2, 0, 0, 0],
          "clip_034.mp4": [1, 0, 2, 1, 2],
          "clip_035.mp4": [1, 2, 1, 1, 1],
          "clip_036.mp4": [2, 1, 1, 2, 2],
          "clip_037.mp4": [1, 2, 1, 1, 1],
          "clip_038.mp4": [2, 1, 2, 2, 1],
          "clip_039.mp4": [2, 2, 1, 1, 2],
          "clip_040.mp4": [2, 2, 2, 1, 1],
          "clip_041.mp4": [2, 2, 2, 1, 1],
          "clip_042.mp4": [2, 2, 2, 2, 2],
          "clip_043.mp4": [1, 2, 0, 0, 0],
          "clip_044.mp4": [2, 0, 2, 1, 2],
          "clip_045.mp4": [1, 2, 2, 0, 1],
          "clip_046.mp4": [2, 2, 2, 2, 2],
          "clip_047.mp4": [2, 2, 2, 2, 2],
          "clip_048.mp4": [2, 2, 2, 1, 2],
          "clip_049.mp4": [1, 2, 2, 1, 1],
          "clip_050.mp4": [2, 2, 2, 2, 2],
          "clip_051.mp4": [2, 2, 2, 2, 2],
          "clip_052.mp4": [1, 2, 2, 2, 2],
          "clip_053.mp4": [2, 2, 2, 2, 2],
          "clip_054.mp4": [2, 2, 2, 2, 2],
          "clip_055.mp4": [2, 2, 2, 2, 2],
          "clip_056.mp4": [2, 2, 2, 2, 2],
          "clip_057.mp4": [1, 2, 2, 2, 2],
          "clip_058.mp4": [1, 2, 2, 1, 2],
          "clip_059.mp4": [1, 1, 1, 1, 2],
          "clip_060.mp4": [1, 1, 0, 1, 0],
          "clip_061.mp4": [1, 1, 0, 2, 2],
          "clip_062.mp4": [2, 2, 0, 2, 2],
          "clip_063.mp4": [0, 2, 2, 2, 2],
          "clip_064.mp4": [1, 2, 1, 2, 2],
          "clip_065.mp4": [2, 0, 1, 2, 2],
          "clip_066.mp4": [0, 2, 2, 2, 1],
          "clip_067.mp4": [1, 2, 2, 1, 1],
          "clip_068.mp4": [2, 0, 1, 2, 2],
          "clip_069.mp4": [2, 1, 2, 2, 2],
          "clip_070.mp4": [1, 2, 1, 2, 2],
          "clip_071.mp4": [0, 2, 0, 1, 0],
          "clip_072.mp4": [1, 0, 1, 1, 0],
          "clip_073.mp4": [1, 0, 0, 2, 2],
          "clip_074.mp4": [2, 0, 1, 2, 2],
          "clip_075.mp4": [2, 1, 1, 1, 1],
          "clip_076.mp4": [2, 2, 1, 2, 2],
          "clip_077.mp4": [2, 2, 2, 2, 2],
          "clip_078.mp4": [1, 2, 2, 2, 1],
          "clip_079.mp4": [1, 1, 2, 0, 1],
          "clip_080.mp4": [1, 2, 0, 0, 1],
          "clip_081.mp4": [2, 1, 0, 0, 2],
          "clip_082.mp4": [2, 0, 0, 1, 2],
          "clip_083.mp4": [2, 0, 2, 1, 2],
          "clip_084.mp4": [0, 2, 0, 0, 2],
          "clip_085.mp4": [2, 0, 0, 2, 2],
          "clip_086.mp4": [0, 0, 2, 0, 1],
          "clip_087.mp4": [2, 2, 0, 2, 2],
          "clip_088.mp4": [2, 0, 2, 2, 2],
          "clip_089.mp4": [2, 2, 2, 2, 2],
          "clip_090.mp4": [1, 2, 2, 2, 1],
          "clip_091.mp4": [2, 2, 2, 1, 1],
          "clip_092.mp4": [0, 2, 2, 1, 2],
          "clip_093.mp4": [0, 2, 2, 2, 2],
          "clip_094.mp4": [2, 0, 1, 2, 1],
          "clip_095.mp4": [2, 1, 0, 2, 2],
          "clip_096.mp4": [2, 0, 1, 1, 2],
          "clip_097.mp4": [1, 2, 1, 1, 2],
          "clip_098.mp4": [2, 2, 0, 2, 1],
          "clip_099.mp4": [1, 2, 2, 2, 2],
          "clip_100.mp4": [2, 2, 2, 2, 2],
          "clip_101.mp4": [2, 0, 2, 1, 2],
          "clip_102.mp4": [2, 2, 2, 2, 2],
          "clip_103.mp4": [1, 1, 1, 2, 2],
          "clip_104.mp4": [1, 2, 2, 2, 1],
          "clip_105.mp4": [1, 1, 1, 2, 2],
          "clip_106.mp4": [1, 2, 2, 2, 2],
          "clip_107.mp4": [0, 1, 2, 2, 2],
          "clip_108.mp4": [2, 1, 2, 2, 2],
          "clip_109.mp4": [2, 1, 2, 2, 2],
          "clip_110.mp4": [2, 2, 2, 2, 2],
          "clip_111.mp4": [0, 2, 2, 2, 2],
          "clip_112.mp4": [1, 2, 1, 2, 2],
          "clip_113.mp4": [2, 1, 1, 2, 2],
          "clip_114.mp4": [0, 2, 1, 1, 2],
          "clip_115.mp4": [2, 2, 1, 0, 1],
          "clip_116.mp4": [1, 2, 2, 1, 2],
          "clip_117.mp4": [0, 2, 1, 1, 1],
          "clip_118.mp4": [0, 2, 0, 1, 1],
          "clip_119.mp4": [0, 2, 1, 1, 2],
          "clip_120.mp4": [0, 2, 1, 1, 2],
          "clip_121.mp4": [1, 2, 1, 1, 2],
          "clip_122.mp4": [2, 2, 2, 1, 2],
          "clip_123.mp4": [2, 2, 1, 2, 2],
          "clip_124.mp4": [2, 2, 2, 2, 2],
          "clip_125.mp4": [0, 2, 2, 2, 1],
          "clip_126.mp4": [2, 2, 2, 2, 0],
          "clip_127.mp4": [0, 2, 1, 1, 1],
          "clip_128.mp4": [0, 2, 2, 2, 2],
          "clip_129.mp4": [2, 2, 2, 2, 2],
          "clip_130.mp4": [2, 1, 2, 1, 2],
          "clip_131.mp4": [0, 2, 2, 2, 2],
          "clip_132.mp4": [0, 2, 2, 2, 2],
}

import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical

def preprocess_frame(frame):
    """
    Preprocess the frame by converting it to grayscale and applying histogram equalization
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)  # Improve contrast for better face detection
    return gray

def extract_landmarks_from_frame(frame):
    """
    Extract landmarks from a given frame using a combination of DNN face detection and Dlib landmarks
    """
    # Prepare the frame for deep learning face detection
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    if detections.shape[2] == 0:
        return None  # No faces detected

    # Assuming the first face is the one we want to analyze
    confidence = detections[0, 0, 0, 2]
    if confidence < 0.4:  # Confidence threshold, can adjust
        return None

    # Get the bounding box for the detected face
    box = detections[0, 0, 0, 3:7] * np.array([w, h, w, h])
    (startX, startY, endX, endY) = box.astype("int")
    face_rect = dlib.rectangle(startX, startY, endX, endY)

    # Extract landmarks from the detected face
    gray = preprocess_frame(frame)
    faces = face_detector(gray)

    if len(faces) == 0:
        # Retry with slight modifications (e.g., apply Gaussian blur)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        faces = face_detector(gray)
        if len(faces) == 0:
            return None  # Skip if still no faces found

    # Process the largest detected face
    largest_face = max(faces, key=lambda rect: rect.width() * rect.height())
    landmarks_data = []
    landmarks = landmark_predictor(gray, largest_face)
    for n in range(68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        landmarks_data.append((x, y))

    return np.array(landmarks_data).flatten() if landmarks_data else None

# Initialize an empty list to store features and labels
X_data = []
y_data = []

# Process each video and collect landmarks
for video_file in os.listdir(video_folder_path):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(video_folder_path, video_file)
        video = cv2.VideoCapture(video_path)
        frame_count = 0
        video_landmarks = []

        while True:
            ret, frame = video.read()
            if not ret:
                break

            # Extract landmarks every few frames (e.g., every 30 frames for a 1-second interval)
            if frame_count % 30 == 0:
                landmarks = extract_landmarks_from_frame(frame)
                if landmarks is not None and landmarks.shape == (136,):  # Ensure correct shape
                    video_landmarks.append(landmarks)
                    print(f"land mark added")
                else:
                    print(f"Skipped a frame in {video_file} due to landmark shape issues.")

            frame_count += 1
        video.release()

        # Check if video_landmarks has data and calculate mean
        if video_landmarks:
            video_features = np.mean(video_landmarks, axis=0)
            if video_features.shape == (136,):  # Ensure final feature vector has the expected shape
                X_data.append(video_features)

                # Retrieve label from label_dict and handle missing labels
                if video_file in label_dict:
                    y_data.append(label_dict[video_file])
                else:
                    print(f"Warning: Label for {video_file} not found in label_dict.")
            else:
                print(f"Unexpected shape for video features in {video_file}: {video_features.shape}")

# Convert data to numpy arrays if we have any data collected
if X_data and y_data:
    X_data = np.array(X_data)
    y_data = np.array(y_data)
    y_data = to_categorical(y_data, num_classes=50)  # Assuming 50 output classes

    # Now X_data and y_data are ready to be used with the CNN model
    print("Data is ready for training!")
else:
    print("No valid data collected.")

# Re-create y_data based on label_dict
# Assuming label_dict has keys as video file names and values as lists of 5 trait labels (e.g., [1, 0, 2, 1, 2])
y_data = np.array([label_dict[video_file] for video_file in sorted(label_dict.keys())])  # Sort to maintain order if needed
print("Corrected y_data shape:", y_data.shape)  # Should be (120, 5)

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# Shuffle the data to improve model generalizability
X_data, y_data = shuffle(X_data, y_data, random_state=42)

# Split the training and validation sets after shuffling
X_train, X_val, y_train, y_val = train_test_split(X_data, y_data, test_size=0.2, random_state=42)

# Ensure each y_* array is properly one-hot encoded with shape (120, 3)
y_openness = to_categorical(y_data[:, 0], num_classes=3)
y_conscientiousness = to_categorical(y_data[:, 1], num_classes=3)
y_extraversion = to_categorical(y_data[:, 2], num_classes=3)
y_agreeableness = to_categorical(y_data[:, 3], num_classes=3)
y_emotional_stability = to_categorical(y_data[:, 4], num_classes=3)

# Split the training and validation labels into individual traits
# Split each trait into training and validation sets
y_openness_train, y_openness_val = train_test_split(y_openness, test_size=0.2, random_state=42)
y_conscientiousness_train, y_conscientiousness_val = train_test_split(y_conscientiousness, test_size=0.2, random_state=42)
y_extraversion_train, y_extraversion_val = train_test_split(y_extraversion, test_size=0.2, random_state=42)
y_agreeableness_train, y_agreeableness_val = train_test_split(y_agreeableness, test_size=0.2, random_state=42)
y_emotional_stability_train, y_emotional_stability_val = train_test_split(y_emotional_stability, test_size=0.2, random_state=42)

# Check final shapes to ensure correctness
print("y_openness_train shape:", y_openness_train.shape)
print("y_openness_val shape:", y_openness_val.shape)
print("y_conscientiousness_train shape:", y_conscientiousness_train.shape)
print("y_conscientiousness_val shape:", y_conscientiousness_val.shape)
print("y_extraversion_train shape:", y_extraversion_train.shape)
print("y_extraversion_val shape:", y_extraversion_val.shape)
print("y_agreeableness_train shape:", y_agreeableness_train.shape)
print("y_agreeableness_val shape:", y_agreeableness_val.shape)
print("y_emotional_stability_train shape:", y_emotional_stability_train.shape)
print("y_emotional_stability_val shape:", y_emotional_stability_val.shape)

from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True
    )

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input, Dropout, BatchNormalization, Conv1D, Flatten
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler
import numpy as np

# Standardize input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# Updated model without LSTM, using Conv1D instead
def create_simple_trait_model(input_shape):
    input_layer = Input(shape=(input_shape, 1))  # Reshape for Conv1D
    x = Conv1D(64, kernel_size=3, activation='relu')(input_layer)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)

    x = Conv1D(32, kernel_size=3, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)

    x = Flatten()(x)

    x = Dense(64, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)

    x = Dense(32, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.2)(x)

    output_layer = Dense(1)(x)  # Single output per trait with MSE loss

    model = Model(inputs=input_layer, outputs=output_layer)
    model.compile(optimizer=Adam(learning_rate=0.0001), loss='mse', metrics=['mse'])

    return model

# Reshape X_train and X_val for Conv1D input
X_train_expanded = np.expand_dims(X_train, axis=-1)
X_val_expanded = np.expand_dims(X_val, axis=-1)

# Train a separate model for each trait
models = {}
histories = {}
for i, (trait, y_train, y_val) in enumerate(zip(
    ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_stability'],
    [y_openness_train[:, 1], y_conscientiousness_train[:, 1], y_extraversion_train[:, 1], y_agreeableness_train[:, 1], y_emotional_stability_train[:, 1]],  # Use single dimension labels
    [y_openness_val[:, 1], y_conscientiousness_val[:, 1], y_extraversion_val[:, 1], y_agreeableness_val[:, 1], y_emotional_stability_val[:, 1]]
)):
    print(f"\nTraining simple model for {trait}...")
    model = create_simple_trait_model(X_train_expanded.shape[1])
    history = model.fit(
        X_train_expanded, y_train,
        validation_data=(X_val_expanded, y_val),
        epochs=1000,
        batch_size=16,
        callbacks=[EarlyStopping(monitor='val_loss', patience=80, restore_best_weights=True)],
        verbose=1
    )
    models[trait] = model
    histories[trait] = history

# Evaluate models
for i, (trait, y_val) in enumerate(zip(
    ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_stability'],
    [y_openness_val[:, 1], y_conscientiousness_val[:, 1], y_extraversion_val[:, 1], y_agreeableness_val[:, 1], y_emotional_stability_val[:, 1]]
)):
    print(f"\nEvaluating simple model for {trait}...")
    evaluation_results = models[trait].evaluate(X_val_expanded, y_val, verbose=0)
    print(f"{trait.capitalize()} - MSE: {evaluation_results[0]:.4f}")

# Example for one trait
history.history['loss']       # Training loss
history.history['val_loss']   # Validation loss

import matplotlib.pyplot as plt

# Plot training and validation loss for each trait
for trait in histories.keys():
    plt.figure(figsize=(8, 6))
    plt.plot(histories[trait].history['loss'], label='Training Loss')
    plt.plot(histories[trait].history['val_loss'], label='Validation Loss')
    plt.title(f"Training and Validation Loss for {trait.capitalize()}")
    plt.xlabel('Epochs')
    plt.ylabel('Loss (MSE)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Collect evaluation MSE results for each trait
mse_results = {trait: models[trait].evaluate(X_val_expanded, y_val, verbose=0)[0]
               for trait, y_val in zip(
                   ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_stability'],
                   [y_openness_val[:, 1], y_conscientiousness_val[:, 1], y_extraversion_val[:, 1], y_agreeableness_val[:, 1], y_emotional_stability_val[:, 1]]
               )}

# Plot MSE for each trait
plt.figure(figsize=(8, 6))
plt.bar(mse_results.keys(), mse_results.values(), color='skyblue')
plt.title("Mean Squared Error (MSE) for Each Trait")
plt.xlabel("Personality Traits")
plt.ylabel("MSE")
plt.grid(axis='y')
plt.show()

import pandas as pd

# Convert MSE results to a DataFrame
mse_df = pd.DataFrame(list(mse_results.items()), columns=['Trait', 'MSE'])
print(mse_df)

# Optional: Save to a file
mse_df.to_csv("mse_results.csv", index=False)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np  # Ensure numpy is imported

# Collect predictions and ground truth for each trait
predictions = {}
true_values = {}

for trait, y_val in zip(
    ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_stability'],
    [y_openness_val[:, 1], y_conscientiousness_val[:, 1], y_extraversion_val[:, 1], y_agreeableness_val[:, 1], y_emotional_stability_val[:, 1]]
):
    predictions[trait] = models[trait].predict(X_val_expanded).flatten()
    true_values[trait] = y_val


# Assuming `predictions[trait]` holds predicted values and `true_values[trait]` holds actual values for each trait

for trait in ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_stability']:
    y_true = true_values[trait]
    y_pred = predictions[trait]

    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)  # Manually compute the square root of MSE for RMSE
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    print(f"\nMetrics for {trait.capitalize()}:")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R-squared: {r2:.4f}")

print(X_train)

# Mapping from loop trait names to rule dictionary keys
trait_name_mapping = {
    "openness": "Openness to Experience",
    "conscientiousness": "Conscientiousness",
    "extraversion": "Extraversion",
    "agreeableness": "Agreeableness",
    "emotional_stability": "Emotional Stability"
}

def map_trait_to_ksa(trait, score):
    rules = {
        "Openness to Experience": {
            "threshold": 0.4,
            "strong": ["Innovation (Strong)"],
            "weak": ["Innovation (Weak)"]
        },
        "Conscientiousness": {
            "threshold": 0.5,
            "strong": ["Responsibility (Strong)"],
            "weak": ["Responsibility (Weak)"]
        },
        "Extraversion": {
            "threshold": 0.5,
            "strong": ["Communication Skills (Strong)"],
            "weak": ["Communication Skills (Weak)"]
        },
        "Agreeableness": {
            "threshold": 0.5,
            "strong": ["Collaboration (Strong)"],
            "weak": ["Collaboration (Weak)"]
        },
        "Emotional Stability": {  # Use the original format
            "threshold": 0.3,
            "strong": ["Focus (Strong)"],
            "weak": ["Focus (Weak)"]
        }
    }

    # Convert trait name using the mapping
    trait_key = trait_name_mapping.get(trait, None)
    if trait_key and trait_key in rules:
        threshold = rules[trait_key]["threshold"]
        if score > threshold:
            ksa_mapping = rules[trait_key]["strong"]
        else:
            ksa_mapping = rules[trait_key]["weak"]
    else:
        ksa_mapping = ["Unknown KSA"]

    return {
        "Personality Trait": trait,
        "Score": score,
        "Relevant KSA": ksa_mapping
    }

# Generate predictions for validation data and apply rule-based KSA mapping
for trait in ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_stability']:
    # Generate predictions
    y_pred = models[trait].predict(X_val_expanded).flatten()  # Flatten to get a 1D array

    # Map predictions to KSAs
    print(f"\nKSA Mapping for {trait.capitalize()} Predictions:")
    for score in y_pred:
        mapped_result = map_trait_to_ksa(trait, score)  # Pass the lowercase trait name directly
        print(mapped_result)

for trait in models.keys():
    models[trait].save(f"{newfeaturepath}/{trait}_model.keras")

from tensorflow.keras.models import load_model

# Load saved models
loaded_models = {}
for trait in ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_stability']:
    loaded_models[trait] = load_model(f"{newfeaturepath}/{trait}_model.keras")

new_video_features = []

new_video_folder_path = "/content"

for video_file in os.listdir(new_video_folder_path):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(new_video_folder_path, video_file)
        video = cv2.VideoCapture(video_path)
        frame_count = 0
        video_landmarks = []

        while True:
            ret, frame = video.read()
            if not ret:
                break

            # Extract landmarks every 30 frames
            if frame_count % 30 == 0:
                landmarks = extract_landmarks_from_frame(frame)
                if landmarks is not None and landmarks.shape == (136,):
                    video_landmarks.append(landmarks)

            frame_count += 1
        video.release()

        if video_landmarks:
            video_features = np.mean(video_landmarks, axis=0)
            new_video_features.append(video_features)

# Standardize the features
new_video_features = scaler.transform(new_video_features)
new_video_features_expanded = np.expand_dims(new_video_features, axis=-1)

predictions = {}

for trait in loaded_models.keys():
    predictions[trait] = loaded_models[trait].predict(new_video_features_expanded).flatten()

# Mapping to translate trait names into rule keys
trait_name_mapping = {
    "openness": "Openness to Experience",
    "conscientiousness": "Conscientiousness",
    "extraversion": "Extraversion",
    "agreeableness": "Agreeableness",
    "emotional_stability": "Emotional Stability"
}

# Rule-based KSA mapping function
def map_trait_to_ksa(trait, score):
    # Rules for personality trait thresholds and KSAs
    rules = {
        "Openness to Experience": {
            "threshold": 0.1,
            "strong": ["Innovation (Strong)"],
            "weak": ["Innovation (Weak)"]
        },
        "Conscientiousness": {
            "threshold": 0.5,
            "strong": ["Responsibility (Strong)"],
            "weak": ["Responsibility (Weak)"]
        },
        "Extraversion": {
            "threshold": 0.5,
            "strong": ["Communication Skills (Strong)"],
            "weak": ["Communication Skills (Weak)"]
        },
        "Agreeableness": {
            "threshold": 0.5,
            "strong": ["Collaboration (Strong)"],
            "weak": ["Collaboration (Weak)"]
        },
        "Emotional Stability": {
            "threshold": 0.3,
            "strong": ["Focus (Strong)"],
            "weak": ["Focus (Weak)"]
        }
    }

    # Convert trait name to match rules dictionary
    trait_key = trait_name_mapping.get(trait.lower())  # Use lowercase for input trait
    if trait_key and trait_key in rules:
        threshold = rules[trait_key]["threshold"]
        if score > threshold:
            ksa_mapping = rules[trait_key]["strong"]
        else:
            ksa_mapping = rules[trait_key]["weak"]
    else:
        ksa_mapping = ["Unknown KSA"]

    return {
        "Personality Trait": trait,
        "Score": score,
        "Relevant KSA": ksa_mapping
    }

# Testing the mapping
for trait, scores in predictions.items():
    print(f"\nKSA Mapping for {trait.capitalize()} Predictions:")
    for score in scores:
        # Pass the lowercase trait name to map_trait_to_ksa
        mapped_result = map_trait_to_ksa(trait, score)
        print(mapped_result)
# 🌱 **Plant Disease Detection System** 🔎

**Plant Disease Detection** is a cutting-edge machine learning project designed to help **farmers and agricultural professionals** identify and classify plant diseases accurately using **Convolutional Neural Networks (CNNs)**. This system offers a **fast and reliable diagnosis** that enables timely intervention, reducing crop losses and enhancing agricultural productivity.

🚀 **[Check out the Live Demo](https://github.com/16sepsaumya/Farmers-friend.git)**

---

## 📂 **Project Structure**

This repository includes the following core components:

- **`Plant_Disease_Detection.ipynb`** – Jupyter Notebook for training the CNN model on plant disease images.
- **`main_app.py`** – Streamlit web app for easy interaction and disease prediction.
- **`plant_disease_model.h5`** – Pre-trained model weights for making real-time predictions.
- **`requirements.txt`** – A list of Python dependencies required to run the project.

---

## 🚀 **Installation Instructions**

Follow these steps to set up and run the project locally:

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Sayan0406/Plant_disease_detection-.git
```

### 2️⃣ **Navigate to the Project Directory**
```bash
cd Plant-Disease-Detection
```

### 3️⃣ **Install the Required Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Launch the Streamlit Web Application**
```bash
streamlit run main_app.py
```

---

## 🌿 **How It Works**

1. Run the Streamlit application on your local machine.
2. Access the web interface by navigating to **[http://localhost:8501](http://localhost:8501)** in your browser.
3. Upload an image of a **plant leaf** you wish to analyze.
4. The system will use the trained model to **detect any diseases** and return a prediction.

---

## 🧠 **Model Training Process**

The **CNN-based model** for plant disease detection is trained using the **`Plant_Disease_Detection.ipynb`** notebook. It employs a dataset containing images of plants categorized by their respective diseases. Once the model is trained, its weights are saved in **`plant_disease_model.h5`**, which is then used in the **Streamlit app** for real-time predictions.

---

## 🌐 **Web Application Overview**

The **Streamlit web application** (`main_app.py`) allows users to:

- Upload plant leaf images for analysis.
- Receive real-time predictions on plant diseases.
- Take immediate, AI-powered action based on the diagnosis.

---

## 🛠️ **System Requirements**

Ensure the following Python packages are installed:

- `Keras==2.8.0`
- `numpy==1.21.4`
- `streamlit==1.18.0`
- `opencv-python-headless==4.5.3`
- `tensorflow==2.7.0`

---

## 🚀 **Start Protecting Your Crops Today!**

Harness the power of machine learning with the **Plant Disease Detection** system to improve crop health monitoring and safeguard your plants against diseases. With this tool, farmers and agricultural experts can take prompt actions to mitigate risks and optimize crop yields. 🌿💡

---



# Eye Disease Detection using Fundus Images

##  Project Overview

This project focuses on the **classification of eye diseases from fundus images** using deep learning. The model is trained to detect **8 different eye conditions** from retinal images.

##  Objective

The primary goal is to develop a robust multi-label classification model that can accurately identify various eye diseases from fundus photographs, including:
- **N**: Normal
- **D**: Diabetes
- **G**: Glaucoma
- **C**: Cataract
- **A**: AMD (Age-related Macular Degeneration)
- **H**: Hypertension
- **M**: Myopia
- **O**: Other

##  Dataset

The dataset used is the **ODIR-5K** (Ocular Disease Recognition) dataset, which contains:
- **Total Images**: 6,392
- **Unique Patients**: 3,358
- **Training Samples**: 2,350
- **Validation Samples**: 504
- **Test Samples**: 504

### Data Structure
The dataset includes:
- Fundus images (both left and right eye)
- Patient information (age, gender)
- Multi-label disease annotations
- Diagnostic keywords

## 🔍 Exploratory Data Analysis (EDA)

Key insights from the dataset:

### Disease Distribution
- **Diabetes (D)** and **Normal (N)** are the most common classes
- **Hypertension (H)** is the rarest class with only 203 samples
- Imbalance ratio: 10.46 (most to least frequent)

### Patient Demographics
- **Age Distribution**: Ranges from 42 to 69 years
- **Gender**: Slightly more male patients (3,424) than female (2,968)

### Multi-label Analysis
- Most images have **1 disease label** (5,391 images)
- **2 diseases**: 955 images
- **3 diseases**: 46 images

### Disease Correlations
- Strong correlations between certain disease pairs
- Particularly **D (Diabetes)** and **O (Other)**

##  Project Structure

```
Eye Disease Detection/
├── Data_Balancing.ipynb    # Data preprocessing and balancing
├── Eye_Disease.ipynb       # Model training and evaluation
├── README.md               # Project documentation

```

##  Data Balancing Strategy

The project implements a sophisticated two-stage balancing approach:

### Stage 1: Eye-Level Balancing
- Converts patient data into eye-level records
- Creates **4,491** eye samples from **2,350** patients
- Uses **WeightedRandomSampler** with moderated weights
- Weight formula: `sqrt(max_positive_count / disease_count)`
- Caps sample weights at **3.0**

### Stage 2: Bilateral Patient-Level Balancing
- Focuses on patients with **both eyes** available
- **2,141** bilateral patients
- Patient-level weighted sampling
- Ensures balanced representation of rare diseases

##  Model Architecture

The project uses **PyTorch** with:
- ResNet-based architecture (planned)
- Multi-label classification head
- Image transformations for data augmentation:
  - Random horizontal flips
  - Random rotations
  - Random resized crops
  - Normalization

##  Key Results

- **Training Samples**: 4,491 eye-level samples
- **Validation Samples**: 504 patients
- **Test Samples**: 504 patients
- **Maximum Sample Weight**: 3.0
- **Minimum Sample Weight**: 1.0

##  Technical Stack

- **Framework**: PyTorch
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Image Processing**: PIL, OpenCV
- **Data Balancing**: WeightedRandomSampler
- **GPU Support**: CUDA-enabled

##  Getting Started

### Prerequisites
```bash
python >= 3.8
torch >= 1.9.0
torchvision >= 0.10.0
pandas >= 1.3.0
numpy >= 1.21.0
matplotlib >= 3.4.0
seaborn >= 0.11.0
Pillow >= 8.3.0
opencv-python >= 4.5.0
scikit-learn >= 0.24.0
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/eye-disease-detection.git
cd eye-disease-detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the ODIR-5K dataset

4. Update the `ROOT` path in the notebooks to point to your dataset location

5. Run the notebooks:
```bash
jupyter notebook
```

##  Data Preparation

1. Mount Google Drive (if using Colab)
2. Load patient-level CSV files
3. Preprocess images (resize to 224x224)
4. Apply data augmentation
5. Create data loaders with balanced sampling

##  Model Training

The training pipeline includes:
1. **Data Loading**: Custom ODIRDataset class
2. **Data Augmentation**: Training-time augmentations
3. **Balanced Sampling**: WeightedRandomSampler
4. **Multi-Label Classification**: Binary cross-entropy loss
5. **Evaluation**: Per-class metrics

##  Visualization

The project includes comprehensive visualization:
- **EDA Visualizations**:
  - Disease distribution plots
  - Age and gender distributions
  - Disease correlation heatmaps
  - Multi-label distribution
- **Model Visualizations**:
  - Training loss curves
  - Augmented image samples
  - Prediction visualizations
---


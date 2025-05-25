# Thermal Image Preprocessor

This tool enhances and analyzes thermal images from drone cameras to improve visibility and feature extraction, including edge detection and threshold-based segmentation.

## 🔥 Use Case
Used in UAVs scanning for heat signatures — for example, survivors trapped under rubble — by refining noisy thermal data.

## 🧪 Features
- Gaussian blur & histogram equalization
- Adaptive and binary thresholding
- Contour detection & heat zone isolation

## 📁 Structure
- `notebooks/`: Interactive test notebook
- `scripts/`: Core image preprocessing tools
- `data/`: Place sample thermal images here
- `assets/`: Example visual results

## 🛠️ How to Use
1. Place thermal images in `data/`
2. Use `filter.py` to preprocess or detect features
3. Or run visual demo in `thermal_processing_notebook.ipynb`

## 🔮 Future Work
- Integration with survivor detection
- Automatic anomaly flagging from heat blobs

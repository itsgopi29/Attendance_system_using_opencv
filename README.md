A computer vision-based student attendance system that uses face recognition to automatically mark attendance. This project utilizes OpenCV for real-time face detection and recognition, offering a reliable and efficient solution for managing classroom attendance.

📌 Features
Real-time face detection and recognition

Automatically marks attendance with timestamp

Stores attendance records in CSV format

GUI for ease of use (if you added one)

Easy-to-update student database

🛠️ Technologies Used
Python 🐍

OpenCV 🎥

NumPy 📊

Tkinter (optional - for GUI) 🖥️

CSV (for attendance records) 📁

📷 How It Works
Face Registration
Capture and store images of each student with a unique ID or name.

Training Model
Use the collected images to train the face recognizer (LBPH or other model supported by OpenCV).

Real-Time Recognition
The webcam captures live video, detects faces, and matches them against the trained model.

Attendance Logging
If a face is recognized, the system logs the student's name, ID, date, and time in a CSV file.

🚀 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/attendance-system-opencv.git
cd attendance-system-opencv
Install dependencies:

bash
Copy
Edit
pip install opencv-python numpy
Run the system:

bash
Copy
Edit
python attendance.py
📂 Project Structure
perl
Copy
Edit
attendance-system-opencv/
│
├── dataset/             # Folder to store student face images
├── trainer/             # Trained model saved here
├── Attendance.csv       # Attendance records
├── attendance.py        # Main file to run the system
├── train.py             # Script to train the model
├── capture_faces.py     # Script to register new students
└── README.md            # Project documentation
📸 Sample Output
(Add screenshots or a demo video link here if available)

📅 Future Enhancements
Email notification on attendance

Face mask detection

Integration with cloud database

Mobile app support

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

📄 License
This project is open-source and available under the MIT License.

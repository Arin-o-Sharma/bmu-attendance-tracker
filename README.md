# 🎓 BMU Attendance & Bunk Tracker

An automated Python tool designed for BML Munjal University (BMU) students. This script securely logs into the Maitri portal, scrapes your live subject-wise attendance, and calculates exactly how many classes you can afford to skip while safely maintaining the mandatory 75% requirement.

## 🚀 Features
* **Automated Data Extraction:** No more clicking through menus; gets your attendance in seconds.
* **Smart "Bunk Math":** Dynamically calculates your safe skips based on the *actual* number of classes conducted, not a fixed guess.
* **Privacy First:** Uses Python's `getpass` module to hide your password while typing. Your credentials are **never** saved, stored, or sent anywhere except directly to the official BMU Maitri server.
* **Clear Status Indicators:** Instantly tells you if a subject is in the "SAFE" zone or the "DANGER" zone.

## 🛠️ Prerequisites
Before running this script, you need to have the following installed on your PC:
1. **Python 3.x** (Download from [python.org](https://www.python.org/downloads/))
2. **Microsoft Edge Browser** (The script uses the Edge WebDriver)

## 📦 Installation

1. **Clone the repository** (or download the ZIP file):
   ```bash
   git clone [https://github.com/YOUR-USERNAME/bmu-attendance-tracker.git](https://github.com/YOUR-USERNAME/bmu-attendance-tracker.git)
   cd bmu-attendance-tracker
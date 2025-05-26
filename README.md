# 📊 JSON to Excel Converter (Flask App)

This project is a lightweight Flask-based web application that allows users to fetch JSON data from a specified URL and convert it into a formatted Excel file (`.xlsx`). It’s especially useful for APIs that return simple JSON objects (e.g., IP geolocation data).

---

## 🚀 Features

- Fetches JSON data from any public API.
- Converts key-value pairs into a well-formatted Excel spreadsheet.
- Applies basic formatting (colors, bold text, borders).
- Allows file download directly from the web interface.

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Requests
- XlsxWriter
- HTML (Jinja2 templates)

---

## 🧑‍💻 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd project-folder
2. Install dependencies
```bash
pip install flask requests xlsxwriter
```
3. Run the application
```bash
python app.py
```
4. Open in browser
```bash
http://127.0.0.1:5000/
```

## 📝 Usage

- Enter a public URL that returns JSON (e.g., https://ipinfo.io/161.185.160.93/geo)
- Click Submit
- The app fetches the data, converts it to Excel, and automatically downloads the .xlsx file.

- ## ❗ Notes

- The dataFiles/ folder is automatically created to store generated Excel files.
- Make sure the input URL returns a JSON object (not an array or nested JSON) for best results.

 ## 📄 License
This project is open-source and free to use for educational and non-commercial purposes.

from flask import Flask, render_template, request, send_file
from apiToExcel import get_data, write_to_excel
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        url = request.form['url']
        data = get_data(url)

        if not write_to_excel(data, url):
            error = "Failed to write to Excel file."
        else:
            filename = f'{url.split("/")[2]}.xlsx'
            filepath = os.path.join('dataFiles',filename)
            return send_file(
                filepath,
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                as_attachment=True,
                download_name=filename
            )
    
    return render_template('index.html', error=error)

import os
import requests
import xlsxwriter


def get_data(url):
    """Fetches JSON data from the specified URL."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: HTTP status code {response.status_code}"
    except Exception as e:
        return f"Error: Unable to fetch data from the specified URL. Details: {e}"


def write_to_excel(data, url):
    """Writes key-value pairs from a dictionary to an Excel file."""
    try:
        os.makedirs('dataFiles', exist_ok=True)

        filename = f"{url.split('/')[2]}.xlsx"
        filepath = os.path.join('dataFiles', filename)

        workbook = xlsxwriter.Workbook(filepath)
        worksheet = workbook.add_worksheet()

        key_cell_format = workbook.add_format({
            'bold': True,
            'font_color': 'blue',
            'border': 1
        })

        value_cell_format = workbook.add_format({
            'bold': True,
            'font_color': 'green',
            'border': 1
        })

        worksheet.write(0, 0, "Key", key_cell_format)
        worksheet.write(0, 1, "Value", value_cell_format)

        for i, (key, value) in enumerate(data.items()):
            worksheet.write(i + 1, 0, key)
            worksheet.write(i + 1, 1, str(value))
        worksheet.autofit(max_width=2500)
        workbook.close()
        return True
    except Exception as e:
        print(f"Error while writing to Excel: {e}")
        return False

# url = "https://ipinfo.io/161.185.160.93/geo"
# write_to_excel(get_data(url))
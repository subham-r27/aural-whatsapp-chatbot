import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from config import SPREADSHEET_ID, GOOGLE_CREDENTIALS_FILE


scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    GOOGLE_CREDENTIALS_FILE,
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key(SPREADSHEET_ID).sheet1


def store_lead(phone, message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sheet.append_row([
        phone,
        message,
        timestamp
    ])
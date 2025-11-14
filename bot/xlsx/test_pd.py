import os
import pandas as pd
from bot.config import BASE_DIR

# [x] Oddiy dict data
# data = {
#     "Ismlar": ["Ali", "Vali", "Eshmat"],
#     "Yoshlar": [34, 24, 23],
#     "Daraja": ["Magister", "Bakalavr", "Bakalavr"]
# }

# [x] pandas DataFrame
# df = pd.DataFrame(data)
# print(df)

# [x] Excel Write
# EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'bot/xlsx/data/students.xlsx')
# df.to_excel(EXCEL_FILE_PATH)


# [x] Excel Read
# EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'bot/xlsx/data/students.xlsx')
# df = pd.read_excel(EXCEL_FILE_PATH)
# print(df)
# print(df[df['Yoshlar'] >= 24])


# [x] Excel create sheet_name
# EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'bot/xlsx/data/school.xlsx')
#
# d1 = {
#     "Category": ["Math", "Math", "English", "English"],
#     "Subcategory": ["1-class", "2-class", "2-class", "3-class"],
#     "Quiz": ["2 + 2 =?", "2 * 2 = ?", "My name ... John.", "... is your name?"],
#     "A_true": ["4", "4", "is", "What"],
#     "B": ["5", "8", "are", "Where"],
#     "C": ["2", "1", "or", "When"],
#     "D": ["22", "5", "no", "Why"],
# }
#
# d2 = {
#     "Name": ["Alex", "Bob", "John"],
#     "Age": [7, 8, 9],
# }
#
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
#
# with pd.ExcelWriter(EXCEL_FILE_PATH, engine='openpyxl') as writer:
#     df1.to_excel(writer, sheet_name='quizzes', index=False)
#     df2.to_excel(writer, sheet_name='students', index=False)


# [x] sheet_name dan ma'lumot o'qish
# EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'bot/xlsx/data/school.xlsx')
# df = pd.read_excel(EXCEL_FILE_PATH, sheet_name='students')
# print(df)

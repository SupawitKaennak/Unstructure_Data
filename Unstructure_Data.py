import kaggle
import pandas as pd

# ดาวน์โหลดชุดข้อมูลจาก Kaggle โดยใช้ API ของ Kaggle
kaggle.api.dataset_download_files('datadrivenx/video-game-stocks-financial-market-data', path='.', unzip=True)
print("Path to dataset files: . (ตำแหน่งที่เก็บไฟล์ข้อมูล)")

# อ่านข้อมูลจากไฟล์ CSV ที่ดาวน์โหลดมา และแปลงให้เป็น DataFrame ของ pandas
file_path = 'Top10VideoGameStocks.csv'  # แก้ไขเส้นทางไฟล์ตามที่ดาวน์โหลด
df = pd.read_csv(file_path)  # อ่านไฟล์ CSV

# แสดงข้อมูลบางส่วนจาก DataFrame ก่อนการจัดเรียง
print("Data before sorting: (ข้อมูลก่อนการจัดเรียง)")
print(df.head())  # แสดง 5 แถวแรกจาก DataFrame

# แปลงข้อมูลในคอลัมน์ 'Date' ให้เป็นชนิดข้อมูล datetime เพื่อให้สามารถจัดเรียงได้
df['Date'] = pd.to_datetime(df['Date'])  # แปลงคอลัมน์ 'Date' เป็น datetime

# จัดเรียงข้อมูลตาม 'Date' จากวันที่เก่ามาที่ใหม่
df_sorted = df.sort_values(by='Date')  # จัดเรียงข้อมูลตามคอลัมน์ 'Date'

# แสดงข้อมูลหลังจากการจัดเรียงตามคอลัมน์ 'Date'
print("\nData sorted by 'Date': (ข้อมูลหลังจากการจัดเรียงตามวันที่)")
print(df_sorted.head())  # แสดง 5 แถวแรกหลังจากการจัดเรียง

# การจัดเรียงข้อมูลตามหลายคอลัมน์ เช่น 'Date' และ 'Adj Close' (ราคาหุ้นที่ปรับแล้ว) จากเก่ามาใหม่และจากสูงไปต่ำ
df_sorted_multi = df.sort_values(by=['Date', 'Adj Close'], ascending=[True, False])  # จัดเรียงตาม 'Date' และ 'Adj Close'

# แสดงข้อมูลหลังจากการจัดเรียงหลายคอลัมน์
print("\nData sorted by 'Date' and 'Adj Close': (ข้อมูลหลังจากการจัดเรียงหลายคอลัมน์ตามวันที่และราคาหุ้นที่ปรับแล้ว)")
print(df_sorted_multi.head())  # แสดง 5 แถวแรกหลังการจัดเรียงหลายคอลัมน์

# บันทึกข้อมูลที่จัดเรียงแล้วลงในไฟล์ใหม่
df_sorted_multi.to_csv('sorted_video_game_stocks.csv', index=False)  # บันทึก DataFrame ที่จัดเรียงแล้วเป็นไฟล์ CSV ใหม่

# ตรวจสอบข้อมูลที่หายไปในแต่ละคอลัมน์
print("\nMissing values in each column: (ค่าที่หายไปในแต่ละคอลัมน์)")
print(df.isnull().sum())  # แสดงจำนวนค่าที่หายไปในแต่ละคอลัมน์

# กรณีที่ต้องการลบแถวที่มีข้อมูลหายไป
df_cleaned = df.dropna()  # ลบแถวที่มีค่า missing (NaN)
print("\nData after dropping rows with missing values: (ข้อมูลหลังจากลบแถวที่มีข้อมูลหายไป)")
print(df_cleaned.head())  # แสดงข้อมูลหลังจากลบแถวที่มีค่า missing

# กรณีที่ต้องการแทนที่ข้อมูลหายไปด้วยค่าเฉลี่ยของคอลัมน์
df['Adj Close'] = df['Adj Close'].fillna(df['Adj Close'].mean())  # แทนที่ค่าที่หายไปในคอลัมน์ 'Adj Close' ด้วยค่าเฉลี่ยของคอลัมน์
print("\nData after filling missing values with the mean: (ข้อมูลหลังจากแทนที่ค่าที่หายไปด้วยค่าเฉลี่ย)")
print(df.head())  # แสดงข้อมูลหลังจากแทนที่ค่าที่หายไป

# แสดงชื่อคอลัมน์ทั้งหมดใน DataFrame
print("\nFinal DataFrame columns: (ชื่อคอลัมน์ทั้งหมดใน DataFrame)", df.columns)  # แสดงชื่อคอลัมน์ทั้งหมดใน DataFrame

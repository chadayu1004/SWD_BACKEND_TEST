
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

def number_to_thai_text(number):
    thai_numbers = {
        0: 'ศูนย์',
        1: 'หนึ่ง',
        2: 'สอง',
        3: 'สาม',
        4: 'สี่',
        5: 'ห้า',
        6: 'หก',
        7: 'เจ็ด',
        8: 'แปด',
        9: 'เก้า',
        10: 'สิบ',
        20: 'ยี่สิบ'
    }

    thai_units = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

    if 0 <= number < 10000000:
        num_text = ""

        
        num_str = str(number)
        num_length = len(num_str)

        for i, digit in enumerate(num_str):
            digit = int(digit)
            unit_idx = num_length - i - 1

            if digit == 2 and unit_idx == 1 and number >= 20:
                num_text += thai_numbers[20]
            elif digit != 0:
                num_text += thai_numbers[digit] + thai_units[unit_idx]

        return num_text
    else:
        return "ค่าที่รับต้องอยู่ในช่วง 0 ถึง 10 ล้านเท่านั้น"


input_number = int(input("กรุณาใส่ตัวเลขระหว่าง 0 ถึง 10 ล้าน: "))
thai_text = number_to_thai_text(input_number)
print("ค่าของคุณเป็น:", thai_text)




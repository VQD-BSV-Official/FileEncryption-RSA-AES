import os
import string

def list_drives():
    # Liệt kê các ổ đĩa đang tồn tại
    drives = []
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives

def scan_files(drive_path):
    file_count = 0
    for root, dirs, files in os.walk(drive_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)  # In ra đường dẫn file (hoặc xử lý gì đó)
            file_count += 1
    return file_count

if __name__ == "__main__":
    drives = list_drives()
    for drive in drives:
        print(f"\n📁 Đang quét phân vùng: {drive}")
        total = scan_files(drive)
        print(f"🔍 Tổng số file trong {drive}: {total}")

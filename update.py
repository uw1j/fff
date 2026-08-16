import os
import sys
import requests

def update_tool():
    print("جاري التحديث...")
    repo_url = "https://raw.githubusercontent.com/lm9011109t-pixel/ps/main/"
    files_to_update = [
        "main.py",
        "config.py",
        "logo.py",
        "ua_generator.py",
        "password_manager.py",
        "proxy_manager.py",
        "m1_graph.py",
        "m2_bgraph.py",
        "m3_api.py",
        "main_menu.py"
    ]
    for file in files_to_update:
        try:
            response = requests.get(repo_url + file)
            if response.status_code == 200:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                print(f"✓ تم تحديث {file}")
            else:
                print(f"✗ فشل تحميل {file}")
        except Exception as e:
            print(f"✗ خطأ في {file}: {e}")
    print("اكتمل التحديث!")
    print("شغّل الأداة: python main.py")

if __name__ == "__main__":
    update_tool()
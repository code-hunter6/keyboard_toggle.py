import os
import sys

# আপনার টিভির ডিফল্ট কিবোর্ডের প্যাকেজ নাম (সাধারণত Gboard বা Android IME)
# এটি চেক করার কমান্ড: adb shell ime list -s
DEFAULT_KEYBOARD = "com.google.android.inputmethod.latin/.AndroidInputMethodService"

def disable_virtual_keyboard():
    print("টার্গেট: ভার্চুয়াল কিবোর্ড বন্ধ করা হচ্ছে...")
    # কিবোর্ড ডিজেবল করার কমান্ড
    os.system(f"adb shell ime disable {DEFAULT_KEYBOARD}")
    print("ভার্চুয়াল কিবোর্ড বন্ধ হয়েছে। এখন এক্সটার্নাল কিবোর্ড আরামসে ব্যবহার করুন।")

def enable_virtual_keyboard():
    print("টার্গেট: ভার্চুয়াল কিবোর্ড চালু করা হচ্ছে...")
    # কিবোর্ড এনাবল এবং ডিফল্ট করার কমান্ড
    os.system(f"adb shell ime enable {DEFAULT_KEYBOARD}")
    os.system(f"adb shell ime set {DEFAULT_KEYBOARD}")
    print("ভার্চুয়াল কিবোর্ড আবার চালু হয়েছে।")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ব্যবহার নিয়ম: python keyboard_toggle.py [off / on]")
        sys.exit(1)
        
    action = sys.argv[1].lower()
    
    if action == "off":
        disable_virtual_keyboard()
    elif action == "on":
        enable_virtual_keyboard()
    else:
        print("ভুল কমান্ড! শুধু 'on' অথবা 'off' ব্যবহার করুন।")

import os
import sys

# আপনার টিভির ডিফল্ট কিবোর্ডের প্যাকেজ নাম 
DEFAULT_KEYBOARD = "com.google.android.inputmethod.latin/.AndroidInputMethodService"

def disable_virtual_keyboard():
    print("ভার্চুয়াল কিবোর্ড বন্ধ করা হচ্ছে...")
    # ডেবিয়ান থেকে সরাসরি অ্যান্ড্রয়েড সিস্টেমে কমান্ড পাঠানোর জন্য
    os.system(f"am broadcast -a android.intent.action.CLOSE_SYSTEM_DIALOGS")
    os.system(f"ime disable {DEFAULT_KEYBOARD}")
    print("ভার্চুয়াল কিবোর্ড সফলভাবে বন্ধ করা হয়েছে।")

def enable_virtual_keyboard():
    print("ভার্চুয়াল কিবোর্ড চালু করা হচ্ছে...")
    os.system(f"ime enable {DEFAULT_KEYBOARD}")
    os.system(f"ime set {DEFAULT_KEYBOARD}")
    print("ভার্চুয়াল কিবোর্ড আবার চালু হয়েছে।")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ব্যবহার নিয়ম: python3 keyboard_toggle.py [off / on]")
        sys.exit(1)
        
    action = sys.argv[1].lower()
    
    if action == "off":
        disable_virtual_keyboard()
    elif action == "on":
        enable_virtual_keyboard()
    else:
        print("ভুল কমান্ড! শুধু 'on' অথবা 'off' ব্যবহার করুন।")

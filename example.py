import requests
import re

# הכתובת לקובץ ה-JSON הגולמי מהמאגר בגיטהאב
GITHUB_RAW_URL = "https://raw.githubusercontent.com/rb077858/hebrew-blacklist/main/badwords.json"

def get_bad_words():
    try:
        response = requests.get(GITHUB_RAW_URL)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"שגיאה במשיכת המאגר: {e}")
    return []

def filter_text(text, blacklist):
    if not blacklist:
        return text
    
    # יצירת תבנית Regex שמתאימה למילים ברשימה
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, blacklist)) + r')\b', re.IGNORECASE)
    
    # החלפת כל מילה פוגענית בכוכביות לפי אורך המילה
    return pattern.sub(lambda x: '*' * len(x.group()), text)

# בדיקה מעשית
if __name__ == "__main__":
    # 1. מושכים את הרשימה המעודכנת מהגיטהאב (כמו בקשת API)
    hebrew_blacklist = get_bad_words()
    
    # 2. טקסט לבדיקה
    user_input = "איזה יום דפוק, הכל הולך חרא היום"
    
    # 3. סינון הטקסט
    clean_output = filter_text(user_input, hebrew_blacklist)
    
    print("המקור:", user_input)
    print("המסונן:", clean_output)

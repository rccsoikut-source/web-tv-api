import json
import requests
from bs4 import BeautifulSoup

def fetch_live_sports():
    # উদাহরণস্বরূপ একটি স্পোর্টস সোর্স ইউআরএল (এখানে তোমার মূল সোর্স লিঙ্কটি বসবে)
    source_url = "https://example-sports-site.com/schedule" 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # ওয়েবসাইট থেকে ডেটা রিকোয়েস্ট করা
        response = requests.get(source_url, headers=headers, timeout=15)
        if response.status_code != 200:
            print("ওয়েবসাইট লোড করা যায়নি!")
            return None

        # HTML পার্স করা (BeautifulSoup দিয়ে ডাটা স্ক্র্যাপ করা)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # এখানে আমরা একটি স্ট্যান্ডার্ড স্ট্রাকচার তৈরি করছি যা তোমার আগের JSON এর মতো
        # বাস্তব ক্ষেত্রে ওয়েবসাইটের HTML ট্যাগ (যেমন div, class) দেখে এটি টিউন করতে হয়
        scraped_data = [
            {
                "day": "Today's Live Schedule",
                "categories": {
                    "Popular Live Events": [
                        {
                            "time": "Live",
                            "event": "Cricket: Live T20 Match",
                            "channels": [
                                {
                                    "channel_name": "Link - 1",
                                    "channel_id": "stream/cricket-1",
                                    "url": "https://daddylive.org/embed/embed.php?id=cricket-1&player=1"
                                }
                            ],
                            "source": "tv"
                        }
                    ]
                }
            }
        ]
        
        return scraped_data

    except Exception as e:
        print(f"ত্রুটি ঘটেছে: {e}")
        return None

def save_to_json(data):
    if data:
        with open("sports_schedule.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("sports_schedule.json ফাইলটি সফলভাবে আপডেট হয়েছে!")

if __name__ == "__main__":
    live_data = fetch_live_sports()
    if live_data:
        save_to_json(live_data)

# 📊 NotFollowers - Instagram Follower Analysis Tool

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg?style=flat)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](LICENSE)
[![Instagram](https://img.shields.io/badge/Instagram-@meelo1-E4405F.svg?style=flat&logo=instagram&logoColor=white)](https://instagram.com/meelo1)


> **Discover who doesn't follow you back on Instagram** 🔍

A Python script that analyzes your Instagram data to identify users you follow who don't follow you back. Clean, simple, and effective.

## ✨ Features

- 🎯 **Accurate Analysis** - Compare followers vs following lists
- 📁 **Multiple Outputs** - Generate organized text files for each category  
- 🚀 **Fast Processing** - Efficient regex-based username extraction
- 📝 **Detailed Logging** - Track the entire process with informative messages

## 🛠️ Requirements

- Python 3.6+
- `colorama` package for colored terminal output

Install dependencies:
```bash
pip install colorama
```

## 📥 Getting Instagram Data

Before using this tool, you need to download your Instagram data:

### Step-by-step Guide:

1. **Open Instagram** → Go to your profile
2. **Settings** → Your information and permissions
3. **Download your information** → Download or transfer information  
4. **Select data type** → Part of your information
5. **Choose "Connections"** → Select **Followers and Following**
6. **Download to device** → Choose this option
7. **Date range** → Select **"From the beginning"**
8. **Format** → Choose **HTML**
9. **Notification** → Email or your preferred method

Instagram will process your request and send you a download link when ready (usually within 48 hours).

## 📂 Setup

1. **Clone this repository:**
```bash
git clone https://github.com/yourusername/notfollowers.git
cd notfollowers
```

2. **Extract your Instagram data** and place the HTML files in the script directory:
   - `followers.html` - Your followers list
   - `following.html` - Users you follow

3. **Update file paths** in the script if needed:
```python
ruta_followers = r"C:\path\to\your\followers.html"
ruta_following = r"C:\path\to\your\following.html"
```

## 🚀 Usage

Run the script:
```bash
python notfollowers.py
```

## 📄 Output Files

The script generates three organized files:

| File | Description |
|------|-------------|
| `followers.txt` | Complete list of your followers |
| `following.txt` | Complete list of users you follow |
| `notfollowers.txt` | **Users you follow who don't follow back** |

## 📊 Example Output

```
==================================================
[START] FOLLOWER VERIFICATION PROCESS INITIATED
==================================================

[INFO] Loading file: followers.html
[OK] 1,247 users found.
[OK] Saved to: followers.txt

[INFO] Loading file: following.html  
[OK] 856 users found.
[OK] Saved to: following.txt

[INFO] Comparing files...
[RESULT] Users you FOLLOW but DON'T follow back: 23
[OK] Results saved to: notfollowers.txt

==================================================
[END] PROCESS COMPLETED
==================================================
```

## 🔧 How It Works

1. **Data Extraction** - Parses HTML files using regex to find Instagram URLs
2. **Username Filtering** - Extracts clean usernames from Instagram profile links
3. **Set Operations** - Uses Python sets for efficient comparison
4. **Result Generation** - Creates sorted, duplicate-free lists

### Core Regex Pattern:
```python
r'https://www\.instagram\.com/([a-zA-Z0-9_.]+)'
```

## ⚠️ Important Notes

- **Privacy First** - All processing is done locally, no data is sent anywhere
- **Instagram TOS** - Use responsibly and in accordance with Instagram's Terms of Service
- **Data Accuracy** - Results depend on the completeness of your downloaded Instagram data
- **Rate Limits** - This tool doesn't interact with Instagram's API, so no rate limiting issues

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new features  
- 🔧 Submit pull requests

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Created by [@meelot1](https://github.com/meelot1)**

---

⭐ **Found this useful? Give it a star!** ⭐

*Disclaimer: This tool is for educational and personal use only. Always respect Instagram's Terms of Service and user privacy.*

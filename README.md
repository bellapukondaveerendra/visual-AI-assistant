# 🧠 Visual AI Assistant (Screen Region Helper)

A lightweight and intuitive AI assistant that lets you **select any region on your screen**, ask a question about it, and receive AI-generated answers in real-time using OpenAI GPT-4o. Built using Python and Tkinter, this tool is perfect for getting contextual help on screen content without switching tabs or copying data manually.

---

## ✨ Features

- ⚡ **Hotkey Activation** (`Ctrl + Shift + H`)

- 🖼️ **Live Region Selector** on screen (no screenshot needed upfront)

- 💬 **Need Help?** button appears above selected region

- 📝 Transforms into a prompt textbox for typing queries

- 🤖 Sends both the selected screen region and your question to **OpenAI GPT-4o**

- 📋 Shows AI response in a popup window

- 🪶 Minimal dependencies, no browser or GUI frameworks needed beyond Tkinter

---

## 🔧 Installation

### 1. Clone the repository:

```bash

git clone https://github.com/yourusername/visual-ai-assistant.git

cd visual-ai-assistant
```

### 2\. Install dependencies:

Make sure you're using Python 3.10 or above.

bash
`pip install -r requirements.txt`

### `requirements.txt` includes:

`pyautogui
keyboard
openai`

> 📌 Note: This script uses `Tkinter`, which is built into Python's standard library.

## 🚀 Usage

1.  Set your OpenAI API key inside the script:

python
`client = OpenAI(api_key="your-api-key-here")`

1.  Run the application:

bash

`python visual_ai_assistant.py`

1.  Press `Ctrl + Shift + H` to activate the assistant.

2.  Select a region on your screen you want AI to analyze.

3.  Click the **"Need Help?"** button → type your question → click **"Ask AI"**.

4.  A popup will appear with your AI-generated response.

---

## 📸 How It Works

| Step                 | What Happens                                |
| -------------------- | ------------------------------------------- |
| 🔥 Hotkey Trigger    | Starts the region selection                 |
| 📐 You Select Region | Draw a box over the area you want help with |
| 💬 Need Help?        | Button appears above that box               |
| ✍️ Ask AI            | Enter your question                         |
| 🧠 GPT-4o            | OpenAI processes image + query              |
| 📥 AI Response       | Answer shown in popup window                |

---

## 📂 Project Structure

visual-ai-assistant/
│
├── visual_ai_assistant.py # Main script
├── capture.png # Temporary screenshot
└── README.md # Project documentation

## 💡 Use Cases

- Ask questions about a code block, web page, or diagram on your screen

- Instantly get help without switching windows

- Improve productivity while studying or debugging

---

## 🙏 Credits

- [OpenAI API](https://platform.openai.com)

- [PyAutoGUI](https://pyautogui.readthedocs.io/)

- [Tkinter](https://docs.python.org/3/library/tkinter.html)

---

## 📜 License

MIT License -- free to use and modify.

---

## 👨‍💻 Built By

**Veerendra Bellapukonda**\
[LinkedIn](https://www.linkedin.com/in/veerendra-bellapukonda-3a1245235/) - [GitHub](github.com/bellapukondaveerendra) - [Portfolio](https://bellapukondaveerendra.github.io/my-portfolio/)

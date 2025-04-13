import tkinter as tk
from tkinter import ttk
import keyboard
import threading
import pyautogui
import base64
from openai import OpenAI

# 🔑 Replace with your own OpenAI API key
client = OpenAI(api_key="****")



def start_region_selector():
    overlay = tk.Tk()
    overlay.attributes("-fullscreen", True)
    overlay.attributes("-alpha", 0.3)
    overlay.attributes("-topmost", True)
    overlay.configure(bg='black', cursor="crosshair")

    canvas = tk.Canvas(overlay, cursor="crosshair", bg="black")
    canvas.pack(fill="both", expand=True)

    rect_id = None
    start_x = start_y = 0

    def on_mouse_down(event):
        nonlocal start_x, start_y, rect_id
        start_x, start_y = event.x, event.y
        rect_id = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red", width=2)

    def on_mouse_move(event):
        nonlocal rect_id
        if rect_id:
            canvas.coords(rect_id, start_x, start_y, event.x, event.y)

    def on_mouse_up(event):
        end_x, end_y = event.x, event.y
        canvas.delete(rect_id)

        x1, y1 = min(start_x, end_x), min(start_y, end_y)
        x2, y2 = max(start_x, end_x), max(start_y, end_y)
        width, height = x2 - x1, y2 - y1

        canvas.create_rectangle(x1, y1, x2, y2, fill='yellow', stipple='gray25', outline='black', width=2)

        # Help Button
        # help_btn = ttk.Button(canvas, text="💬 Need Help on This?", command=lambda: transform_to_text(x1, y1, x2, y2, canvas))
        help_btn = tk.Button(canvas, text="💬 Need Help on This?",command=lambda: transform_to_text(x1, y1, x2, y2, canvas),bg="#2196F3", fg="white",font=("Segoe UI", 10, "bold"))
        canvas.create_window(x1 + 10, y1 - 25, anchor="nw", window=help_btn)

    def transform_to_text(x1, y1, x2, y2, canvas):
        canvas.delete("all")
        canvas.create_rectangle(x1, y1, x2, y2, fill='yellow', stipple='gray25', outline='black', width=2)
        text_area = tk.Text(canvas, width=40, height=4, font=("Segoe UI", 10, "bold"))
        canvas.create_window(x1, y1 - 80, anchor="nw", window=text_area)

        ask_button = tk.Button(canvas, text="Ask AI", bg="#2196F3", fg="white",font=("Segoe UI", 10, "bold"),command=lambda: send_to_ai(x1, y1, x2, y2, text_area.get("1.0", "end").strip()))
        canvas.create_window(x1 + 10, y2 - 30, anchor="nw", window=ask_button)

    # def send_to_ai(x1, y1, x2, y2, prompt):
    #     print(f"📸 Screenshot region: ({x1}, {y1}) to ({x2}, {y2})")
    #     print("🧠 User Prompt:", prompt)
    #     overlay.destroy()


    def send_to_ai(x1, y1, x2, y2, prompt):
        print("📸 Capturing region and sending to OpenAI...")

        def task():
            # Step 1: Screenshot
            screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
            screenshot.save("capture.png")

            # Step 2: Encode
            with open("capture.png", "rb") as f:
                b64_image = base64.b64encode(f.read()).decode("utf-8")

            # Step 3: Ask OpenAI
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_image}"}}
                    ]
                }],
                max_tokens=800
            )

            answer = response.choices[0].message.content
            # answer = response
            print("User prompt:", prompt)

            def show_response_window():
                overlay.destroy()
                res_win = tk.Toplevel()
                res_win.title("🧠 AI Response")
                res_win.geometry("600x400+100+100")
                res_win.configure(bg="white")
                res_win.attributes("-topmost", True)

                text_widget = tk.Text(res_win, wrap="word", bg="white", fg="black", font=("Segoe UI", 10))
                text_widget.insert("1.0", answer)
                text_widget.config(state="disabled")
                text_widget.pack(padx=10, pady=10, fill="both", expand=True)

                close_btn = tk.Button(res_win, text="❌ Close", command=res_win.destroy, bg="#e53935", fg="white")
                close_btn.pack(pady=(0, 10))
            canvas.after(0, show_response_window)

        threading.Thread(target=task).start()

    canvas.bind("<Button-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_move)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    overlay.mainloop()


def show_instruction_window():
    window = tk.Tk()
    window.title("🧠 AI Assistant")
    window.geometry("300x120+1200+100")  # adjust position to top-right corner
    window.attributes("-topmost", True)
    window.configure(bg="white")

    label = tk.Label(window, text="📌 Select the region you want AI to watch",
                     font=("Segoe UI", 11), wraplength=280, bg="white")
    label.pack(pady=(20, 10))
    ok_button = ttk.Button(window, text="OK, Let's Go", command=lambda: [window.destroy(), start_region_selector()])
    ok_button.pack(pady=(0, 10))

    window.mainloop()

def hotkey_listener():
    print("✅ Press Ctrl + Shift + H to activate AI assistant")
    keyboard.add_hotkey('ctrl+shift+h', lambda: threading.Thread(target=show_instruction_window).start())
    keyboard.wait('esc')  # optional: Esc to exit





if __name__ == "__main__":
    hotkey_listener()

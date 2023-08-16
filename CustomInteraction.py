import time
import win32api
import win32con


def drag_mouse(curr_x, new_x, y=1020, speed=0.5):
    if speed > 1 or speed < 0:
        raise ValueError(f'Parameter "speed" is defined to be in range: [0, 1] but is: {speed}')

    maxi = 50
    mini = 200
    smoothing_steps = round((speed*(maxi-mini))+mini)  # Reverse min-max normalization

    win32api.SetCursorPos((curr_x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, curr_x, y, 0, 0)

    # Compute intermediate steps for smooth movement
    for i in range(1, smoothing_steps + 1):
        intermediate_x = curr_x + (new_x - curr_x) * i / smoothing_steps
        win32api.SetCursorPos((int(intermediate_x), y))
        time.sleep(0.01)

    time.sleep(0.05)
    win32api.SetCursorPos((new_x, y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, new_x, y, 0, 0)

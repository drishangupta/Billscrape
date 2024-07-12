import ctypes
WS_EX_TOPMOST = 0x40000
windowTitle = "Refresh VPN"
message = "Click Yes if you have refreshed VPN"

# display a message box; execution will stop here until user acknowledges
ctypes.windll.user32.MessageBoxExW(None, message, windowTitle, WS_EX_TOPMOST)

print("User clicked OK.")

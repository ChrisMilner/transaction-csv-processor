import msvcrt

from ctypes import windll, sizeof, c_wchar, c_wchar_p, memmove, CDLL, get_errno, wintypes, c_size_t


# TODO: Extract and refactor
GMEM_MOVEABLE = 0x0002
CF_UNICODETEXT = 13

msvcrt = CDLL('msvcrt')

safeSetClipboardData = windll.user32.SetClipboardData
safeSetClipboardData.argtypes = [wintypes.UINT, wintypes.HANDLE]
safeSetClipboardData.restype = wintypes.HANDLE

safeGlobalAlloc = windll.kernel32.GlobalAlloc
safeGlobalAlloc.argtypes = [wintypes.UINT, c_size_t]
safeGlobalAlloc.restype = wintypes.HGLOBAL

GlobalLock = windll.kernel32.GlobalLock
GlobalLock.argtypes = wintypes.HGLOBAL,
GlobalLock.restype = wintypes.LPVOID

GlobalUnlock = windll.kernel32.GlobalUnlock
GlobalUnlock.argtypes = wintypes.HGLOBAL,
GlobalUnlock.restype = wintypes.BOOL

def copy_to_clipboard(text):
    hwnd = windll.user32.CreateWindowExA(0, b"STATIC", None, 0, 0, 0, 0, 0, None, None, None, None)
    windll.user32.OpenClipboard(hwnd)

    count = msvcrt.wcslen(text) + 1
    handle = safeGlobalAlloc(GMEM_MOVEABLE, count * sizeof(c_wchar))

    locked_handle = GlobalLock(handle)
    memmove(c_wchar_p(locked_handle), c_wchar_p(text), count * sizeof(c_wchar))
    windll.kernel32.GlobalUnlock(handle)

    safeSetClipboardData(CF_UNICODETEXT, handle)
    windll.user32.CloseClipboard()
    windll.user32.DestroyWindow(hwnd)
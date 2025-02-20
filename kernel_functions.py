from ctypes import windll, sizeof, c_wchar, c_wchar_p, memmove, CDLL, get_errno, wintypes, c_size_t


class KernelFunctions():
    GMEM_MOVEABLE = 0x0002
    CF_UNICODETEXT = 13

    wcslen = CDLL('msvcrt').wcslen

    openClipboard = windll.user32.OpenClipboard
    closeClipboard = windll.user32.CloseClipboard

    setClipboardData = windll.user32.SetClipboardData
    setClipboardData.argtypes = [wintypes.UINT, wintypes.HANDLE]
    setClipboardData.restype = wintypes.HANDLE

    globalAlloc = windll.kernel32.GlobalAlloc
    globalAlloc.argtypes = [wintypes.UINT, c_size_t]
    globalAlloc.restype = wintypes.HGLOBAL

    globalLock = windll.kernel32.GlobalLock
    globalLock.argtypes = wintypes.HGLOBAL,
    globalLock.restype = wintypes.LPVOID

    globalUnlock = windll.kernel32.GlobalUnlock
    globalUnlock.argtypes = wintypes.HGLOBAL,
    globalUnlock.restype = wintypes.BOOL

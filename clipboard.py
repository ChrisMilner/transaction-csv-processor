from ctypes import sizeof, c_wchar, c_wchar_p, memmove

from kernel_functions import KernelFunctions

def copy_to_clipboard(text):
    KernelFunctions.openClipboard(None)

    count = KernelFunctions.wcslen(text) + 1
    handle = KernelFunctions.globalAlloc(KernelFunctions.GMEM_MOVEABLE, count * sizeof(c_wchar))

    locked_handle = KernelFunctions.globalLock(handle)
    memmove(c_wchar_p(locked_handle), c_wchar_p(text), count * sizeof(c_wchar))
    KernelFunctions.globalUnlock(handle)

    KernelFunctions.setClipboardData(KernelFunctions.CF_UNICODETEXT, handle)
    KernelFunctions.closeClipboard()

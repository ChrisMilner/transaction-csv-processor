import contextlib
from ctypes import sizeof, c_wchar, c_wchar_p

from src.kernel_functions import KernelFunctions


@contextlib.contextmanager
def open_clipboard():
    KernelFunctions.openClipboard(None)

    try:
        yield
    finally:
        KernelFunctions.closeClipboard()

@contextlib.contextmanager
def global_lock_handle(handle):
    try:
        yield KernelFunctions.globalLock(handle)
    finally:
        KernelFunctions.globalUnlock(handle)

def copy_to_clipboard(text):
    with open_clipboard():
        length = KernelFunctions.wcslen(text) + 1
        handle = KernelFunctions.globalAlloc(KernelFunctions.GMEM_MOVEABLE, length * sizeof(c_wchar))

        with global_lock_handle(handle) as locked_handle:
            KernelFunctions.memmove(c_wchar_p(locked_handle), c_wchar_p(text), length * sizeof(c_wchar))

        KernelFunctions.setClipboardData(KernelFunctions.CF_UNICODETEXT, handle)

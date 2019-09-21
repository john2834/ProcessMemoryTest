import ctypes as c
from ctypes import wintypes as w



k32 = c.windll.kernel32

OpenProcess = k32.OpenProcess
OpenProcess.argtypes = [w.DWORD, w.BOOL, w.DWORD]
OpenProcess.restype = w.HANDLE

ReadProcessMemory = k32.ReadProcessMemory
ReadProcessMemory.argtypes = [w.HANDLE, w.LPCVOID, w.LPVOID, c.c_size_t, c.POINTER(c.c_size_t)]
ReadProcessMemory.restype = w.BOOL

WriteProcessMemory = k32.WriteProcessMemory
WriteProcessMemory.argtypes = [w.HANDLE, w.LPVOID, w.LPCVOID, c.c_size_t, c.POINTER(c.c_size_t)]
WriteProcessMemory.restype = w.BOOL


CloseHandle = k32.CloseHandle
CloseHandle.argtypes = [w.HANDLE]
CloseHandle.restype = w.BOOL

pid = 7664
processHandle = OpenProcess(0x10, False, pid)
print(processHandle)

addr = 0x5101F395
data = c.c_ulonglong()
OneMemory = ReadProcessMemory(processHandle, addr, c.byref(data), 4, None)
print('讀出內容：{} ({})'.format(data.value,OneMemory))

wPM = WriteProcessMemory(processHandle, addr, c.byref(c.c_longlong(100)), 4, None)
print('修改結果：{}'.format(wPM))

OneMemory = ReadProcessMemory(processHandle, addr, c.byref(data), 4, None)
print('修改後內容：{} ({})'.format(data.value,OneMemory))


CloseHandle(processHandle)


def set_dpi_awarness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwarness(1)
    except:
        pass

import sys
import os


def get_source_path(relative_path):
    if hasattr(sys,"_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)


dat_file_ico = get_source_path("1489187695-billingdatayencurrency_81853.ico")
dat_file_gr_png = get_source_path("gradient_400_500.png")
dat_file_gr_png2 = get_source_path("gradient_630_200.png")
dat_file_gr_png3 = get_source_path("gradient_800_340.png")
dat_file_gr_png4 = get_source_path("gradient_530_350.png")



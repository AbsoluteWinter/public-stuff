"""
Python Picture to PNG

Python 3.9+
"""

__version__ = "1.2.0"

import shutil
from pathlib import Path
from typing import List, Union

from PIL import Image
from pillow_heif import register_heif_opener
from tqdm import tqdm

register_heif_opener()

VALID_SUFFIX = {".jpg", ".jpeg", ".heic", ".heif"}
PIC_BACKUP_FOLDER = "AAAAA_OLD_PICS"


class Pic2Png:
    def __init__(self, path: Union[str, Path]) -> None:
        self.path = Path(path)
        self.old_pic_path = self.path.joinpath(PIC_BACKUP_FOLDER)
        self.old_pic_path.mkdir(parents=True, exist_ok=True)

        self._convert_desc = "Converting to png..."

    @property
    def pic_list(self) -> List[Path]:
        out = [
            x
            for x in self.path.glob("**/*")
            if x.suffix.lower() in VALID_SUFFIX
            and not x.is_dir()
            and x.parent.name != PIC_BACKUP_FOLDER
        ]
        return out

    def cleanup(self) -> None:
        """Clean up old pic folder"""
        shutil.rmtree(self.old_pic_path, ignore_errors=True)
        self.old_pic_path.mkdir(parents=True, exist_ok=True)

    def _convert_action(self, img: Path, delete_after_convert: bool = False) -> None:
        image = Image.open(img)
        image.save(img.with_suffix(".png"), "png")
        try:
            if delete_after_convert:
                img.unlink(missing_ok=True)
            shutil.move(img, self.old_pic_path)
        except Exception as e:
            print(f"File existed {e}")

    def convert(self, delete_after_convert: bool = False) -> None:
        for x in tqdm(
            self.pic_list, desc=self._convert_desc, unit_scale=True, ncols=88
        ):
            self._convert_action(x, delete_after_convert=delete_after_convert)

    # def convert_multithread(self):
    #     from joblib import Parallel, delayed
    #     self.cleanup()

    #     # Multithread
    #     Parallel(n_jobs=-1)(
    #         delayed(self._convert_action)(img)
    #         for img in tqdm(
    #             self.pic_list, desc=self._convert_desc, unit_scale=True, ncols=88
    #         )
    #     )


if __name__ == "__main__":
    here = Path(__file__).parent
    test = Pic2Png(here)
    test.convert()

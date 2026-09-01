import os
from pathlib import Path

def get_folders_and_files(path: str | Path, only_folders: bool = False, only_files: bool = False) -> tuple[list[Path], list[Path]] | list[Path]:
	path = Path(path)
	files: list[Path] = []
	folders: list[Path] = []

	for el in path.rglob("*"):
		if os.path.isdir(el) and not only_files:
			folders.append(el)

		elif not only_folders:
			files.append(el)

	if only_folders:
		return folders
	if only_files:
		return files
	return folders,files

def get_rsi(path: Path | None = None, folders: list[Path] | None = None) -> list[Path]:
	pass


if __name__ == '__main__':
	print(get_folders_and_files('D:/Projects/C', only_folders=True))
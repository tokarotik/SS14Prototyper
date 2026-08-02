import os

from pathlib import Path
from argparse import Namespace

from .static_config import StaticConfig

class Config:
	PATH_PROJECT: Path = Path()
	PATH_WORKING: Path = Path()


	def __init__(self, parsed_arguments: Namespace, static_cfg: StaticConfig) -> None:
		args = parsed_arguments

		self.PATH_PROJECT = Path(args.path_project)
		self.PATH_WORKING = self.PATH_PROJECT / static_cfg.FOLDER_RESOURCES


		if not os.path.isdir(self.PATH_PROJECT):
			raise FileExistsError(f'folder \'{self.PATH_PROJECT}\' doesn\'t exists')
		
		if not os.path.isdir(self.PATH_WORKING):
			raise FileExistsError(f'folder \'{self.PATH_WORKING}\' doesn\'t exists')
		


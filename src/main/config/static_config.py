from argparse import Namespace

class StaticConfig:
	FOLDER_RESOURCES = 'Resources'
	


	def __init__(self, parsed_arguments: Namespace) -> None:
		args = parsed_arguments

		if args.static_config_resources != None:
			self.FOLDER_RESOURCES = args.static_config_resources
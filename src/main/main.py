import sys
import traceback

from argparse import ArgumentParser, Namespace

from .config import StaticConfig, Config


def main(args: Namespace) -> int:
	try:
		## initialize configs
		static_config: StaticConfig = StaticConfig(args)
		config: Config = Config(args, static_config)

		## run
		print(config.PATH_PROJECT)

		return 0
	
	except:
		if args.debug: traceback.print_exc()
		return 1

if __name__ == "__main__":
	## init parser
	parser = ArgumentParser(prog='ss14-prototyper')

	## arguments	
	# positions
	parser.add_argument('path_project', help='path to root server what contain folder \'Resources\'')

	#optional
	parser.add_argument('--static_config_resources', type=str)
	parser.add_argument('--debug', action='store_true')

	## parsing
	args: Namespace = parser.parse_args()

	## launch
	sys.exit(main(args))

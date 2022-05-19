import argparse
import os


def parse_cli():
    project_path = os.getcwd()

    parser = argparse.ArgumentParser(description="page-loader")

    parser.add_argument("--output",
                        dest='save_path',
                        type=str,
                        default=project_path,
                        help='save path (default: project path)')
    parser.add_argument("webpage", type=str, help="address to webpage")

    args = parser.parse_args()
    save_path = args.save_path
    args_dict = vars(args)
    webpage = args_dict["webpage"]

    return save_path, webpage

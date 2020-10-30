import sys
if __package__:
    from .command import version
    from .command import *
else:
    from command import version
    from command import *


args = sys.argv


def main():
    if args[0] == 'update':
        return update()
    elif args[0] == 'upgrade':
        return upgrade()
    elif args[0] == 'install':
        return install(args[1:])
    elif args[0] == '-h' or args[0] == '--help':
        return show_help()
    elif args[0] == '-v' or args[0] == '--version':
        return show_version()
    else:
        return exit('Unknown command.')


if __name__ == '__main__':
    main()

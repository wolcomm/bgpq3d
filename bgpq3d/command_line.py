from bgpq3d import parser, dispatch


def main():
    args = parser.Parser().args
    dispatcher = dispatch.Dispatcher(args=args)
    return dispatcher.dispatch()

if __name__ == "__main__":
    result = main()
    exit(result)

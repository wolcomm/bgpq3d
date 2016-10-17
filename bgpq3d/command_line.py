from bgpq3d import parser, dispatch


def main():
    args = parser.Parser().args
    dispatcher = dispatch.Dispatcher(args=args)
    output = dispatcher.dispatch()
    print output

if __name__ == "__main__":
    main()

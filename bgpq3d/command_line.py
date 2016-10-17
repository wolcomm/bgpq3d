from bgpq3d import parser, bgpq3


def main():
    args = parser.Parser().args
    output = bgpq3.Bgpq3(args=args).pl()
    print output

if __name__ == "__main__":
    main()

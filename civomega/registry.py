class ParserRegistry(object):

    def __init__(self):
        self.parsers = {}

    def add_parser(self, name, parser_cls):
        self.parsers[name] = parser_cls

    def __iter__(self):
        return self.parsers.values()


REGISTRY = ParserRegistry()

# REGISTRY.add_parser('census', CensusParser)

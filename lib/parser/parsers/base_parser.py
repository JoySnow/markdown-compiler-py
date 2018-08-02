#from parser_factory import ParserFactory

class BaseParser(object):

    # We use some reflection to prettify the parser depedencies.
    # Basically, from calling a `foo_parser` method is the same as
    # doing `ParserFactory.build('foo_parser')`.

    # def method_missing(self, name):
    #     pass

    #NOTE: This method_missing is not never called in this prject,
    #      commented it out here ....
    pass

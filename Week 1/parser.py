import enum
import re


class TokenType(enum.Enum):
    T_NUM = 0
    T_DICE = 1
    T_PLUS = 2
    T_MINUS = 3
    T_MULT = 4
    T_DIV = 5
    T_MOD = 6
    T_CEIL = 7
    T_FLOOR = 8
    T_ROUND = 9
    T_ADV = 10
    T_DIS = 11
    T_HIGH = 12
    T_LOW = 13
    T_SET = 14
    T_UNIQUE = 10
    T_LPAR = 15
    T_RPAR = 16
    T_DELIN = 17
    T_END = 18


class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []


def lexical_analysis(string):
    mappings = {
        'd': TokenType.T_DICE,
        '+': TokenType.T_PLUS,
        '-': TokenType.T_MINUS,
        'x': TokenType.T_MULT, '*': TokenType.T_MULT,
        '/': TokenType.T_DIV,
        '%': TokenType.T_MOD,
        '^': TokenType.T_CEIL,
        'v': TokenType.T_FLOOR,
        'a': TokenType.T_ADV,
        'z': TokenType.T_DIS, 'b': TokenType.T_DIS,
        'h': TokenType.T_HIGH,
        'l': TokenType.T_LOW,
        '(': TokenType.T_LPAR,
        ')': TokenType.T_RPAR,
        ',': TokenType.T_DELIN,
        ';': TokenType.T_END,
        's': TokenType.T_SET,
        'u': TokenType.T_UNIQUE
    }
    tokens = []
    string = string.lower()
    for c in string:
        if c in mappings:
            token_type = mappings[c]
            token = Node(token_type, value=c)
            if not tokens:
                default_roll = Node(TokenType.T_NUM, value=1)
                tokens.append(default_roll)
            elif token_type == TokenType.T_DICE and tokens[-1].token_type != TokenType.T_NUM and tokens[-1].token_type != TokenType.T_RPAR:
                default_roll = Node(TokenType.T_NUM, value=1)
                tokens.append(default_roll)
        elif re.match(r'\d', c):
            if tokens and tokens[-1].token_type == TokenType.T_NUM:
                token = tokens.pop()
                token.value = int("{}{}".format(token.value, c))
            else:
                token = Node(TokenType.T_NUM, value=int(c))
        else:
            raise Exception('Invalid token: {}'.format(c))
        tokens.append(token)
    tokens.append(Node(TokenType.T_END))
    return tokens


def match(tokens, token):
    if tokens[0].token_type == token:
        return tokens.pop(0)
    else:
        raise Exception('Invalid syntax on token{}'.format(tokens[0].token_type))


def parse_e(tokens):
    left_node = parse_e2(tokens)

    while tokens[0].token_type in [TokenType.T_PLUS, TokenType.T_MINUS]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e2(tokens))
        left_node = node

    return left_node


def parse_e2(tokens):
    left_node = parse_e3(tokens)

    while tokens[0].token_type in [TokenType.T_MULT, TokenType.T_DIV, TokenType.T_MOD]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e3(tokens))
        left_node = node

    return left_node


def parse_e3(tokens):
    left_node = parse_e0(tokens)

    while tokens[0].token_type in [TokenType.T_DICE, TokenType.T_ADV, TokenType.T_DIS]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e3(tokens))
        left_node = node

    return left_node


def parse_e0(tokens):
    if tokens[0].token_type == TokenType.T_NUM:
        return tokens.pop(0)

    match(tokens, TokenType.T_LPAR)
    expression = parse_e(tokens)
    match(tokens, TokenType.T_RPAR)

    return expression


def parse(inputstring):
    tokens = lexical_analysis(inputstring)
    ast = parse_e(tokens)
    match(tokens, TokenType.T_END)
    return ast

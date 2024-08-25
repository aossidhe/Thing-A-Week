#!/usr/bin/env python3

import stdio
import sys
import random
import operator
import parser
import dice

# TODO: add --verbose, --help, etc
# TODO: add custom definitions?

operations = {
    parser.TokenType.T_PLUS: operator.add,
    parser.TokenType.T_MINUS: operator.sub,
    parser.TokenType.T_MULT: operator.mul,
    parser.TokenType.T_DIV: operator.floordiv,
    parser.TokenType.T_MOD: operator.mod,
    parser.TokenType.T_DICE: dice.roll,
    parser.TokenType.T_ADV: dice.advantage,
    parser.TokenType.T_DIS: dice.disadvantage,
    # parser.TokenType.T_LOW: dice.lowest,
    # parser.TokenType.T_HIGH: dice.highest
}


def compute(node):
    if node.token_type == parser.TokenType.T_NUM:
        return node.value
    left_result = compute(node.children[0])
    right_result = compute(node.children[1])
    operation = operations[node.token_type]
    return operation(left_result, right_result)


if __name__ == '__main__':
    ast = parser.parse(sys.argv[1])
    result = compute(ast)
    print(result)

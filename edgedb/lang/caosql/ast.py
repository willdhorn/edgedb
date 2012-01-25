##
# Copyright (c) 2008-2012 Sprymix Inc.
# All rights reserved.
#
# See LICENSE for details.
##


from semantix.caos.tree import ast as tree_ast
from semantix.utils import ast


class RootNode(ast.AST): __fields = ['children']

class ArgListNode(ast.AST): __fields = ['name', ('args', list)]
class BinOpNode(ast.AST):  __fields = ['left', 'op', 'right']
class FunctionCallNode(ast.AST): __fields = ['func', ('args', list), ('agg_sort', list)]

class VarNode(ast.AST): __fields = ['name']
class PathVarNode(VarNode): pass
class ConstantNode(ast.AST): __fields = ['value', 'index']

class UnaryOpNode(ast.AST): __fields = ['op', 'operand']

class PostfixOpNode(ast.AST): __fields = ['op', 'operand']

class PathNode(ast.AST): __fields = [('steps', list), 'quantifier', 'var', 'lvar']

class PathDisjunctionNode(ast.AST): __fields = ['left', 'right']

class PathStepNode(ast.AST): __fields = ['namespace', 'expr', 'link_expr']

class LinkNode(ast.AST): __fields = ['name', 'namespace', 'direction']

class LinkExprNode(ast.AST): __fields = ['expr']

class LinkPropExprNode(ast.AST): __fields = ['expr']

class SelectQueryNode(ast.AST):
    __fields = ['namespaces', 'distinct', ('targets', list), 'where', ('groupby', list),
                ('orderby', list), 'offset', 'limit', '_hash', ('cges', list)]

class CGENode(ast.AST):
    __fields = ['expr', 'alias']

class NamespaceDeclarationNode(ast.AST): __fields = ['namespace', 'alias']

class SortExprNode(ast.AST): __fields = ['path', 'direction', 'nones_order']

class PredicateNode(ast.AST): __fields = ['expr']

class ExistsPredicateNode(PredicateNode): pass

class SelectExprNode(ast.AST): __fields = ['expr', 'alias']

class FromExprNode(ast.AST): __fields = ['expr', 'alias']

class SequenceNode(ast.AST): __fields = [('elements', list)]

class PrototypeRefNode(ast.AST): __fields = ['name', 'module']

class TypeCastNode(ast.AST): __fields = ['expr', 'type']

class TypeRefNode(ast.AST): __fields = ['expr']

class CaosQLOperator(ast.ops.Operator):
    pass

LIKE = CaosQLOperator('~~')
NOT_LIKE = CaosQLOperator('!~~')
ILIKE = CaosQLOperator('~~*')
NOT_ILIKE = CaosQLOperator('!~~*')
IS_OF = CaosQLOperator('IS OF')
IS_NOT_OF = CaosQLOperator('IS NOT OF')


class SortOrder(tree_ast.SortOrder):
    _map = {
        tree_ast.SortAsc: 'SortAsc',
        tree_ast.SortDesc: 'SortDesc',
        tree_ast.SortDefault: 'SortDefault'
    }

SortAsc = SortOrder(tree_ast.SortAsc)
SortDesc = SortOrder(tree_ast.SortDesc)
SortDefault = SortOrder(tree_ast.SortDefault)


class NonesOrder(tree_ast.NonesOrder):
    _map = {
        tree_ast.NonesFirst: 'NonesFirst',
        tree_ast.NonesLast: 'NonesLast'
    }

NonesFirst = NonesOrder(tree_ast.NonesFirst)
NonesLast = NonesOrder(tree_ast.NonesLast)

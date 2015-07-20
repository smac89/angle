from kast import ast_export
# from kast.ast_export import emit_pyc
from parser_test_helper import *


class CompilerPythonEquivalenceTest(ParserBaseTest):
    def test_compiler_output_equivalence(self):
        source='../kast/tests/hi.py'
        contents=open(source).readlines()# all()
        contents="\n".join(contents)
        contents="print('hi')"
        inline="(string)" # compile from inline string source:
        source=inline
        file_ast=compile(contents, source, 'exec',ast.PyCF_ONLY_AST)
        # x=ast.dump(file_ast, annotate_fields=True, include_attributes=True)
        angle_ast=parse_tree(contents)
        print(ast.dump(file_ast, annotate_fields=False, include_attributes=False))
        print(ast.dump(angle_ast, annotate_fields=False, include_attributes=False))
        assert_equal(file_ast,angle_ast)
        code=compile(angle_ast, 'file', 'exec')
        if source==inline:
            ast_export.emit_pyc(code)
        else:
            ast_export.emit_pyc(code,source+".pyc")
        exec(code)

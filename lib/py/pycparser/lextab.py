# lextab.py. This file automatically created by PLY (version 3.10). Don't edit!
_tabversion = '3.10'
_lextokens = set(
    ('VOID', 'LBRACKET', 'WCHAR_CONST', 'FLOAT_CONST', 'MINUS', 'RPAREN',
     'LONG', 'PLUS', 'ELLIPSIS', 'GT', 'GOTO', 'ENUM', 'PERIOD', 'GE',
     'INT_CONST_DEC', 'ARROW', '__INT128', 'HEX_FLOAT_CONST', 'DOUBLE',
     'MINUSEQUAL', 'INT_CONST_OCT', 'TIMESEQUAL', 'OR', 'SHORT', 'RETURN',
     'RSHIFTEQUAL', 'RESTRICT', 'STATIC', 'SIZEOF', 'UNSIGNED', 'UNION',
     'COLON', 'WSTRING_LITERAL', 'DIVIDE', 'FOR', 'PLUSPLUS', 'EQUALS', 'ELSE',
     'INLINE', 'EQ', 'AND', 'TYPEID', 'LBRACE', 'PPHASH', 'INT', 'SIGNED',
     'CONTINUE', 'NOT', 'OREQUAL', 'MOD', 'RSHIFT', 'DEFAULT', 'CHAR', 'WHILE',
     'DIVEQUAL', 'EXTERN', 'CASE', 'LAND', 'REGISTER', 'MODEQUAL', 'NE',
     'SWITCH', 'INT_CONST_HEX', '_COMPLEX', 'PPPRAGMASTR', 'PLUSEQUAL',
     'STRUCT', 'CONDOP', 'BREAK', 'VOLATILE', 'PPPRAGMA', 'ANDEQUAL',
     'INT_CONST_BIN', 'DO', 'LNOT', 'CONST', 'LOR', 'CHAR_CONST', 'LSHIFT',
     'RBRACE', '_BOOL', 'LE', 'SEMI', 'LT', 'COMMA', 'OFFSETOF', 'TYPEDEF',
     'XOR', 'AUTO', 'TIMES', 'LPAREN', 'MINUSMINUS', 'ID', 'IF',
     'STRING_LITERAL', 'FLOAT', 'XOREQUAL', 'LSHIFTEQUAL', 'RBRACKET'))
_lexreflags = 64
_lexliterals = ''
_lexstateinfo = {
    'ppline': 'exclusive',
    'pppragma': 'exclusive',
    'INITIAL': 'inclusive'
}
_lexstatere = {
    'ppline':
    [('(?P<t_ppline_FILENAME>"([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*")|(?P<t_ppline_LINE_NUMBER>(0(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?)|([1-9][0-9]*(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?))|(?P<t_ppline_NEWLINE>\\n)|(?P<t_ppline_PPLINE>line)',
      [
          None, ('t_ppline_FILENAME', 'FILENAME'), None, None, None, None, None,
          None, ('t_ppline_LINE_NUMBER', 'LINE_NUMBER'), None, None, None, None,
          None, None, None, None, None, None, None, None, None, None, None,
          None, ('t_ppline_NEWLINE', 'NEWLINE'), ('t_ppline_PPLINE', 'PPLINE')
      ])],
    'pppragma':
    [('(?P<t_pppragma_NEWLINE>\\n)|(?P<t_pppragma_PPPRAGMA>pragma)|(?P<t_pppragma_STR>.+)',
      [
          None, ('t_pppragma_NEWLINE', 'NEWLINE'),
          ('t_pppragma_PPPRAGMA', 'PPPRAGMA'), ('t_pppragma_STR', 'STR')
      ])],
    'INITIAL':
    [('(?P<t_PPHASH>[ \\t]*\\#)|(?P<t_NEWLINE>\\n+)|(?P<t_LBRACE>\\{)|(?P<t_RBRACE>\\})|(?P<t_FLOAT_CONST>((((([0-9]*\\.[0-9]+)|([0-9]+\\.))([eE][-+]?[0-9]+)?)|([0-9]+([eE][-+]?[0-9]+)))[FfLl]?))|(?P<t_HEX_FLOAT_CONST>(0[xX]([0-9a-fA-F]+|((([0-9a-fA-F]+)?\\.[0-9a-fA-F]+)|([0-9a-fA-F]+\\.)))([pP][+-]?[0-9]+)[FfLl]?))|(?P<t_INT_CONST_HEX>0[xX][0-9a-fA-F]+(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?)',
      [
          None, ('t_PPHASH', 'PPHASH'), ('t_NEWLINE', 'NEWLINE'), ('t_LBRACE',
                                                                   'LBRACE'),
          ('t_RBRACE', 'RBRACE'), ('t_FLOAT_CONST', 'FLOAT_CONST'), None, None,
          None, None, None, None, None, None, None, ('t_HEX_FLOAT_CONST',
                                                     'HEX_FLOAT_CONST'), None,
          None, None, None, None, None, None, ('t_INT_CONST_HEX',
                                               'INT_CONST_HEX')
      ]),
     ('(?P<t_INT_CONST_BIN>0[bB][01]+(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?)|(?P<t_BAD_CONST_OCT>0[0-7]*[89])|(?P<t_INT_CONST_OCT>0[0-7]*(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?)|(?P<t_INT_CONST_DEC>(0(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?)|([1-9][0-9]*(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?))|(?P<t_CHAR_CONST>\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))\')|(?P<t_WCHAR_CONST>L\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))\')|(?P<t_UNMATCHED_QUOTE>(\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*\\n)|(\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*$))|(?P<t_BAD_CHAR_CONST>(\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))[^\'\n]+\')|(\'\')|(\'([\\\\][^a-zA-Z._~^!=&\\^\\-\\\\?\'"x0-7])[^\'\\n]*\'))',
      [
          None, ('t_INT_CONST_BIN', 'INT_CONST_BIN'), None, None, None, None,
          None, None, None, ('t_BAD_CONST_OCT',
                             'BAD_CONST_OCT'), ('t_INT_CONST_OCT',
                                                'INT_CONST_OCT'), None, None,
          None, None, None, None, None, ('t_INT_CONST_DEC', 'INT_CONST_DEC'),
          None, None, None, None, None, None, None, None, None, None, None,
          None, None, None, None, None, ('t_CHAR_CONST', 'CHAR_CONST'), None,
          None, None, None, None, None, ('t_WCHAR_CONST',
                                         'WCHAR_CONST'), None, None, None, None,
          None, None, ('t_UNMATCHED_QUOTE',
                       'UNMATCHED_QUOTE'), None, None, None, None, None, None,
          None, None, None, None, None, None, None, None, ('t_BAD_CHAR_CONST',
                                                           'BAD_CHAR_CONST')
      ]),
     ('(?P<t_WSTRING_LITERAL>L"([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*")|(?P<t_BAD_STRING_LITERAL>"([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*?([\\\\][^a-zA-Z._~^!=&\\^\\-\\\\?\'"x0-7])([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*")|(?P<t_ID>[a-zA-Z_$][0-9a-zA-Z_$]*)|(?P<t_STRING_LITERAL>"([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*")|(?P<t_ELLIPSIS>\\.\\.\\.)|(?P<t_PLUSPLUS>\\+\\+)|(?P<t_LOR>\\|\\|)|(?P<t_XOREQUAL>\\^=)|(?P<t_OREQUAL>\\|=)|(?P<t_LSHIFTEQUAL><<=)|(?P<t_RSHIFTEQUAL>>>=)|(?P<t_PLUSEQUAL>\\+=)|(?P<t_TIMESEQUAL>\\*=)|(?P<t_PLUS>\\+)|(?P<t_MODEQUAL>%=)|(?P<t_DIVEQUAL>/=)',
      [
          None, ('t_WSTRING_LITERAL', 'WSTRING_LITERAL'), None, None, None,
          None, None, None, ('t_BAD_STRING_LITERAL',
                             'BAD_STRING_LITERAL'), None, None, None, None,
          None, None, None, None, None, None, None, None, None, ('t_ID', 'ID'),
          (None,
           'STRING_LITERAL'), None, None, None, None, None, None, (None,
                                                                   'ELLIPSIS'),
          (None, 'PLUSPLUS'), (None, 'LOR'), (None, 'XOREQUAL'), (None,
                                                                  'OREQUAL'),
          (None, 'LSHIFTEQUAL'), (None, 'RSHIFTEQUAL'), (None, 'PLUSEQUAL'),
          (None, 'TIMESEQUAL'), (None, 'PLUS'), (None, 'MODEQUAL'), (None,
                                                                     'DIVEQUAL')
      ]),
     ('(?P<t_RBRACKET>\\])|(?P<t_CONDOP>\\?)|(?P<t_XOR>\\^)|(?P<t_LSHIFT><<)|(?P<t_LE><=)|(?P<t_LPAREN>\\()|(?P<t_ARROW>->)|(?P<t_EQ>==)|(?P<t_NE>!=)|(?P<t_MINUSMINUS>--)|(?P<t_OR>\\|)|(?P<t_TIMES>\\*)|(?P<t_LBRACKET>\\[)|(?P<t_GE>>=)|(?P<t_RPAREN>\\))|(?P<t_LAND>&&)|(?P<t_RSHIFT>>>)|(?P<t_MINUSEQUAL>-=)|(?P<t_PERIOD>\\.)|(?P<t_ANDEQUAL>&=)|(?P<t_EQUALS>=)|(?P<t_LT><)|(?P<t_COMMA>,)|(?P<t_DIVIDE>/)|(?P<t_AND>&)|(?P<t_MOD>%)|(?P<t_SEMI>;)|(?P<t_MINUS>-)|(?P<t_GT>>)|(?P<t_COLON>:)|(?P<t_NOT>~)|(?P<t_LNOT>!)',
      [
          None, (None, 'RBRACKET'), (None, 'CONDOP'), (None, 'XOR'),
          (None, 'LSHIFT'), (None, 'LE'), (None, 'LPAREN'), (None, 'ARROW'),
          (None, 'EQ'), (None, 'NE'), (None, 'MINUSMINUS'), (None, 'OR'),
          (None, 'TIMES'), (None, 'LBRACKET'), (None, 'GE'), (None, 'RPAREN'),
          (None, 'LAND'), (None, 'RSHIFT'), (None, 'MINUSEQUAL'), (None,
                                                                   'PERIOD'),
          (None, 'ANDEQUAL'), (None, 'EQUALS'), (None, 'LT'), (None, 'COMMA'),
          (None, 'DIVIDE'), (None, 'AND'), (None, 'MOD'), (None, 'SEMI'),
          (None, 'MINUS'), (None, 'GT'), (None, 'COLON'), (None,
                                                           'NOT'), (None,
                                                                    'LNOT')
      ])]
}
_lexstateignore = {'ppline': ' \t', 'pppragma': ' \t', 'INITIAL': ' \t'}
_lexstateerrorf = {
    'ppline': 't_ppline_error',
    'pppragma': 't_pppragma_error',
    'INITIAL': 't_error'
}
_lexstateeoff = {}

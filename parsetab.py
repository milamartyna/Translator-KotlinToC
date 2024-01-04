
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARITHMOP ARRAYTYPE ASSIGN ASSIGNOP BLOCKCOMMENT CBRACE COLON COMA COMMENT COMPOP CRBRACKET DOT ELSE FALSE FLOATNUMBER FOR FUN ID IF IN INCRDECR INT LOGICOP NEWLINE NUMBER OBRACE ORBRACKET RETURN SSTRING TRUE TYPE VAR WHILEstart : functionsfunctions : FUN function_header body functions\n        | emptyfunction_header : ID ORBRACKET function_variables CRBRACKET COLON TYPE\n        | ID ORBRACKET function_variables CRBRACKETfunction_variables : ID COLON TYPE\n        | ID COLON TYPE COMA function_variables\n        | emptyfunction_args : run_function\n        | value\n        | ID\n        | value COMA function_args\n        | emptybody : OBRACE NEWLINE actual_body CBRACEactual_body : return_line\n        | statement\n        | statement actual_body\n        | emptyreturn_line : RETURN expression\n        | RETURN run_function\n        | RETURN value NEWLINE\n        | RETURN ID NEWLINE\n        | emptystatement : expression\n        | var_assign\n        | while_loop\n        | run_function\n        | if_sentenceexpression : ID ARITHMOP ID NEWLINE\n        | ID INCRDECR NEWLINEvar_assign : VAR ID COLON TYPE ASSIGN value\n    | var_assign NEWLINErun_function : ID ORBRACKET function_args CRBRACKET\n    | ID ORBRACKET function_args CRBRACKET NEWLINEif_sentence : IF ORBRACKET bool_expression CRBRACKET body NEWLINE\n        | if_sentence else_sentenceelse_sentence : ELSE body NEWLINEwhile_loop : WHILE ORBRACKET bool_expression CRBRACKET body NEWLINEbool_expression : bool_expression and_or bool_expression\n                | ORBRACKET bool_expression CRBRACKET\n                | ID COMPOP ID\n                | value COMPOP value\n                | value COMPOP ID\n                | ID COMPOP value\n                | TRUE\n                | FALSEand_or : LOGICOPvalue : FLOATNUMBER\n    | NUMBER\n    | SSTRING\n    | TRUE\n    | FALSE\n    | emptyempty :'
    
_lr_action_items = {'FUN':([0,7,31,],[3,3,-14,]),'$end':([0,1,2,4,7,10,31,],[-54,0,-1,-3,-54,-2,-14,]),'ID':([3,9,11,17,19,20,21,23,24,25,26,37,38,39,40,41,42,43,45,46,47,50,51,57,65,72,74,75,76,77,81,82,83,84,87,89,98,99,100,],[6,12,22,22,36,-24,-27,-25,-26,-28,49,-48,-49,-50,-51,-52,-53,56,58,-32,-36,67,67,-30,67,12,-29,-33,58,-37,67,-47,93,96,-34,-54,-31,-38,-35,]),'OBRACE':([5,30,48,73,80,85,],[8,-5,8,-4,8,8,]),'ORBRACKET':([6,22,27,28,36,50,51,58,65,81,82,],[9,45,50,51,45,65,65,45,65,65,-47,]),'NEWLINE':([8,19,23,31,35,36,37,38,39,40,41,42,44,46,56,63,75,89,91,97,98,],[11,-54,46,-14,54,55,-48,-49,-50,-51,-52,-53,57,-32,74,77,87,-54,99,100,-31,]),'CRBRACKET':([9,13,14,37,38,39,40,41,42,45,52,58,59,60,61,62,66,69,70,71,72,75,76,79,83,84,86,87,88,90,92,93,94,95,96,],[-54,30,-8,-48,-49,-50,-51,-52,-53,-54,-6,-11,75,-9,-10,-13,80,-45,-46,85,-54,-33,-54,90,-54,-54,-7,-34,-12,-40,-39,-41,-44,-42,-43,]),'RETURN':([11,17,20,21,23,24,25,37,38,39,40,41,42,46,47,57,74,75,77,87,89,98,99,100,],[19,19,-24,-27,-25,-26,-28,-48,-49,-50,-51,-52,-53,-32,-36,-30,-29,-33,-37,-34,-54,-31,-38,-35,]),'CBRACE':([11,15,16,17,18,20,21,23,24,25,32,33,34,37,38,39,40,41,42,46,47,54,55,57,74,75,77,87,89,98,99,100,],[-54,31,-15,-16,-18,-24,-27,-25,-26,-28,-17,-19,-20,-48,-49,-50,-51,-52,-53,-32,-36,-21,-22,-30,-29,-33,-37,-34,-54,-31,-38,-35,]),'VAR':([11,17,20,21,23,24,25,37,38,39,40,41,42,46,47,57,74,75,77,87,89,98,99,100,],[26,26,-24,-27,-25,-26,-28,-48,-49,-50,-51,-52,-53,-32,-36,-30,-29,-33,-37,-34,-54,-31,-38,-35,]),'WHILE':([11,17,20,21,23,24,25,37,38,39,40,41,42,46,47,57,74,75,77,87,89,98,99,100,],[27,27,-24,-27,-25,-26,-28,-48,-49,-50,-51,-52,-53,-32,-36,-30,-29,-33,-37,-34,-54,-31,-38,-35,]),'IF':([11,17,20,21,23,24,25,37,38,39,40,41,42,46,47,57,74,75,77,87,89,98,99,100,],[28,28,-24,-27,-25,-26,-28,-48,-49,-50,-51,-52,-53,-32,-36,-30,-29,-33,-37,-34,-54,-31,-38,-35,]),'COLON':([12,30,49,],[29,53,64,]),'FLOATNUMBER':([19,45,50,51,65,76,81,82,83,84,89,],[37,37,37,37,37,37,37,-47,37,37,37,]),'NUMBER':([19,45,50,51,65,76,81,82,83,84,89,],[38,38,38,38,38,38,38,-47,38,38,38,]),'SSTRING':([19,45,50,51,65,76,81,82,83,84,89,],[39,39,39,39,39,39,39,-47,39,39,39,]),'TRUE':([19,45,50,51,65,76,81,82,83,84,89,],[40,40,69,69,69,40,69,-47,40,40,40,]),'FALSE':([19,45,50,51,65,76,81,82,83,84,89,],[41,41,70,70,70,41,70,-47,41,41,41,]),'ARITHMOP':([22,36,],[43,43,]),'INCRDECR':([22,36,],[44,44,]),'ELSE':([25,47,77,100,],[48,-36,-37,-35,]),'TYPE':([29,53,64,],[52,73,78,]),'COMA':([37,38,39,40,41,45,52,61,62,76,],[-48,-49,-50,-51,-52,-54,72,76,-53,-54,]),'COMPOP':([37,38,39,42,50,51,65,67,68,69,70,81,82,],[-48,-49,-50,-53,-54,-54,-54,83,84,-51,-52,-54,-47,]),'LOGICOP':([37,38,39,40,41,42,66,69,70,71,79,83,84,90,92,93,94,95,96,],[-48,-49,-50,-51,-52,-53,82,-45,-46,82,82,-54,-54,-40,82,-41,-44,-42,-43,]),'ASSIGN':([78,],[89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'functions':([0,7,],[2,10,]),'empty':([0,7,9,11,17,19,45,50,51,65,72,76,81,83,84,89,],[4,4,14,18,18,42,62,42,42,42,14,62,42,42,42,42,]),'function_header':([3,],[5,]),'body':([5,48,80,85,],[7,63,91,97,]),'function_variables':([9,72,],[13,86,]),'actual_body':([11,17,],[15,32,]),'return_line':([11,17,],[16,16,]),'statement':([11,17,],[17,17,]),'expression':([11,17,19,],[20,20,33,]),'run_function':([11,17,19,45,76,],[21,21,34,60,60,]),'var_assign':([11,17,],[23,23,]),'while_loop':([11,17,],[24,24,]),'if_sentence':([11,17,],[25,25,]),'value':([19,45,50,51,65,76,81,83,84,89,],[35,61,68,68,68,61,68,94,95,98,]),'else_sentence':([25,],[47,]),'function_args':([45,76,],[59,88,]),'bool_expression':([50,51,65,81,],[66,71,79,92,]),'and_or':([66,71,79,92,],[81,81,81,81,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> functions','start',1,'p_start','main.py',78),
  ('functions -> FUN function_header body functions','functions',4,'p_functions','main.py',86),
  ('functions -> empty','functions',1,'p_functions','main.py',87),
  ('function_header -> ID ORBRACKET function_variables CRBRACKET COLON TYPE','function_header',6,'p_function_header','main.py',95),
  ('function_header -> ID ORBRACKET function_variables CRBRACKET','function_header',4,'p_function_header','main.py',96),
  ('function_variables -> ID COLON TYPE','function_variables',3,'p_function_variables','main.py',107),
  ('function_variables -> ID COLON TYPE COMA function_variables','function_variables',5,'p_function_variables','main.py',108),
  ('function_variables -> empty','function_variables',1,'p_function_variables','main.py',109),
  ('function_args -> run_function','function_args',1,'p_function_args','main.py',123),
  ('function_args -> value','function_args',1,'p_function_args','main.py',124),
  ('function_args -> ID','function_args',1,'p_function_args','main.py',125),
  ('function_args -> value COMA function_args','function_args',3,'p_function_args','main.py',126),
  ('function_args -> empty','function_args',1,'p_function_args','main.py',127),
  ('body -> OBRACE NEWLINE actual_body CBRACE','body',4,'p_body','main.py',135),
  ('actual_body -> return_line','actual_body',1,'p_actual_body','main.py',140),
  ('actual_body -> statement','actual_body',1,'p_actual_body','main.py',141),
  ('actual_body -> statement actual_body','actual_body',2,'p_actual_body','main.py',142),
  ('actual_body -> empty','actual_body',1,'p_actual_body','main.py',143),
  ('return_line -> RETURN expression','return_line',2,'p_return_line','main.py',151),
  ('return_line -> RETURN run_function','return_line',2,'p_return_line','main.py',152),
  ('return_line -> RETURN value NEWLINE','return_line',3,'p_return_line','main.py',153),
  ('return_line -> RETURN ID NEWLINE','return_line',3,'p_return_line','main.py',154),
  ('return_line -> empty','return_line',1,'p_return_line','main.py',155),
  ('statement -> expression','statement',1,'p_statement','main.py',165),
  ('statement -> var_assign','statement',1,'p_statement','main.py',166),
  ('statement -> while_loop','statement',1,'p_statement','main.py',167),
  ('statement -> run_function','statement',1,'p_statement','main.py',168),
  ('statement -> if_sentence','statement',1,'p_statement','main.py',169),
  ('expression -> ID ARITHMOP ID NEWLINE','expression',4,'p_expression','main.py',174),
  ('expression -> ID INCRDECR NEWLINE','expression',3,'p_expression','main.py',175),
  ('var_assign -> VAR ID COLON TYPE ASSIGN value','var_assign',6,'p_var_assign','main.py',185),
  ('var_assign -> var_assign NEWLINE','var_assign',2,'p_var_assign','main.py',186),
  ('run_function -> ID ORBRACKET function_args CRBRACKET','run_function',4,'p_run_function','main.py',197),
  ('run_function -> ID ORBRACKET function_args CRBRACKET NEWLINE','run_function',5,'p_run_function','main.py',198),
  ('if_sentence -> IF ORBRACKET bool_expression CRBRACKET body NEWLINE','if_sentence',6,'p_if_sentence','main.py',206),
  ('if_sentence -> if_sentence else_sentence','if_sentence',2,'p_if_sentence','main.py',207),
  ('else_sentence -> ELSE body NEWLINE','else_sentence',3,'p_else_sentence','main.py',215),
  ('while_loop -> WHILE ORBRACKET bool_expression CRBRACKET body NEWLINE','while_loop',6,'p_while_loop','main.py',220),
  ('bool_expression -> bool_expression and_or bool_expression','bool_expression',3,'p_bool_expression','main.py',225),
  ('bool_expression -> ORBRACKET bool_expression CRBRACKET','bool_expression',3,'p_bool_expression','main.py',226),
  ('bool_expression -> ID COMPOP ID','bool_expression',3,'p_bool_expression','main.py',227),
  ('bool_expression -> value COMPOP value','bool_expression',3,'p_bool_expression','main.py',228),
  ('bool_expression -> value COMPOP ID','bool_expression',3,'p_bool_expression','main.py',229),
  ('bool_expression -> ID COMPOP value','bool_expression',3,'p_bool_expression','main.py',230),
  ('bool_expression -> TRUE','bool_expression',1,'p_bool_expression','main.py',231),
  ('bool_expression -> FALSE','bool_expression',1,'p_bool_expression','main.py',232),
  ('and_or -> LOGICOP','and_or',1,'p_and_or','main.py',240),
  ('value -> FLOATNUMBER','value',1,'p_value','main.py',245),
  ('value -> NUMBER','value',1,'p_value','main.py',246),
  ('value -> SSTRING','value',1,'p_value','main.py',247),
  ('value -> TRUE','value',1,'p_value','main.py',248),
  ('value -> FALSE','value',1,'p_value','main.py',249),
  ('value -> empty','value',1,'p_value','main.py',250),
  ('empty -> <empty>','empty',0,'p_empty','main.py',255),
]

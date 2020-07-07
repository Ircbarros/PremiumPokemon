************* Module main
main.py:74:0: R0902: Too many instance attributes (19/7) (too-many-instance-attributes)
main.py:182:4: R0201: Method could be a function (no-self-use)
main.py:199:8: W0603: Using the global statement (global-statement)
main.py:226:12: C0103: Variable name "x" doesn't conform to snake_case naming style (invalid-name)
main.py:228:12: C0103: Variable name "y" doesn't conform to snake_case naming style (invalid-name)
main.py:270:8: W0107: Unnecessary pass statement (unnecessary-pass)
main.py:154:8: W0201: Attribute 'all_sprites' defined outside __init__ (attribute-defined-outside-init)
main.py:155:8: W0201: Attribute 'limits' defined outside __init__ (attribute-defined-outside-init)
main.py:156:8: W0201: Attribute 'items' defined outside __init__ (attribute-defined-outside-init)
main.py:164:20: W0201: Attribute 'player' defined outside __init__ (attribute-defined-outside-init)
main.py:168:8: W0201: Attribute 'camera' defined outside __init__ (attribute-defined-outside-init)
main.py:175:8: W0201: Attribute 'playing' defined outside __init__ (attribute-defined-outside-init)
main.py:201:8: W0201: Attribute 'pokebolas_qtd' defined outside __init__ (attribute-defined-outside-init)
main.py:214:8: W0201: Attribute 'hits' defined outside __init__ (attribute-defined-outside-init)
main.py:340:12: W0601: Global variable 'DESIRED_PATH' undefined at the module level (global-variable-undefined)


Report
======
120 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |NC         |NC         |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |1      |NC         |NC         |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|method   |11     |NC         |NC         |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |2      |NC         |NC         |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+



External dependencies
---------------------
::

    pygame (main)
    world 
      \-settings (main)
      \-sprites (main)
      \-tilemap (main)



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |139    |39.49 |NC       |NC         |
+----------+-------+------+---------+-----------+
|docstring |143    |40.62 |NC       |NC         |
+----------+-------+------+---------+-----------+
|comment   |41     |11.65 |NC       |NC         |
+----------+-------+------+---------+-----------+
|empty     |29     |8.24  |NC       |NC         |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |NC       |NC         |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |NC       |NC         |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |2      |NC       |NC         |
+-----------+-------+---------+-----------+
|refactor   |2      |NC       |NC         |
+-----------+-------+---------+-----------+
|warning    |11     |NC       |NC         |
+-----------+-------+---------+-----------+
|error      |0      |NC       |NC         |
+-----------+-------+---------+-----------+



Messages
--------

+-------------------------------+------------+
|message id                     |occurrences |
+===============================+============+
|attribute-defined-outside-init |8           |
+-------------------------------+------------+
|invalid-name                   |2           |
+-------------------------------+------------+
|unnecessary-pass               |1           |
+-------------------------------+------------+
|too-many-instance-attributes   |1           |
+-------------------------------+------------+
|no-self-use                    |1           |
+-------------------------------+------------+
|global-variable-undefined      |1           |
+-------------------------------+------------+
|global-statement               |1           |
+-------------------------------+------------+




------------------------------------------------------------------
Your code has been rated at 8.75/10 (previous run: 8.75/10, +0.00)


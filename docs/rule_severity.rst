Rule Severity
=============

VSG supports rule severity with two built in levels:  Error and Warning.
The default behavior for most rules is **Error**.
Only the **Error** severity level will result in an exit status of 1.
**Errors** will also be the only errors written to a JUnit XML file if that option is chosen.

The table below summarizes the built in severities:

+-------------+---------+-------------+-------+-----------+---------------------------------------------------------------+
| Name        |  Type   | Exit Status | JUnit | Syntastic | Description                                                   |
+=============+=========+=============+=======+===========+===============================================================+
| Error       |  error  |      1      |  Yes  |   ERROR   | A rule which must be fixed.                                   |
+-------------+---------+-------------+-------+-----------+---------------------------------------------------------------+
| Warning     | warning |      0      |  No   |  WARNING  | A rule which should be fixed if it is reasonable to do so.    |
+-------------+---------+-------------+-------+-----------+---------------------------------------------------------------+

Configuring Severity Levels
---------------------------

The existing severity level of a rule can be configured.
For example, if you want to change the line length rule, *length_001*, to a **Warning** instead of an **Error**, use the following configuration:

.. code-block:: json

   {
       "rule":{
           "length_001":{
               "severity": "Warning"
           }
       }
   }

Defining Severity Levels
------------------------

VSG supports user defined severity level.
Any new severity level will follow the same rules as a **Warning** severity.
It will be reported to the screen, but will not be reported in JUnit XML files and will not force an exit status of 1.

To create your own severity level, create a configuration which defines just the severity level following this format:

.. code-block:: json

   {
       "severity":{
           "Guideline":{
               "type":"warning"
           },
           "Todo":{
               "type":"error"
           }
       }
   }

This configuration defines two new severities:  **Guideline** and **Todo**.
The **Guideline** severity is set to the **warning** type.
The **Todo** severity is set to the **error** type.

The newly defined severity levels can then be applied to a rule using a second configuration.

.. code-block:: json

   {
       "rule":{
           "length_001":{
               "severity": "Guideline"
           }
       }
   }

Apply the defined severity levels by calling both configurations:

.. code-block:: mono

   vsg -c severity.json rule_configuration.json -f fifo.vhd


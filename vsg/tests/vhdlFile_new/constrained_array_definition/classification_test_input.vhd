
architecture RTL of FIFO is

  type Real_Matrix is array (1 to 10) of REAL;

  type BYTE is array (0 to 7) of BIT;

  type Log_4_Vector is array (POSITIVE range 1 to 8, POSITIVE range 1 to 2) of Log_4;

--  type X is (LOW, HIGH);

  type DATA_BUS is array (0 to 7, X) of BIT;

begin

end architecture RTL;

namespace py calculadora

# Adaptado de https://github.com/apache/thrift/blob/master/tutorial/tutorial.thrift

typedef i32 int 

/**
 * Tipos de datos disponibles:
 *
 *  bool        Boolean, one byte
 *  i8 (byte)   Signed 8-bit integer
 *  i16         Signed 16-bit integer
 *  i32         Signed 32-bit integer
 *  i64         Signed 64-bit integer
 *  double      64-bit floating point value
 *  string      String
 *  binary      Blob (byte array)
 *  map<t1,t2>  Map from one type to another
 *  list<t1>    Ordered list of one type
 *  set<t1>     Set of unique elements of one type
 */

enum Operaciones {
  SUMA = 1,
  RESTA = 2,
  PRODUCTO = 3,
  DIVISION = 4
}

struct Proceso {
  1: int num1,
  2: int num2,
  3: Operaciones op
}

service CalculadoraService
{
  int  calcular(1:Proceso p)
}
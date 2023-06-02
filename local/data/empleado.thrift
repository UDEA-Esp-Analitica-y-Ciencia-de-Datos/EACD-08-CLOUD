namespace py Empleado

struct Empleado {
	1: i32 id,
  	2: string nombre,
  	3: i32 edad,
  	4: string sexo,
  	5: string profesion,
  	6: i32 salario,
}


service EmpleadoServicio {
	string msg(),
	string send_Emp(1: Empleado new_emp),
	bool mayor40(1: Empleado emp)
}
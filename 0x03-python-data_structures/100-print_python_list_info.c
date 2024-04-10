#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p);
{
	long int size = PyList_Size(p);
	int iterator;
	PyListObject *obj = (PyListobject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (iterator = 0; iterator < size; iterator++)
		printf("Element %i: %s\n", iterator, Py_TYPE(obj->ob_item[iterator])->tp_name);
}

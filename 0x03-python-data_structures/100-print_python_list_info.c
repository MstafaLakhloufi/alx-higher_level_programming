#include <Python.h>

/**
* print_python_list_info- Prints basic info about python list 
* @p: A Pyobject list.
*/

void print_python_list_info (PyObject *p)
{
	int size, alloc, i;
	Pyobject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListobject *)p)->allocated:

	printf("[*] Size of the Python List = %d\n", size); 
	printf("[*] Allocated = %d\n", alloc);

	for (i=0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE (obj)->tp_name);
	}
}

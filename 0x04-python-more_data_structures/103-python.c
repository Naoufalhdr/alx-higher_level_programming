#include "Python.h"

/**
  * print_python_list - Prints information about python lists objects
  * @p: PyObject pointer to print info about
  */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, py_list_size;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object_cast;

	list_object_cast = (PyListObject *)p;
	py_list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) py_list_size);
	printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);
	for (i = 0; i < py_list_size; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = (PyObject*(item))->ob_size->tp_name;
		printf("Element %d: %s\n", (int) i, item_type);
	}
}

/**
  * print_python_bytes - Prints information about python bytes objects
  * @p: PyObject pointer to print info about
  */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	unsigned char i, size;

	/* Check if the input is a valid bytes object */
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));

	size = (unsigned char)PyBytes_Size(p);
	if (size > 10)
		size = 10;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}


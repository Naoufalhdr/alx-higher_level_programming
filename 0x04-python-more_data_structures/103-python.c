#include "Python.h"

/**
  * print_python_list - Prints information about python lists objects
  * @p: PyObject pointer to print info about
  */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, py_list_size;
	PyObject *item;
	PyTypeObject *type;

	/* Check if the input is a valid list object */
	if (!PyList_Check(p))
	{
		printf("[*] Size of the Python List = 0\n");
		printf("[*] Allocated = 0\n");
		return;
	}

	py_list_size = ((PyVarObject *)p)->ob_size;

	printf("[*] Size of the Python List = %ld\n", py_list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < py_list_size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		type = PyObject_Type(item);
		printf("Element %ld: %s\n", i, type->tp_name);
		Py_DECREF(type);
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


#include <algorithm>
#include "Python.h"
extern void ccsort(int **, int);

using namespace std;

void sort(int **a, int len) {
    sort(*a, *a + len);
    return;
}

PyObject* mycc_sort(PyObject* self, PyObject* args)
{
    int **a;
    int len;

    if (!PyArg_ParseTuple(args, "ii", *a, &len))
        return NULL;
    sort(a, len)
    return Py_BuildValue("i", a);
}

static PyMethodDef myccmethods[] = {
    {"sort", mycc_sort, METH_VARARGS},
    {NULL},
};

void initmycc()
{
    Py_InitModule("mycc", myccmethods);
}


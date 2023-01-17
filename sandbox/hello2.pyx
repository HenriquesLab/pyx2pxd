# cython: infer_types=True, wraparound=False, nonecheck=False, boundscheck=False, autogen_pxd=True, cdivision=True, language_level=3, profile=True

cdef float repeater(float v):
    return v
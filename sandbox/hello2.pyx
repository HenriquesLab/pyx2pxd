# cython: infer_types=True, wraparound=False, nonecheck=False, boundscheck=False, autogen_pxd=True, cdivision=True, language_level=3, profile=True

cdef float repeater(float v):
    return v


cdef class Repeater2:

    # autogen_pxd: cdef float v

    def __init__(self, v):
        self.v = v

    cdef float repeat(self):
        return self.v
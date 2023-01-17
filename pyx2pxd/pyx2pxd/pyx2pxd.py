"""Main module."""

import os, sys


def find_files(root_dir, extension):
    """
    Returns a list of files with given extension in the root directory.
    """
    target_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(extension):
                target_files.append(os.path.join(root, file))
                print(f"Found file {file}")

    return target_files


def autogenerate_pxd_files(filename):
    """Autogenerate pxd files from pyx files"""

    ext = os.path.splitext(filename)[1]
    assert ext == ".pyx", "File must be a pyx file"

    pxd_filename = os.path.splitext(filename)[0] + ".pxd"

    autogen = False
    cdefs = []

    # extract pre-existing pxd imports
    if os.path.exists(pxd_filename):
        with open(pxd_filename, "r") as f:
            pxd_file = f.read()
            lines = pxd_file.splitlines()
            ignore = False
            for line in lines:
                if "# autogen_pxd - ignore start" in line:
                    ignore = True
                elif "# autogen_pxd - ignore end" in line:
                    ignore = False

                if line.startswith("from") or ignore:
                    cdefs.append(line)

    cdefs.append("")

    # read the pyx file
    with open(filename, "r") as f:
        pyx_file = f.read()
        lines = pyx_file.splitlines()

        for line in lines:
            if line.startswith("# cython:") and "autogen_pxd=False" in line:
                return
            elif line.startswith("# cython:") and "autogen_pxd=True" in line:
                autogen = True
            elif line.startswith("cdef class"):
                cdefs.append("")
                cdefs.append(line)
            elif (
                (line.startswith("cdef") or line.startswith("    cdef"))
                and line.endswith(":")
                and ")" in line
            ):
                cdefs.append(line[:-1])

        cdefs.append("")

    if not autogen:
        return

    # write the pxd file
    pxd_text = "\n".join(cdefs)

    if not os.path.exists(pxd_filename) or open(pxd_filename).read() != pxd_text:
        with open(pxd_filename, "w") as f:
            print("Autogenerating pxd file: ", pxd_filename)
            f.write("\n".join(cdefs))

def main():
    if len(sys.argv) == 1:
        return
    
    path = sys.argv[1]
    if not os.path.exists(path):
        raise RuntimeError(f"{path} does not exist")

    print(f"Searching {path} for .pyx files...")
    pyx_files = find_files(path, ".pyx")
    for file in pyx_files:
        autogenerate_pxd_files(file)
    
if __name__ == "__main__":
    main()
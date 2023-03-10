"""Main module."""

import os
import sys


def find_files(root_dir: str, extension: str) -> list:
    """
    Returns a list of files with given extension in the root directory.
    :param root_dir: Root directory to search
    :param extension: File extension to search for
    :return: List of files with given extension
    """
    target_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(extension):
                path = os.path.join(root, file)
                target_files.append(path)
                # print(f"Found file: {path}")

    return target_files


def autogenerate_pxd_file(pyx_filename: str):
    """
    Autogenerate pxd file for given pyx file
    :param pyx_filename: .pyx file to autogenerate pxd file for
    """

    ext = os.path.splitext(pyx_filename)[1]
    assert ext == ".pyx", "File must be a pyx file"

    pxd_filename = os.path.splitext(pyx_filename)[0] + ".pxd"

    autogen = False
    pxd_prefix_txt = ""
    pxd_lines = [
        "# Code below is autogenerated by pyx2pxd - https://github.com/HenriquesLab/pyx2pxd",
        "",
    ]

    # extract pre-existing pxd imports
    if os.path.exists(pxd_filename):
        with open(pxd_filename, "r") as f:
            pxd_file_txt = f.read()

            tag = "# pyx2pxd: starting point"
            if tag in pxd_file_txt:
                splitter = pxd_file_txt.find(tag) + len(tag)
                pxd_prefix_txt = pxd_file_txt[:splitter] + "\n"
                pxd_file_txt = pxd_file_txt[splitter:]

            lines = pxd_file_txt.splitlines()
            for line in lines:
                if line.startswith("from"):
                    pxd_lines.append(line)

    # read the pyx file
    with open(pyx_filename, "r") as f:
        pyx_txt = f.read()
        lines = pyx_txt.splitlines()

        for line in lines:
            if line.startswith("# cython:") and "autogen_pxd=False" in line:
                return (
                    "- Skipping .pxd autogen (autogen_pxd=False): "
                    + pyx_filename
                )
            elif line.startswith("# cython:") and "autogen_pxd=True" in line:
                autogen = True
            elif line.startswith("cdef class"):
                pxd_lines.append("")
                pxd_lines.append(line)
            elif "# autogen_pxd: " in line:
                pxd_lines.append(line.replace("# autogen_pxd: ", ""))
            elif (
                (line.startswith("cdef") or line.startswith("    cdef"))
                and line.endswith(":")
                and ")" in line
            ):
                pxd_lines.append(line[:-1])

        pxd_lines.append("")

    if not autogen:
        return "- Skipping .pxd autogen (not enabled): " + pyx_filename

    # write the pxd file
    pxd_text = pxd_prefix_txt + "\n".join(pxd_lines)

    if os.path.exists(pxd_filename) and open(pxd_filename).read() == pxd_text:
        return (
            "- Skipping .pxd autogen (already exists, no changes needed): "
            + pyx_filename
        )

    with open(pxd_filename, "w") as f:
        f.write(pxd_text)
        return "- Generating .pxd file: " + pxd_filename


def autogenerate_pxd_files(root_dir: str):
    """
    Autogenerate pxd files for all .pyx files in the root directory
    :param root_dir: Root directory to search
    """

    print(f"Searching {root_dir} for .pyx files...")
    pyx_files = find_files(root_dir, ".pyx")
    print("Autogenerating .pxd files...")
    msgs = []
    for file in pyx_files:
        msgs.append(autogenerate_pxd_file(file))

    print("\n".join(sorted(msgs)))


def main():
    if len(sys.argv) == 1:
        return

    print(
        """
                        ______                 __ 
    .-----.--.--.--.--.|__    |.-----.--.--.--|  |
    |  _  |  |  |_   _||    __||  _  |_   _|  _  |
    |   __|___  |__.__||______||   __|__.__|_____|
    |__|  |_____|              |__|               
       https://github.com/HenriquesLab/pyx2pxd
    """
    )

    path = sys.argv[-1]
    if not os.path.exists(path):
        raise RuntimeError(f"{path} does not exist")

    autogenerate_pxd_files(path)


if __name__ == "__main__":
    main()

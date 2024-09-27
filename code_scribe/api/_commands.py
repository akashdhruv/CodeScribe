"""Command line interface for Jobrunner"""

import os
from code_scribe import lib


def index(root_dir):
    """
    API command for creating an index for directory tree
    """
    lib.create_scribe_yaml(root_dir)
    return f"Project structure saved to scribe.yaml."


def draft(fortran_file, root_dir):
    """
    API command for creating a draft files
    """
    item_index_list = lib.create_indexes(root_dir)
    lib.annotate_fortran_file(fortran_file, item_index_list)
    return f'Generated draft file for LLM consumption {os.path.splitext(fortran_file)[0] + ".scribe"}'


def save_prompts(filelist, prompt):
    """
    API command for creating a draft files
    """
    mapping = lib.create_src_mapping(filelist)
    lib.save_prompt(mapping, prompt)


def neural_translate(filelist, model, prompt):
    """
    API command for creating a draft files
    """
    mapping = lib.create_src_mapping(filelist)
    lib.translate(mapping, model, prompt)

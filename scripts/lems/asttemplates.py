#!/usr/bin/env python3
"""
Templates for LEMS ast generator

File: scripts/lems/asttemplates.py

Copyright 2023 NeuroML contributors
"""

import textwrap
from jinja2 import Environment

env = Environment()


"""Template for the page header"""
page_header = env.from_string(textwrap.dedent(
    """
    (lemsschema:page:{{ section_data[0]|lower|replace(" ", "_") }}_)=
    # {{ section_data[0] }}

    {% if section_data[1] | length > 0 -%}
        **{{- section_data[1] -}}**

    ---
    {%- endif %}

    Generated on {{ todays_date }}.
    Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

    ---
    """))


"""Template for element types"""
elementtype = env.from_string(textwrap.dedent(
    """
    (lemsschema:{{ et['@name']|lower|replace(" ", "_") }}_)=
    ## {{ et['@name'] }}

    <i>{{ et.Info| default("")  }}</i>

    """
))

"""Template for property"""
prop = env.from_string(textwrap.dedent(
    """
    ````{tab-item} Properties
    ```{csv-table}
    :widths: 1, 2, 7
    :width: 100%
    :delim: $

    {% for prop in props -%}
    **{{ prop['@name'] }}**$ {{ prop['@type'] }}$ {{ prop['#text'] }}
    {% endfor %}
    ```
    ````
    """

))

"""Template for list property"""
listprop = env.from_string(textwrap.dedent(
    """
    ````{tab-item} can contain these elements
    ```{csv-table}
    :widths: 2, 8
    :width: 100%
    :delim: $

    {% for prop in lprops -%}
    **{{ prop['@name'] }}**$ {ref}`lemsschema:{{ prop['@type'] | lower|replace(" ", "_") }}_`
    {% endfor %}
    ```
    ````
    """

))
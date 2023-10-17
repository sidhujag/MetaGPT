#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 14:43
@Author  : alexanderwu
@File    : __init__.py
"""

from metagpt.roles.role import Role
from metagpt.roles.architect import Architect
from metagpt.roles.project_manager import ProjectManager
from metagpt.roles.product_manager import ProductManager
from metagpt.roles.manager import Manager
from metagpt.roles.group import Group
from metagpt.roles.searcher import Searcher
from metagpt.roles.engineer import Engineer
from metagpt.roles.qa_engineer import QaEngineer
from metagpt.roles.tutorial_assistant import TutorialAssistant
from metagpt.roles.sales import Sales
from metagpt.roles.researcher import Researcher
from metagpt.roles.customer_service import CustomerService

# SYSCOIN
ROLES_LIST = [
{
    'name': 'ProductManager',
    'description': 'A professional product manager, the goal is to design a concise, usable, and efficient product.',
    'requirements': 'Can only be selected when the task involves Python code development',
    'tools': [],
    'suggestions': '',
    'prompt': 'A professional product manager, the goal is to design a concise, usable, and efficient product.',
},
{
    'name': 'Architect',
    'description': 'A professional architect; the goal is to design a SOTA PEP8-compliant python system; make the best use of good open source tools.',
    'requirements': 'Can only be selected when the task involves Python code development',
    'tools': [],
    'suggestions': '',
    'prompt': 'A professional architect; the goal is to design a SOTA PEP8-compliant python system; make the best use of good open source tools.',
},
{
    'name': 'ProjectManager',
    'description': 'A project manager for Python development; the goal is to break down tasks according to PRD/technical design, give a task list, and analyze task dependencies to start with the prerequisite modules.',
    'requirements': 'Can only be selected when the task involves Python code development',
    'tools': [],
    'suggestions': '',
    'prompt': 'A project manager for Python development; the goal is to break down tasks according to PRD/technical design, give a task list, and analyze task dependencies to start with the prerequisite modules.',
},
{
    'name': 'Engineer',
    'description': 'A professional engineer; the main goal is to write PEP8 compliant, elegant, modular, easy to read and maintain Python code.',
    'requirements': "There is a dependency relationship between the Engineer, ProjectManager, and Architect. If an Engineer is required, both Project Manager and Architect must also be selected.",
    'tools': [],
    'suggestions': '',
    'prompt': 'A professional engineer; the main goal is to write PEP8 compliant, elegant, modular, easy to read and maintain Python code.',
},
{
    'name': 'QaEngineer',
    'description': 'A professional engineer; Write comprehensive and robust tests to ensure codes will work as expected without bugs.',
    'requirements': "Can only be selected when the task involves Python code development.",
    'tools': [],
    'suggestions': '',
    'prompt': 'A professional engineer; Write comprehensive and robust tests to ensure codes will work as expected without bugs.',
},
{
    'name': 'Searcher',
    'description': 'A professional web searcher; Responsible for real-time information for queries that need it.',
    'requirements': "When you need to find things real-time information.",
    'tools': [],
    'suggestions': '',
    'prompt': 'A professional web searcher; Responsible for real-time information for queries that need it..',
},
{
    'name': 'Researcher',
    'description': 'A professional online researcher; Gathers information from the web and conduct research via gathering links, ranking them and summarizing the results.',
    'requirements': "When online research is required to complete tasks, can help with code development or general online research.",
    'tools': [],
    'suggestions': '',
    'prompt': 'A professional online researcher; Gathers information from the web and conduct research via gathering links, ranking them and summarizing the results.',
},
{
    'name': 'TutorialAssistant',
    'description': 'An assistant to help write tutorials in a chosen topic and language.',
    'requirements': "When user needs a markdown compliant format for education.",
    'tools': [],
    'suggestions': '',
    'prompt': 'A professional product manager, the goal is to design a concise, usable, and efficient product.',
},
]
ROLES_MAPPING = {
    'ProductManager': ProductManager,
    'Architect': Architect,
    'ProjectManager': ProjectManager,
    'Engineer': Engineer,
    'QaEngineer': QaEngineer,
    'Researcher': Researcher,
    'TutorialAssistant': TutorialAssistant,
}

__all__ = [
    "Role",
    "Architect",
    "ProjectManager",
    "ProductManager",
    "Engineer",
    "QaEngineer",
    "Searcher",
    "Sales",
    "CustomerService",
]

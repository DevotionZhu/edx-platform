from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'program_enrollments.management.commands.link_program_enrollments')

from lms.djangoapps.program_enrollments.management.commands.link_program_enrollments import *

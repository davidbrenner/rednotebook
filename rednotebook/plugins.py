"""
Support for rednotebook plugins
"""
# Currently this is an extremely simple macro plugin interface. Plugins are
# located in the rnplugins directory and must inherit from the
# RedNotebookPlugin class. Plugins are loaded by and communicate via this 
# module.

# The only type of plugins currently supported are template macro scripts.
# There may be a demand for other types of plugins in the future.

# When {PLUGIN:plugin_name} is encountered in an inserted template, the plugin
# works as a macro interface, calling
# plugin_name.RedNoteBookPluginSubclass.get_text() and replacing
# {PLUGIN:plugin_name} with the result.

# I plan to support {PLUGIN:plugin_name:plugin_args} syntax, but that is yet to
# be implemented.

# Plugins are loaded dynamically as they are used. The plugin.day object is a
# datetime.date object representing the journal's day that the template is
# being inserted into.

import logging
import datetime

log = logging.getLogger('rednotebook')

class RedNotebookPlugin(object):
    """ The base class for all rednotebook plugins """

    def __init__(self, day):
        """ Plugin setup. """
        assert type(day) is datetime.date, "day argument is not type date"
        self.day = day
        self.log = log

    def set_day(self, day):
        """ Set day """
        assert type(day) is datetime.date, "day argument is not type date"
        self.day = day

    def get_text(self):
        """ Returns text to be inserted """
        # Implement this method
        raise NotImplementedError("You must implement get_text in your plugin")

_classes = []
def load_plugin(name):
    """ Imports the plugin module for the given name. The module must be under 
    the rednotebook.rnplugins namespace and inherit from RedNotebookPlugin
    """
    module_name = '%s.%s' % ('rnplugins', name)
    try:
        try:
            namespace = __import__(module_name, None, None)
        except ImportError as exc:
            if exc.args[0].endswith(' ' + name):
                log.warn('** plugin %s not found' % name)
            else:
                raise
        else:
            for obj in getattr(namespace, name).__dict__.values():
                if isinstance(obj, type) and issubclass(obj, 
                        RedNotebookPlugin) and obj != RedNotebookPlugin:
                    _classes.append(obj)
                    return obj
    except:
        log.warn('** error loading plugin %s' % name)
        return None

_instances = {}
def find_plugin(name):
    """ Returns a BeetsPlugin subclass instance for the given module name.
    """
    log.debug("called find plugin")
    if name not in _instances:
        plugin_class = load_plugin(name)
        if plugin_class:
            _instances[name] = plugin_class(datetime.date.today())
        else:
            return None
    return _instances[name]

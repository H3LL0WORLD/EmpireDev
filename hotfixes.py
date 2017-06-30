from lib.common import helpers


class Module:

    def __init__(self, mainMenu, params=[]):

        # Metadata info about the module, not modified during runtime
        self.info = {
            # Name for the module that will appear in module menus
            'Name': 'Hotfixes',

            # List of one or more authors for the module
            'Author': ['@H3LL0WORLD'],

            # More verbose multi-line description of the module
            'Description': ('Get a list of installed hotfixes using WMI'),

            # True if the module needs to run in the background
            'Background': False,

            # File extension to save the file as
            'OutputExtension': None,

            # True if the module needs admin rights to run
            'NeedsAdmin': False,

            # True if the method doesn't touch disk/is reasonably opsec safe
            'OpsecSafe': True,

            # The language for this module
            'Language': 'powershell',

            # The minimum PowerShell version needed for the module to run
            'MinLanguageVersion': '2',

            # List of any references/other comments
            'Comments':[] 
        }

        # Any options needed by the module, settable during runtime
        self.options = {
            # Format:
            #   value_name : {description, required, default_value}
            'Agent': {
                # The 'Agent' option is the only one that MUST be in a module
                'Description':   'Agent to grab a screenshot from.',
                'Required'   :   True,
                'Value'      :   ''
            }
        }

        # Save off a copy of the mainMenu object to access external
        #   functionality like listeners/agent handlers/etc.
        self.mainMenu = mainMenu

        # During instantiation, any settable option parameters are passed as
        #   an object set to the module and the options dictionary is
        #   automatically set. This is mostly in case options are passed on
        #   the command line.
        if params:
            for param in params:
                # Parameter format is [Name, Value]
                option, value = param
                if option in self.options:
                    self.options[option]['Value'] = value

    def generate(self):

        # Second method: For calling your imported source, or holding your
        #   inlined script. If you're importing source using the first method,
        #   ensure that you append to the script variable rather than set.
        #
        # The script should be stripped of comments, with a link to any
        #   original reference script included in the comments.
        #
        # If your script is more than a few lines, it's probably best to use
        #   the first method to source it.
        #
        # script += """
        script = """
        Get-WmiObject Win32_QuickFixEngineering | Select HotFixID, Description, InstalledOn | Out-String
"""

        # Add any arguments to the end execution of the script
        for option, values in self.options.iteritems():
            if option.lower() != "agent":
                if values['Value'] and values['Value'] != '':
                    if values['Value'].lower() == "true":
                        # if we're just adding a switch
                        script += " -" + str(option)
                    else:
                        script += " -" + str(option) + " " + str(values['Value'])

        return script

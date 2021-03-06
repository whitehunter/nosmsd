

def _(text):
    return text

ERROR_MESSAGES = [
    ("UNKNOWN", _(u"Unknown Error")),
    ("NONE", _(u"No error.")),
    ("DEVICEOPENERROR", _(u"Error opening device. "
                          u"Unknown, busy or no permissions.")),
    ("DEVICELOCKED", _(u"Error opening device, it is locked.")),
    ("DEVICENOTEXIST", _(u"Error opening device, it doesn't exist.")),
    ("DEVICEBUSY", _(u"Error opening device, "
                     u"it is already opened by other application.")),
    ("DEVICENOPERMISSION", _(u"Error opening device, "
                             u"you don't have permissions.")),
    ("DEVICENODRIVER", _(u"Error opening device. "
                         u"No required driver in operating system.")),
    ("DEVICENOTWORK", _(u"Error opening device. Some hardware not "
                        u"connected/wrongly configured.")),
    ("DEVICEDTRRTSERROR", _(u"Error setting device DTR or RTS.")),
    ("DEVICECHANGESPEEDERROR", _(u"Error setting device speed. "
                                 u"Maybe speed not supported.")),
    ("DEVICEWRITEERROR", _(u"Error writing to the device.")),
    ("DEVICEREADERROR", _(u"Error during reading from the device.")),
    ("DEVICEPARITYERROR", _(u"Can't set parity on the device.")),
    ("TIMEOUT", _(u"No response in specified timeout. "
                  u"Probably phone not connected.")),
    ("FRAMENOTREQUESTED", _(u"Frame not requested right now. "
                            u"See <http://wammu.eu/support/bugs/> "
                            u"for information how to report it.")),
    ("UNKNOWNRESPONSE", _(u"Unknown response from phone. "
                          u"See <http://wammu.eu/support/bugs/> "
                          u"for information how to report it.")),
    ("UNKNOWNFRAME", _(u"Unknown frame. "
                       u"See <http://wammu.eu/support/bugs/> "
                       u"for information how to report it.")),
    ("UNKNOWNCONNECTIONTYPESTRING", _(u"Unknown connection type string. "
                                      u"Check config file.")),
    ("UNKNOWNMODELSTRING", _(u"Unknown model type string. "
                             u"Check config file.")),
    ("SOURCENOTAVAILABLE", _(u"Some functions not available for your system "
                             u"(disabled in config or not implemented).")),
    ("NOTSUPPORTED", _(u"Function not supported by phone.")),
    ("EMPTY", _(u"Entry is empty.")),
    ("SECURITYERROR", _(u"Security error. Maybe no PIN?")),
    ("INVALIDLOCATION", _(u"Invalid location. Maybe too high?")),
    ("NOTIMPLEMENTED", _(u"Functionality not implemented. "
                         u"You are welcome to help authors with it.")),
    ("FULL", _(u"Memory full.")),
    ("UNKNOWN", _(u"Unknown error.")),
    ("CANTOPENFILE", _(u"Can not open specified file.")),
    ("MOREMEMORY", _(u"More memory required...")),
    ("PERMISSION", _(u"Operation not allowed by phone.")),
    ("EMPTYSMSC", _(u"No SMSC number given. Provide it manually or "
                    u"use the one configured in phone.")),
    ("INSIDEPHONEMENU", _(u"You're inside phone menu (maybe editing?). "
                          u"Leave it and try again.")),
    ("NOTCONNECTED", _(u"Phone is not connected.")),
    ("WORKINPROGRESS", _(u"Function is currently being implemented. "
                         u"If you want to help, please contact authors.")),
    ("PHONEOFF", _(u"Phone is disabled and connected to charger.")),
    ("FILENOTSUPPORTED", _(u"File format not supported by Gammu.")),
    ("BUG", _(u"Nobody is perfect, some bug appeared in protocol "
              u"implementation. Please contact authors.")),
    ("CANCELED", _(u"Transfer was canceled by phone, "
                   u"maybe you pressed cancel on phone.")),
    ("NEEDANOTHERANSWER", _(u"Phone module need to "
                            u"send another answer frame.")),
    ("OTHERCONNECTIONREQUIRED", _(u"Current connection type "
                                  u"doesn't support called function.")),
    ("WRONGCRC", _(u"CRC error.")),
    ("INVALIDDATETIME", _(u"Invalid date or time specified.")),
    ("MEMORY", _(u"Phone memory error, maybe it is read only.")),
    ("INVALIDDATA", _(u"Invalid data given to phone.")),
    ("FILEALREADYEXIST", _(u"File with specified name already exists.")),
    ("FILENOTEXIST", _(u"File with specified name doesn't exist.")),
    ("SHOULDBEFOLDER", _(u"You have to give folder name and not file name.")),
    ("SHOULDBEFILE", _(u"You have to give file name and not folder name.")),
    ("NOSIM", _(u"Can not access SIM card.")),
    ("GNAPPLETWRONG", _(u"Wrong GNAPPLET version in phone. "
                        u"Use version from currently used Gammu.")),
    ("FOLDERPART", _(u"Only part of folder has been listed.")),
    ("FOLDERNOTEMPTY", _(u"Folder must be empty.")),
    ("DATACONVERTED", _(u"Data were converted.")),
    ("UNCONFIGURED", _(u"Gammu is not configured.")),
    ("WRONGFOLDER", _(u"Wrong folder used.")),
    ("PHONE_INTERNAL", _(u"Internal phone error.")),
    ("WRITING_FILE", _(u"Error writing file to disk.")),
    ("NONE_SECTION", _(u"No such section exists.")),
    ("USING_DEFAULTS", _(u"Using default values.")),
    ("CORRUPTED", _(u"Corrupted data returned by phone.")),
    ("BADFEATURE", _(u"Bad feature string in configuration.")),
    ("DISABLED", _(u"Desired functionality has been "
                   u"disabled on compile time.")),
    ("SPECIFYCHANNEL", _(u"Bluetooth configuration requires channel option.")),
    ("NOTRUNNING", _(u"Service is not running.")),
    ("NOSERVICE", _(u"Service configuration is missing.")),
    ("BUSY", _(u"Command rejected because device was busy. "
               u"Wait and restart.")),
    ("COULDNT_CONNECT", _(u"Could not connect to the server.")),
    ("COULDNT_RESOLVE", _(u"Could not resolve the host name.")),
    ("GETTING_SMSC", _(u"Failed to get SMSC number from phone.")),
    ("ABORTED", _(u"Operation aborted.")),
    ("INSTALL_NOT_FOUND", _(u"Installation data not found, "
                            u"please consult debug log and/or documentation "
                            u"for more details.")),
    ("READ_ONLY", _(u"Entry is read only."))]

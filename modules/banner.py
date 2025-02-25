from modules import color

version = "v1.61"

menu1 = f"""

    {color.WHITE}1. {color.GREEN}Connect a Device             {color.WHITE}6. {color.GREEN}Get Screenshot                       {color.WHITE}11. {color.GREEN}Install an APK  
    {color.WHITE}2. {color.GREEN}List Connected Devices       {color.WHITE}7. {color.GREEN}Screen Record                        {color.WHITE}12. {color.GREEN}Uninstall an App
    {color.WHITE}3. {color.GREEN}Disconnect All Devices       {color.WHITE}8. {color.GREEN}Download File/Folder from Device     {color.WHITE}13. {color.GREEN}List Installed Apps 
    {color.WHITE}4. {color.GREEN}Scan Network for Devices     {color.WHITE}9. {color.GREEN}Send File/Folder to Device           {color.WHITE}14. {color.GREEN}Access Device Shell
    {color.WHITE}5. {color.GREEN}Mirror & Control Device     {color.WHITE}10. {color.GREEN}Run an App                           {color.WHITE}15. {color.GREEN}Hack Device {color.RED}(Using Metasploit)


   {color.YELLOW} 
  N : Next Page                                      (Page : 1 / 3)"""

menu2 = f"""

    {color.WHITE}16. {color.GREEN}List All Folders/Files      {color.WHITE}21. {color.GREEN}Anonymous Screenshot                {color.WHITE}26. {color.GREEN}Play a Video on Device
    {color.WHITE}17. {color.GREEN}Send SMS                    {color.WHITE}22. {color.GREEN}Anonymous Screen Record             {color.WHITE}27. {color.GREEN}Get Device Information
    {color.WHITE}18. {color.GREEN}Copy WhatsApp Data          {color.WHITE}23. {color.GREEN}Open a Link on Device               {color.WHITE}28. {color.GREEN}Get Battery Information
    {color.WHITE}19. {color.GREEN}Copy All Screenshots        {color.WHITE}24. {color.GREEN}Display a Photo on Device           {color.WHITE}29. {color.GREEN}Restart Device
    {color.WHITE}20. {color.GREEN}Copy All Camera Photos      {color.WHITE}25. {color.GREEN}Play an Audio on Device             {color.WHITE}30. {color.GREEN}Advanced Reboot Options


   {color.YELLOW} 
  P : Previous Page         N : Next Page            (Page : 2 / 3)"""

menu3 = f"""

    {color.WHITE}31. {color.GREEN}Unlock Device               {color.WHITE}36. {color.GREEN}Extract APK from Installed App      {color.WHITE}41. {color.GREEN}Record Mic Audio
    {color.WHITE}32. {color.GREEN}Lock Device                 {color.WHITE}37. {color.GREEN}Stop ADB Server                     {color.WHITE}42. {color.GREEN}Listen Device Audio
    {color.WHITE}33. {color.GREEN}Dump All SMS                {color.WHITE}38. {color.GREEN}Power Off Device                    {color.WHITE}43. {color.GREEN}Record Device Audio
    {color.WHITE}34. {color.GREEN}Dump All Contacts           {color.WHITE}39. {color.GREEN}Use Keycodes (Control Device)       {color.WHITE}44. {color.GREEN}Update PhoneSploit-Pro
    {color.WHITE}35. {color.GREEN}Dump Call Logs              {color.WHITE}40. {color.GREEN}Listen Mic Audio                    {color.WHITE}45. {color.GREEN}Visit PhoneSploit-Pro on GitHub


   {color.YELLOW} 
  P : Previous Page                                  (Page : 3 / 3)"""

menu = [menu1, menu2, menu3]

instruction = f"""

This attack will launch Metasploit-Framework    (msfconsole)

Use 'Ctrl + C' to stop at any point

1. Wait until you see:
    
    {color.GREEN}meterpreter >      {color.WHITE}

2. Then use 'help' command to see all meterpreter commands:

    {color.GREEN}meterpreter > {color.YELLOW}help       {color.WHITE}

3. To exit meterpreter enter 'exit' or To exit Metasploit enter 'exit -y':

    {color.GREEN}meterpreter > {color.YELLOW}exit       {color.WHITE}

    {color.GREEN}msf6 > {color.YELLOW}exit -y       {color.WHITE}
     
{color.RED}[PhoneSploit Pro]   {color.WHITE}Press 'Enter' to continue attack / '0' to Go Back to Main Menu
    """

banner2 = f"""
                                                                                                                        
    _/      _/    _/_/    _/_/_/    _/_/_/  _/        _/_/_/_/      _/_/_/_/_/    _/_/    _/    _/  _/_/_/_/  _/_/_/    
   _/_/  _/_/  _/    _/  _/    _/    _/    _/        _/                _/      _/    _/  _/  _/    _/        _/    _/   
  _/  _/  _/  _/    _/  _/_/_/      _/    _/        _/_/_/            _/      _/_/_/_/  _/_/      _/_/_/    _/_/_/      
 _/      _/  _/    _/  _/    _/    _/    _/        _/                _/      _/    _/  _/  _/    _/        _/    _/     
_/      _/    _/_/    _/_/_/    _/_/_/  _/_/_/_/  _/_/_/_/          _/      _/    _/  _/    _/  _/_/_/_/  _/    _/      


            {color.RED}{version}{color.WHITE}            {color.WHITE}By geetorus..
"""

banner3 = f"""

     __  __  ___   ____ ___     _ _____   _____  _    __  _ _____  ____ 
    |  \/  |/ _ \ ( __ |_ _|   | |____ | |_   _|/ \   \ \| |____ |/ _  |
    | |\/| | | | |/ _  || |    | | |_  |   | | / _ \   \ ` | |_  | (_| |
    | |  | | |_| | (_| || | ___| |___| |   | |/ ___ \  / . |___| |> _  |
    |_|  |_|\___/ \____|___|_____|_____|   |_/_/   \_\/_/|_|_____/_/ |_|

            {color.RED}{version}{color.WHITE}             {color.WHITE}By geetorus..
"""

banner4 = f"""
     _______ _______ _______ _______ _______ _______     _______ _______ _______ _______ _______ 
    |\     /|\     /|\     /|\     /|\     /|\     /|   |\     /|\     /|\     /|\     /|\     /|
    | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ | +---+ |
    | |   | | |   | | |   | | |   | | |   | | |   | |   | |   | | |   | | |   | | |   | | |   | |
    | |M  | | |O  | | |B  | | |I  | | |L  | | |E  | |   | |T  | | |A  | | |K  | | |E  | | |R  | |
    | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ | +---+ |
    |/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|   |/_____\|/_____\|/_____\|/_____\|/_____\|                                                                                                                                                                    
                                                                                                                                                                                           


        {color.RED}{version}{color.WHITE}                             {color.WHITE}By geetorus..
"""
banner5 = f"""
    |\/|/~\|~)|| [~  ~|~|~||/[~|~)
    |  |\_/|_)||_[_   | |~||\[_|~\                                                                            

        {color.RED}{version}{color.WHITE}        {color.WHITE}By geetorus..
"""

banner6 = f"""
     ______   _____  ______ _____ _       _______    _______        _    _ _______ ______  
    |  ___ \ / ___ \(____  (_____) |     (_______)  (_______)  /\  | |  / |_______|_____ \ 
    | | _ | | |   | |____)  ) _  | |      _____      _        /  \ | | / / _____   _____) )
    | || || | |   | |  __  ( | | | |     |  ___)    | |      / /\ \| |< < |  ___) (_____ ( 
    | || || | |___| | |__)  )| |_| |_____| |_____   | |_____| |__| | | \ \| |_____      | |
    |_||_||_|\_____/|______(_____)_______)_______)   \______)______|_|  \_)_______)     |_|
                                                                                 
    
           {color.RED}{version}{color.WHITE}               {color.WHITE}By geetorus..

"""

banner10 = f"""
         ___ __ __  ______   _______   ________ __      ______       _________ ________  ___   ___  ______  ______       
         /__//_//_/\/_____/\/_______/\ /_______/Y_/\    /_____/\     /________/Y_______/\/___/\/__/\/_____/\/_____/\      
        \::\| \| \ \:::_ \ \::: _  \ \\__.::._\|:\ \   \::::_\/_    \__.::.__\|::: _  \ \::.\ \\ \ \::::_\/\:::_ \ \     
         \:.      \ \:\ \ \ \::(_)  \/_  \::\ \ \:\ \   \:\/___/\      \::\ \  \::(_)  \ \:: \/_) \ \:\/___/\:(_) ) )_   
          \:.\-/\  \ \:\ \ \ \::  _  \ \ _\::\ \_\:\ \___\::___\/_      \::\ \  \:: __  \ \:. __  ( (\::___\/\: __ `\ \  
           \. \  \  \ \:\_\ \ \::(_)  \ Y__\::\__/\:\/___/\:\____/\      \::\ \  \:.\ \  \ \: \ )  \ \\:\____/\ \ `\ \ \ 
            \__\/ \__\/\_____\/\_______\|________\/\_____\/\_____\/       \__\/   \__\/\__\/\__\/\__\/ \_____\/\_\/ \_\/                                             

            {color.RED}{version}{color.WHITE}                                {color.WHITE}By geetorus..

"""

banner11 = f"""
     ___           ___           ___                        ___       ___                                  ___           ___           ___           ___     
     /  /\         /  /\         /  /\           ___        /  /\     /  /\                   ___          /  /\         /  /\         /  /\         /  /\    
    /  /::|       /  /::\       /  /::\         /__/\      /  /:/    /  /::\                 /__/\        /  /::\       /  /:/        /  /::\       /  /::\   
   /  /:|:|      /  /:/\:\     /  /:/\:\        \__\:\    /  /:/    /  /:/\:\                \  \:\      /  /:/\:\     /  /:/        /  /:/\:\     /  /:/\:\  
  /  /:/|:|__   /  /:/  \:\   /  /::\ \:\       /  /::\  /  /:/    /  /::\ \:\                \__\:\    /  /::\ \:\   /  /::\____   /  /::\ \:\   /  /::\ \:\ 
 /__/:/_|::::\ /__/:/ \__\:\ /__/:/\:\_\:|   __/  /:/\/ /__/:/    /__/:/\:\ \:\               /  /::\  /__/:/\:\_\:\ /__/:/\:::::\ /__/:/\:\ \:\ /__/:/\:\_\:\
 \__\/  /~~/:/ \  \:\ /  /:/ \  \:\ \:\/:/  /__/\/:/    \  \:\    \  \:\ \:\_\/              /  /:/\:\ \__\/  \:\/:/ \__\/~|:|~~~~ \  \:\ \:\_\/ \__\/~|::\/:/
       /  /:/   \  \:\  /:/   \  \:\_\::/   \  \::/      \  \:\    \  \:\ \:\               /  /:/__\/      \__\::/     |  |:|      \  \:\ \:\      |  |:|::/ 
      /  /:/     \  \:\/:/     \  \:\/:/     \  \:\       \  \:\    \  \:\_\/              /__/:/           /  /:/      |  |:|       \  \:\_\/      |  |:|\/  
     /__/:/       \  \::/       \__\::/       \__\/        \  \:\    \  \:\                \__\/           /__/:/       |__|:|        \  \:\        |__|:|~   
     \__\/         \__\/            ~~                      \__\/     \__\/                                \__\/         \__\|         \__\/         \__\|                                               

            {color.RED}{version}{color.WHITE}                            {color.WHITE}By geetorus..

"""

banner12 = f"""

    ,--.   ,--. ,-----. ,-----. ,--.,--.   ,------. ,--------. ,---.  ,--. ,--.,------.,------.  
    |   `.'   |'  .-.  '|  |) /_|  ||  |   |  .---' '--.  .--'/  O  \ |  .'   /|  .---'|  .--. ' 
    |  |'.'|  ||  | |  ||  .-.  \  ||  |   |  `--,     |  |  |  .-.  ||  .   ' |  `--, |  '--'.' 
    |  |   |  |'  '-'  '|  '--' /  ||  '--.|  `---.    |  |  |  | |  ||  |\   \|  `---.|  |\  \  
    `--'   `--' `-----' `------'`--'`-----'`------'    `--'  `--' `--'`--' '--'`------'`--' '--' 

            {color.RED}{version}{color.WHITE}                            {color.WHITE}By geetorus..

"""
banner_list = [
    banner2,
    banner3,
    banner4,
    banner5,
    banner6,
    banner10,
    banner11,
    banner12,
]

instructions_banner = f"""{color.CYAN}
        ____           __                  __  _                 
       /  _/___  _____/ /________  _______/ /_(_)___  ____  _____
       / // __ \/ ___/ __/ ___/ / / / ___/ __/ / __ \/ __ \/ ___/
     _/ // / / (__  ) /_/ /  / /_/ / /__/ /_/ / /_/ / / / (__  ) 
    /___/_/ /_/____/\__/_/   \__,_/\___/\__/_/\____/_/ /_/____/  
        {color.WHITE}                                                        
"""

hacking_banner = f"""{color.GREEN}
    
    █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀ ░ ░ ░
    █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█ ▄ ▄ ▄
    {color.WHITE}
"""

keycode_menu = f"""
    {color.WHITE}1. {color.GREEN}Keyboard Text Input                {color.WHITE}11. {color.GREEN}Enter
    {color.WHITE}2. {color.GREEN}Home                               {color.WHITE}12. {color.GREEN}Volume Up
    {color.WHITE}3. {color.GREEN}Back                               {color.WHITE}13. {color.GREEN}Volume Down          
    {color.WHITE}4. {color.GREEN}Recent Apps                        {color.WHITE}14. {color.GREEN}Media Play           
    {color.WHITE}5. {color.GREEN}Power Button                       {color.WHITE}15. {color.GREEN}Media Pause
    {color.WHITE}6. {color.GREEN}DPAD Up                            {color.WHITE}16. {color.GREEN}Tab 
    {color.WHITE}7. {color.GREEN}DPAD Down                          {color.WHITE}17. {color.GREEN}Esc
    {color.WHITE}8. {color.GREEN}DPAD Left           
    {color.WHITE}9. {color.GREEN}DPAD Right
   {color.WHITE}10. {color.GREEN}Delete/Backspace
"""
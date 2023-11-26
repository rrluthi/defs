from colorama import Fore as f

from app.utils import get_version


INTRO_BANNER = f"""{f.RED}
{f.RED}|====================================================================|
{f.RED}|{f.YELLOW}                   _               __                          {f.RED} |
{f.RED}|{f.YELLOW}                __| |     ___     / _|    ___                  {f.RED} |
{f.RED}|{f.YELLOW}               / _` |    / _ \   | |_    / __|                 {f.RED} |
{f.RED}|{f.YELLOW}              | (_| |   |  __/   |  _|   \__ \                 {f.RED} |
{f.RED}|{f.YELLOW}               \__,_|    \___|   |_|     |___/                 {f.RED} |
|=====================================================================|
|     STRING & FILE ENCODER/DECODER/HASHER/UNIQUE STRING GENERATOR    |
|=====================================================================|
| Licence: Mit                                                        |
| Commands: hash, enc, dec, file, help, exit                          |
| Language: {f.CYAN}Python3.12                                        |
| Version: {get_version()}                                            |
|=====================================================================|
"""

VERSION_BANNER = f"""
DEFS Version: {get_version()}
"""

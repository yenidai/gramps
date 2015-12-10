#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2015-      Serge Noiraud
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# https://en.wikipedia.org/wiki/Miscellaneous_Symbols
# http://www.w3schools.com/charsets/ref_utf_symbols.asp
#

#-------------------------------------------------------------------------
#
# Standard python modules
#
#-------------------------------------------------------------------------
from gramps.gen.const import GRAMPS_LOCALE as glocale
_ = glocale.translation.sgettext
import fontconfig

class Symbols():
    # genealogical symbols
    SYMBOL_LESBIAN                   = 0
    SYMBOL_MALE_HOMOSEXUAL           = 1
    SYMBOL_HETEROSEXUAL              = 2
    SYMBOL_TRANSGENDER_HERMAPHRODITE = 3
    SYMBOL_TRANSGENDER               = 4
    SYMBOL_ASEXUAL_SEXLESS           = 5
    SYMBOL_MARRIAGE                  = 6
    SYMBOL_DIVORCE                   = 7
    SYMBOL_UNMARRIED_PARTNERSHIP     = 8
    SYMBOL_BURIED                    = 9
    SYMBOL_CREMATED                  = 10

    all_symbols = [
               # Name                                            (UNICODE char) (HTML char) SUBSTITUTION string
               (_("Lesbianism"),                                 '\u26a2',      "&#9890;",  ""),
               (_("Male homosexuality"),                         '\u26a3',      "&#9891;",  ""),
               (_("Heterosexality"),                             '\u26a4',      "&#9892;",  ""),
               (_("Transgender, hermaphrodite (in entomology)"), '\u26a5',      "&#9893;",  ""),
               (_("Transgender"),                                '\u26a6',      "&#9894;",  ""),
               (_("Asexuality, sexless, genderless"),            '\u26aa',      "&#9898;",  ""),
               (_("Marriage"),                                   '\u26ad',      "&#9901;",  "oo"),
               (_("Divorce"),                                    '\u26ae',      "&#9902;",  "o|o"),
               (_("Unmarried partnership"),                      '\u26af',      "&#10016;", "o-o"),
               (_("Buried"),                                     '\u26b0',      "&#10016;", "d"),
               (_("Cremated"),                                   '\u26b1',      "&#10016;", "d"),
              ]

    # genealogical death symbols
    DEATH_SYMBOL_NONE                      = 0
    DEATH_SYMBOL_X                         = 1
    DEATH_SYMBOL_SKULL                     = 2
    DEATH_SYMBOL_ANKH                      = 3
    DEATH_SYMBOL_ORTHODOX_CROSS            = 4
    DEATH_SYMBOL_CHI_RHO                   = 5
    DEATH_SYMBOL_LORRAINE_CROSS            = 6
    DEATH_SYMBOL_JERUSALEM_CROSS           = 7
    DEATH_SYMBOL_STAR_CRESCENT             = 8
    DEATH_SYMBOL_WEST_SYRIAC_CROSS         = 9
    DEATH_SYMBOL_EAST_SYRIAC_CROSS         = 10
    DEATH_SYMBOL_HEAVY_GREEK_CROSS         = 11
    DEATH_SYMBOL_LATIN_CROSS               = 12
    DEATH_SYMBOL_MALTESE_CROSS             = 13
    DEATH_SYMBOL_STAR_OF_DAVID             = 14
    DEATH_SYMBOL_DEAD                      = 15

    # The following is used in the global preferences in the display tab.
    #                Name                              (UNICODE char) (HTML char) SUBSTITUTION string
    death_symbols = [(_("Nothing"),                           "",         "",        ""),
                 ("x",                                    "x",        "x",       "x"),
                 (_("Skull and crossbones") +' : \u2620', "&#9760;",  "\u2620",  "+"),
                 (_("Ankh")                 +' : \u2625', "&#9765;",  "\u2625",  "+"),
                 (_("Orthodox cross")       +' : \u2626', "&#9766;",  "\u2626",  "+"),
                 (_("Chi rho")              +' : \u2627', "&#9767;",  "\u2627",  "+"),
                 (_("Cross of lorraine")    +' : \u2628', "&#9768;",  "\u2628",  "+"),
                 (_("Cross of jerusalem")   +' : \u2629', "&#9769;",  "\u2629",  "+"),
                 (_("Star and crescent")    +' : \u262a', "&#9770;",  "\u262a",  "+"),
                 (_("West syriac cross")    +' : \u2670', "&#9840;",  "\u2670",  "+"),
                 (_("East syriac cross")    +' : \u2671', "&#9841;",  "\u2671",  "+"),
                 (_("Heavy greek cross")    +' : \u271a', "&#10010;", "\u271a",  "+"),
                 (_("Latin cross")          +' : \u271e', "&#10014;", "\u271e",  "+"),
                 (_("Maltese cross")        +' : \u2720', "&#10016;", "\u2720",  "+"),
                 (_("Star of david")        +' : \u2721', "&#10017;", "\u2721",  "+"),
                 (_("Dead"),                              _("Dead"),  _("Dead"), _("Dead"))
                ]

    def __init__(self):
        self.symbols = None 
    #
    # functions for general symbols
    #
    def get_symbol_for_html(self, symbol):
        """ retun the html string like '&#9898;' """
        return self.all_symbols[symbol][2]

    def get_symbol_for_string(self, symbol):
        """ retun the utf-8 character like '\u2670' """
        return self.all_symbols[symbol][1]

    def get_symbol_replacement(self, symbol):
        """
        Return the replacement string.
        This is used if the utf-8 symbol in not present within a font.
        """
        return self.all_symbols[symbol][3]

    #
    # functions for death symbols
    #
    def get_death_symbols(self):
        """
        Return the list of death symbols.
        This is used in the global preference to choose which symbol we will use.
        """
        return self.death_symbols

    def get_death_symbol_for_html(self, symbol):
        """ return the html string like '&#9898;'. Should be used only here for test. """
        return self.death_symbols[symbol][1]

    def get_death_symbol_for_string(self, value):
        """
        Return the utf-8 character for the symbol.
        The value correspond to the selected string for html which is saved
        in the config section for interface.death-symbol
        """
        for element in self.death_symbols:
            if element[1] == value:
                return element[2]
        return ""

    def get_death_symbol_replacement(self, value):
        """
        Return the string replacement for the symbol.
        The value correspond to the selected string for html which is saved
        in the config section for interface.death-symbol
        """
        for element in self.death_symbols:
            if element[1] == value:
                return element[3]
        return ""

    #
    # functions for all symbols
    #
    def get_how_many_symbols(self):
        return len(self.death_symbols) + len(self.all_symbols) - 3

if __name__ == '__main__':
    """
    Test all possible with this symbols.
    """
    import random

    symbols = Symbols()
    print("#")
    print("# TEST for HTML results")
    print("#")

    # test first entry in the tab
    value = symbols.get_symbol_for_html(symbols.SYMBOL_LESBIAN)
    if value == "&#9890;":
        example = '<em><font size +1>%s</font></em>' % value
        print("The first element is correct :", value, "example is ", example)
    # test the last entry
    value = symbols.get_symbol_for_html(symbols.SYMBOL_CREMATED)
    if value == "&#10016;":
        example = '<em><font size +1>%s</font></em>' % value
        print("The last element is correct :", value, "example is ", example)
    # test a random entry
    rand = random.randint(symbols.SYMBOL_LESBIAN, symbols.SYMBOL_CREMATED)
    value = symbols.get_symbol_for_html(rand)
    example = '<em><font size +1>%s</font></em>' % value
    print("The element is :", value, " for", rand, "example is ", example)

    print("#")
    print("# TEST for STRING results")
    print("#")

    # test first entry in the tab
    value = symbols.get_symbol_for_string(symbols.SYMBOL_LESBIAN)
    if value == '\u26a2':
        example = '<em><font size +1>%s</font></em>' % value
        print("The first element is correct :", value)
    # test the last entry
    value = symbols.get_symbol_for_string(symbols.SYMBOL_CREMATED)
    if value == '\u26b1':
        print("The last element is correct :", value)
    # test a random entry
    rand = random.randint(symbols.SYMBOL_LESBIAN, symbols.SYMBOL_CREMATED)
    value = symbols.get_symbol_for_string(rand)
    print("The element is :", value, " for", rand)
    print("#")
    print("# TEST for all genealogical symbols")
    print("#")

    # try to get all the possible response.
    for rand in range(symbols.SYMBOL_LESBIAN, symbols.SYMBOL_CREMATED+1):
        value = symbols.get_symbol_for_html(rand)
        value1 = symbols.get_symbol_for_string(rand)
        value2 = symbols.get_symbol_replacement(rand)
        print("Tha utf-8 char for '%s' is '%s' and the replacement value is '%s'" % (value, value1, value2))

    print("#")
    print("# TEST for death symbol")
    print("#")

    # trying to get the utf-8 char
    value = symbols.get_death_symbol_for_string("&#9760;")
    value2 = symbols.get_death_symbol_replacement("&#9760;")
    print("Tha utf-8 char for %s is %s and the replacement value is %s" % ('&#9760;', value, value2))

    # trying to get the utf-8 char from a random value
    rand = random.randint(symbols.DEATH_SYMBOL_NONE, symbols.DEATH_SYMBOL_DEAD)
    value = symbols.get_death_symbol_for_html(rand)
    value1 = symbols.get_death_symbol_for_string(value)
    value2 = symbols.get_death_symbol_replacement(value)
    print("The utf-8 char for %s is %s and the replacement value is %s" % (value, value1, value2))

    print("#")
    print("# TEST for all death symbol")
    print("#")

    # try to get all the possible response.
    for rand in range(symbols.DEATH_SYMBOL_NONE, symbols.DEATH_SYMBOL_DEAD+1):
        value = symbols.get_death_symbol_for_html(rand)
        value1 = symbols.get_death_symbol_for_string(value)
        value2 = symbols.get_death_symbol_replacement(value)
        print("Tha utf-8 char for '%s' is '%s' and the replacement value is '%s'" % (value, value1, value2))


    # test all fonts for your distrib
    print("#")
    print("# TEST for all fonts available on your system")
    print("#")


    fonts = fontconfig.query()
     
    print("#")
    print("# you have ", len(fonts), "fonts on your system.")
    print("#")

    all_fonts = {}
    for rand in range(symbols.SYMBOL_LESBIAN, symbols.SYMBOL_CREMATED+1):
        string = symbols.get_symbol_for_html(rand)
        value = symbols.get_symbol_for_string(rand)
        nbx = 0
        for idx in range(0, len(fonts)):
            font = fonts[idx]
            fontname = font.family[0][1]
            try:
                vals = all_fonts[fontname]
            except:
                all_fonts[fontname] = []
            if font.has_char(value):
                nbx += 1
                if value not in all_fonts[fontname]:
                    all_fonts[fontname].append(value)
        print("The char '%s' is present in %d font(s)" % (value, nbx))

    for rand in range(symbols.DEATH_SYMBOL_SKULL, symbols.DEATH_SYMBOL_DEAD):
        string = symbols.get_death_symbol_for_html(rand)
        value = symbols.get_death_symbol_for_string(string)
        nbx = 0
        for idx in range(0, len(fonts)):
            font = fonts[idx]
            fontname = font.family[0][1]
            try:
                vals = all_fonts[fontname]
            except:
                all_fonts[fontname] = []
            if font.has_char(value):
                nbx += 1
                if value not in all_fonts[fontname]:
                    all_fonts[fontname].append(value)
        print("The char '%s' is present in %d font(s)" % (value, nbx))

    print("#")
    print("# TEST for all death symbol")
    print("#")
    nb1 = nb2 = 0
    for font in all_fonts.keys():
        font_usage = all_fonts[font]
        if not font_usage:
           continue
        nb1 += 1
        if len(font_usage) == 24: # If the font use the 24 symbols
            nb2 += 1
        #print("font :", font, " use :",font_usage)

    print("#")
    print("# %d fonts use partialy genealogy symbols." % nb1)
    print("#")
    print("# %d fonts use all genealogy symbols." % nb2)
    print("#")
    print("# These usable fonts for genealogy are :")
    for font in all_fonts.keys():
        font_usage = all_fonts[font]
        if not font_usage:
           continue
        if len(font_usage) == 24: # If the font use the 24 symbols
            print("# You can use :", font)
            nb2 += 1
    print("#")

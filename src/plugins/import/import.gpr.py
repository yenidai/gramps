
#------------------------------------------------------------------------
#
# Comma _Separated Values Spreadsheet (CSV)
#
#------------------------------------------------------------------------

_mime_type = "text/x-comma-separated-values" # CSV Document
_mime_type_rfc_4180 = "text/csv" # CSV Document   See rfc4180 for mime type
plg = newplugin()
plg.id    = 'im_csv'
plg.name  = _("Comma _Separated Values Spreadsheet (CSV)")
plg.description =  _("Import data from CSV files")
plg.version = '1.0'
plg.status = STABLE
plg.fname = 'ImportCsv.py'
plg.ptype = IMPORT
plg.import_function = 'importData'
plg.extension = "csv"

#------------------------------------------------------------------------
#
# GEDCOM
#
#------------------------------------------------------------------------

plg = newplugin()
plg.id    = 'im_ged'
plg.name  = _('GEDCOM')
plg.description =  _('GEDCOM is used to transfer data between genealogy programs. '
                'Most genealogy software will accept a GEDCOM file as input.')
plg.version = '1.0'
plg.status = STABLE
plg.fname = 'ImportGedcom.py'
plg.ptype = IMPORT
plg.import_function = 'importData'
plg.extension = "ged"

#------------------------------------------------------------------------
#
# Geneweb
#
#------------------------------------------------------------------------

plg = newplugin()
plg.id    = 'im_geneweb'
plg.name  = _('GeneWeb')
plg.description =  _('Import data from GeneWeb files')
plg.version = '1.0'
plg.status = STABLE
plg.fname = 'ImportGeneWeb.py'
plg.ptype = IMPORT
plg.import_function = 'importData'
plg.extension = "gw"

#------------------------------------------------------------------------
#
# GRAMPS package (portable XML)
#
#------------------------------------------------------------------------

plg = newplugin()
plg.id    = 'im_gpkg'
plg.name  = _('GRAMPS package (portable XML)')
plg.description =  _('Import data from a GRAMPS package (an archived XML '
                     'family tree together with the media object files.')
plg.version = '1.0'
plg.status = STABLE
plg.fname = 'ImportGpkg.py'
plg.ptype = IMPORT
plg.import_function = 'impData'
plg.extension = "gpkg"

#------------------------------------------------------------------------
#
# GRAMPS XML database
#
#------------------------------------------------------------------------

plg = newplugin()
plg.id    = 'im_gramps'
plg.name  = _('GRAMPS XML Family Tree')
plg.description =  _('The GRAMPS XML format is a text '
                     'version of a family tree. It is '
                     'read-write compatible with the '
                     'present GRAMPS database format.')
plg.version = '1.0'
plg.status = STABLE
plg.fname = 'ImportXml.py'
plg.ptype = IMPORT
plg.import_function = 'importData'
plg.extension = "gramps"

#------------------------------------------------------------------------
#
# GRDB database
#
#------------------------------------------------------------------------

plg = newplugin()
plg.id    = 'im_grdb'
plg.name  = _('GRAMPS 2.x database')
plg.description =  _('Import data from GRAMPS 2.x database files')
plg.version = '1.0'
plg.status = STABLE
plg.fname = 'ImportGrdb.py'
plg.ptype = IMPORT
plg.import_function = 'importData'
plg.extension = "grdb"

#------------------------------------------------------------------------
#
# Pro-Gen Files
#
#------------------------------------------------------------------------

plg = newplugin()
plg.id    = 'im_progen'
plg.name  = _('Pro-Gen')
plg.description =  _('Import data from Pro-Gen files')
plg.version = '1.0'
plg.status = STABLE
plg.fname = 'ImportProGen.py'
plg.ptype = IMPORT
plg.import_function = '_importData'
plg.extension = "def"

#------------------------------------------------------------------------
#
# SQLite Import
#
#------------------------------------------------------------------------

plg = newplugin()
plg.id    = 'im_sqlite'
plg.name  = _('SQLite Import')
plg.description =  _('SQLite is a common local database format')
plg.version = '1.0'
plg.status = UNSTABLE
plg.fname = 'ImportSql.py'
plg.ptype = IMPORT
plg.import_function = 'importData'
plg.extension = "sql"

#------------------------------------------------------------------------
#
# vCard
#
#------------------------------------------------------------------------

plg = newplugin()
plg.id    = 'im_vcard'
plg.name  = _('vCard')
plg.description =  _('Import data from vCard files')
plg.version = '1.0'
plg.status = STABLE
plg.fname = 'ImportVCard.py'
plg.ptype = IMPORT
plg.import_function = 'importData'
plg.extension = "vcf"
